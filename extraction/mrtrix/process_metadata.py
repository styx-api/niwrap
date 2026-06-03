#!/usr/bin/env python3
"""Promote raw MRtrix3 metadata dumps into the NiWrap descriptor layout.

Reads the per-version dumps produced by the Docker pipeline

    extraction/mrtrix/dump/<version>/
    ├── VERSION
    ├── cpp/      <command>.json   (native __print_usage_json__)
    └── python/   <command>.json   (argdump + mrtrix metadata)

and writes the committed, build-consumable tree

    src/niwrap/mrtrix/<version>/
    ├── version.json                  # { name, container, apps, executables }
    └── <command>/
        ├── mrtrix.json | argdump.json    # the dump, copied verbatim
        └── app.json                      # { name, source:{type,path}, docs }

and registers the version in src/niwrap/mrtrix/package.json.

This step does NOT interpret the command interface — that is the job of the
`load_mrtrix` / `load_argdump` Styx frontends at build time. It only lays out
files, writes routing metadata, and extracts a human-readable description for
the docs/coverage tooling. The descriptor itself is a verbatim, provenance-
preserving copy of what the tool emitted.

Migration note: when run against a tree that still holds Boutiques descriptors,
each rewritten command directory has its stale `boutiques.json` (and the other
descriptor type) pruned so only one descriptor remains. The `app.json` then
points at a `source.type` (`mrtrix`/`argdump`) that the build only understands
once the frontends are wired in — so run this only together with that wiring.
"""

import argparse
import json
import shutil
from pathlib import Path

# .../extraction/mrtrix/process_metadata.py -> repo root is two levels up.
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DUMP_ROOT = Path(__file__).resolve().parent / "dump"
DEFAULT_OUT = REPO_ROOT / "src" / "niwrap" / "mrtrix"

CONTAINER_TEMPLATE = "mrtrix3/mrtrix3:{version}"

# Commands MRtrix ships that we never wrap (GUI apps, shell helpers). Merged with
# any `executables.ignored` already recorded in an existing version.json so the
# curated list is preserved across regenerations.
DEFAULT_IGNORED = frozenset({"for_each", "mrtrix_cleanup", "mrview", "shview"})

# dump subdir -> (descriptor filename, app.json source type)
SOURCES = {
    "cpp": ("mrtrix.json", "mrtrix"),
    "python": ("argdump.json", "argdump"),
}
# every descriptor filename we might write — used to prune stale ones on rewrite
ALL_DESCRIPTORS = {"boutiques.json", "mrtrix.json", "argdump.json"}


def _write_json(path: Path, data: dict) -> None:
    # newline="\n" so output is LF on every platform (Windows default is CRLF).
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _version_key(version: str):
    """Sort versions numerically where possible (3.0.10 after 3.0.4)."""
    parts = []
    for token in version.replace("-", ".").split("."):
        parts.append((0, int(token)) if token.isdigit() else (1, token))
    return parts


def _paragraphs(value) -> list:
    """Coerce a description/free-text field to a clean list of strings."""
    if value is None:
        return []
    if isinstance(value, str):
        value = [value]
    return [str(item) for item in value if item is not None and str(item) != ""]


def _citation_text(citation) -> str:
    """A citation is a string or a [condition, text] pair (possibly empty)."""
    if isinstance(citation, (list, tuple)):
        return str(citation[-1]) if citation else ""
    return str(citation)


def _build_description(synopsis: str, description, references) -> str:
    """`<synopsis>.` + description paragraphs + a References section, joining
    only the sections that are actually present (no dangling headers)."""
    sections: list[str] = []
    if synopsis:
        sections.append(f"{synopsis}.")
    sections.extend(_paragraphs(description))
    refs = [r for r in (_citation_text(c) for c in (references or [])) if r]
    if refs:
        sections.append("References:\n\n" + "\n\n".join(refs))
    return "\n\n".join(sections)


def _cpp_description(dump: dict) -> str:
    return _build_description(
        dump.get("synopsis", ""), dump.get("description"), dump.get("references")
    )


def _python_description(dump: dict) -> str:
    meta = dump.get("mrtrix", {})
    return _build_description(
        meta.get("synopsis", ""), meta.get("description"), meta.get("citations")
    )


def _load_json_or_none(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def process_version(version_dump: Path, out_root: Path, version: str) -> list:
    """Write one version's descriptors; return the sorted list of command names."""
    version_out = out_root / version

    existing_version = _load_json_or_none(version_out / "version.json") or {}
    existing_exe = existing_version.get("executables", {})
    ignored = DEFAULT_IGNORED | set(existing_exe.get("ignored", []))

    names: list[str] = []
    skipped: list[str] = []

    for kind, (descriptor_name, source_type) in SOURCES.items():
        src_dir = version_dump / kind
        if not src_dir.is_dir():
            continue
        for dump_file in sorted(src_dir.glob("*.json")):
            name = dump_file.stem  # the filename is the authoritative command name
            if name in ignored:
                continue
            try:
                dump = json.loads(dump_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                print(f"    ! skipping {dump_file} (invalid JSON: {exc})")
                skipped.append(name)
                continue

            description = (
                _cpp_description(dump) if kind == "cpp" else _python_description(dump)
            )

            cmd_dir = version_out / name
            cmd_dir.mkdir(parents=True, exist_ok=True)

            # prune any stale descriptor (e.g. a leftover boutiques.json) so the
            # directory ends up with exactly one descriptor
            for stale in ALL_DESCRIPTORS - {descriptor_name}:
                (cmd_dir / stale).unlink(missing_ok=True)

            shutil.copyfile(dump_file, cmd_dir / descriptor_name)
            _write_json(
                cmd_dir / "app.json",
                {
                    "name": name,
                    "source": {"type": source_type, "path": descriptor_name},
                    "docs": {"description": description},
                },
            )
            names.append(name)

    names.sort()

    # Regenerate version.json, preserving any existing fields (release_date, etc.).
    version_json = dict(existing_version)
    version_json["name"] = version
    version_json["container"] = CONTAINER_TEMPLATE.format(version=version)
    version_json["apps"] = names
    version_json["executables"] = {
        **existing_exe,
        "required": names,
        "ignored": sorted(ignored),
    }
    _write_json(version_out / "version.json", version_json)

    if skipped:
        print(f"    ({len(skipped)} skipped: {', '.join(skipped)})")
    return names


def update_package(out_root: Path, versions: list) -> None:
    """Add the processed versions to package.json's version list (idempotent)."""
    package_file = out_root / "package.json"
    if not package_file.exists():
        print(f"  ! {package_file} not found — skipping version registration")
        return
    package = json.loads(package_file.read_text(encoding="utf-8"))
    existing = package.get("versions", [])
    merged = sorted(set(existing) | set(versions), key=_version_key)
    if merged != existing:
        package["versions"] = merged
        _write_json(package_file, package)
        print(f"  registered versions: {merged}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Lay out MRtrix metadata dumps as NiWrap descriptors."
    )
    parser.add_argument(
        "--dump-root",
        type=Path,
        default=DEFAULT_DUMP_ROOT,
        help="directory holding <version>/ dump subdirectories",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="destination package directory",
    )
    args = parser.parse_args()

    version_dumps = sorted(
        d
        for d in args.dump_root.iterdir()
        if (d / "cpp").is_dir() or (d / "python").is_dir()
    )
    if not version_dumps:
        raise SystemExit(f"no version dumps found under {args.dump_root}")

    processed = []
    for version_dump in version_dumps:
        version_file = version_dump / "VERSION"
        version = (
            version_file.read_text(encoding="utf-8").strip()
            if version_file.exists()
            else version_dump.name
        )
        names = process_version(version_dump, args.out, version)
        cpp = len(list((version_dump / "cpp").glob("*.json"))) if (version_dump / "cpp").is_dir() else 0
        py = len(list((version_dump / "python").glob("*.json"))) if (version_dump / "python").is_dir() else 0
        print(f"  {version}: {len(names)} apps ({cpp} cpp + {py} python dumps) -> {args.out / version}")
        processed.append(version)

    update_package(args.out, processed)


if __name__ == "__main__":
    main()

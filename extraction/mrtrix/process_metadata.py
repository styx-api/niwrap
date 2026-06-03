#!/usr/bin/env python3
"""Promote raw MRtrix3 metadata dumps into the NiWrap descriptor layout.

Reads the per-version dumps produced by the Docker pipeline

    extraction/mrtrix/dump/<version>/
    ├── VERSION
    ├── cpp/      <command>.json   (native __print_usage_json__)
    └── python/   <command>.json   (argdump + mrtrix metadata)

and writes the committed, build-consumable tree

    src/niwrap/mrtrix/<version>/
    ├── version.json                  # { name, container, apps: [...] }
    └── <command>/
        ├── mrtrix.json | argparse.json   # the dump, copied verbatim
        └── app.json                      # { name, source:{type,path}, docs }

and registers the version in src/niwrap/mrtrix/package.json.

This step does NOT interpret the command interface — that is the job of the
`load_mrtrix` / `load_argparse` Styx frontends at build time. It only lays out
files, writes routing metadata, and extracts a human-readable description for
the docs/coverage tooling. The descriptor itself is a verbatim, provenance-
preserving copy of what the tool emitted.
"""

import argparse
import json
import shutil
from pathlib import Path

CONTAINER_TEMPLATE = "mrtrix3/mrtrix3:{version}"

# dump subdir -> (descriptor filename, app.json source type)
SOURCES = {
    "cpp": ("mrtrix.json", "mrtrix"),
    "python": ("argparse.json", "argparse"),
}


def _write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def _citation_text(citation) -> str:
    """A citation is either a string or a [condition, text] pair."""
    if isinstance(citation, (list, tuple)):
        return str(citation[-1])
    return str(citation)


def _build_description(synopsis: str, description: list, references: list) -> str:
    """Reproduce the description string the existing descriptors use:
    `<synopsis>.\\n\\n<paragraphs>\\n\\nReferences:\\n\\n<refs>`."""
    return (
        f"{synopsis}.\n\n"
        + "\n\n".join(description)
        + "\n\nReferences:\n\n"
        + "\n\n".join(references)
    )


def _cpp_description(dump: dict) -> str:
    return _build_description(
        dump.get("synopsis", ""),
        dump.get("description", []),
        dump.get("references", []),
    )


def _python_description(dump: dict) -> str:
    meta = dump.get("mrtrix", {})
    return _build_description(
        meta.get("synopsis", ""),
        meta.get("description", []),
        [_citation_text(c) for c in meta.get("citations", [])],
    )


def _command_name(kind: str, dump: dict, fallback: str) -> str:
    if kind == "cpp":
        return dump.get("name") or fallback
    return dump.get("prog") or fallback  # argparse: top-level prog


def process_version(version_dump: Path, out_root: Path, version: str) -> list:
    """Write one version's descriptors; return the sorted list of command names."""
    container = CONTAINER_TEMPLATE.format(version=version)
    version_out = out_root / version
    names: list[str] = []

    for kind, (descriptor_name, source_type) in SOURCES.items():
        src_dir = version_dump / kind
        if not src_dir.is_dir():
            continue
        for dump_file in sorted(src_dir.glob("*.json")):
            dump = json.loads(dump_file.read_text(encoding="utf-8"))
            name = _command_name(kind, dump, dump_file.stem)
            description = (
                _cpp_description(dump)
                if kind == "cpp"
                else _python_description(dump)
            )

            cmd_dir = version_out / name
            cmd_dir.mkdir(parents=True, exist_ok=True)

            # 1) descriptor: verbatim copy of the tool's own output
            shutil.copyfile(dump_file, cmd_dir / descriptor_name)

            # 2) app.json: catalog entry + routing pointer
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
    _write_json(
        version_out / "version.json",
        {"name": version, "container": container, "apps": names},
    )
    return names


def update_package(out_root: Path, versions: list) -> None:
    """Add the processed versions to package.json's version list (idempotent)."""
    package_file = out_root / "package.json"
    if not package_file.exists():
        print(f"  ! {package_file} not found — skipping version registration")
        return
    package = json.loads(package_file.read_text(encoding="utf-8"))
    existing = package.get("versions", [])
    merged = sorted(set(existing) | set(versions))
    if merged != existing:
        package["versions"] = merged
        _write_json(package_file, package)
        print(f"  registered versions: {merged}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dump-root",
        type=Path,
        default=Path("extraction/mrtrix/dump"),
        help="directory holding <version>/ dump subdirectories",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("src/niwrap/mrtrix"),
        help="destination package directory",
    )
    args = parser.parse_args()

    version_dumps = sorted(
        d for d in args.dump_root.iterdir() if (d / "cpp").is_dir() or (d / "python").is_dir()
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
        print(f"  {version}: {len(names)} commands ({cpp} cpp + {py} python) -> {args.out / version}")
        processed.append(version)

    update_package(args.out, processed)


if __name__ == "__main__":
    main()

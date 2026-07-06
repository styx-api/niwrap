"""Build the version-first hosted layout for the niwrap.dev hub.

Phase C / architecture A: the hub bundles ``@styx-api/core`` and compiles
descriptors in the browser, so the hosted layout carries only the raw descriptors
plus a metadata manifest - no compiled (per-language) artefacts.

Emitted under ``--out`` (which maps to ``niwrap.dev/niwrap/`` once published):

    index.json                                releases registry (latest + versions)
    <version>/catalog.json                    the one manifest the hub fetches
    <version>/descriptors/<pkg>/<app>.json     verbatim descriptor copies
    <version>/glossary.json                   neuroimaging term glossary (when present)

``<version>`` is the niwrap release version (``project.json``). Each package
contributes its default version as metadata; the descriptor path is keyed by
``<pkg>/<app>`` (the catalog app id = its source directory / URL slug), which is
unambiguous within a single release.

The manifest deliberately carries no compiled ``@type``: the compiler owns name
scrubbing (e.g. workbench's ``volume-create`` -> ``volume_create``), so the hub
resolves the runtime ``@type`` by compiling the descriptor in-browser rather than
recomputing names from the catalog id.
"""

import shutil
from pathlib import Path
from typing import Any, Optional

from wrap.apps.find_niwrap import find_niwrap
from wrap.catalog import AppType, DocsType, PackageType
from wrap.catalog_niwrap import (
    get_project_niwrap,
    get_version_niwrap,
    iter_apps_niwrap,
    iter_packages_niwrap,
)
from wrap.utils import read_json, write_json

#: Default compiler pin recorded in the manifest. Must match the ``@styx-api/core``
#: version the hub bundles, so the rendered snippets/command line a user sees match
#: the published ``niwrap`` package (the C8 lockstep). Override with ``--compiler``.
DEFAULT_COMPILER = "@styx-api/core@0.6.1"

#: Bump when the manifest shape changes incompatibly, so the hub can guard on it.
SCHEMA_VERSION = 1

#: Sub-directory (relative to a version's catalog.json) holding the descriptors.
DESCRIPTOR_BASE = "descriptors"

#: Filename of the published glossary (relative to a version's catalog.json),
#: copied from the project source (``src/<project>/glossary.json``) when present.
GLOSSARY_FILE = "glossary.json"

#: Cap on the embedded per-app summary; full text stays in the descriptor.
MAX_SUMMARY_CHARS = 240


def _summary(docs: Optional[DocsType]) -> Optional[str]:
    """A one-line summary for gallery/search, or ``None``.

    Boutiques descriptions are usually a single line; workbench descriptions lead
    with a summary sentence and then expand over several paragraphs, so the first
    line is the right summary in both cases. The full description stays in the
    descriptor (and the schema the hub compiles in-browser), so this is only for
    listings - kept short to keep the manifest lean.
    """
    if not docs:
        return None
    description = docs.get("description")
    if not description:
        return None
    summary = description.split("\n", 1)[0].strip()
    if len(summary) > MAX_SUMMARY_CHARS:
        summary = summary[:MAX_SUMMARY_CHARS].rstrip() + "..."
    return summary or None


def _app_entry(pkg_name: str, app: AppType, version_dir: Path) -> dict[str, Any]:
    """Build one app manifest entry and copy its descriptor (if any) verbatim.

    Apps without a ``source`` (listed but not yet wrapped) get no ``descriptor`` /
    ``format`` keys, so the hub shows the "not yet available" state without a fetch.
    """
    app_name = app["name"]
    entry: dict[str, Any] = {"name": app_name}
    summary = _summary(app.get("docs"))
    if summary:
        entry["description"] = summary

    source = app.get("source")
    if source:
        app_dir = app["__path__"].parent
        descriptor_src = app_dir / source["path"]
        rel_path = f"{DESCRIPTOR_BASE}/{pkg_name}/{app_name}.json"
        descriptor_dst = version_dir / rel_path
        descriptor_dst.parent.mkdir(parents=True, exist_ok=True)
        # Byte-verbatim: the gate compiles exactly what the hub will, and the file
        # stays diffable against the source descriptor.
        shutil.copyfile(descriptor_src, descriptor_dst)
        entry["descriptor"] = rel_path
        entry["format"] = source["type"]

    return entry


def _package_entry(pkg: PackageType, version_dir: Path) -> dict[str, Any]:
    """Build one package manifest entry (its default version + that version's apps)."""
    pkg_name = pkg["name"]
    default_version = pkg["default"]
    version = get_version_niwrap(pkg_name, default_version)

    entry: dict[str, Any] = {
        "name": pkg_name,
        "version": version["name"],
    }
    container = version.get("container")
    if container:
        entry["container"] = container
    neurodesk_id = pkg.get("neurodeskId")
    if neurodesk_id:
        entry["neurodeskId"] = neurodesk_id
    docs = pkg.get("docs")
    if docs:
        entry["docs"] = docs

    entry["apps"] = [
        _app_entry(pkg_name, app, version_dir)
        for app in iter_apps_niwrap(pkg_name, default_version)
    ]
    return entry


def _compiler_object(spec: str) -> dict[str, str]:
    """Split a ``name@version`` compiler spec into ``{name, version}``.

    ``rfind`` so the leading ``@`` of a scoped package (``@styx-api/core``) is kept.
    """
    at = spec.rfind("@")
    if at <= 0:
        raise ValueError(f"invalid --compiler spec (want name@version): {spec!r}")
    return {"name": spec[:at], "version": spec[at + 1 :]}


def build_hub_layout(out_dir: Path, compiler: str) -> dict[str, int]:
    """Walk the niwrap catalog and write the hosted layout under ``out_dir``.

    Returns counts (packages / apps / descriptors) for the caller to report.
    """
    project = get_project_niwrap()
    version = project["version"]
    version_dir = out_dir / version

    # Clean rebuild of this version's tree so stale descriptors can't linger.
    if version_dir.exists():
        shutil.rmtree(version_dir)

    packages = [_package_entry(pkg, version_dir) for pkg in iter_packages_niwrap()]

    # Publish the project's neuroimaging glossary next to the catalog when present,
    # so every front-end (hub, docs) annotates descriptions from one shared source.
    glossary_src = project["__path__"].parent / GLOSSARY_FILE
    has_glossary = glossary_src.exists()
    if has_glossary:
        write_json(version_dir / GLOSSARY_FILE, read_json(glossary_src))

    catalog: dict[str, Any] = {
        "schemaVersion": SCHEMA_VERSION,
        "project": project["name"],
        "version": version,
        "compiler": _compiler_object(compiler),
        "descriptorBase": DESCRIPTOR_BASE,
    }
    if has_glossary:
        catalog["glossary"] = GLOSSARY_FILE
    catalog["docs"] = project.get("docs", {})
    catalog["packages"] = packages
    write_json(version_dir / "catalog.json", catalog)

    index = {
        "schemaVersion": SCHEMA_VERSION,
        "project": project["name"],
        "latest": version,
        "versions": [
            {
                "version": version,
                "catalog": f"{version}/catalog.json",
                "compiler": compiler,
            }
        ],
    }
    write_json(out_dir / "index.json", index)

    app_count = sum(len(pkg["apps"]) for pkg in packages)
    descriptor_count = sum(
        1 for pkg in packages for app in pkg["apps"] if "descriptor" in app
    )
    return {
        "packages": len(packages),
        "apps": app_count,
        "descriptors": descriptor_count,
    }


def main(args: Any) -> int:
    # find_niwrap() lands us at the repo root (it chdir's up from tooling/ when run
    # via `uv --directory tooling`). Resolve --out *after* it, so a relative path is
    # anchored to the repo root - not to uv's working directory.
    find_niwrap()
    out_dir = Path(args.out).resolve()

    stats = build_hub_layout(out_dir, args.compiler)
    print(
        f"Wrote hub layout to {out_dir}: "
        f"{stats['packages']} packages, {stats['apps']} apps, "
        f"{stats['descriptors']} descriptors."
    )
    return 0


def register_command(subparsers: Any) -> None:
    parser = subparsers.add_parser(
        "hub-build",
        help="Build the version-first hosted layout for the niwrap.dev hub",
    )
    parser.add_argument(
        "--out",
        default="dist/pages",
        help="Output directory (maps to niwrap.dev/niwrap/ when published)",
    )
    parser.add_argument(
        "--compiler",
        default=DEFAULT_COMPILER,
        help=(
            "Compiler pin recorded in the manifest (name@version); must match the "
            f"@styx-api/core the hub bundles (default: {DEFAULT_COMPILER})"
        ),
    )
    parser.set_defaults(func=main)

from shutil import rmtree
import time

import pathlib as pl

import styx.backend
from wrap.apps.build.loaders import load_source
from wrap.apps.sync import build_package_overview_table
from wrap.catalog import DocsType, PackageType, ProjectType, VersionType
from wrap.catalog_niwrap import (
    get_project_niwrap,
    get_version_niwrap,
    iter_packages_niwrap,
    iter_apps_niwrap,
)

from styx.backend import compile_language
from styx.ir import core as ir
from styx.ir.optimize import optimize

PATH_BUILD_TEMPLATES = pl.Path("tooling/build-templates")
PATH_DIST_ROOT = pl.Path("dist")

ICON_PACKAGE = "📦"
ICON_OK = "✅"
ICON_WARN = "⚠️"
ICON_ERROR = "❌"

# For historical reasons we use other names
# than the Styx backend identifier as repo names.
BUILD_TARGET_TO_DIST_DIR = {
    "typescript": "js",
    "jsonschema": "json-schema",
    "ir": "ir-dump",
}


def to_ir_docs(docs: DocsType | None) -> ir.Documentation:
    if docs is None:
        return ir.Documentation()
    return ir.Documentation(
        title=docs.get("title"),
        description=docs.get("description"),
        authors=docs.get("authors", []),
        literature=docs.get("literature", []),
        urls=docs.get("urls", []),
    )


def to_ir_package(pkg: PackageType, version: VersionType) -> ir.Package:
    return ir.Package(
        name=pkg["name"],
        version=version["name"],  # ! watch out when we add versions
        docker=version.get("container"),
        docs=to_ir_docs(pkg.get("docs")),
    )


def to_ir_project(project: ProjectType) -> ir.Project:
    return ir.Project(
        name=project["name"],
        version=project["version"],
        license=project["license"],
        docs=to_ir_docs(project.get("docs")),
        extras={},
    )


def generate_python_readme() -> str:
    """Generate README for Python distribution."""
    template_path = PATH_BUILD_TEMPLATES / "python/README-template.md"
    template = template_path.read_text(encoding="utf-8")
    return template.replace("{{PACKAGES_TABLE}}", build_package_overview_table(False))


def build_target_stream():
    for pkg in iter_packages_niwrap():
        version = get_version_niwrap(pkg["name"], pkg["default"])

        print(f"    {ICON_PACKAGE} {pkg['docs']['title']:<24} ", end="", flush=True)

        ir_pkg = to_ir_package(pkg, version)

        errors = []

        def _stream_inner():
            for app in iter_apps_niwrap(pkg["name"], pkg["default"]):
                if not (source := app.get("source")):
                    continue  # todo print/count/something?
                app_path = pl.Path(app["__path__"])
                try:
                    yield optimize(load_source(source, app_path))
                except Exception as e:
                    error_msg = f"{app['__path__']}: {str(e)}"
                    errors.append(error_msg)
                    print(f"\n      {ICON_ERROR} {error_msg}", end="")

            status = ICON_WARN if errors else ICON_OK
            print(f"{status}")

        yield ir_pkg, _stream_inner()


def main(targets: list[str]) -> str | int:
    try:
        project = get_project_niwrap()
    except:
        import os

        os.chdir("..")
        try:
            project = get_project_niwrap()
        except:
            print("Error: This needs to be run in the NiWrap repo root.")
            return 1

    print(
        f"Found {project.get('docs', {}).get('title', project['name'])} version {project['version']} repo."
    )

    rmtree(PATH_DIST_ROOT, ignore_errors=True)
    PATH_DIST_ROOT.mkdir(parents=True, exist_ok=True)

    backends = {b.id_: b for b in styx.backend.get_backends()}

    if len(targets):
        for target in targets:
            if target not in backends.keys():
                print(
                    f"Error: Invalid target '{target}', available targets: {list(backends.keys())}"
                )
                return 1
    else:
        # exclude r and boutiques from defaults
        targets = list(set(backends.keys()) - {"r", "boutiques"})

    ir_project = to_ir_project(project)

    for target in targets:
        backend = backends[target]
        print(f"\nBuilding {backend.name}.")
        start = time.time()

        dist_name = BUILD_TARGET_TO_DIST_DIR.get(target, target)

        ir_project.extras["dist_repo_url"] = (
            f"https://github.com/styx-api/niwrap-{dist_name}"
        )
        ir_project.extras["readme_md"] = (
            generate_python_readme() if target == "python" else None
        )

        file_count = 0

        dist_path = PATH_DIST_ROOT / f"{project['name']}-{dist_name}"

        for file in compile_language(backend.id_, ir_project, build_target_stream()):
            file.write(dist_path)
            file_count += 1

        elapsed = time.time() - start
        print(f"    → {file_count} files ({elapsed:.1f}s)")

    return 0


def register_command(subparsers):
    parser = subparsers.add_parser("build", help="Build distributions")
    parser.add_argument(
        "target",
        nargs="*",
        help=f"Any (can be multiple) of {[b.id_ for b in styx.backend.get_backends()]}",
    )

    parser.set_defaults(func=lambda args: main(args.target))

import json
import os
from pathlib import Path
from shutil import rmtree
import time

from styx.backend import compile_language
from styx.backend.python.languageprovider import PythonLanguageProvider
from styx.frontend.boutiques import from_boutiques
from styx.ir.core import Documentation
from styx.ir.optimize import optimize

PATH_PACKAGES = Path("packages")
PATH_DESCRIPTORS = Path("descriptors")

PATH_BUILD_TEMPLATES = Path("build-templates")
PATH_DIST_ROOT = Path("dist")
PATH_DIST_PYTHON = PATH_DIST_ROOT / "niwrap-python"


def iter_packages():
    for filename_package in PATH_PACKAGES.glob("*.json"):
        with open(filename_package) as filehandle_package:
            yield filename_package, json.load(filehandle_package)


def iter_descriptors(package):
    for filename_descriptor in sorted(
        (PATH_DESCRIPTORS / package["id"]).glob("**/*.json")
    ):
        with open(filename_descriptor, "r", encoding="utf-8") as filehandle_descriptor:
            yield filename_descriptor, json.load(filehandle_descriptor)


# =============================================================================
# |                               COMPILE                                     |
# =============================================================================


def stream_descriptors_package(package):
    """Compile and stream descriptors for a given package."""
    package_name = package["name"]

    # Print header with package name
    print(f"\n📦 Processing package: {package_name} ".ljust(80, "─"))

    # Track statistics for summary
    total_descriptors = 0
    patched_descriptors = 0

    start_time = time.time()

    for file_descriptor, descriptor in iter_descriptors(package):
        total_descriptors += 1
        descriptor_name = file_descriptor.stem

        # Show progress with indentation for better readability
        print(f"  ⚙️  Processing: {descriptor_name}")

        # Check if name needs patching
        if descriptor_name != descriptor["name"]:
            patched_descriptors += 1
            print(f"    ↪ Patching name: '{descriptor['name']}' → '{descriptor_name}'")
            descriptor["name"] = descriptor_name

        # Add container information
        descriptor["container-image"] = {
            "image": package["container"],
            "type": "docker",
        }

        # Create documentation object
        package_docs = Documentation(
            title=package_name,
            urls=[package["url"]],
            description=package["description"],
        )

        yield from_boutiques(descriptor, package["id"], package_docs)

    # Print summary
    elapsed_time = time.time() - start_time
    print(
        f"  ✅ Processed {total_descriptors} descriptors "
        f"({patched_descriptors} patched) in {elapsed_time:.2f}s"
    )


def stream_descriptors():
    for _, package in iter_packages():
        yield from stream_descriptors_package(package)


def compile_wrappers():
    rmtree(PATH_DIST_ROOT, ignore_errors=True)

    with open("VERSION", "r", encoding="utf-8") as file:
        niwrap_version = file.read().strip()

    PATH_DIST_ROOT.mkdir(parents=True, exist_ok=True)

    # ------ PYTHON -----------------------------------------------------------
    TEMPLATE_ROOT_PYPROJECT = (
        PATH_BUILD_TEMPLATES / "python/root-pyproject.toml"
    ).read_text(encoding="utf8")
    TEMPLATE_SUBPACKAGE_PYPROJECT = (
        PATH_BUILD_TEMPLATES / "python/subpackage-pyproject.toml"
    ).read_text(encoding="utf8")
    TEMPLATE_README = (PATH_BUILD_TEMPLATES / "python/README-template.md").read_text(
        encoding="utf8"
    )
    SNIPPET_EXTRA_UTILS = (PATH_BUILD_TEMPLATES / "python/extra-utils.py").read_text(
        encoding="utf8"
    )

    PATH_DIST_PYTHON.mkdir(parents=True, exist_ok=True)

    package_reexports = []
    for _, package in iter_packages():
        package_name = f'niwrap_{package["id"]}'
        path_package = PATH_DIST_PYTHON / package_name
        (path_package / "src").mkdir(parents=True, exist_ok=True)

        tsp = TEMPLATE_SUBPACKAGE_PYPROJECT

        tsp = tsp.replace("{{PACKAGE}}", package["id"])
        tsp = tsp.replace(
            "{{PACKAGE_DESCRIPTION}}", f"NiWrap wrappers for {package['name']}."
        )
        tsp = tsp.replace(
            "{{STYXDEFS_VERSION}}",
            PythonLanguageProvider.styxdefs_compat().replace("^", "~="),
        )
        tsp = tsp.replace("{{VERSION}}", niwrap_version)

        (path_package / "pyproject.toml").write_text(tsp, encoding="utf8")

        tsp = f"""# NiWrap wrappers for [{package["name"]}]({package["url"]})

{package["description"]}

{package["name"]} is made by {package["author"]}.

This package contains wrappers only and has no affiliation with the original authors.
"""
        (path_package / "README.md").write_text(tsp, encoding="utf8")

        package_reexports.append(package["id"])

        for compiled_file in compile_language(
            "python", (optimize(d) for d in stream_descriptors_package(package))
        ):
            compiled_file.write(path_package / "src" / package_name)

    # NiWrap root package

    path_niwrap_root = PATH_DIST_PYTHON / "niwrap"
    path_niwrap_root.mkdir(parents=True, exist_ok=True)

    tsp = TEMPLATE_ROOT_PYPROJECT

    tsp = tsp.replace(
        "{{DEPENDENCIES}}", ",\n".join([f'  "niwrap_{x}"' for x in package_reexports])
    )
    tsp = tsp.replace("{{VERSION}}", niwrap_version)

    (path_niwrap_root / "pyproject.toml").write_text(tsp, encoding="utf8")

    tsp = TEMPLATE_README

    tsp = tsp.replace("{{PACKAGES_TABLE}}", build_package_overview_table())

    (path_niwrap_root / "README.md").write_text(tsp, encoding="utf8")
    (PATH_DIST_PYTHON / "README.md").write_text(
        tsp, encoding="utf8"
    )  # Copy for repo root. Should this look different?
    (PATH_DIST_PYTHON / "index.txt").write_text(
        "\n".join(package_reexports), encoding="utf8"
    )

    (path_niwrap_root / "src/niwrap").mkdir(parents=True, exist_ok=True)
    (path_niwrap_root / "src/niwrap/__init__.py").write_text(
        "\n".join([f"from niwrap_{x} import {x}" for x in package_reexports])
        + f"\n{SNIPPET_EXTRA_UTILS}",
        encoding="utf8",
    )


# =============================================================================
# |                           UPDATE README                                   |
# =============================================================================


def build_package_overview_table():
    packages = sorted(
        [package for _, package in iter_packages()], key=lambda x: x["name"]
    )

    buf = "| Package | Status | Version | API Coverage |\n"
    buf += "| --- | --- | --- | --- |\n"

    for package in packages:
        name_link = f"[{package['name']}]({package['url']})"

        # calculate coverage percent
        total_endpoints = len(package["api"]["endpoints"])
        done_endpoints = len(
            [x for x in package["api"]["endpoints"] if x["status"] == "done"]
        )
        missing_endpoints = len(
            [x for x in package["api"]["endpoints"] if x["status"] == "missing"]
        )
        ignored_endpoints = len(
            [x for x in package["api"]["endpoints"] if x["status"] == "ignore"]
        )

        assert total_endpoints == done_endpoints + missing_endpoints + ignored_endpoints

        relevant_endpoints = total_endpoints - ignored_endpoints

        coverage_percent = done_endpoints / relevant_endpoints * 100

        coverage = ""
        if missing_endpoints == 0:
            coverage = f"{done_endpoints}/{relevant_endpoints} (100% 🎉)"
        else:
            coverage = (
                f"{done_endpoints}/{relevant_endpoints} ({coverage_percent:.1f}%)"
            )

        container_tag = package.get("container")
        if container_tag:
            docker_image, _ = package["container"].split(":")
            docker_hub = f"https://hub.docker.com/r/{docker_image}"
            container = f"[`{package['version']}`]({docker_hub})"

        buf += f"| {name_link} | {package['status']} | {container if container_tag else '?'} | {coverage} |\n"
    return buf


def update_endpoint_lists():
    package_dir = "packages"
    descriptors_dir = "descriptors"
    changes_summary = []

    # Iterate through all JSON files in the packages directory
    for package_file in os.listdir(package_dir):
        if package_file.endswith(".json"):
            package_path = os.path.join(package_dir, package_file)

            # Load the package JSON file
            with open(package_path, "r", encoding="utf-8") as f:
                package_data = json.load(f)

            package_id = package_data.get("id")
            if not package_id:
                print(f"Missing 'id' in {package_file}")
                continue

            # Check each endpoint's descriptor
            updated = False
            for endpoint in package_data.get("api", {}).get("endpoints", []):
                target = endpoint.get("target")
                target = target.removeprefix("wb_command -")
                status = endpoint.get("status")
                if not target:
                    continue

                descriptor_path = os.path.join(
                    descriptors_dir, package_id, f"{target}.json"
                )

                # Check if the descriptor file exists
                if os.path.exists(descriptor_path):
                    if status != "done":
                        endpoint["status"] = "done"
                        endpoint["descriptor"] = descriptor_path.replace("\\", "/")
                        updated = True
                else:
                    if status == "ignore":
                        continue  # Skip if status is 'ignore'
                    if status != "missing":
                        endpoint["status"] = "missing"
                        endpoint.pop("descriptor", None)  # Remove descriptor if missing
                        updated = True

            # If updates were made, save the updated package file
            if updated:
                with open(package_path, "w", encoding="utf-8") as f:
                    json.dump(package_data, f, indent=2)

                changes_summary.append(f"Updated {package_file}")

    # Print the summary of changes
    if changes_summary:
        print("Summary of changes:")
        for change in changes_summary:
            print(f"  {change}")
    else:
        print("No changes made.")


# =============================================================================
# |                           VALIDATE BUILD                                  |
# =============================================================================


def validate_build():
    print("Validating build...")

    # Check if the output directory exists
    if not PATH_DIST_PYTHON.exists():
        raise ValueError(f"Output directory {PATH_DIST_PYTHON} does not exist.")

    # Check if there are Python files in the output directory
    python_files = [
        f for f in PATH_DIST_PYTHON.glob("**/*.py") if f.name != "__init__.py"
    ]
    if not python_files:
        raise ValueError(f"No Python files found in {PATH_DIST_PYTHON}")

    # Check if the number of Python files matches the number of descriptors
    descriptor_count = sum(1 for _ in Path(PATH_DESCRIPTORS).glob("**/*.json"))
    if len(python_files) != descriptor_count:
        raise ValueError(
            f"Mismatch in number of Python files ({len(python_files)}) and descriptors ({descriptor_count})"
        )

    # Check if all packages have at least one descriptor
    for package_file in PATH_PACKAGES.glob("*.json"):
        with open(package_file, "r", encoding="utf-8") as f:
            package_data = json.load(f)
            package_id = package_data.get("id")
            if not package_id:
                raise ValueError(f"Package {package_file.name} is missing 'id' field")
            package_descriptors = list(
                (PATH_DESCRIPTORS / package_id).glob("**/*.json")
            )
            if not package_descriptors:
                raise ValueError(f"No descriptors found for package {package_id}")

    print("Build validation completed successfully.")


# =============================================================================
# |                                BUILD                                      |
# =============================================================================


def time_execution(func, description):
    """Execute a function and print its execution time."""
    print(f"\n📌 {description} ".ljust(80, "─"))
    start_time = time.time()
    result = func()
    elapsed_time = time.time() - start_time
    print(f"✓ Completed in {elapsed_time:.2f} seconds")
    return result


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    assert PATH_DESCRIPTORS.exists() and PATH_PACKAGES.exists()

    print("🚀 Starting build process...")

    # Execute each step with timing information
    time_execution(compile_wrappers, "Compile Wrappers")
    time_execution(update_endpoint_lists, "Update Endpoint List")
    time_execution(validate_build, "Validate Build")

    print("\n✅ Build process completed successfully!")

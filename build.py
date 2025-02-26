import json
import os
from pathlib import Path
from shutil import rmtree

from styx.backend import compile_language 
from styx.backend.python.languageprovider import PythonLanguageProvider 
from styx.frontend.boutiques import from_boutiques
from styx.ir.core import Documentation
from styx.ir.optimize import optimize

PATH_PACKAGES = Path("packages")
PATH_DESCRIPTORS = Path("descriptors")
PATH_OUTPUT = Path("python/src/niwrap")


def iter_packages():
    for filename_package in PATH_PACKAGES.glob("*.json"):
        with open(filename_package) as filehandle_package:
            yield filename_package, json.load(filehandle_package)


def iter_descriptors(package):
    for filename_descriptor in sorted((PATH_DESCRIPTORS / package["id"]).glob("**/*.json")):
        with open(filename_descriptor, "r", encoding="utf-8") as filehandle_descriptor:
            yield filename_descriptor, json.load(filehandle_descriptor)


# =============================================================================
# |                               COMPILE                                     |
# =============================================================================


def stream_descriptors():
    for _, package in iter_packages():
        print("*" * 80)
        print(f"COMPILING {package['name']}")
        print("*" * 80)
        for file_descriptor, descriptor in iter_descriptors(package):
            print(f"> Compiling: {file_descriptor}")
            if file_descriptor.stem != descriptor["name"]:
                print("Patching name...")
                descriptor["name"] = file_descriptor.stem

            descriptor["container-image"] = {
                "image": package["container"],
                "type": "docker"
            }
            
            package_docs = Documentation(
                title=package["name"], 
                urls=[package["url"]],
                description=package["description"]
            )
            yield from_boutiques(descriptor, package["id"], package_docs)


def compile_wrappers():
    rmtree(PATH_OUTPUT, ignore_errors=True)

    for compiled_file in compile_language("python", (optimize(d) for d in stream_descriptors())):
        compiled_file.write(PATH_OUTPUT)


# =============================================================================
# |                           UPDATE PYTHON METADATA                          |
# =============================================================================


def update_styxdefs_version():
    import re
    file_path = PATH_OUTPUT / "../../pyproject.toml"
    styxdefs_version = PythonLanguageProvider.styxdefs_compat()
    with open("VERSION", 'r', encoding="utf-8") as file:
        package_version = file.read().strip()
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    pattern = r'(styxdefs\s*=\s*")[^"]+"'
    content = re.sub(pattern, f'\\g<1>{styxdefs_version}"', content)
    pattern = r'(version\s*=\s*")[^"]+"'
    content = re.sub(pattern, f'\\g<1>{package_version}"', content)
    with open(file_path, 'w') as file:
        file.write(content)


def update_python_metadata():
    print("Create package __init__.py")
    PATH_MAIN_INIT = PATH_OUTPUT / "__init__.py"
    PATH_MAIN_INIT.write_text('""".. include:: ../../README.md"""\n', encoding="utf-8")
    
    print("Update package readme")
    patch_section(
        file=PATH_OUTPUT / "../../README.md",
        replacement=build_package_overview_table(),
        token="PACKAGES_TABLE"
    )

    print("Update package styxdefs version")
    update_styxdefs_version()


# =============================================================================
# |                           UPDATE README                                   |
# =============================================================================


def patch_section(file, replacement, token):
    # Replace text in file between <!-- START_{token} --> and <!-- END_{token} -->
    TOKEN_START = f'<!-- START_{token} -->'
    TOKEN_END = f'<!-- END_{token} -->'

    with open(file, 'r', encoding="utf-8") as f:
        readme = f.read()
        start = readme.find(TOKEN_START) + len(TOKEN_START)
        end = readme.find(TOKEN_END)
        assert start >= 0
        assert end >= 0
        assert start < end
        new_readme = readme[:start] + "\n\n" + replacement + "\n" + readme[end:]

    with open(file, 'w', encoding="utf-8") as f:
        f.write(new_readme)


def build_package_overview_table():
    packages = sorted([package for _, package in iter_packages()], key=lambda x: x['name'])

    buf = "| Package | Status | Version | API Coverage |\n"
    buf += "| --- | --- | --- | --- |\n"


    for package in packages:
        name_link = f"[{package['name']}]({package['url']})"
        
        # calculate coverage percent
        total_endpoints = len(package['api']['endpoints'])
        done_endpoints = len([x for x in package['api']['endpoints'] if x['status'] == 'done'])
        missing_endpoints = len([x for x in package['api']['endpoints'] if x['status'] == 'missing'])
        ignored_endpoints = len([x for x in package['api']['endpoints'] if x['status'] == 'ignore'])

        assert total_endpoints == done_endpoints + missing_endpoints + ignored_endpoints

        relevant_endpoints = total_endpoints - ignored_endpoints

        coverage_percent = done_endpoints / relevant_endpoints * 100

        coverage = ""
        if missing_endpoints == 0:
            coverage = f"{done_endpoints}/{relevant_endpoints} (100% 🎉)"
        else:
            coverage = f"{done_endpoints}/{relevant_endpoints} ({coverage_percent:.1f}%)"

        container_tag = package.get('container')
        if container_tag:
            docker_image, _ = package['container'].split(':')
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
            with open(package_path, 'r', encoding='utf-8') as f:
                package_data = json.load(f)
            
            package_id = package_data.get('id')
            if not package_id:
                print(f"Missing 'id' in {package_file}")
                continue
            
            # Check each endpoint's descriptor
            updated = False
            for endpoint in package_data.get('api', {}).get('endpoints', []):
                target = endpoint.get('target')
                target = target.removeprefix("wb_command -")
                status = endpoint.get('status')
                if not target:
                    continue

                descriptor_path = os.path.join(descriptors_dir, package_id, f"{target}.json")
                
                # Check if the descriptor file exists
                if os.path.exists(descriptor_path):
                    if status != 'done':
                        endpoint['status'] = 'done'
                        endpoint['descriptor'] = descriptor_path.replace('\\', '/')
                        updated = True
                else:
                    if status == 'ignore':
                        continue  # Skip if status is 'ignore'
                    if status != 'missing':
                        endpoint['status'] = 'missing'
                        endpoint.pop('descriptor', None)  # Remove descriptor if missing
                        updated = True
            
            # If updates were made, save the updated package file
            if updated:
                with open(package_path, 'w', encoding='utf-8') as f:
                    json.dump(package_data, f, indent=2)
                
                changes_summary.append(f"Updated {package_file}")

    # Print the summary of changes
    if changes_summary:
        print("Summary of changes:")
        for change in changes_summary:
            print(f"  {change}")
    else:
        print("No changes made.")


def update_readme():
    print("Update endpoint lists")
    update_endpoint_lists()
    print("Update repo readme")
    patch_section(
        file=Path("README.md"),
        replacement=build_package_overview_table(),
        token="PACKAGES_TABLE"
    )


# =============================================================================
# |                           VALIDATE BUILD                                  |
# =============================================================================


def validate_build():
    print("Validating build...")

    # Check if the output directory exists
    if not PATH_OUTPUT.exists():
        raise ValueError(f"Output directory {PATH_OUTPUT} does not exist.")

    # Check if there are Python files in the output directory
    python_files = [f for f in PATH_OUTPUT.glob("**/*.py") if f.name != "__init__.py"]
    if not python_files:
        raise ValueError(f"No Python files found in {PATH_OUTPUT}")

    # Check if the number of Python files matches the number of descriptors
    descriptor_count = sum(1 for _ in Path(PATH_DESCRIPTORS).glob("**/*.json"))
    if len(python_files) != descriptor_count:
        raise ValueError(f"Mismatch in number of Python files ({len(python_files)}) and descriptors ({descriptor_count})")

    # Check if __init__.py exists in the output directory
    if not (PATH_OUTPUT / "__init__.py").exists():
        raise ValueError(f"__init__.py not found in {PATH_OUTPUT}")

    # Check if README.md has been updated
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
        if "<!-- START_PACKAGES_TABLE -->" not in readme_content or "<!-- END_PACKAGES_TABLE -->" not in readme_content:
            raise ValueError("README.md does not contain the expected package table markers")

    # Check if pyproject.toml has been updated
    with open(PATH_OUTPUT / "../../pyproject.toml", "r", encoding="utf-8") as f:
        pyproject_content = f.read()
        if "styxdefs =" not in pyproject_content or "version =" not in pyproject_content:
            raise ValueError("pyproject.toml does not contain expected version information")

    # Check if all packages have at least one descriptor
    for package_file in PATH_PACKAGES.glob("*.json"):
        with open(package_file, "r", encoding="utf-8") as f:
            package_data = json.load(f)
            package_id = package_data.get("id")
            if not package_id:
                raise ValueError(f"Package {package_file.name} is missing 'id' field")
            package_descriptors = list((PATH_DESCRIPTORS / package_id).glob("**/*.json"))
            if not package_descriptors:
                raise ValueError(f"No descriptors found for package {package_id}")

    print("Build validation completed successfully.")


# =============================================================================
# |                                BUILD                                      |
# =============================================================================


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    assert PATH_DESCRIPTORS.exists() and PATH_PACKAGES.exists()

    print("=== COMPILE WRAPPERS ===")
    compile_wrappers()

    print("=== UPDATE PYTHON METADATA ===")
    update_python_metadata()

    print("=== UPDATE README ===")
    update_readme()

    print("=== VALIDATE BUILD ===")
    validate_build()

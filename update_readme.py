"""Update main repo README.md + package endpoint JSONs."""

import json
import os
from pathlib import Path

PATH_PACKAGES = Path("packages")
PATH_DESCRIPTORS = Path("descriptors")

PATH_BUILD_TEMPLATES = Path("build-templates")
PATH_DIST_ROOT = Path("dist")
PATH_DIST_PYTHON = PATH_DIST_ROOT / "niwrap-python"
PATH_DIST_JS = PATH_DIST_ROOT / "niwrap-js"


def iter_packages():
    for filename_package in PATH_PACKAGES.glob("*.json"):
        with open(filename_package) as filehandle_package:
            yield filename_package, json.load(filehandle_package)


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


def patch_section(file, replacement, token):
    # Replace text in file between <!-- START_{token} --> and <!-- END_{token} -->
    TOKEN_START = f"<!-- START_{token} -->"
    TOKEN_END = f"<!-- END_{token} -->"

    with open(file, "r", encoding="utf-8") as f:
        readme = f.read()
        start = readme.find(TOKEN_START) + len(TOKEN_START)
        end = readme.find(TOKEN_END)
        assert start >= 0
        assert end >= 0
        assert start < end
        new_readme = readme[:start] + "\n\n" + replacement + "\n" + readme[end:]

    with open(file, "w", encoding="utf-8") as f:
        f.write(new_readme)


def main():
    print("Update endpoint lists")
    update_endpoint_lists()
    print("Update repo readme")
    patch_section(
        file=Path("README.md"),
        replacement=build_package_overview_table(),
        token="PACKAGES_TABLE",
    )


if __name__ == "__main__":
    main()

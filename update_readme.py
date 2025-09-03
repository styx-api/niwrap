"""Update main repo README.md + package endpoint JSONs."""

import base64
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


def calculate_api_coverage(endpoints: list[dict[str, str]]) -> tuple[int, int, float]:
    done = sum(1 for ep in endpoints if ep["status"] == "done")
    ignored = sum(1 for ep in endpoints if ep["status"] == "ignore")
    relevant = len(endpoints) - ignored

    if relevant == 0:
        return done, relevant, 0.0

    percentage = done / relevant * 100
    return done, relevant, percentage


def svg_progress_bar(percentage: float, done: int, total: int) -> str:
    color = "#22c55e" if percentage == 100 else "#3b82f6"
    width = max(3, percentage * 1.25)

    svg = f'<svg width="125" height="24" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="r"><rect width="125" height="24" rx="8"/></clipPath></defs><g clip-path="url(#r)"><rect width="125" height="24" fill="#fff" fill-opacity=".15"/><rect width="{width}" height="24" fill="{color}"/></g><text x="62.5" y="16" text-anchor="middle" fill="#fff" font-size="12" font-weight="600" font-family="system-ui,sans-serif">{done}/{total}</text></svg>'
    
    encoded = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    return f'<img src="data:image/svg+xml;base64,{encoded}" alt="{done}/{total}">'


def build_package_overview_table() -> str:
    packages = sorted([pkg for _, pkg in iter_packages()], key=lambda x: x["name"])

    lines = [
        "| Package | Status | Version | API Coverage |",
        "| --- | --- | --- | --- |",
    ]

    for pkg in packages:
        # Package name with link
        name_link = f"[{pkg['name']}]({pkg['url']})"

        # Container version
        container_tag = pkg.get("container", "")
        if container_tag:
            docker_image = container_tag.split(":")[0]
            docker_hub = f"https://hub.docker.com/r/{docker_image}"
            container = f"[`{pkg['version']}`]({docker_hub})"
        else:
            container = "?"

        # API coverage with SVG progress bar
        done, relevant, percentage = calculate_api_coverage(pkg["api"]["endpoints"])
        if relevant == 0:
            coverage = "N/A"
        else:
            coverage = svg_progress_bar(percentage, done, relevant)

        lines.append(f"| {name_link} | {pkg['status']} | {container} | {coverage} |")

    return "\n".join(lines)


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

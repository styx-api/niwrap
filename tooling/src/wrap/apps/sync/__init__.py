"""Sync repo metadata. (E.g. update coverage tables)"""

import os
from pathlib import Path

from wrap.apps.sync.markdown_utils import (
    dict_to_markdown_table,
    markdown_url,
    progress_bar,
    patch_section,
)
from wrap.catalog_niwrap import (
    get_project_niwrap,
    get_version_niwrap,
    iter_packages_niwrap,
)


# def update_endpoint_lists():
#     package_dir = "packages"
#     descriptors_dir = "descriptors"
#     changes_summary = []

#     # Iterate through all JSON files in the packages directory
#     for package_file in os.listdir(package_dir):
#         if package_file.endswith(".json"):
#             package_path = os.path.join(package_dir, package_file)

#             # Load the package JSON file
#             with open(package_path, "r", encoding="utf-8") as f:
#                 package_data = json.load(f)

#             package_id = package_data.get("id")
#             if not package_id:
#                 print(f"Missing 'id' in {package_file}")
#                 continue

#             # Check each endpoint's descriptor
#             updated = False
#             for endpoint in package_data.get("api", {}).get("endpoints", []):
#                 target = endpoint.get("target")
#                 target = target.removeprefix("wb_command -")
#                 status = endpoint.get("status")
#                 if not target:
#                     continue

#                 descriptor_path = os.path.join(
#                     descriptors_dir, package_id, f"{target}.json"
#                 )

#                 # Check if the descriptor file exists
#                 if os.path.exists(descriptor_path):
#                     if status != "done":
#                         endpoint["status"] = "done"
#                         endpoint["descriptor"] = descriptor_path.replace("\\", "/")
#                         updated = True
#                 else:
#                     if status == "ignore":
#                         continue  # Skip if status is 'ignore'
#                     if status != "missing":
#                         endpoint["status"] = "missing"
#                         endpoint.pop("descriptor", None)  # Remove descriptor if missing
#                         updated = True

#             # If updates were made, save the updated package file
#             if updated:
#                 with open(package_path, "w", encoding="utf-8") as f:
#                     json.dump(package_data, f, indent=2)

#                 changes_summary.append(f"Updated {package_file}")


# def calculate_api_coverage(endpoints: list[dict[str, str]]) -> tuple[int, int, float]:
#     done = sum(1 for ep in endpoints if ep["status"] == "done")
#     ignored = sum(1 for ep in endpoints if ep["status"] == "ignore")
#     relevant = len(endpoints) - ignored

#     if relevant == 0:
#         return done, relevant, 0.0

#     percentage = done / relevant * 100
#     return done, relevant, percentage


def build_package_overview_table() -> str:
    packages = sorted([pkg for pkg in iter_packages_niwrap()], key=lambda x: x["name"])

    table = {
        "Package": [],
        "Default Version": [],
        "API Coverage": [],
    }

    for pkg in packages:
        # Package name with link
        name_link = markdown_url(
            pkg.get("docs", {}).get("urls", ["https://example.com"])[0], pkg["name"]
        )

        default_version = get_version_niwrap(pkg["name"], pkg["default"])

        # Container version
        container_tag = default_version.get("container", "")
        if container_tag:
            docker_image = container_tag.split(":")[0]
            container = markdown_url(
                f"https://hub.docker.com/r/{docker_image}",
                f"`{default_version['name']}`",
            )
        else:
            container = "?"

        # API coverage with SVG progress bar
        # done, relevant, percentage = calculate_api_coverage(pkg["api"]["endpoints"])
        # if relevant == 0:
        #     coverage = "N/A"
        # else:
        coverage = progress_bar(69, 100)

        table["Package"].append(name_link)
        table["Default Version"].append(container)
        table["API Coverage"].append(coverage)

    return dict_to_markdown_table(table)


def main(args):
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

    # print("Update endpoint lists")
    # update_endpoint_lists()
    print("Update repo readme")
    patch_section(
        file=Path("README.md"),
        replacement=build_package_overview_table(),
        token="PACKAGES_TABLE",
    )


def register_command(subparsers):
    sync_parser = subparsers.add_parser("sync", help="Synchronize files")

    sync_parser.set_defaults(func=main)

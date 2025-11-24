"""Sync repo metadata. (E.g. update coverage tables)"""

from pathlib import Path

from wrap.apps.find_niwrap import find_niwrap
from wrap.apps.sync.markdown_utils import (
    dict_to_markdown_table,
    markdown_url,
    patch_section,
    progress_bar,
    progress_bar_boring,
)
from wrap.catalog_niwrap import (
    get_project_niwrap,
    get_version_niwrap,
    iter_apps_niwrap,
    iter_packages_niwrap,
)


def build_package_overview_table(pretty_progress_bar=True) -> str:
    packages = sorted([pkg for pkg in iter_packages_niwrap()], key=lambda x: x["name"])

    table = {
        "Package": [],
        "Default Version": [],
        "API Coverage": [],
    }

    for pkg in packages:
        # Package name with link
        name_link = markdown_url(
            pkg.get("docs", {}).get("urls", ["https://example.com"])[0],
            pkg.get("docs", {}).get("title", pkg["name"]),
        )

        default_version = get_version_niwrap(pkg["name"], pkg["default"])

        all_apps = dict.fromkeys(default_version.get("apps", []), False)

        for app in iter_apps_niwrap(pkg["name"], pkg["default"]):
            if app.get("source"):
                all_apps[app["name"]] = True

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

        num_apps = len(all_apps)
        num_covered = sum(all_apps.values())

        coverage = (progress_bar if pretty_progress_bar else progress_bar_boring)(
            num_covered, num_apps
        )

        table["Package"].append(name_link)
        table["Default Version"].append(container)
        table["API Coverage"].append(coverage)

    return dict_to_markdown_table(table)


def main(args):
    find_niwrap()

    print("Update repo readme")
    patch_section(
        file=Path("README.md"),
        replacement=build_package_overview_table(),
        token="PACKAGES_TABLE",
    )


def register_command(subparsers):
    sync_parser = subparsers.add_parser(
        "sync", help="Synchronize metadata (i.e. build coverage tables for READMEs...)"
    )

    sync_parser.set_defaults(func=main)

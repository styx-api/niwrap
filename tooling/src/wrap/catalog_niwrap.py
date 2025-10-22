"""niwrap-specific catalog functions."""

from wrap.catalog import (
    AppContext,
    AppType,
    PackageType,
    ProjectType,
    VersionContext,
    VersionType,
    get_app,
    get_package,
    get_project,
    get_version,
    iter_apps,
    iter_packages,
    iter_versions,
)


PROJECT_NAME_NIWRAP = "niwrap"


def get_project_niwrap() -> ProjectType:
    return get_project(PROJECT_NAME_NIWRAP)


def get_package_niwrap(package_name: str) -> PackageType:
    return get_package(PROJECT_NAME_NIWRAP, package_name)


def get_version_niwrap(package_name: str, version_name: str) -> VersionType:
    return get_version(PROJECT_NAME_NIWRAP, package_name, version_name)


def get_app_niwrap(package_name: str, version_name: str, app_name: str) -> AppType:
    return get_app(PROJECT_NAME_NIWRAP, package_name, version_name, app_name)


def iter_packages_niwrap():
    project = get_project_niwrap()
    yield from iter_packages(project)


def iter_versions_niwrap(package_name: str):
    package = get_package_niwrap(package_name)
    yield from iter_versions(PROJECT_NAME_NIWRAP, package)


def iter_apps_niwrap(package_name: str, version_name: str):
    version = get_version_niwrap(package_name, version_name)
    yield from iter_apps(PROJECT_NAME_NIWRAP, package_name, version)


def iter_all_packages_niwrap():
    yield from iter_packages_niwrap()


def iter_all_versions_niwrap():
    project = get_project_niwrap()
    for package in iter_packages_niwrap():
        for version in iter_versions(PROJECT_NAME_NIWRAP, package):
            yield VersionContext(project, package, version)


def iter_all_apps_niwrap():
    project = get_project_niwrap()
    for package in iter_packages_niwrap():
        package_name = package["name"]
        for version in iter_versions(PROJECT_NAME_NIWRAP, package):
            for app in iter_apps(PROJECT_NAME_NIWRAP, package_name, version):
                yield AppContext(project, package, version, app)

"""Example functions for wrap."""

import pathlib as pl
from typing import Literal, NamedTuple, NotRequired, TypedDict

from wrap.utils import read_json

SRC_ROOT = "src"
FILE_PROJECTS = "projects.json"
FILE_PROJECT = "project.json"
FILE_PACKAGE = "package.json"
FILE_VERSION = "version.json"
FILE_APP = "app.json"


class ProjectsType(TypedDict):
    projects: list[str]
    __path__: pl.Path


class DocsType(TypedDict, total=False):
    title: str
    description: str
    authors: list[str]
    literature: list[str]
    urls: list[str]


class ProjectType(TypedDict):
    name: str
    version: str
    license: str
    packages: list[str]
    __path__: pl.Path

    docs: NotRequired[DocsType]


class PackageType(TypedDict):
    name: str
    neurodeskId: NotRequired[str]
    versions: list[str]
    default: str
    __path__: pl.Path

    docs: NotRequired[DocsType]


class ExecutablesType(TypedDict, total=False):
    required: list[str]
    ignored: list[str]


class VersionType(TypedDict):
    name: str
    __path__: pl.Path

    container: NotRequired[str]
    apps: NotRequired[list[str]]
    executables: NotRequired[ExecutablesType]
    release_date: NotRequired[str]
    deprecated: NotRequired[bool]
    docs: NotRequired[DocsType]


class DescriptorSourceType(TypedDict):
    type: Literal["boutiques"]
    path: str


class AppType(TypedDict):
    name: str
    __path__: pl.Path

    exe: NotRequired[str]
    args: NotRequired[list[str]]
    source: NotRequired[DescriptorSourceType]
    docs: NotRequired[DocsType]


def get_projects() -> ProjectsType:
    path = pl.Path(SRC_ROOT) / FILE_PROJECTS
    data = read_json(path)
    data["__path__"] = path
    return data


def get_project(project_name: str) -> ProjectType:
    path = pl.Path(SRC_ROOT) / project_name / FILE_PROJECT
    data = read_json(path)
    data["__path__"] = path
    return data


def get_package(project_name: str, package_name: str) -> PackageType:
    path = pl.Path(SRC_ROOT) / project_name / package_name / FILE_PACKAGE
    data = read_json(path)
    data["__path__"] = path
    return data


def get_version(project_name: str, package_name: str, version_name: str) -> VersionType:
    path = pl.Path(SRC_ROOT) / project_name / package_name / version_name / FILE_VERSION
    data = read_json(path)
    data["__path__"] = path
    return data


def get_app(
    project_name: str, package_name: str, version_name: str, app_name: str
) -> AppType:
    path = (
        pl.Path(SRC_ROOT)
        / project_name
        / package_name
        / version_name
        / app_name
        / FILE_APP
    )
    data = read_json(path)
    data["__path__"] = path
    return data


def iter_projects(projects: ProjectsType):
    for name in projects["projects"]:
        yield get_project(name)


def iter_packages(project: ProjectType):
    project_name = project["name"]
    for package_name in project["packages"]:
        yield get_package(project_name, package_name)


def iter_versions(project_name: str, package: PackageType):
    package_name = package["name"]
    for version_name in package["versions"]:
        yield get_version(project_name, package_name, version_name)


def iter_apps(project_name: str, package_name: str, version: VersionType):
    version_name = version["name"]
    if "apps" in version:
        for app_name in version["apps"]:
            yield get_app(project_name, package_name, version_name, app_name)


class PackageContext(NamedTuple):
    project: ProjectType
    package: PackageType


class VersionContext(NamedTuple):
    project: ProjectType
    package: PackageType
    version: VersionType


class AppContext(NamedTuple):
    project: ProjectType
    package: PackageType
    version: VersionType
    app: AppType


def iter_all_packages(projects: ProjectsType):
    for project in iter_projects(projects):
        for package in iter_packages(project):
            yield PackageContext(project, package)


def iter_all_versions(projects: ProjectsType):
    for project in iter_projects(projects):
        project_name = project["name"]
        for package in iter_packages(project):
            for version in iter_versions(project_name, package):
                yield VersionContext(project, package, version)


def iter_all_apps(projects: ProjectsType):
    for project in iter_projects(projects):
        project_name = project["name"]
        for package in iter_packages(project):
            package_name = package["name"]
            for version in iter_versions(project_name, package):
                for app in iter_apps(project_name, package_name, version):
                    yield AppContext(project, package, version, app)

"""NiWrap project discovery."""

from wrap.catalog import ProjectType
from wrap.catalog_niwrap import get_project_niwrap


def find_niwrap() -> ProjectType:
    """Find and return the NiWrap project from the current or parent directory."""
    try:
        project = get_project_niwrap()
    except Exception:
        import os

        os.chdir("..")
        try:
            project = get_project_niwrap()
        except Exception as e:
            raise FileNotFoundError(
                "Could not find NiWrap project. "
                "This needs to be run from the NiWrap repo root."
            ) from e

    title = project.get("docs", {}).get("title", project["name"])
    print(f"Found {title} version {project['version']} repo.")

    return project

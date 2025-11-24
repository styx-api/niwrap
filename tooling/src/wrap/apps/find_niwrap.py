from wrap.catalog_niwrap import get_project_niwrap


def find_niwrap():
    try:
        project = get_project_niwrap()
    except:
        import os

        os.chdir("..")
        try:
            project = get_project_niwrap()
        except:
            raise Exception("Error: This needs to be run in the NiWrap repo root.")

    print(
        f"Found {project.get('docs', {}).get('title', project['name'])} version {project['version']} repo."
    )

    return project

from wrap.apps.test.test import run_tests

from wrap.catalog_niwrap import get_project_niwrap

# TEST IMPORTS:
import wrap.apps.test.boutiques.test_schema  # noqa: F401
import wrap.apps.test.boutiques.test_command_line  # noqa: F401
import wrap.apps.test.boutiques.test_optional_default_value  # noqa: F401
import wrap.apps.test.boutiques.test_path_template  # noqa: F401
import wrap.apps.test.boutiques.test_value_keys  # noqa: F401


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

    run_tests()


def register_command(subparsers):
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.add_argument("pattern", nargs="?", default="*")
    test_parser.set_defaults(func=main)

from typing import Any

import wrap.apps.test.boutiques.test_command_line  # noqa: F401
import wrap.apps.test.boutiques.test_optional_default_value  # noqa: F401
import wrap.apps.test.boutiques.test_path_template  # noqa: F401
import wrap.apps.test.boutiques.test_schema  # noqa: F401
import wrap.apps.test.boutiques.test_value_keys  # noqa: F401
from wrap.apps.find_niwrap import find_niwrap
from wrap.apps.test.test import run_tests


def main(args: Any) -> None:
    find_niwrap()

    run_tests()


def register_command(subparsers: Any) -> None:
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.add_argument("pattern", nargs="?", default="*")
    test_parser.set_defaults(func=main)

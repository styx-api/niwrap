from typing import Any
from wrap.apps.test.test import test_boutiques, ok, error

import pathlib as pl
import re


@test_boutiques
def test_invalid_chars(path: pl.Path, data: Any):
    """Ensure 'path-template' does not contain invalid characters (e.g. glob)."""

    command_line = data.get("command-line")
    if not command_line:
        return error("No command-line found")

    invalid_keys = set()
    pattern = r"[<>:\"\\|?*]+"

    for output_item in data.get("output-files", []):
        value = output_item.get("path-template")
        if value and re.search(pattern, value):
            invalid_keys.add(value)

    if invalid_keys:
        invalid_list = "\n".join("  " + key for key in invalid_keys)
        return error(f"Found path-templates with invalid format:\n{invalid_list}")

    return ok()

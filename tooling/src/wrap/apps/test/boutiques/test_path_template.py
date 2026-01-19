import pathlib as pl
import re
from typing import Any

from wrap.apps.test.test import error, ok, test_boutiques


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


@test_boutiques
def test_duplicate_path_templates(path: pl.Path, data: Any):
    """Ensure there are no duplicate 'path-template' values across output-files."""
    output_files = data.get("output-files", [])
    if not output_files:
        return ok()

    seen: dict[str, list[str]] = {}
    for output_item in output_files:
        value = output_item.get("path-template")
        if value:
            output_id = output_item.get("id", "<unknown>")
            seen.setdefault(value, []).append(output_id)

    duplicates = {template: ids for template, ids in seen.items() if len(ids) > 1}

    if duplicates:
        dup_list = "\n".join(
            f"  '{template}' used by: {', '.join(ids)}"
            for template, ids in duplicates.items()
        )
        return error(f"Found duplicate path-templates:\n{dup_list}")

    return ok()

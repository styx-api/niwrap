import pathlib as pl
import re
from collections import defaultdict
from typing import Any

from wrap.apps.test.test import error, ok, test_boutiques


@test_boutiques
def test_unused_value_keys(path: pl.Path, data: Any):
    """All input value-keys should be used in the command-line."""
    command_line = data.get("command-line")
    if not command_line:
        return error("No command-line found")

    # Collect all value-keys from inputs
    value_keys = set()
    for input_item in data.get("inputs", []):
        value_key = input_item.get("value-key")
        if value_key:
            value_keys.add(value_key)

    # Check each value-key appears in command-line
    unused_keys = set()
    for value_key in value_keys:
        if value_key not in command_line:
            unused_keys.add(value_key)

    if unused_keys:
        unused_list = "\n".join("  " + key for key in unused_keys)
        return error(f"Found unused value-keys:\n{unused_list}")

    return ok()


@test_boutiques
def test_unmapped_command_entries(path: pl.Path, data: Any):
    """All [UPPER_CASE] entries in command-line should match input value-keys."""
    command_line = data.get("command-line")
    if not command_line:
        return error("No command-line found")

    # Collect all value-keys from inputs
    value_keys = set()
    for input_item in data.get("inputs", []):
        value_key = input_item.get("value-key")
        if value_key:
            value_keys.add(value_key)

    # Find all [UPPER_CASE] patterns in command-line
    pattern = r"\[([A-Z0-9_]+)\]"
    command_entries = set(re.findall(pattern, command_line))

    # Check each command entry has matching value-key
    unmapped_entries = set()
    for entry in command_entries:
        if f"[{entry}]" not in value_keys:
            unmapped_entries.add(entry)

    if unmapped_entries:
        unmapped_list = "\n".join("  [" + entry + "]" for entry in unmapped_entries)
        return error(
            f"Found command-line entries without matching value-keys:\n{unmapped_list}"
        )

    return ok()


@test_boutiques
def test_value_key_format(path: pl.Path, data: Any):
    """All value-keys should follow the [UPPER_CASE] format."""
    invalid_keys = set()
    pattern = r"^\[[A-Z0-9_]+\]$"

    for input_item in data.get("inputs", []):
        value_key = input_item.get("value-key")
        if value_key and not re.match(pattern, value_key):
            invalid_keys.add(value_key)

    if invalid_keys:
        invalid_list = "\n".join("  " + key for key in invalid_keys)
        return error(f"Found value-keys with invalid format:\n{invalid_list}")

    return ok()


@test_boutiques
def test_duplicate_command_value_key(path: pl.Path, data: Any):
    """All input value keys should be unique."""
    command_line = data.get("command-line")
    if not command_line:
        return error("No command-line found")

    # Check each value-key only appears once
    pattern = r"\[([A-Z0-9_]+)\]"
    command_entries = set(re.findall(pattern, command_line))

    seen, duplicates = set(), set()
    for value_key in command_entries:
        if value_key in seen:
            duplicates.add(value_key)
        else:
            seen.add(value_key)

    if len(duplicates) > 0:
        duplicate_list = "\n".join("  " + key for key in duplicates)
        return error(f"Found duplicate value-keys:\n{duplicate_list}")

    return ok()


@test_boutiques
def test_aliased_inputs(path: pl.Path, data: Any):
    """Ensure inputs are using subcommands or unique value-keys."""
    aliased_input = defaultdict(list)
    for input_item in data.get("inputs", []):
        value_key = input_item.get("value-key")
        if value_key is None:
            continue
        aliased_input[value_key].append(input_item.get("command-line-flag"))

    aliased_input = {k: v for k, v in aliased_input.items() if len(v) > 1}

    if aliased_input:
        aliased_list = "\n".join("  " + f"{k}: {v}" for k, v in aliased_input.items())
        return error(f"Found aliased value-keys:\n{aliased_list}")

    return ok()

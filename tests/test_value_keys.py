import glob
import json
import re

import pytest


def load_descriptors():
    return glob.glob("descriptors/**/*.json", recursive=True)


@pytest.mark.parametrize("descriptor_path", load_descriptors())
class TestInputValueKeys:
    def test_unused_value_keys(self, descriptor_path):
        """All input value-keys should be used in the command-line."""

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        command_line = descriptor.get("command-line")
        assert command_line, f"No command-line found in {descriptor_path}"

        # Collect all value-keys from inputs
        value_keys = set()
        for input_item in descriptor.get("inputs", []):
            value_key = input_item.get("value-key")
            if value_key:
                value_keys.add(value_key)

        # Check each value-key appears in command-line
        unused_keys = set()
        for value_key in value_keys:
            if value_key not in command_line:
                unused_keys.add(value_key)

        assert not unused_keys, (
            f"Found unused value-keys in {descriptor_path}:\n"
            f"{chr(10).join('  ' + key for key in unused_keys)}"
        )

    def test_unmapped_command_entries(self, descriptor_path):
        """All [UPPER_CASE] entries in command-line should match input value-keys."""

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        command_line = descriptor.get("command-line")
        assert command_line, f"No command-line found in {descriptor_path}"

        # Collect all value-keys from inputs
        value_keys = set()
        for input_item in descriptor.get("inputs", []):
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

        assert not unmapped_entries, (
            f"Found command-line entries without matching value-keys in {descriptor_path}:\n"
            f"{chr(10).join('  [' + entry + ']' for entry in unmapped_entries)}"
        )

    def test_value_key_format(self, descriptor_path):
        """All value-keys should follow the [UPPER_CASE] format."""

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        invalid_keys = set()
        pattern = r"^\[[A-Z0-9_]+\]$"

        for input_item in descriptor.get("inputs", []):
            value_key = input_item.get("value-key")
            if value_key and not re.match(pattern, value_key):
                invalid_keys.add(value_key)

        assert not invalid_keys, (
            f"Found value-keys with invalid format in {descriptor_path}:\n"
            f"{chr(10).join('  ' + key for key in invalid_keys)}"
        )

    def test_duplicate_value_key(self, descriptor_path):
        """All input value keys should be unique."""
        with open(descriptor_path) as f:
            descriptor = json.load(f)

        command_line = descriptor.get("command-line")
        assert command_line, f"No command-line found in {descriptor_path}"

        # Check each value-key only appears once
        seen = set()
        duplicates = set()
        for value_key in command_line.split():
            if value_key in seen:
                duplicates.add(value_key)
            else:
                seen.add(value_key)

        assert len(duplicates) == 0, (
            f"Found duplicate value-keys in {descriptor_path}:\n"
            f"{chr(10).join('  ' + key for key in duplicates)}"
        )

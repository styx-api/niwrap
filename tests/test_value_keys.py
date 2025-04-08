import glob
import json
import re
from collections import defaultdict

import pytest


def load_descriptors():
    return glob.glob("descriptors/**/*.json", recursive=True)


@pytest.mark.parametrize("descriptor_path", load_descriptors())
class TestInputValueKeys:
    def load_descriptor(self, descriptor_path):
        """Load individual descriptor."""
        with open(descriptor_path) as f:
            descriptor = json.load(f)

        command_line = descriptor.get("command-line")
        assert command_line, f"No command-line found in {descriptor_path}"

        return descriptor, command_line

    def test_unused_value_keys(self, descriptor_path):
        """All input value-keys should be used in the command-line."""
        descriptor, command_line = self.load_descriptor(descriptor_path)

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
        descriptor, command_line = self.load_descriptor(descriptor_path)

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
        descriptor, _ = self.load_descriptor(descriptor_path)

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

    def test_duplicate_command_value_key(self, descriptor_path):
        """All input value keys should be unique."""
        descriptor, command_line = self.load_descriptor(descriptor_path)

        # Check each value-key only appears once
        pattern = r"\[([A-Z0-9_]+)\]"
        command_entries = set(re.findall(pattern, command_line))

        seen, duplicates = set(), set()
        for value_key in command_entries:
            if value_key in seen:
                duplicates.add(value_key)
            else:
                seen.add(value_key)

        assert len(duplicates) == 0, (
            f"Found duplicate value-keys in {descriptor_path}:\n"
            f"{chr(10).join('  ' + key for key in duplicates)}"
        )

    def test_aliased_inputs(self, descriptor_path):
        """Ensure inputs are using subcommands or unique value-keys."""
        descriptor, _ = self.load_descriptor(descriptor_path)

        aliased_input = defaultdict(list)
        for input_item in descriptor.get("inputs", []):
            value_key = input_item.get("value-key")
            if value_key is None:
                continue
            aliased_input[value_key].append(input_item.get("command-line-flag"))

        aliased_input = {k: v for k, v in aliased_input.items() if len(v) > 1}

        assert aliased_input == {}, (
            f"Found aliased value-keys in {descriptor_path}:\n"
            f"{chr(10).join('  ' + f'{k}: {v}' for k, v in aliased_input.items())}"
        )

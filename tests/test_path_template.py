import glob
import json
import re
from collections import defaultdict

import pytest


def load_descriptors():
    return glob.glob("descriptors/**/*.json", recursive=True)


@pytest.mark.parametrize("descriptor_path", load_descriptors())
class TestOutputPathTemplate:
    def load_descriptor(self, descriptor_path):
        """Load individual descriptor."""
        with open(descriptor_path) as f:
            descriptor = json.load(f)

        command_line = descriptor.get("command-line")
        assert command_line, f"No command-line found in {descriptor_path}"

        return descriptor, command_line

    def test_invalid_chars(self, descriptor_path):
        """Ensure 'path-template' does not contain invalid characters (e.g. glob)."""
        descriptor, _ = self.load_descriptor(descriptor_path)

        invalid_keys = set()
        pattern = r"[<>:\"\\|?*]+"

        for output_item in descriptor.get("output-files", []):
            value = output_item.get("path-template")
            if value and re.search(pattern, value):
                invalid_keys.add(value)

        assert not invalid_keys, (
            f"Found path-templates with invalid format in {descriptor_path}:\n"
            f"{chr(10).join('  ' + key for key in invalid_keys)}"
        )

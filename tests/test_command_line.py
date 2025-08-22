import pytest
import glob
import json


def load_descriptors():
    return glob.glob("descriptors/**/*.json", recursive=True)


SUSPICIOUS_CHARS = [
    "  ",  # double space
    *"<>|&%/\\´`#'+~@\"-\t\n=:.,;(){}§€$?!^°",
]


@pytest.mark.parametrize("descriptor_path", load_descriptors())
class TestCommandLine:
    def test_suspicious_command_line(self, descriptor_path):
        """Command-line fields should not contain suspicious characters."""

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        command_line = descriptor.get("command-line")
        name = descriptor.get("name", "")

        assert isinstance(command_line, str), (
            f"Command-line missing in {descriptor_path}"
        )

        # Remove first wb_command subcommand
        command_line_clean = command_line.removeprefix("wb_command -").removeprefix(
            name
        )

        for sus in SUSPICIOUS_CHARS:
            if sus in command_line_clean:
                assert False, f"Suspicious string '{sus}' in '{command_line}'"

    def test_command_line_starts_with_name(self, descriptor_path):
        """Command-line fields should start with name followed by a space."""

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        name = descriptor.get("name", None)
        command_line = descriptor.get("command-line", None)

        assert name, "Descriptor has no name"
        assert command_line, "Descriptor has no command-line"

        # Remove wb_command prefix
        command_line_clean = command_line.removeprefix("wb_command -")

        # Check if 'command-line' starts with 'name' followed by a space
        assert command_line_clean.startswith(f"{name} "), (
            f"Name {name} does not match command-line '{command_line}'"
        )

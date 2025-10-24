from typing import Any
from wrap.apps.test.test import test_boutiques, ok, error

import pathlib as pl


SUSPICIOUS_CHARS = [
    "  ",  # double space
    *"<>|&%/\\´`#'+~@\"-\t\n=:.,;(){}§€$?!^°",
]


@test_boutiques
def test_suspicious_command_line(path: pl.Path, data: Any):
    """Command-line fields should not contain suspicious characters."""

    command_line = data.get("command-line")
    name = data.get("name", "")

    if not isinstance(command_line, str):
        return error("Command-line missing")

    # todo: remove
    # Remove first wb_command subcommand
    command_line_clean = command_line.removeprefix("wb_command -").removeprefix(name)

    for sus in SUSPICIOUS_CHARS:
        if sus in command_line_clean:
            return error(f"Suspicious string '{sus}' in '{command_line}'")

    return ok()


@test_boutiques
def test_command_line_starts_with_name(path: pl.Path, data: Any):
    """Command-line fields should start with name followed by a space."""

    name = data.get("name", None)
    command_line = data.get("command-line", None)

    if not name:
        error("Descriptor has no name")
    if not command_line:
        error("Descriptor has no command-line")

    # Remove wb_command prefix
    command_line_clean = command_line.removeprefix("wb_command -")

    # Check if 'command-line' starts with 'name' followed by a space
    if not command_line_clean.startswith(f"{name} "):
        error(f"Name {name} does not match command-line '{command_line}'")

    return ok()

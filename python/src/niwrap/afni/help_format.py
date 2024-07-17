# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

HELP_FORMAT_METADATA = Metadata(
    id="549ff7dfec4d36f3418f69489e6a52f6dd8008ed",
    name="help_format",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="unknown",
)


class HelpFormatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `help_format(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    formatted_output: OutputPathType
    """The formatted text with hyperlinks"""


def help_format(
    stdin: str,
    runner: Runner | None = None,
) -> HelpFormatOutputs:
    """
    help_format by Unknown.
    
    Formats text by converting URLs into HTML hyperlinks.
    
    Args:
        stdin: Standard input text to be formatted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HelpFormatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HELP_FORMAT_METADATA)
    cargs = []
    cargs.append("help_format")
    ret = HelpFormatOutputs(
        root=execution.output_file("."),
        formatted_output=execution.output_file(f"formatted_output.html"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "HELP_FORMAT_METADATA",
    "HelpFormatOutputs",
    "help_format",
]

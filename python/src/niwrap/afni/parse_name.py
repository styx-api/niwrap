# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PARSE_NAME_METADATA = Metadata(
    id="a67788b0c0514057052216aadee90c72b904dbb1.boutiques",
    name="ParseName",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ParseNameOutputs(typing.NamedTuple):
    """
    Output object returned when calling `parse_name(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def parse_name(
    runner: Runner | None = None,
) -> ParseNameOutputs:
    """
    Parses filename into components useful for AFNI.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/ParseName.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ParseNameOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PARSE_NAME_METADATA)
    cargs = []
    cargs.append("ParseName")
    cargs.append("[OPTIONAL_PARAMETERS]")
    cargs.append("<FName>")
    ret = ParseNameOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PARSE_NAME_METADATA",
    "ParseNameOutputs",
    "parse_name",
]

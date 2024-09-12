# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__PARSE_NAME_METADATA = Metadata(
    id="dc595da5a1d86ec673a1a5f7595c19d7c38fd4ad.boutiques",
    name="@parse_name",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VParseNameOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__parse_name(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_path: OutputPathType
    """The path of the filename"""
    output_prefix: OutputPathType
    """The prefix of the filename"""
    output_extension: OutputPathType
    """The extension of the filename"""


def v__parse_name(
    name: str,
    runner: Runner | None = None,
) -> VParseNameOutputs:
    """
    A script to parse a filename into path, prefix, and extension strings.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@parse_name.html
    
    Args:
        name: The filename to parse.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VParseNameOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__PARSE_NAME_METADATA)
    cargs = []
    cargs.append("@parse_name")
    cargs.append(name)
    ret = VParseNameOutputs(
        root=execution.output_file("."),
        output_path=execution.output_file(name + "_path"),
        output_prefix=execution.output_file(name + "_prefix"),
        output_extension=execution.output_file(name + "_extension"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VParseNameOutputs",
    "V__PARSE_NAME_METADATA",
    "v__parse_name",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__STATAUXCODE_METADATA = Metadata(
    id="f6c1767e1a9b29b920fca298ee485697451c9d8a.boutiques",
    name="@statauxcode",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VStatauxcodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__statauxcode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """Output file containing the result of the conversion"""


def v__statauxcode(
    code_: str,
    runner: Runner | None = None,
) -> VStatauxcodeOutputs:
    """
    Returns the name or number of a statistics code based on specified mappings.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        code_: The statistical code or its numerical equivalent to be\
            converted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VStatauxcodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__STATAUXCODE_METADATA)
    cargs = []
    cargs.append("@statauxcode")
    cargs.append(code_)
    ret = VStatauxcodeOutputs(
        root=execution.output_file("."),
        output=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VStatauxcodeOutputs",
    "V__STATAUXCODE_METADATA",
    "v__statauxcode",
]

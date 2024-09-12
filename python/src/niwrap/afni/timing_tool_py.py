# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TIMING_TOOL_PY_METADATA = Metadata(
    id="44a18ee84951e77612dd8bc063de7bce71b77863.boutiques",
    name="timing_tool.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class TimingToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `timing_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_timing_file: OutputPathType
    """Output timing file as specified"""
    timing_to_1_d_output: OutputPathType
    """Output 1D formatted stimulus data"""


def timing_tool_py(
    runner: Runner | None = None,
) -> TimingToolPyOutputs:
    """
    Tool for manipulating and evaluating stimulus timing files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/timing_tool.py.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TimingToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TIMING_TOOL_PY_METADATA)
    cargs = []
    cargs.append("timing_tool.py")
    cargs.append("[COMMANDS]")
    ret = TimingToolPyOutputs(
        root=execution.output_file("."),
        output_timing_file=execution.output_file("[OUTPUT_FILE]"),
        timing_to_1_d_output=execution.output_file("[TIMING_TO_1D_FILE]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TIMING_TOOL_PY_METADATA",
    "TimingToolPyOutputs",
    "timing_tool_py",
]

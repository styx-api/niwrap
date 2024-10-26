# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONCAT_BVARS_METADATA = Metadata(
    id="5283f97ed637a2315c5de4abba7730176df76ea8.boutiques",
    name="concat_bvars",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class ConcatBvarsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `concat_bvars(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Concatenated output .bvars file"""


def concat_bvars(
    output_bvars: InputPathType,
    runner: Runner | None = None,
) -> ConcatBvarsOutputs:
    """
    Concatenate multiple .bvars files into a single .bvars file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_bvars: Output .bvars file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConcatBvarsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONCAT_BVARS_METADATA)
    cargs = []
    cargs.append("concat_bvars")
    cargs.append(execution.input_file(output_bvars))
    cargs.append("[INPUT_BVARS...]")
    ret = ConcatBvarsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(output_bvars).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONCAT_BVARS_METADATA",
    "ConcatBvarsOutputs",
    "concat_bvars",
]

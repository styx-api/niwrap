# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLINTERLEAVE_METADATA = Metadata(
    id="81664bf9535c37ba0485f9a84b1dc7b328fb4fb2.boutiques",
    name="fslinterleave",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslinterleaveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslinterleave(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    interleaved_output: OutputPathType
    """Interleaved output image"""


def fslinterleave(
    infile1: InputPathType,
    infile2: InputPathType,
    outfile: str,
    reverse_slice_order_flag: bool = False,
    runner: Runner | None = None,
) -> FslinterleaveOutputs:
    """
    Interleaves two input images slice-by-slice to produce an output image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile1: First input image.
        infile2: Second input image.
        outfile: Output interleaved image.
        reverse_slice_order_flag: Reverse slice order.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslinterleaveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLINTERLEAVE_METADATA)
    cargs = []
    cargs.append("fslinterleave")
    cargs.append(execution.input_file(infile1))
    cargs.append(execution.input_file(infile2))
    cargs.append(outfile)
    if reverse_slice_order_flag:
        cargs.append("-i")
    ret = FslinterleaveOutputs(
        root=execution.output_file("."),
        interleaved_output=execution.output_file(outfile + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLINTERLEAVE_METADATA",
    "FslinterleaveOutputs",
    "fslinterleave",
]

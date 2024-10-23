# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCC_METADATA = Metadata(
    id="39e2d4230b27cc7b8202577c5ebeea8323d5f9cd.boutiques",
    name="fslcc",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslccOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslcc(
    first_input: InputPathType,
    second_input: InputPathType,
    mask: InputPathType | None = None,
    noabs_flag: bool = False,
    nodemean_flag: bool = False,
    threshold: float | None = 0.1,
    decimal_places: float | None = 2,
    runner: Runner | None = None,
) -> FslccOutputs:
    """
    Cross-correlate two time-series, timepoint by timepoint.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        first_input: First input time-series.
        second_input: Second input time-series.
        mask: Mask file name.
        noabs_flag: Don't return absolute values (keep sign).
        nodemean_flag: Don't demean the input files.
        threshold: Threshold (default 0.1).
        decimal_places: Number of decimal places to display in output (default\
            2).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslccOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCC_METADATA)
    cargs = []
    cargs.append("fslcc")
    cargs.append(execution.input_file(first_input))
    cargs.append(execution.input_file(second_input))
    if mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask)
        ])
    if noabs_flag:
        cargs.append("--noabs")
    if nodemean_flag:
        cargs.append("--nodemean")
    if threshold is not None:
        cargs.extend([
            "-t",
            str(threshold)
        ])
    if decimal_places is not None:
        cargs.extend([
            "-p",
            str(decimal_places)
        ])
    ret = FslccOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLCC_METADATA",
    "FslccOutputs",
    "fslcc",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SWAP_SUBJECTWISE_METADATA = Metadata(
    id="cba7139360838bd3ee999955a172ec36a1bbee24.boutiques",
    name="swap_subjectwise",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SwapSubjectwiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swap_subjectwise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def swap_subjectwise(
    dyads: InputPathType,
    fmean: InputPathType,
    mask: InputPathType | None = None,
    obasename: str | None = None,
    xthresh: float | None = None,
    averageonly_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> SwapSubjectwiseOutputs:
    """
    Reordering of the dyadic vectors and fsamples according to average inter-subject
    modal orientations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        dyads: List of list of dyads.
        fmean: List of list of mean fsamples.
        mask: Filename of brain mask.
        obasename: Output obasename [default=swapped].
        xthresh: A.R.D. threshold - default=0.1.
        averageonly_flag: Average only?.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SwapSubjectwiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SWAP_SUBJECTWISE_METADATA)
    cargs = []
    cargs.append("swap_subjectwise")
    cargs.extend([
        "-r",
        execution.input_file(dyads)
    ])
    cargs.extend([
        "-f",
        execution.input_file(fmean)
    ])
    if mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask)
        ])
    if obasename is not None:
        cargs.extend([
            "-b",
            obasename
        ])
    if xthresh is not None:
        cargs.extend([
            "--xthresh",
            str(xthresh)
        ])
    if averageonly_flag:
        cargs.append("--averageonly")
    if verbose_flag:
        cargs.append("--verbose")
    ret = SwapSubjectwiseOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SWAP_SUBJECTWISE_METADATA",
    "SwapSubjectwiseOutputs",
    "swap_subjectwise",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__COMPUTE_GCOR_METADATA = Metadata(
    id="b94ef87dbf1368c4e5a1039cde31a45efb508360.boutiques",
    name="@compute_gcor",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VComputeGcorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__compute_gcor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corr_vol_brik: OutputPathType | None
    """Output correlation volume BRIK file"""
    corr_vol_head: OutputPathType | None
    """Output correlation volume HEAD file"""


def v__compute_gcor(
    input_: InputPathType,
    mask: InputPathType | None = None,
    corr_vol_prefix: str | None = None,
    initial_trs: float | None = None,
    no_demean: bool = False,
    save_tmp: bool = False,
    verbose: float | None = None,
    runner: Runner | None = None,
) -> VComputeGcorOutputs:
    """
    Compute GCOR, the global correlation.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@compute_gcor.html
    
    Args:
        input_: Specify input dataset to compute the GCOR over.
        mask: Specify mask dataset, for restricting the computation.
        corr_vol_prefix: Specify prefix for correlation volume output.
        initial_trs: Specify number of initial TRs to ignore.
        no_demean: Do not demean as the first step.
        save_tmp: Save temporary files (do not remove at end).
        verbose: Set verbose level (0=quiet, 3=max).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VComputeGcorOutputs`).
    """
    if verbose is not None and not (0 <= verbose <= 3): 
        raise ValueError(f"'verbose' must be between 0 <= x <= 3 but was {verbose}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__COMPUTE_GCOR_METADATA)
    cargs = []
    cargs.append("@compute_gcor")
    cargs.append(execution.input_file(input_))
    if mask is not None:
        cargs.append(execution.input_file(mask))
    if corr_vol_prefix is not None:
        cargs.extend([
            "-corr_vol",
            corr_vol_prefix
        ])
    if initial_trs is not None:
        cargs.extend([
            "-nfirst",
            str(initial_trs)
        ])
    if no_demean:
        cargs.append("-no_demean")
    if save_tmp:
        cargs.append("-savetmp")
    if verbose is not None:
        cargs.extend([
            "-verb",
            str(verbose)
        ])
    ret = VComputeGcorOutputs(
        root=execution.output_file("."),
        corr_vol_brik=execution.output_file(corr_vol_prefix + "+tlrc.BRIK") if (corr_vol_prefix is not None) else None,
        corr_vol_head=execution.output_file(corr_vol_prefix + "+tlrc.HEAD") if (corr_vol_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VComputeGcorOutputs",
    "V__COMPUTE_GCOR_METADATA",
    "v__compute_gcor",
]

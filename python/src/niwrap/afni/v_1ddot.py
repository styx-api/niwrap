# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1DDOT_METADATA = Metadata(
    id="89e3bea294b27fb22b4f6d2f28db83dbf8daea66.boutiques",
    name="1ddot",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1ddotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1ddot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout_output: OutputPathType
    """Output correlation or covariance matrix printed to stdout."""


def v_1ddot(
    input_files: list[InputPathType],
    one_flag: bool = False,
    dem_flag: bool = False,
    cov_flag: bool = False,
    inn_flag: bool = False,
    rank_flag: bool = False,
    terse_flag: bool = False,
    okzero_flag: bool = False,
    runner: Runner | None = None,
) -> V1ddotOutputs:
    """
    Computes the correlation matrix of the input 1D files and their inverse
    correlation matrix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input 1D files.
        one_flag: Make 1st vector be all 1's.
        dem_flag: Remove mean from all vectors (conflicts with '-one').
        cov_flag: Compute with covariance matrix instead of correlation.
        inn_flag: Compute with inner product matrix instead.
        rank_flag: Compute Spearman rank correlation instead (also implies\
            '-terse').
        terse_flag: Output only the correlation or covariance matrix without\
            any garnish.
        okzero_flag: Do not quit if a vector is all zeros. The correlation\
            matrix will have 0 where NaNs ought to go.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1ddotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DDOT_METADATA)
    cargs = []
    cargs.append("1ddot")
    if one_flag:
        cargs.append("-one")
    if dem_flag:
        cargs.append("-dem")
    if cov_flag:
        cargs.append("-cov")
    if inn_flag:
        cargs.append("-inn")
    if rank_flag:
        cargs.append("-rank")
    if terse_flag:
        cargs.append("-terse")
    if okzero_flag:
        cargs.append("-okzero")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.append(">")
    cargs.append("stdout.txt")
    ret = V1ddotOutputs(
        root=execution.output_file("."),
        stdout_output=execution.output_file("stdout.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1ddotOutputs",
    "V_1DDOT_METADATA",
    "v_1ddot",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GRAD_UNWARP_METADATA = Metadata(
    id="5eba6b18ea47c7542212c1e8983cc8a9d0f64b9e.boutiques",
    name="grad_unwarp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class GradUnwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `grad_unwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mgh_output: OutputPathType
    """Output file in MGH format"""
    cor_output: OutputPathType
    """Output directory in COR format"""


def grad_unwarp(
    infile: InputPathType,
    outfile: str,
    seriesno: str | None = None,
    unwarp_type: str | None = None,
    nojac: bool = False,
    corfov: bool = False,
    cor: bool = False,
    interp: str | None = None,
    matlab_binary: str | None = "/space/lyon/6/pubsw/common/matlab/6.5/bin/matlab",
    runner: Runner | None = None,
) -> GradUnwarpOutputs:
    """
    Convert, dewarp, and resample DICOM files to MGH files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file or directory (dcmfile, dcmdir, or mghfile).
        outfile: Output file in MGH format.
        seriesno: DICOM series number, required if input is a directory.
        unwarp_type: Gradient unwarping displacement type or map file (required\
            for MGH file).
        nojac: Do not perform jacobian correction when unwarping.
        corfov: Resample to Coronal FOV.
        cor: Output in COR format instead of MGH.
        interp: Interpolation method (cubic, linear, nearest, spline).
        matlab_binary: Path to the Matlab binary, version 6.5 or higher\
            required.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GradUnwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GRAD_UNWARP_METADATA)
    cargs = []
    cargs.append("grad_unwarp")
    cargs.append(execution.input_file(infile))
    if seriesno is not None:
        cargs.extend([
            "-s",
            seriesno
        ])
    if unwarp_type is not None:
        cargs.extend([
            "-unwarp",
            unwarp_type
        ])
    if nojac:
        cargs.append("-nojac")
    if corfov:
        cargs.append("-corfov")
    if cor:
        cargs.append("-cor")
    if interp is not None:
        cargs.extend([
            "-interp",
            interp
        ])
    cargs.extend([
        "-o",
        outfile
    ])
    if matlab_binary is not None:
        cargs.extend([
            "-matlab",
            matlab_binary
        ])
    ret = GradUnwarpOutputs(
        root=execution.output_file("."),
        mgh_output=execution.output_file(outfile),
        cor_output=execution.output_file(outfile + "/"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GRAD_UNWARP_METADATA",
    "GradUnwarpOutputs",
    "grad_unwarp",
]

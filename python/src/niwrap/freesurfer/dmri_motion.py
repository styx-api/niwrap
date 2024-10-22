# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_MOTION_METADATA = Metadata(
    id="048916457dffa5f7ad56158093c3d50d93fd7f6c.boutiques",
    name="dmri_motion",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriMotionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_motion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    motion_measures_out: OutputPathType
    """Output file of motion measures"""
    frame_by_frame_out: OutputPathType | None
    """Output frame-by-frame motion measures file"""


def dmri_motion(
    outfile: InputPathType,
    outf: InputPathType | None = None,
    mat: InputPathType | None = None,
    dwi: list[InputPathType] | None = None,
    bval: list[InputPathType] | None = None,
    threshold: float | None = 100,
    diffusivity: float | None = 0.001,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DmriMotionOutputs:
    """
    A tool for calculating motion measures from DWI scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outfile: Output text file of motion measures.
        outf: Output text file of frame-by-frame motion measures.
        mat: Input text file of volume-to-baseline affine transformations.
        dwi: Input DWI scan(s), unprocessed.
        bval: Input b-value table(s), one per scan.
        threshold: Low-b image intensity threshold.
        diffusivity: Nominal diffusivity.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriMotionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_MOTION_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/dmri_motion")
    cargs.append("--out")
    cargs.extend([
        "--out",
        execution.input_file(outfile)
    ])
    if outf is not None:
        cargs.extend([
            "--outf",
            execution.input_file(outf)
        ])
    if mat is not None:
        cargs.extend([
            "--mat",
            execution.input_file(mat)
        ])
    if dwi is not None:
        cargs.extend([
            "--dwi",
            *[execution.input_file(f) for f in dwi]
        ])
    if bval is not None:
        cargs.extend([
            "--bval",
            *[execution.input_file(f) for f in bval]
        ])
    if threshold is not None:
        cargs.extend([
            "--T",
            str(threshold)
        ])
    if diffusivity is not None:
        cargs.extend([
            "--D",
            str(diffusivity)
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = DmriMotionOutputs(
        root=execution.output_file("."),
        motion_measures_out=execution.output_file(pathlib.Path(outfile).name),
        frame_by_frame_out=execution.output_file(pathlib.Path(outf).name) if (outf is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_MOTION_METADATA",
    "DmriMotionOutputs",
    "dmri_motion",
]

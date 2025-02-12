# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_MOTION_METADATA = Metadata(
    id="e4e3f3c86352739f602bc72ec495f7919e215248.boutiques",
    name="dmri_motion",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriMotionParameters = typing.TypedDict('DmriMotionParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_motion"],
    "outfile": InputPathType,
    "outf": typing.NotRequired[InputPathType | None],
    "mat": typing.NotRequired[InputPathType | None],
    "dwi": typing.NotRequired[list[InputPathType] | None],
    "bval": typing.NotRequired[list[InputPathType] | None],
    "threshold": typing.NotRequired[float | None],
    "diffusivity": typing.NotRequired[float | None],
    "debug": bool,
    "checkopts": bool,
    "help": bool,
    "version": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "dmri_motion": dmri_motion_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "dmri_motion": dmri_motion_outputs,
    }.get(t)


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


def dmri_motion_params(
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
) -> DmriMotionParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_motion",
        "outfile": outfile,
        "debug": debug,
        "checkopts": checkopts,
        "help": help_,
        "version": version,
    }
    if outf is not None:
        params["outf"] = outf
    if mat is not None:
        params["mat"] = mat
    if dwi is not None:
        params["dwi"] = dwi
    if bval is not None:
        params["bval"] = bval
    if threshold is not None:
        params["threshold"] = threshold
    if diffusivity is not None:
        params["diffusivity"] = diffusivity
    return params


def dmri_motion_cargs(
    params: DmriMotionParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("dmri_motion")
    cargs.extend([
        "--out",
        execution.input_file(params.get("outfile"))
    ])
    if params.get("outf") is not None:
        cargs.extend([
            "--outf",
            execution.input_file(params.get("outf"))
        ])
    if params.get("mat") is not None:
        cargs.extend([
            "--mat",
            execution.input_file(params.get("mat"))
        ])
    if params.get("dwi") is not None:
        cargs.extend([
            "--dwi",
            *[execution.input_file(f) for f in params.get("dwi")]
        ])
    if params.get("bval") is not None:
        cargs.extend([
            "--bval",
            *[execution.input_file(f) for f in params.get("bval")]
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--T",
            str(params.get("threshold"))
        ])
    if params.get("diffusivity") is not None:
        cargs.extend([
            "--D",
            str(params.get("diffusivity"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def dmri_motion_outputs(
    params: DmriMotionParameters,
    execution: Execution,
) -> DmriMotionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriMotionOutputs(
        root=execution.output_file("."),
        motion_measures_out=execution.output_file(pathlib.Path(params.get("outfile")).name),
        frame_by_frame_out=execution.output_file(pathlib.Path(params.get("outf")).name) if (params.get("outf") is not None) else None,
    )
    return ret


def dmri_motion_execute(
    params: DmriMotionParameters,
    execution: Execution,
) -> DmriMotionOutputs:
    """
    A tool for calculating motion measures from DWI scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriMotionOutputs`).
    """
    cargs = dmri_motion_cargs(params, execution)
    ret = dmri_motion_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = dmri_motion_params(outfile=outfile, outf=outf, mat=mat, dwi=dwi, bval=bval, threshold=threshold, diffusivity=diffusivity, debug=debug, checkopts=checkopts, help_=help_, version=version)
    return dmri_motion_execute(params, execution)


__all__ = [
    "DMRI_MOTION_METADATA",
    "DmriMotionOutputs",
    "DmriMotionParameters",
    "dmri_motion",
    "dmri_motion_params",
]

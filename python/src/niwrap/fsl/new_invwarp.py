# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

NEW_INVWARP_METADATA = Metadata(
    id="c1339243d2b878297e61fc1b6693396e5c46a980.boutiques",
    name="new_invwarp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
NewInvwarpParameters = typing.TypedDict('NewInvwarpParameters', {
    "__STYX_TYPE__": typing.Literal["new_invwarp"],
    "warpvol": InputPathType,
    "outvol": str,
    "refvol": InputPathType,
    "relflag": bool,
    "absflag": bool,
    "noconstraintflag": bool,
    "jmin": typing.NotRequired[float | None],
    "jmax": typing.NotRequired[float | None],
    "debugflag": bool,
    "verboseflag": bool,
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
        "new_invwarp": new_invwarp_cargs,
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
        "new_invwarp": new_invwarp_outputs,
    }.get(t)


class NewInvwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `new_invwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_volume: OutputPathType
    """Output inverse warped volume"""


def new_invwarp_params(
    warpvol: InputPathType,
    outvol: str,
    refvol: InputPathType,
    relflag: bool = False,
    absflag: bool = False,
    noconstraintflag: bool = False,
    jmin: float | None = 0.01,
    jmax: float | None = 100.0,
    debugflag: bool = False,
    verboseflag: bool = False,
) -> NewInvwarpParameters:
    """
    Build parameters.
    
    Args:
        warpvol: Filename for warp/shiftmap transform (volume).
        outvol: Filename for output (inverse warped) image.
        refvol: Filename for new reference image, i.e., what was originally the\
            input image (determines inverse warpvol's FOV and pixdims).
        relflag: Use relative warp convention: x' = x + w(x).
        absflag: Use absolute warp convention (default): x' = w(x).
        noconstraintflag: Do not apply the Jacobian constraint.
        jmin: Minimum acceptable Jacobian value for constraint (default 0.01).
        jmax: Maximum acceptable Jacobian value for constraint (default 100.0).
        debugflag: Turn on debugging output.
        verboseflag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "new_invwarp",
        "warpvol": warpvol,
        "outvol": outvol,
        "refvol": refvol,
        "relflag": relflag,
        "absflag": absflag,
        "noconstraintflag": noconstraintflag,
        "debugflag": debugflag,
        "verboseflag": verboseflag,
    }
    if jmin is not None:
        params["jmin"] = jmin
    if jmax is not None:
        params["jmax"] = jmax
    return params


def new_invwarp_cargs(
    params: NewInvwarpParameters,
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
    cargs.append("invwarp")
    cargs.extend([
        "-w",
        execution.input_file(params.get("warpvol"))
    ])
    cargs.extend([
        "-o",
        params.get("outvol")
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("refvol"))
    ])
    if params.get("relflag"):
        cargs.append("--rel")
    if params.get("absflag"):
        cargs.append("--abs")
    if params.get("noconstraintflag"):
        cargs.append("--noconstraint")
    if params.get("jmin") is not None:
        cargs.extend([
            "--jmin",
            str(params.get("jmin"))
        ])
    if params.get("jmax") is not None:
        cargs.extend([
            "--jmax",
            str(params.get("jmax"))
        ])
    if params.get("debugflag"):
        cargs.append("--debug")
    if params.get("verboseflag"):
        cargs.append("-v")
    return cargs


def new_invwarp_outputs(
    params: NewInvwarpParameters,
    execution: Execution,
) -> NewInvwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = NewInvwarpOutputs(
        root=execution.output_file("."),
        out_volume=execution.output_file(params.get("outvol")),
    )
    return ret


def new_invwarp_execute(
    params: NewInvwarpParameters,
    execution: Execution,
) -> NewInvwarpOutputs:
    """
    Inverse warp tool from FSL suite.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `NewInvwarpOutputs`).
    """
    cargs = new_invwarp_cargs(params, execution)
    ret = new_invwarp_outputs(params, execution)
    execution.run(cargs)
    return ret


def new_invwarp(
    warpvol: InputPathType,
    outvol: str,
    refvol: InputPathType,
    relflag: bool = False,
    absflag: bool = False,
    noconstraintflag: bool = False,
    jmin: float | None = 0.01,
    jmax: float | None = 100.0,
    debugflag: bool = False,
    verboseflag: bool = False,
    runner: Runner | None = None,
) -> NewInvwarpOutputs:
    """
    Inverse warp tool from FSL suite.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        warpvol: Filename for warp/shiftmap transform (volume).
        outvol: Filename for output (inverse warped) image.
        refvol: Filename for new reference image, i.e., what was originally the\
            input image (determines inverse warpvol's FOV and pixdims).
        relflag: Use relative warp convention: x' = x + w(x).
        absflag: Use absolute warp convention (default): x' = w(x).
        noconstraintflag: Do not apply the Jacobian constraint.
        jmin: Minimum acceptable Jacobian value for constraint (default 0.01).
        jmax: Maximum acceptable Jacobian value for constraint (default 100.0).
        debugflag: Turn on debugging output.
        verboseflag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NewInvwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NEW_INVWARP_METADATA)
    params = new_invwarp_params(warpvol=warpvol, outvol=outvol, refvol=refvol, relflag=relflag, absflag=absflag, noconstraintflag=noconstraintflag, jmin=jmin, jmax=jmax, debugflag=debugflag, verboseflag=verboseflag)
    return new_invwarp_execute(params, execution)


__all__ = [
    "NEW_INVWARP_METADATA",
    "NewInvwarpOutputs",
    "NewInvwarpParameters",
    "new_invwarp",
    "new_invwarp_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CHECK_RECONS_SH_METADATA = Metadata(
    id="52142d2a907acd3a0d9631fc56bcb011b2c8e9af.boutiques",
    name="check_recons.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
CheckReconsShParameters = typing.TypedDict('CheckReconsShParameters', {
    "__STYX_TYPE__": typing.Literal["check_recons.sh"],
    "subject_directory": typing.NotRequired[str | None],
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
        "check_recons.sh": check_recons_sh_cargs,
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
    }.get(t)


class CheckReconsShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `check_recons_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def check_recons_sh_params(
    subject_directory: str | None = None,
) -> CheckReconsShParameters:
    """
    Build parameters.
    
    Args:
        subject_directory: Directory where subjects are being processed. If not\
            specified, uses SUBJECTS_DIR.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "check_recons.sh",
    }
    if subject_directory is not None:
        params["subject_directory"] = subject_directory
    return params


def check_recons_sh_cargs(
    params: CheckReconsShParameters,
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
    cargs.append("check_recons.sh")
    if params.get("subject_directory") is not None:
        cargs.append(params.get("subject_directory"))
    return cargs


def check_recons_sh_outputs(
    params: CheckReconsShParameters,
    execution: Execution,
) -> CheckReconsShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CheckReconsShOutputs(
        root=execution.output_file("."),
    )
    return ret


def check_recons_sh_execute(
    params: CheckReconsShParameters,
    execution: Execution,
) -> CheckReconsShOutputs:
    """
    Checks the status of subjects being processed by recon-all in the SUBJECTS_DIR
    or a specified directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CheckReconsShOutputs`).
    """
    cargs = check_recons_sh_cargs(params, execution)
    ret = check_recons_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def check_recons_sh(
    subject_directory: str | None = None,
    runner: Runner | None = None,
) -> CheckReconsShOutputs:
    """
    Checks the status of subjects being processed by recon-all in the SUBJECTS_DIR
    or a specified directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_directory: Directory where subjects are being processed. If not\
            specified, uses SUBJECTS_DIR.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CheckReconsShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CHECK_RECONS_SH_METADATA)
    params = check_recons_sh_params(subject_directory=subject_directory)
    return check_recons_sh_execute(params, execution)


__all__ = [
    "CHECK_RECONS_SH_METADATA",
    "CheckReconsShOutputs",
    "CheckReconsShParameters",
    "check_recons_sh",
    "check_recons_sh_params",
]

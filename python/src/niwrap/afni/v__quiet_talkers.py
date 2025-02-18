# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__QUIET_TALKERS_METADATA = Metadata(
    id="b3ed968e44cf181f4b5122510d5d661ee6ef707c.boutiques",
    name="@Quiet_Talkers",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VQuietTalkersParameters = typing.TypedDict('VQuietTalkersParameters', {
    "__STYX_TYPE__": typing.Literal["@Quiet_Talkers"],
    "sudo": bool,
    "prog": typing.NotRequired[list[str] | None],
    "npb_val": typing.NotRequired[list[float] | None],
    "npb_range": typing.NotRequired[list[float] | None],
    "pif_key": typing.NotRequired[str | None],
    "no_npb": bool,
    "list": bool,
    "quiet": bool,
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
        "@Quiet_Talkers": v__quiet_talkers_cargs,
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


class VQuietTalkersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__quiet_talkers(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__quiet_talkers_params(
    sudo: bool = False,
    prog: list[str] | None = None,
    npb_val: list[float] | None = None,
    npb_range: list[float] | None = None,
    pif_key: str | None = None,
    no_npb: bool = False,
    list_: bool = False,
    quiet: bool = False,
) -> VQuietTalkersParameters:
    """
    Build parameters.
    
    Args:
        sudo: Invoke higher powers to kill processes that you do not own.
        prog: Instead of the default program list, only kill the specified\
            program. You can use multiple -prog options.
        npb_val: Kill those programs using NIML port block NV.
        npb_range: Kill those using NIML port blocks between NV0 and NV1.
        pif_key: Kill those programs that have a string matching KEY_STRING in\
            their commandline.
        no_npb: Kill any program in the list regardless of -npb options or -pif.
        list_: Just list process numbers, don't run kill command.
        quiet: Do it quietly.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@Quiet_Talkers",
        "sudo": sudo,
        "no_npb": no_npb,
        "list": list_,
        "quiet": quiet,
    }
    if prog is not None:
        params["prog"] = prog
    if npb_val is not None:
        params["npb_val"] = npb_val
    if npb_range is not None:
        params["npb_range"] = npb_range
    if pif_key is not None:
        params["pif_key"] = pif_key
    return params


def v__quiet_talkers_cargs(
    params: VQuietTalkersParameters,
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
    cargs.append("@Quiet_Talkers")
    if params.get("sudo"):
        cargs.append("-sudo")
    if params.get("prog") is not None:
        cargs.extend([
            "-prog",
            *params.get("prog")
        ])
    if params.get("npb_val") is not None:
        cargs.extend([
            "-npb_val",
            *map(str, params.get("npb_val"))
        ])
    if params.get("npb_range") is not None:
        cargs.extend([
            "-npb_range",
            *map(str, params.get("npb_range"))
        ])
    if params.get("pif_key") is not None:
        cargs.extend([
            "-pif",
            params.get("pif_key")
        ])
    if params.get("no_npb"):
        cargs.append("-no_npb")
    if params.get("list"):
        cargs.append("-list")
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v__quiet_talkers_outputs(
    params: VQuietTalkersParameters,
    execution: Execution,
) -> VQuietTalkersOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VQuietTalkersOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__quiet_talkers_execute(
    params: VQuietTalkersParameters,
    execution: Execution,
) -> VQuietTalkersOutputs:
    """
    A script to find and kill AFNI processes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VQuietTalkersOutputs`).
    """
    cargs = v__quiet_talkers_cargs(params, execution)
    ret = v__quiet_talkers_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__quiet_talkers(
    sudo: bool = False,
    prog: list[str] | None = None,
    npb_val: list[float] | None = None,
    npb_range: list[float] | None = None,
    pif_key: str | None = None,
    no_npb: bool = False,
    list_: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> VQuietTalkersOutputs:
    """
    A script to find and kill AFNI processes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        sudo: Invoke higher powers to kill processes that you do not own.
        prog: Instead of the default program list, only kill the specified\
            program. You can use multiple -prog options.
        npb_val: Kill those programs using NIML port block NV.
        npb_range: Kill those using NIML port blocks between NV0 and NV1.
        pif_key: Kill those programs that have a string matching KEY_STRING in\
            their commandline.
        no_npb: Kill any program in the list regardless of -npb options or -pif.
        list_: Just list process numbers, don't run kill command.
        quiet: Do it quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VQuietTalkersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__QUIET_TALKERS_METADATA)
    params = v__quiet_talkers_params(sudo=sudo, prog=prog, npb_val=npb_val, npb_range=npb_range, pif_key=pif_key, no_npb=no_npb, list_=list_, quiet=quiet)
    return v__quiet_talkers_execute(params, execution)


__all__ = [
    "VQuietTalkersOutputs",
    "VQuietTalkersParameters",
    "V__QUIET_TALKERS_METADATA",
    "v__quiet_talkers",
    "v__quiet_talkers_params",
]

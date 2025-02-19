# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_GROUP_METADATA = Metadata(
    id="62e5f1536c9234b5603d09f4124d51072e3633cc.boutiques",
    name="dmri_group",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


DmriGroupParameters = typing.TypedDict('DmriGroupParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_group"],
    "input_list": InputPathType,
    "reference_volume": InputPathType,
    "output_base": str,
    "no_interpolation": bool,
    "sections_num": typing.NotRequired[float | None],
    "debug_mode": bool,
    "check_options": bool,
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
        "dmri_group": dmri_group_cargs,
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


class DmriGroupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_group(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_group_params(
    input_list: InputPathType,
    reference_volume: InputPathType,
    output_base: str,
    no_interpolation: bool = False,
    sections_num: float | None = None,
    debug_mode: bool = False,
    check_options: bool = False,
) -> DmriGroupParameters:
    """
    Build parameters.
    
    Args:
        input_list: Text file with list of individual inputs.
        reference_volume: Reference volume for output path.
        output_base: Base name of output stats files.
        no_interpolation: Do not attempt to interpolate along-tract measures\
            (Assume that subjects are sampled at equivalent positions).
        sections_num: Divide the pathway into a number of sections and output\
            average measures for each section.
        debug_mode: Turn on debugging.
        check_options: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_group",
        "input_list": input_list,
        "reference_volume": reference_volume,
        "output_base": output_base,
        "no_interpolation": no_interpolation,
        "debug_mode": debug_mode,
        "check_options": check_options,
    }
    if sections_num is not None:
        params["sections_num"] = sections_num
    return params


def dmri_group_cargs(
    params: DmriGroupParameters,
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
    cargs.append("dmri_group")
    cargs.extend([
        "--list",
        execution.input_file(params.get("input_list"))
    ])
    cargs.extend([
        "--ref",
        execution.input_file(params.get("reference_volume"))
    ])
    cargs.extend([
        "--out",
        params.get("output_base")
    ])
    if params.get("no_interpolation"):
        cargs.append("--nointerp")
    if params.get("sections_num") is not None:
        cargs.extend([
            "--sec",
            str(params.get("sections_num"))
        ])
    if params.get("debug_mode"):
        cargs.append("--debug")
    if params.get("check_options"):
        cargs.append("--checkopts")
    return cargs


def dmri_group_outputs(
    params: DmriGroupParameters,
    execution: Execution,
) -> DmriGroupOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriGroupOutputs(
        root=execution.output_file("."),
    )
    return ret


def dmri_group_execute(
    params: DmriGroupParameters,
    execution: Execution,
) -> DmriGroupOutputs:
    """
    A tool to process and analyze diffusion MRI group data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriGroupOutputs`).
    """
    params = execution.params(params)
    cargs = dmri_group_cargs(params, execution)
    ret = dmri_group_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_group(
    input_list: InputPathType,
    reference_volume: InputPathType,
    output_base: str,
    no_interpolation: bool = False,
    sections_num: float | None = None,
    debug_mode: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> DmriGroupOutputs:
    """
    A tool to process and analyze diffusion MRI group data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_list: Text file with list of individual inputs.
        reference_volume: Reference volume for output path.
        output_base: Base name of output stats files.
        no_interpolation: Do not attempt to interpolate along-tract measures\
            (Assume that subjects are sampled at equivalent positions).
        sections_num: Divide the pathway into a number of sections and output\
            average measures for each section.
        debug_mode: Turn on debugging.
        check_options: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriGroupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_GROUP_METADATA)
    params = dmri_group_params(
        input_list=input_list,
        reference_volume=reference_volume,
        output_base=output_base,
        no_interpolation=no_interpolation,
        sections_num=sections_num,
        debug_mode=debug_mode,
        check_options=check_options,
    )
    return dmri_group_execute(params, execution)


__all__ = [
    "DMRI_GROUP_METADATA",
    "DmriGroupOutputs",
    "DmriGroupParameters",
    "dmri_group",
    "dmri_group_params",
]

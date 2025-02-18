# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BORDER_RESAMPLE_METADATA = Metadata(
    id="d357466427d16b11843a0546984cb79a3677dbe1.boutiques",
    name="border-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
BorderResampleParameters = typing.TypedDict('BorderResampleParameters', {
    "__STYX_TYPE__": typing.Literal["border-resample"],
    "border_in": InputPathType,
    "current_sphere": InputPathType,
    "new_sphere": InputPathType,
    "border_out": str,
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
        "border-resample": border_resample_cargs,
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
        "border-resample": border_resample_outputs,
    }.get(t)


class BorderResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_out: OutputPathType
    """the output border file"""


def border_resample_params(
    border_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    border_out: str,
) -> BorderResampleParameters:
    """
    Build parameters.
    
    Args:
        border_in: the border file to resample.
        current_sphere: a sphere surface with the mesh that the metric is\
            currently on.
        new_sphere: a sphere surface that is in register with <current-sphere>\
            and has the desired output mesh.
        border_out: the output border file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "border-resample",
        "border_in": border_in,
        "current_sphere": current_sphere,
        "new_sphere": new_sphere,
        "border_out": border_out,
    }
    return params


def border_resample_cargs(
    params: BorderResampleParameters,
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
    cargs.append("wb_command")
    cargs.append("-border-resample")
    cargs.append(execution.input_file(params.get("border_in")))
    cargs.append(execution.input_file(params.get("current_sphere")))
    cargs.append(execution.input_file(params.get("new_sphere")))
    cargs.append(params.get("border_out"))
    return cargs


def border_resample_outputs(
    params: BorderResampleParameters,
    execution: Execution,
) -> BorderResampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BorderResampleOutputs(
        root=execution.output_file("."),
        border_out=execution.output_file(params.get("border_out")),
    )
    return ret


def border_resample_execute(
    params: BorderResampleParameters,
    execution: Execution,
) -> BorderResampleOutputs:
    """
    Resample a border file to a different mesh.
    
    Resamples a border file, given two spherical surfaces that are in register.
    Only borders that have the same structure as current-sphere will be
    resampled.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BorderResampleOutputs`).
    """
    cargs = border_resample_cargs(params, execution)
    ret = border_resample_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def border_resample(
    border_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    border_out: str,
    runner: Runner | None = None,
) -> BorderResampleOutputs:
    """
    Resample a border file to a different mesh.
    
    Resamples a border file, given two spherical surfaces that are in register.
    Only borders that have the same structure as current-sphere will be
    resampled.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        border_in: the border file to resample.
        current_sphere: a sphere surface with the mesh that the metric is\
            currently on.
        new_sphere: a sphere surface that is in register with <current-sphere>\
            and has the desired output mesh.
        border_out: the output border file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_RESAMPLE_METADATA)
    params = border_resample_params(border_in=border_in, current_sphere=current_sphere, new_sphere=new_sphere, border_out=border_out)
    return border_resample_execute(params, execution)


__all__ = [
    "BORDER_RESAMPLE_METADATA",
    "BorderResampleOutputs",
    "BorderResampleParameters",
    "border_resample",
    "border_resample_params",
]

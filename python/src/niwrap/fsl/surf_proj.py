# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_PROJ_METADATA = Metadata(
    id="5abc9adaff464bbe30dc6eaec1fb7d7d51988f84.boutiques",
    name="surf_proj",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SurfProjParameters = typing.TypedDict('SurfProjParameters', {
    "__STYX_TYPE__": typing.Literal["surf_proj"],
    "data": InputPathType,
    "surface": InputPathType,
    "output_file": str,
    "surface_reference": typing.NotRequired[InputPathType | None],
    "transform": typing.NotRequired[InputPathType | None],
    "meshspace": typing.NotRequired[str | None],
    "step_size": typing.NotRequired[float | None],
    "direction": typing.NotRequired[float | None],
    "operation": typing.NotRequired[str | None],
    "surface_output": typing.NotRequired[str | None],
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
        "surf_proj": surf_proj_cargs,
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
        "surf_proj": surf_proj_outputs,
    }.get(t)


class SurfProjOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_proj(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    projected_output: OutputPathType
    """Output of the projection"""
    output_surface: OutputPathType | None
    """Output surface file"""


def surf_proj_params(
    data: InputPathType,
    surface: InputPathType,
    output_file: str,
    surface_reference: InputPathType | None = None,
    transform: InputPathType | None = None,
    meshspace: str | None = None,
    step_size: float | None = None,
    direction: float | None = None,
    operation: str | None = None,
    surface_output: str | None = None,
) -> SurfProjParameters:
    """
    Build parameters.
    
    Args:
        data: Data to project onto surface.
        surface: Surface file.
        output_file: Output file.
        surface_reference: Surface volume reference (default=same as data).
        transform: Data to surface transform (default=Identity).
        meshspace: Mesh space (default='caret').
        step_size: Average over step (mm - default=1).
        direction: If >0 goes towards brain (default=0 i.e. both directions).
        operation: What to do with values: 'mean' (default), 'max', 'median',\
            'last'.
        surface_output: Output surface file, not ASCII matrix (valid only for\
            scalars).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surf_proj",
        "data": data,
        "surface": surface,
        "output_file": output_file,
    }
    if surface_reference is not None:
        params["surface_reference"] = surface_reference
    if transform is not None:
        params["transform"] = transform
    if meshspace is not None:
        params["meshspace"] = meshspace
    if step_size is not None:
        params["step_size"] = step_size
    if direction is not None:
        params["direction"] = direction
    if operation is not None:
        params["operation"] = operation
    if surface_output is not None:
        params["surface_output"] = surface_output
    return params


def surf_proj_cargs(
    params: SurfProjParameters,
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
    cargs.append("surf_proj")
    cargs.extend([
        "-data",
        execution.input_file(params.get("data"))
    ])
    cargs.extend([
        "-surf",
        execution.input_file(params.get("surface"))
    ])
    cargs.extend([
        "-out",
        params.get("output_file")
    ])
    if params.get("surface_reference") is not None:
        cargs.extend([
            "--meshref",
            execution.input_file(params.get("surface_reference"))
        ])
    if params.get("transform") is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(params.get("transform"))
        ])
    if params.get("meshspace") is not None:
        cargs.extend([
            "--meshspace",
            params.get("meshspace")
        ])
    if params.get("step_size") is not None:
        cargs.extend([
            "--step",
            str(params.get("step_size"))
        ])
    if params.get("direction") is not None:
        cargs.extend([
            "--direction",
            str(params.get("direction"))
        ])
    if params.get("operation") is not None:
        cargs.extend([
            "--operation",
            params.get("operation")
        ])
    if params.get("surface_output") is not None:
        cargs.extend([
            "--surfout",
            params.get("surface_output")
        ])
    return cargs


def surf_proj_outputs(
    params: SurfProjParameters,
    execution: Execution,
) -> SurfProjOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfProjOutputs(
        root=execution.output_file("."),
        projected_output=execution.output_file(params.get("output_file")),
        output_surface=execution.output_file(params.get("surface_output")) if (params.get("surface_output") is not None) else None,
    )
    return ret


def surf_proj_execute(
    params: SurfProjParameters,
    execution: Execution,
) -> SurfProjOutputs:
    """
    Projects data onto a surface mesh using specified parameters.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfProjOutputs`).
    """
    params = execution.params(params)
    cargs = surf_proj_cargs(params, execution)
    ret = surf_proj_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_proj(
    data: InputPathType,
    surface: InputPathType,
    output_file: str,
    surface_reference: InputPathType | None = None,
    transform: InputPathType | None = None,
    meshspace: str | None = None,
    step_size: float | None = None,
    direction: float | None = None,
    operation: str | None = None,
    surface_output: str | None = None,
    runner: Runner | None = None,
) -> SurfProjOutputs:
    """
    Projects data onto a surface mesh using specified parameters.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        data: Data to project onto surface.
        surface: Surface file.
        output_file: Output file.
        surface_reference: Surface volume reference (default=same as data).
        transform: Data to surface transform (default=Identity).
        meshspace: Mesh space (default='caret').
        step_size: Average over step (mm - default=1).
        direction: If >0 goes towards brain (default=0 i.e. both directions).
        operation: What to do with values: 'mean' (default), 'max', 'median',\
            'last'.
        surface_output: Output surface file, not ASCII matrix (valid only for\
            scalars).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfProjOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_PROJ_METADATA)
    params = surf_proj_params(
        data=data,
        surface=surface,
        output_file=output_file,
        surface_reference=surface_reference,
        transform=transform,
        meshspace=meshspace,
        step_size=step_size,
        direction=direction,
        operation=operation,
        surface_output=surface_output,
    )
    return surf_proj_execute(params, execution)


__all__ = [
    "SURF_PROJ_METADATA",
    "SurfProjOutputs",
    "SurfProjParameters",
    "surf_proj",
    "surf_proj_params",
]

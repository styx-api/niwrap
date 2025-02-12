# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_MC_METADATA = Metadata(
    id="60a4e6264f565573c6fbb9368b3b82aa19a0f230.boutiques",
    name="mri_mc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriMcParameters = typing.TypedDict('MriMcParameters', {
    "__STYX_TYPE__": typing.Literal["mri_mc"],
    "input_volume": InputPathType,
    "label_value": float,
    "output_surface": str,
    "connectivity": typing.NotRequired[float | None],
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
        "mri_mc": mri_mc_cargs,
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
        "mri_mc": mri_mc_outputs,
    }.get(t)


class MriMcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    extracted_surface: OutputPathType
    """The extracted surface output file."""


def mri_mc_params(
    input_volume: InputPathType,
    label_value: float,
    output_surface: str,
    connectivity: float | None = 1,
) -> MriMcParameters:
    """
    Build parameters.
    
    Args:
        input_volume: The input volume from which to extract the surface.
        label_value: The label value of the structure to extract.
        output_surface: The file where the extracted surface mesh will be\
            saved.
        connectivity: The connectivity used for Marching Cubes. Options are:\
            1=6+, 2=18, 3=6, 4=26.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_mc",
        "input_volume": input_volume,
        "label_value": label_value,
        "output_surface": output_surface,
    }
    if connectivity is not None:
        params["connectivity"] = connectivity
    return params


def mri_mc_cargs(
    params: MriMcParameters,
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
    cargs.append("mri_mc")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(str(params.get("label_value")))
    if params.get("connectivity") is not None:
        cargs.append(params.get("output_surface") + str(params.get("connectivity")))
    return cargs


def mri_mc_outputs(
    params: MriMcParameters,
    execution: Execution,
) -> MriMcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMcOutputs(
        root=execution.output_file("."),
        extracted_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mri_mc_execute(
    params: MriMcParameters,
    execution: Execution,
) -> MriMcOutputs:
    """
    Extract a surface from a label volume using Marching Cubes algorithm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMcOutputs`).
    """
    cargs = mri_mc_cargs(params, execution)
    ret = mri_mc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_mc(
    input_volume: InputPathType,
    label_value: float,
    output_surface: str,
    connectivity: float | None = 1,
    runner: Runner | None = None,
) -> MriMcOutputs:
    """
    Extract a surface from a label volume using Marching Cubes algorithm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: The input volume from which to extract the surface.
        label_value: The label value of the structure to extract.
        output_surface: The file where the extracted surface mesh will be\
            saved.
        connectivity: The connectivity used for Marching Cubes. Options are:\
            1=6+, 2=18, 3=6, 4=26.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MC_METADATA)
    params = mri_mc_params(input_volume=input_volume, label_value=label_value, output_surface=output_surface, connectivity=connectivity)
    return mri_mc_execute(params, execution)


__all__ = [
    "MRI_MC_METADATA",
    "MriMcOutputs",
    "MriMcParameters",
    "mri_mc",
    "mri_mc_params",
]

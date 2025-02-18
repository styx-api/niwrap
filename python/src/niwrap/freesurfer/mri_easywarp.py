# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EASYWARP_METADATA = Metadata(
    id="61155dbff21df2a7da1b05052571570b740944be.boutiques",
    name="mri_easywarp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriEasywarpParameters = typing.TypedDict('MriEasywarpParameters', {
    "__STYX_TYPE__": typing.Literal["mri_easywarp"],
    "input_image": InputPathType,
    "output_image": str,
    "deformation_field": typing.NotRequired[InputPathType | None],
    "nearest_neighbor": bool,
    "num_threads": typing.NotRequired[float | None],
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
        "mri_easywarp": mri_easywarp_cargs,
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
        "mri_easywarp": mri_easywarp_outputs,
    }.get(t)


class MriEasywarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_easywarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_deformed_image: OutputPathType
    """Output deformed image"""


def mri_easywarp_params(
    input_image: InputPathType,
    output_image: str,
    deformation_field: InputPathType | None = None,
    nearest_neighbor: bool = False,
    num_threads: float | None = None,
) -> MriEasywarpParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image.
        output_image: Output (deformed) image.
        deformation_field: Deformation field.
        nearest_neighbor: Use nearest neighbor (rather than linear)\
            interpolation.
        num_threads: Number of cores to be used. Default is 1. You can use -1\
            to use all available cores.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_easywarp",
        "input_image": input_image,
        "output_image": output_image,
        "nearest_neighbor": nearest_neighbor,
    }
    if deformation_field is not None:
        params["deformation_field"] = deformation_field
    if num_threads is not None:
        params["num_threads"] = num_threads
    return params


def mri_easywarp_cargs(
    params: MriEasywarpParameters,
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
    cargs.append("mri_easywarp")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_image"))
    ])
    cargs.extend([
        "--o",
        params.get("output_image")
    ])
    if params.get("deformation_field") is not None:
        cargs.extend([
            "--field",
            execution.input_file(params.get("deformation_field"))
        ])
    if params.get("nearest_neighbor"):
        cargs.append("--nearest")
    if params.get("num_threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("num_threads"))
        ])
    return cargs


def mri_easywarp_outputs(
    params: MriEasywarpParameters,
    execution: Execution,
) -> MriEasywarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriEasywarpOutputs(
        root=execution.output_file("."),
        output_deformed_image=execution.output_file(params.get("output_image") + ".nii.gz"),
    )
    return ret


def mri_easywarp_execute(
    params: MriEasywarpParameters,
    execution: Execution,
) -> MriEasywarpOutputs:
    """
    EasyReg: deep learning registration simple and easy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriEasywarpOutputs`).
    """
    cargs = mri_easywarp_cargs(params, execution)
    ret = mri_easywarp_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_easywarp(
    input_image: InputPathType,
    output_image: str,
    deformation_field: InputPathType | None = None,
    nearest_neighbor: bool = False,
    num_threads: float | None = None,
    runner: Runner | None = None,
) -> MriEasywarpOutputs:
    """
    EasyReg: deep learning registration simple and easy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input image.
        output_image: Output (deformed) image.
        deformation_field: Deformation field.
        nearest_neighbor: Use nearest neighbor (rather than linear)\
            interpolation.
        num_threads: Number of cores to be used. Default is 1. You can use -1\
            to use all available cores.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEasywarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EASYWARP_METADATA)
    params = mri_easywarp_params(input_image=input_image, output_image=output_image, deformation_field=deformation_field, nearest_neighbor=nearest_neighbor, num_threads=num_threads)
    return mri_easywarp_execute(params, execution)


__all__ = [
    "MRI_EASYWARP_METADATA",
    "MriEasywarpOutputs",
    "MriEasywarpParameters",
    "mri_easywarp",
    "mri_easywarp_params",
]

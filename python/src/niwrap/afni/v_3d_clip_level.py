# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_CLIP_LEVEL_METADATA = Metadata(
    id="d74c5cd045e053e286d1b5c8e3587d88d871f128.boutiques",
    name="3dClipLevel",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dClipLevelParameters = typing.TypedDict('V3dClipLevelParameters', {
    "__STYX_TYPE__": typing.Literal["3dClipLevel"],
    "dataset": InputPathType,
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
        "3dClipLevel": v_3d_clip_level_cargs,
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


class V3dClipLevelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_clip_level(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_clip_level_params(
    dataset: InputPathType,
) -> V3dClipLevelParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset (e.g. dataset.nii.gz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dClipLevel",
        "dataset": dataset,
    }
    return params


def v_3d_clip_level_cargs(
    params: V3dClipLevelParameters,
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
    cargs.append("3dClipLevel")
    cargs.append("[options]")
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_clip_level_outputs(
    params: V3dClipLevelParameters,
    execution: Execution,
) -> V3dClipLevelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dClipLevelOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_clip_level_execute(
    params: V3dClipLevelParameters,
    execution: Execution,
) -> V3dClipLevelOutputs:
    """
    Estimates the value at which to clip the anatomical dataset so that background
    regions are set to zero.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dClipLevelOutputs`).
    """
    cargs = v_3d_clip_level_cargs(params, execution)
    ret = v_3d_clip_level_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_clip_level(
    dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dClipLevelOutputs:
    """
    Estimates the value at which to clip the anatomical dataset so that background
    regions are set to zero.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset (e.g. dataset.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dClipLevelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CLIP_LEVEL_METADATA)
    params = v_3d_clip_level_params(dataset=dataset)
    return v_3d_clip_level_execute(params, execution)


__all__ = [
    "V3dClipLevelOutputs",
    "V3dClipLevelParameters",
    "V_3D_CLIP_LEVEL_METADATA",
    "v_3d_clip_level",
    "v_3d_clip_level_params",
]

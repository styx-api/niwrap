# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_SHARPEN_METADATA = Metadata(
    id="44eead3d035544b0d1ef18d1ea40f5df1b442bcb.boutiques",
    name="3dSharpen",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dSharpenParameters = typing.TypedDict('V3dSharpenParameters', {
    "__STYX_TYPE__": typing.Literal["3dSharpen"],
    "sharpening_factor": typing.NotRequired[float | None],
    "input_dataset": InputPathType,
    "output_prefix": str,
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
        "3dSharpen": v_3d_sharpen_cargs,
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
        "3dSharpen": v_3d_sharpen_outputs,
    }.get(t)


class V3dSharpenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_sharpen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Sharpened output dataset."""


def v_3d_sharpen_params(
    input_dataset: InputPathType,
    output_prefix: str,
    sharpening_factor: float | None = None,
) -> V3dSharpenParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (e.g., input.nii.gz).
        output_prefix: Name of the output dataset (e.g., output.nii.gz) which\
            will be in floating point format.
        sharpening_factor: Sharpening factor, between 0.1 and 0.9 (inclusive).\
            Larger values mean more sharpening.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dSharpen",
        "input_dataset": input_dataset,
        "output_prefix": output_prefix,
    }
    if sharpening_factor is not None:
        params["sharpening_factor"] = sharpening_factor
    return params


def v_3d_sharpen_cargs(
    params: V3dSharpenParameters,
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
    cargs.append("3dSharpen")
    if params.get("sharpening_factor") is not None:
        cargs.extend([
            "-phi",
            str(params.get("sharpening_factor"))
        ])
    cargs.append(execution.input_file(params.get("input_dataset")))
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    return cargs


def v_3d_sharpen_outputs(
    params: V3dSharpenParameters,
    execution: Execution,
) -> V3dSharpenOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dSharpenOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("output_prefix") + ".nii.gz"),
    )
    return ret


def v_3d_sharpen_execute(
    params: V3dSharpenParameters,
    execution: Execution,
) -> V3dSharpenOutputs:
    """
    Applies a simple 3D sharpening filter to the positive values in the #0 volume of
    the input dataset, and writes out a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dSharpenOutputs`).
    """
    cargs = v_3d_sharpen_cargs(params, execution)
    ret = v_3d_sharpen_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_sharpen(
    input_dataset: InputPathType,
    output_prefix: str,
    sharpening_factor: float | None = None,
    runner: Runner | None = None,
) -> V3dSharpenOutputs:
    """
    Applies a simple 3D sharpening filter to the positive values in the #0 volume of
    the input dataset, and writes out a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g., input.nii.gz).
        output_prefix: Name of the output dataset (e.g., output.nii.gz) which\
            will be in floating point format.
        sharpening_factor: Sharpening factor, between 0.1 and 0.9 (inclusive).\
            Larger values mean more sharpening.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSharpenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SHARPEN_METADATA)
    params = v_3d_sharpen_params(sharpening_factor=sharpening_factor, input_dataset=input_dataset, output_prefix=output_prefix)
    return v_3d_sharpen_execute(params, execution)


__all__ = [
    "V3dSharpenOutputs",
    "V3dSharpenParameters",
    "V_3D_SHARPEN_METADATA",
    "v_3d_sharpen",
    "v_3d_sharpen_params",
]

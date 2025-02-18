# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SYNTHSTRIP_METADATA = Metadata(
    id="b76a61f5aba0de9ca4cafed66778de7469902685.boutiques",
    name="mri_synthstrip",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSynthstripParameters = typing.TypedDict('MriSynthstripParameters', {
    "__STYX_TYPE__": typing.Literal["mri_synthstrip"],
    "image": InputPathType,
    "output_image": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "gpu": bool,
    "border": typing.NotRequired[float | None],
    "exclude_csf": bool,
    "model_weights": typing.NotRequired[InputPathType | None],
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
        "mri_synthstrip": mri_synthstrip_cargs,
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
        "mri_synthstrip": mri_synthstrip_outputs,
    }.get(t)


class MriSynthstripOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_synthstrip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType | None
    """Stripped brain image output."""
    output_mask_file: OutputPathType | None
    """Binary brain mask output."""


def mri_synthstrip_params(
    image: InputPathType,
    output_image: str | None = None,
    mask: InputPathType | None = None,
    gpu: bool = False,
    border: float | None = 1,
    exclude_csf: bool = False,
    model_weights: InputPathType | None = None,
) -> MriSynthstripParameters:
    """
    Build parameters.
    
    Args:
        image: Input image to skullstrip.
        output_image: Save stripped image to path.
        mask: Save binary brain mask to path.
        gpu: Use the GPU.
        border: Mask border threshold in mm. Default is 1.
        exclude_csf: Exclude CSF from brain border.
        model_weights: Alternative model weights.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_synthstrip",
        "image": image,
        "gpu": gpu,
        "exclude_csf": exclude_csf,
    }
    if output_image is not None:
        params["output_image"] = output_image
    if mask is not None:
        params["mask"] = mask
    if border is not None:
        params["border"] = border
    if model_weights is not None:
        params["model_weights"] = model_weights
    return params


def mri_synthstrip_cargs(
    params: MriSynthstripParameters,
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
    cargs.append("mri_synthstrip")
    cargs.extend([
        "-i",
        execution.input_file(params.get("image"))
    ])
    if params.get("output_image") is not None:
        cargs.extend([
            "-o",
            "[" + params.get("output_image") + "]"
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-m",
            "[" + execution.input_file(params.get("mask")) + "]"
        ])
    if params.get("gpu"):
        cargs.append("[" + "-g" + "]")
    if params.get("border") is not None:
        cargs.extend([
            "-b",
            "[" + str(params.get("border")) + "]"
        ])
    if params.get("exclude_csf"):
        cargs.append("[" + "--no-csf" + "]")
    if params.get("model_weights") is not None:
        cargs.extend([
            "--model",
            "[" + execution.input_file(params.get("model_weights")) + "]"
        ])
    return cargs


def mri_synthstrip_outputs(
    params: MriSynthstripParameters,
    execution: Execution,
) -> MriSynthstripOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSynthstripOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")) if (params.get("output_image") is not None) else None,
        output_mask_file=execution.output_file(pathlib.Path(params.get("mask")).name) if (params.get("mask") is not None) else None,
    )
    return ret


def mri_synthstrip_execute(
    params: MriSynthstripParameters,
    execution: Execution,
) -> MriSynthstripOutputs:
    """
    Robust, universal skull-stripping for brain images of any type.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSynthstripOutputs`).
    """
    cargs = mri_synthstrip_cargs(params, execution)
    ret = mri_synthstrip_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_synthstrip(
    image: InputPathType,
    output_image: str | None = None,
    mask: InputPathType | None = None,
    gpu: bool = False,
    border: float | None = 1,
    exclude_csf: bool = False,
    model_weights: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriSynthstripOutputs:
    """
    Robust, universal skull-stripping for brain images of any type.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        image: Input image to skullstrip.
        output_image: Save stripped image to path.
        mask: Save binary brain mask to path.
        gpu: Use the GPU.
        border: Mask border threshold in mm. Default is 1.
        exclude_csf: Exclude CSF from brain border.
        model_weights: Alternative model weights.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSynthstripOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SYNTHSTRIP_METADATA)
    params = mri_synthstrip_params(image=image, output_image=output_image, mask=mask, gpu=gpu, border=border, exclude_csf=exclude_csf, model_weights=model_weights)
    return mri_synthstrip_execute(params, execution)


__all__ = [
    "MRI_SYNTHSTRIP_METADATA",
    "MriSynthstripOutputs",
    "MriSynthstripParameters",
    "mri_synthstrip",
    "mri_synthstrip_params",
]

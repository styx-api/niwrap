# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EXTRACT_LABEL_METADATA = Metadata(
    id="0b9620a7206508bacb4685ef0d5ac119a68d3dd9.boutiques",
    name="mri_extract_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriExtractLabelParameters = typing.TypedDict('MriExtractLabelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_extract_label"],
    "input_volume": InputPathType,
    "labels": list[str],
    "output_name": str,
    "gaussian_smoothing": typing.NotRequired[float | None],
    "transform_file": typing.NotRequired[InputPathType | None],
    "exit_none_found": bool,
    "dilate": typing.NotRequired[float | None],
    "erode": typing.NotRequired[float | None],
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
        "mri_extract_label": mri_extract_label_cargs,
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
        "mri_extract_label": mri_extract_label_outputs,
    }.get(t)


class MriExtractLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_extract_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Extracted labeled voxels output volume."""


def mri_extract_label_params(
    input_volume: InputPathType,
    labels: list[str],
    output_name: str,
    gaussian_smoothing: float | None = None,
    transform_file: InputPathType | None = None,
    exit_none_found: bool = False,
    dilate: float | None = None,
    erode: float | None = None,
) -> MriExtractLabelParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume from which to extract labels.
        labels: Labels to extract. Can include one or more labels.
        output_name: Name of the output file.
        gaussian_smoothing: Apply a Gaussian smoothing kernel with sigma.
        transform_file: Apply the transform in xform file to the extracted\
            volume.
        exit_none_found: Exit with error if none of the specified labels are\
            found.
        dilate: Dilate the output volume n times.
        erode: Erode the output volume n times.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_extract_label",
        "input_volume": input_volume,
        "labels": labels,
        "output_name": output_name,
        "exit_none_found": exit_none_found,
    }
    if gaussian_smoothing is not None:
        params["gaussian_smoothing"] = gaussian_smoothing
    if transform_file is not None:
        params["transform_file"] = transform_file
    if dilate is not None:
        params["dilate"] = dilate
    if erode is not None:
        params["erode"] = erode
    return params


def mri_extract_label_cargs(
    params: MriExtractLabelParameters,
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
    cargs.append("mri_extract_label")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.extend(params.get("labels"))
    cargs.append(params.get("output_name"))
    if params.get("gaussian_smoothing") is not None:
        cargs.extend([
            "-s",
            str(params.get("gaussian_smoothing"))
        ])
    if params.get("transform_file") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("transform_file"))
        ])
    if params.get("exit_none_found"):
        cargs.append("-exit_none_found")
    if params.get("dilate") is not None:
        cargs.extend([
            "-dilate",
            str(params.get("dilate"))
        ])
    if params.get("erode") is not None:
        cargs.extend([
            "-erode",
            str(params.get("erode"))
        ])
    return cargs


def mri_extract_label_outputs(
    params: MriExtractLabelParameters,
    execution: Execution,
) -> MriExtractLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriExtractLabelOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("output_name")),
    )
    return ret


def mri_extract_label_execute(
    params: MriExtractLabelParameters,
    execution: Execution,
) -> MriExtractLabelOutputs:
    """
    Extracts a set of labeled voxels from an image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriExtractLabelOutputs`).
    """
    params = execution.params(params)
    cargs = mri_extract_label_cargs(params, execution)
    ret = mri_extract_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_extract_label(
    input_volume: InputPathType,
    labels: list[str],
    output_name: str,
    gaussian_smoothing: float | None = None,
    transform_file: InputPathType | None = None,
    exit_none_found: bool = False,
    dilate: float | None = None,
    erode: float | None = None,
    runner: Runner | None = None,
) -> MriExtractLabelOutputs:
    """
    Extracts a set of labeled voxels from an image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume from which to extract labels.
        labels: Labels to extract. Can include one or more labels.
        output_name: Name of the output file.
        gaussian_smoothing: Apply a Gaussian smoothing kernel with sigma.
        transform_file: Apply the transform in xform file to the extracted\
            volume.
        exit_none_found: Exit with error if none of the specified labels are\
            found.
        dilate: Dilate the output volume n times.
        erode: Erode the output volume n times.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriExtractLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EXTRACT_LABEL_METADATA)
    params = mri_extract_label_params(
        input_volume=input_volume,
        labels=labels,
        output_name=output_name,
        gaussian_smoothing=gaussian_smoothing,
        transform_file=transform_file,
        exit_none_found=exit_none_found,
        dilate=dilate,
        erode=erode,
    )
    return mri_extract_label_execute(params, execution)


__all__ = [
    "MRI_EXTRACT_LABEL_METADATA",
    "MriExtractLabelOutputs",
    "MriExtractLabelParameters",
    "mri_extract_label",
    "mri_extract_label_params",
]

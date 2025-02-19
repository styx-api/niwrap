# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RESAMPLE_IMAGE_METADATA = Metadata(
    id="243da81f65ea0a482b7b69380239da5960d94d94.boutiques",
    name="ResampleImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


ResampleImageParameters = typing.TypedDict('ResampleImageParameters', {
    "__STYX_TYPE__": typing.Literal["ResampleImage"],
    "image_dimension": int,
    "input_image": InputPathType,
    "output_image": str,
    "size_spacing": str,
    "interpolate_type": typing.NotRequired[typing.Literal["0", "1", "2", "3", "4"] | None],
    "pixeltype": typing.NotRequired[typing.Literal["0", "1", "2", "3", "4", "5", "6", "7"] | None],
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
        "ResampleImage": resample_image_cargs,
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
        "ResampleImage": resample_image_outputs,
    }.get(t)


class ResampleImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `resample_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    resampled_output_image: OutputPathType
    """The resultant image after resampling."""


def resample_image_params(
    image_dimension: int,
    input_image: InputPathType,
    output_image: str,
    size_spacing: str,
    interpolate_type: typing.Literal["0", "1", "2", "3", "4"] | None = None,
    pixeltype: typing.Literal["0", "1", "2", "3", "4", "5", "6", "7"] | None = None,
) -> ResampleImageParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Dimension of the image to be resampled.
        input_image: The image file to be resampled.
        output_image: The output image file after resampling.
        size_spacing: Resampling size and spacing specification, e.g., 'MxNxO'.
        interpolate_type: Specifies the interpolation type. 0: linear\
            (default), 1: nearest-neighbor, 2: gaussian, 3: windowedSinc, 4:\
            B-Spline.
        pixeltype: Specifies the pixel type of the output image. 0: char, 1:\
            unsigned char, 2: short, 3: unsigned short, 4: int, 5: unsigned int, 6:\
            float (default), 7: double.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ResampleImage",
        "image_dimension": image_dimension,
        "input_image": input_image,
        "output_image": output_image,
        "size_spacing": size_spacing,
    }
    if interpolate_type is not None:
        params["interpolate_type"] = interpolate_type
    if pixeltype is not None:
        params["pixeltype"] = pixeltype
    return params


def resample_image_cargs(
    params: ResampleImageParameters,
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
    cargs.append("ResampleImage")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    cargs.append(params.get("size_spacing"))
    if params.get("interpolate_type") is not None:
        cargs.append(params.get("interpolate_type"))
    if params.get("pixeltype") is not None:
        cargs.append(params.get("pixeltype"))
    return cargs


def resample_image_outputs(
    params: ResampleImageParameters,
    execution: Execution,
) -> ResampleImageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ResampleImageOutputs(
        root=execution.output_file("."),
        resampled_output_image=execution.output_file(params.get("output_image")),
    )
    return ret


def resample_image_execute(
    params: ResampleImageParameters,
    execution: Execution,
) -> ResampleImageOutputs:
    """
    ResampleImage is a tool used to resample images to specified sizes and spacings,
    using various interpolation methods and pixel types.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ResampleImageOutputs`).
    """
    params = execution.params(params)
    cargs = resample_image_cargs(params, execution)
    ret = resample_image_outputs(params, execution)
    execution.run(cargs)
    return ret


def resample_image(
    image_dimension: int,
    input_image: InputPathType,
    output_image: str,
    size_spacing: str,
    interpolate_type: typing.Literal["0", "1", "2", "3", "4"] | None = None,
    pixeltype: typing.Literal["0", "1", "2", "3", "4", "5", "6", "7"] | None = None,
    runner: Runner | None = None,
) -> ResampleImageOutputs:
    """
    ResampleImage is a tool used to resample images to specified sizes and spacings,
    using various interpolation methods and pixel types.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimension of the image to be resampled.
        input_image: The image file to be resampled.
        output_image: The output image file after resampling.
        size_spacing: Resampling size and spacing specification, e.g., 'MxNxO'.
        interpolate_type: Specifies the interpolation type. 0: linear\
            (default), 1: nearest-neighbor, 2: gaussian, 3: windowedSinc, 4:\
            B-Spline.
        pixeltype: Specifies the pixel type of the output image. 0: char, 1:\
            unsigned char, 2: short, 3: unsigned short, 4: int, 5: unsigned int, 6:\
            float (default), 7: double.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ResampleImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RESAMPLE_IMAGE_METADATA)
    params = resample_image_params(
        image_dimension=image_dimension,
        input_image=input_image,
        output_image=output_image,
        size_spacing=size_spacing,
        interpolate_type=interpolate_type,
        pixeltype=pixeltype,
    )
    return resample_image_execute(params, execution)


__all__ = [
    "RESAMPLE_IMAGE_METADATA",
    "ResampleImageOutputs",
    "ResampleImageParameters",
    "resample_image",
    "resample_image_params",
]

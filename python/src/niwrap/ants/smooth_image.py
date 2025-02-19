# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SMOOTH_IMAGE_METADATA = Metadata(
    id="c743ecca2407454064c39d3994944e2822b5560a.boutiques",
    name="SmoothImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


SmoothImageParameters = typing.TypedDict('SmoothImageParameters', {
    "__STYX_TYPE__": typing.Literal["SmoothImage"],
    "image_dimension": int,
    "image_ext": InputPathType,
    "smoothing_sigma": str,
    "out_image_ext": str,
    "sigma_units": typing.NotRequired[typing.Literal[0, 1] | None],
    "median_filter": typing.NotRequired[typing.Literal[0, 1] | None],
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
        "SmoothImage": smooth_image_cargs,
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
        "SmoothImage": smooth_image_outputs,
    }.get(t)


class SmoothImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smooth_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    smoothed_image: OutputPathType
    """The output smoothed image file."""


def smooth_image_params(
    image_dimension: int,
    image_ext: InputPathType,
    smoothing_sigma: str,
    out_image_ext: str,
    sigma_units: typing.Literal[0, 1] | None = None,
    median_filter: typing.Literal[0, 1] | None = None,
) -> SmoothImageParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Specifies the dimensionality of the image.
        image_ext: The input image file to be smoothed.
        smoothing_sigma: The sigma value for smoothing. A separate sigma may be\
            specified for each dimension, e.g., '1.5x1x2'.
        out_image_ext: The output smoothed image file.
        sigma_units: Determines if sigma is in spacing units (1) or not (0).\
            Default is 0.
        median_filter: Whether to use median filter. Default is 0. If using\
            median filter, sigma represents the radius in voxels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SmoothImage",
        "image_dimension": image_dimension,
        "image_ext": image_ext,
        "smoothing_sigma": smoothing_sigma,
        "out_image_ext": out_image_ext,
    }
    if sigma_units is not None:
        params["sigma_units"] = sigma_units
    if median_filter is not None:
        params["median_filter"] = median_filter
    return params


def smooth_image_cargs(
    params: SmoothImageParameters,
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
    cargs.append("SmoothImage")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("image_ext")))
    cargs.append(params.get("smoothing_sigma"))
    cargs.append(params.get("out_image_ext"))
    if params.get("sigma_units") is not None:
        cargs.append(str(params.get("sigma_units")))
    if params.get("median_filter") is not None:
        cargs.append(str(params.get("median_filter")))
    return cargs


def smooth_image_outputs(
    params: SmoothImageParameters,
    execution: Execution,
) -> SmoothImageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SmoothImageOutputs(
        root=execution.output_file("."),
        smoothed_image=execution.output_file(params.get("out_image_ext")),
    )
    return ret


def smooth_image_execute(
    params: SmoothImageParameters,
    execution: Execution,
) -> SmoothImageOutputs:
    """
    SmoothImage allows smoothing of images with adjustable sigma values, offering
    optional median filtering functionality.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SmoothImageOutputs`).
    """
    params = execution.params(params)
    cargs = smooth_image_cargs(params, execution)
    ret = smooth_image_outputs(params, execution)
    execution.run(cargs)
    return ret


def smooth_image(
    image_dimension: int,
    image_ext: InputPathType,
    smoothing_sigma: str,
    out_image_ext: str,
    sigma_units: typing.Literal[0, 1] | None = None,
    median_filter: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> SmoothImageOutputs:
    """
    SmoothImage allows smoothing of images with adjustable sigma values, offering
    optional median filtering functionality.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Specifies the dimensionality of the image.
        image_ext: The input image file to be smoothed.
        smoothing_sigma: The sigma value for smoothing. A separate sigma may be\
            specified for each dimension, e.g., '1.5x1x2'.
        out_image_ext: The output smoothed image file.
        sigma_units: Determines if sigma is in spacing units (1) or not (0).\
            Default is 0.
        median_filter: Whether to use median filter. Default is 0. If using\
            median filter, sigma represents the radius in voxels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SmoothImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SMOOTH_IMAGE_METADATA)
    params = smooth_image_params(
        image_dimension=image_dimension,
        image_ext=image_ext,
        smoothing_sigma=smoothing_sigma,
        out_image_ext=out_image_ext,
        sigma_units=sigma_units,
        median_filter=median_filter,
    )
    return smooth_image_execute(params, execution)


__all__ = [
    "SMOOTH_IMAGE_METADATA",
    "SmoothImageOutputs",
    "SmoothImageParameters",
    "smooth_image",
    "smooth_image_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONVERT_SCALAR_IMAGE_TO_RGB_METADATA = Metadata(
    id="9ca4a7950c397eac7a9318ce90e2920bf4776ea6.boutiques",
    name="ConvertScalarImageToRGB",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


ConvertScalarImageToRgbParameters = typing.TypedDict('ConvertScalarImageToRgbParameters', {
    "__STYX_TYPE__": typing.Literal["ConvertScalarImageToRGB"],
    "image_dimension": int,
    "input_image": InputPathType,
    "output_image": str,
    "mask": InputPathType,
    "colormap": typing.Literal["grey", "red", "green", "blue", "copper", "jet", "hsv", "spring", "summer", "autumn", "winter", "hot", "cool", "overunder", "custom"],
    "custom_colormap_file": typing.NotRequired[InputPathType | None],
    "minimum_input": typing.NotRequired[float | None],
    "maximum_input": typing.NotRequired[float | None],
    "minimum_rgb_output": typing.NotRequired[int | None],
    "maximum_rgb_output": typing.NotRequired[int | None],
    "vtk_lookup_table": typing.NotRequired[str | None],
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
        "ConvertScalarImageToRGB": convert_scalar_image_to_rgb_cargs,
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
        "ConvertScalarImageToRGB": convert_scalar_image_to_rgb_outputs,
    }.get(t)


class ConvertScalarImageToRgbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_scalar_image_to_rgb(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rgb_image: OutputPathType
    """The resulting RGB image after conversion."""


def convert_scalar_image_to_rgb_params(
    image_dimension: int,
    input_image: InputPathType,
    output_image: str,
    mask: InputPathType,
    colormap: typing.Literal["grey", "red", "green", "blue", "copper", "jet", "hsv", "spring", "summer", "autumn", "winter", "hot", "cool", "overunder", "custom"],
    custom_colormap_file: InputPathType | None = None,
    minimum_input: float | None = None,
    maximum_input: float | None = None,
    minimum_rgb_output: int | None = 0,
    maximum_rgb_output: int | None = 255,
    vtk_lookup_table: str | None = None,
) -> ConvertScalarImageToRgbParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the image (e.g., 2D or 3D).
        input_image: The input scalar image to be converted to RGB.
        output_image: The output RGB image file.
        mask: The mask image to apply during conversion.
        colormap: The colormap to use for RGB conversion.
        custom_colormap_file: The file specifying the custom colormap (only\
            used if colormap is 'custom').
        minimum_input: The minimum input value for scaling.
        maximum_input: The maximum input value for scaling.
        minimum_rgb_output: The minimum output value for the RGB image.\
            Defaults to 0.
        maximum_rgb_output: The maximum output value for the RGB image.\
            Defaults to 255.
        vtk_lookup_table: The VTK lookup table to apply for additional\
            customization.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ConvertScalarImageToRGB",
        "image_dimension": image_dimension,
        "input_image": input_image,
        "output_image": output_image,
        "mask": mask,
        "colormap": colormap,
    }
    if custom_colormap_file is not None:
        params["custom_colormap_file"] = custom_colormap_file
    if minimum_input is not None:
        params["minimum_input"] = minimum_input
    if maximum_input is not None:
        params["maximum_input"] = maximum_input
    if minimum_rgb_output is not None:
        params["minimum_rgb_output"] = minimum_rgb_output
    if maximum_rgb_output is not None:
        params["maximum_rgb_output"] = maximum_rgb_output
    if vtk_lookup_table is not None:
        params["vtk_lookup_table"] = vtk_lookup_table
    return params


def convert_scalar_image_to_rgb_cargs(
    params: ConvertScalarImageToRgbParameters,
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
    cargs.append("ConvertScalarImageToRGB")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    cargs.append(execution.input_file(params.get("mask")))
    cargs.append(params.get("colormap"))
    if params.get("custom_colormap_file") is not None:
        cargs.append(execution.input_file(params.get("custom_colormap_file")))
    if params.get("minimum_input") is not None:
        cargs.append(str(params.get("minimum_input")))
    if params.get("maximum_input") is not None:
        cargs.append(str(params.get("maximum_input")))
    if params.get("minimum_rgb_output") is not None:
        cargs.append(str(params.get("minimum_rgb_output")))
    if params.get("maximum_rgb_output") is not None:
        cargs.append(str(params.get("maximum_rgb_output")))
    if params.get("vtk_lookup_table") is not None:
        cargs.append(params.get("vtk_lookup_table"))
    return cargs


def convert_scalar_image_to_rgb_outputs(
    params: ConvertScalarImageToRgbParameters,
    execution: Execution,
) -> ConvertScalarImageToRgbOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertScalarImageToRgbOutputs(
        root=execution.output_file("."),
        output_rgb_image=execution.output_file(params.get("output_image")),
    )
    return ret


def convert_scalar_image_to_rgb_execute(
    params: ConvertScalarImageToRgbParameters,
    execution: Execution,
) -> ConvertScalarImageToRgbOutputs:
    """
    Converts a scalar image to an RGB image using specified parameters. Supports
    multiple colormap options and customization.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertScalarImageToRgbOutputs`).
    """
    params = execution.params(params)
    cargs = convert_scalar_image_to_rgb_cargs(params, execution)
    ret = convert_scalar_image_to_rgb_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_scalar_image_to_rgb(
    image_dimension: int,
    input_image: InputPathType,
    output_image: str,
    mask: InputPathType,
    colormap: typing.Literal["grey", "red", "green", "blue", "copper", "jet", "hsv", "spring", "summer", "autumn", "winter", "hot", "cool", "overunder", "custom"],
    custom_colormap_file: InputPathType | None = None,
    minimum_input: float | None = None,
    maximum_input: float | None = None,
    minimum_rgb_output: int | None = 0,
    maximum_rgb_output: int | None = 255,
    vtk_lookup_table: str | None = None,
    runner: Runner | None = None,
) -> ConvertScalarImageToRgbOutputs:
    """
    Converts a scalar image to an RGB image using specified parameters. Supports
    multiple colormap options and customization.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the image (e.g., 2D or 3D).
        input_image: The input scalar image to be converted to RGB.
        output_image: The output RGB image file.
        mask: The mask image to apply during conversion.
        colormap: The colormap to use for RGB conversion.
        custom_colormap_file: The file specifying the custom colormap (only\
            used if colormap is 'custom').
        minimum_input: The minimum input value for scaling.
        maximum_input: The maximum input value for scaling.
        minimum_rgb_output: The minimum output value for the RGB image.\
            Defaults to 0.
        maximum_rgb_output: The maximum output value for the RGB image.\
            Defaults to 255.
        vtk_lookup_table: The VTK lookup table to apply for additional\
            customization.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertScalarImageToRgbOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_SCALAR_IMAGE_TO_RGB_METADATA)
    params = convert_scalar_image_to_rgb_params(
        image_dimension=image_dimension,
        input_image=input_image,
        output_image=output_image,
        mask=mask,
        colormap=colormap,
        custom_colormap_file=custom_colormap_file,
        minimum_input=minimum_input,
        maximum_input=maximum_input,
        minimum_rgb_output=minimum_rgb_output,
        maximum_rgb_output=maximum_rgb_output,
        vtk_lookup_table=vtk_lookup_table,
    )
    return convert_scalar_image_to_rgb_execute(params, execution)


__all__ = [
    "CONVERT_SCALAR_IMAGE_TO_RGB_METADATA",
    "ConvertScalarImageToRgbOutputs",
    "ConvertScalarImageToRgbParameters",
    "convert_scalar_image_to_rgb",
    "convert_scalar_image_to_rgb_params",
]

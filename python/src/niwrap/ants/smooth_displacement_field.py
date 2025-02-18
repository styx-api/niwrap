# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SMOOTH_DISPLACEMENT_FIELD_METADATA = Metadata(
    id="47ffc5bce5c9c966c1031311bf5353dec2fcef8b.boutiques",
    name="SmoothDisplacementField",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
SmoothDisplacementFieldParameters = typing.TypedDict('SmoothDisplacementFieldParameters', {
    "__STYX_TYPE__": typing.Literal["SmoothDisplacementField"],
    "image_dimension": int,
    "input_field": InputPathType,
    "output_field": str,
    "variance_or_mesh_size_base_level": float,
    "number_of_levels": typing.NotRequired[int | None],
    "spline_order": typing.NotRequired[int | None],
    "estimate_inverse": typing.NotRequired[typing.Literal[0, 1] | None],
    "confidence_image": typing.NotRequired[InputPathType | None],
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
        "SmoothDisplacementField": smooth_displacement_field_cargs,
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
        "SmoothDisplacementField": smooth_displacement_field_outputs,
    }.get(t)


class SmoothDisplacementFieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smooth_displacement_field(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    smoothed_field: OutputPathType
    """The output file containing the smoothed displacement field."""
    confidence_image_out: OutputPathType | None
    """The output file containing confidence information from the smoothing
    process."""


def smooth_displacement_field_params(
    image_dimension: int,
    input_field: InputPathType,
    output_field: str,
    variance_or_mesh_size_base_level: float,
    number_of_levels: int | None = 1,
    spline_order: int | None = 3,
    estimate_inverse: typing.Literal[0, 1] | None = 0,
    confidence_image: InputPathType | None = None,
) -> SmoothDisplacementFieldParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the input displacement field.
        input_field: The input displacement field file.
        output_field: The output file for the smoothed displacement field.
        variance_or_mesh_size_base_level: The variance for Gaussian smoothing\
            or mesh size at the base level for B-spline smoothing.
        number_of_levels: The number of levels for multi-resolution smoothing.
        spline_order: The order of the spline for B-spline smoothing.
        estimate_inverse: Estimate the inverse of the displacement field if set\
            to 1.
        confidence_image: Optional confidence image output of the smoothing\
            process.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SmoothDisplacementField",
        "image_dimension": image_dimension,
        "input_field": input_field,
        "output_field": output_field,
        "variance_or_mesh_size_base_level": variance_or_mesh_size_base_level,
    }
    if number_of_levels is not None:
        params["number_of_levels"] = number_of_levels
    if spline_order is not None:
        params["spline_order"] = spline_order
    if estimate_inverse is not None:
        params["estimate_inverse"] = estimate_inverse
    if confidence_image is not None:
        params["confidence_image"] = confidence_image
    return params


def smooth_displacement_field_cargs(
    params: SmoothDisplacementFieldParameters,
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
    cargs.append("SmoothDisplacementField")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_field")))
    cargs.append(params.get("output_field"))
    cargs.append(str(params.get("variance_or_mesh_size_base_level")))
    if params.get("number_of_levels") is not None:
        cargs.append(str(params.get("number_of_levels")))
    if params.get("spline_order") is not None:
        cargs.append(str(params.get("spline_order")))
    if params.get("estimate_inverse") is not None:
        cargs.append(str(params.get("estimate_inverse")))
    if params.get("confidence_image") is not None:
        cargs.append(execution.input_file(params.get("confidence_image")))
    return cargs


def smooth_displacement_field_outputs(
    params: SmoothDisplacementFieldParameters,
    execution: Execution,
) -> SmoothDisplacementFieldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SmoothDisplacementFieldOutputs(
        root=execution.output_file("."),
        smoothed_field=execution.output_file(params.get("output_field")),
        confidence_image_out=execution.output_file(pathlib.Path(params.get("confidence_image")).name) if (params.get("confidence_image") is not None) else None,
    )
    return ret


def smooth_displacement_field_execute(
    params: SmoothDisplacementFieldParameters,
    execution: Execution,
) -> SmoothDisplacementFieldOutputs:
    """
    SmoothDisplacementField applies smoothing to a displacement field over a
    specified number of levels with optional parameters for spline order, inverse
    estimation, and confidence image output.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SmoothDisplacementFieldOutputs`).
    """
    cargs = smooth_displacement_field_cargs(params, execution)
    ret = smooth_displacement_field_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def smooth_displacement_field(
    image_dimension: int,
    input_field: InputPathType,
    output_field: str,
    variance_or_mesh_size_base_level: float,
    number_of_levels: int | None = 1,
    spline_order: int | None = 3,
    estimate_inverse: typing.Literal[0, 1] | None = 0,
    confidence_image: InputPathType | None = None,
    runner: Runner | None = None,
) -> SmoothDisplacementFieldOutputs:
    """
    SmoothDisplacementField applies smoothing to a displacement field over a
    specified number of levels with optional parameters for spline order, inverse
    estimation, and confidence image output.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input displacement field.
        input_field: The input displacement field file.
        output_field: The output file for the smoothed displacement field.
        variance_or_mesh_size_base_level: The variance for Gaussian smoothing\
            or mesh size at the base level for B-spline smoothing.
        number_of_levels: The number of levels for multi-resolution smoothing.
        spline_order: The order of the spline for B-spline smoothing.
        estimate_inverse: Estimate the inverse of the displacement field if set\
            to 1.
        confidence_image: Optional confidence image output of the smoothing\
            process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SmoothDisplacementFieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SMOOTH_DISPLACEMENT_FIELD_METADATA)
    params = smooth_displacement_field_params(image_dimension=image_dimension, input_field=input_field, output_field=output_field, variance_or_mesh_size_base_level=variance_or_mesh_size_base_level, number_of_levels=number_of_levels, spline_order=spline_order, estimate_inverse=estimate_inverse, confidence_image=confidence_image)
    return smooth_displacement_field_execute(params, execution)


__all__ = [
    "SMOOTH_DISPLACEMENT_FIELD_METADATA",
    "SmoothDisplacementFieldOutputs",
    "SmoothDisplacementFieldParameters",
    "smooth_displacement_field",
    "smooth_displacement_field_params",
]

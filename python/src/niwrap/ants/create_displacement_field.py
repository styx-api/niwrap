# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CREATE_DISPLACEMENT_FIELD_METADATA = Metadata(
    id="4dbaa9ddf35cec6b6f78e7c9efdb17f6f5f6d1e2.boutiques",
    name="CreateDisplacementField",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
CreateDisplacementFieldParameters = typing.TypedDict('CreateDisplacementFieldParameters', {
    "__STYX_TYPE__": typing.Literal["CreateDisplacementField"],
    "image_dimension": int,
    "enforce_zero_boundary_flag": typing.Literal[0, 1],
    "component_images": list[InputPathType],
    "output_image": str,
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
        "CreateDisplacementField": create_displacement_field_cargs,
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
        "CreateDisplacementField": create_displacement_field_outputs,
    }.get(t)


class CreateDisplacementFieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_displacement_field(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_displacement_field: OutputPathType
    """The generated itkImage of itkVector pixels representing the displacement
    field."""


def create_displacement_field_params(
    image_dimension: int,
    enforce_zero_boundary_flag: typing.Literal[0, 1],
    component_images: list[InputPathType],
    output_image: str,
) -> CreateDisplacementFieldParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimension of the image, typically 2 or 3.
        enforce_zero_boundary_flag: Create zero-valued vectors along the\
            borders when enabled (pass 1), recommended for better displacement\
            field behavior.
        component_images: Input component images, each used for a vector\
            component. All component images must have the same size, offset,\
            origin, and spacing.
        output_image: The output displacement field image with itkVector\
            pixels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "CreateDisplacementField",
        "image_dimension": image_dimension,
        "enforce_zero_boundary_flag": enforce_zero_boundary_flag,
        "component_images": component_images,
        "output_image": output_image,
    }
    return params


def create_displacement_field_cargs(
    params: CreateDisplacementFieldParameters,
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
    cargs.append("CreateDisplacementField")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(str(params.get("enforce_zero_boundary_flag")))
    cargs.extend([execution.input_file(f) for f in params.get("component_images")])
    cargs.append(params.get("output_image"))
    return cargs


def create_displacement_field_outputs(
    params: CreateDisplacementFieldParameters,
    execution: Execution,
) -> CreateDisplacementFieldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CreateDisplacementFieldOutputs(
        root=execution.output_file("."),
        output_displacement_field=execution.output_file(params.get("output_image")),
    )
    return ret


def create_displacement_field_execute(
    params: CreateDisplacementFieldParameters,
    execution: Execution,
) -> CreateDisplacementFieldOutputs:
    """
    Create an itkImage of itkVector pixels (NOT an itkVectorImage), using each
    scalar input component image for each vector component. An itkImage of
    itkVectors is the standard type for displacement fields in ITK. All component
    images (up to 8) are assumed to have the same size, offset, origin, and spacing.
    The 'EnforceZeroBoundaryFlag' option will create zero-valued vectors along the
    borders when enabled (pass 1), and is recommended for better displacement field
    behavior.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CreateDisplacementFieldOutputs`).
    """
    cargs = create_displacement_field_cargs(params, execution)
    ret = create_displacement_field_outputs(params, execution)
    execution.run(cargs)
    return ret


def create_displacement_field(
    image_dimension: int,
    enforce_zero_boundary_flag: typing.Literal[0, 1],
    component_images: list[InputPathType],
    output_image: str,
    runner: Runner | None = None,
) -> CreateDisplacementFieldOutputs:
    """
    Create an itkImage of itkVector pixels (NOT an itkVectorImage), using each
    scalar input component image for each vector component. An itkImage of
    itkVectors is the standard type for displacement fields in ITK. All component
    images (up to 8) are assumed to have the same size, offset, origin, and spacing.
    The 'EnforceZeroBoundaryFlag' option will create zero-valued vectors along the
    borders when enabled (pass 1), and is recommended for better displacement field
    behavior.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimension of the image, typically 2 or 3.
        enforce_zero_boundary_flag: Create zero-valued vectors along the\
            borders when enabled (pass 1), recommended for better displacement\
            field behavior.
        component_images: Input component images, each used for a vector\
            component. All component images must have the same size, offset,\
            origin, and spacing.
        output_image: The output displacement field image with itkVector\
            pixels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateDisplacementFieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CREATE_DISPLACEMENT_FIELD_METADATA)
    params = create_displacement_field_params(image_dimension=image_dimension, enforce_zero_boundary_flag=enforce_zero_boundary_flag, component_images=component_images, output_image=output_image)
    return create_displacement_field_execute(params, execution)


__all__ = [
    "CREATE_DISPLACEMENT_FIELD_METADATA",
    "CreateDisplacementFieldOutputs",
    "CreateDisplacementFieldParameters",
    "create_displacement_field",
    "create_displacement_field_params",
]

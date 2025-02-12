# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SUPER_RESOLUTION_METADATA = Metadata(
    id="cd1212b3e1e62a6349afb70d130bc6b89439a7a0.boutiques",
    name="SuperResolution",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
SuperResolutionParameters = typing.TypedDict('SuperResolutionParameters', {
    "__STYX_TYPE__": typing.Literal["SuperResolution"],
    "image_dimension": int,
    "output_image": str,
    "domain_image": InputPathType,
    "gradient_sigma": float,
    "mesh_size": float,
    "number_of_levels": int,
    "input_image_files": list[InputPathType],
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
        "SuperResolution": super_resolution_cargs,
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
        "SuperResolution": super_resolution_outputs,
    }.get(t)


class SuperResolutionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `super_resolution(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    super_resolved_image: OutputPathType
    """The output super-resolved image file."""


def super_resolution_params(
    image_dimension: int,
    output_image: str,
    domain_image: InputPathType,
    gradient_sigma: float,
    mesh_size: float,
    number_of_levels: int,
    input_image_files: list[InputPathType],
) -> SuperResolutionParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Specifies the dimensionality of the input images\
            (e.g., 2 for 2D images, 3 for 3D images).
        output_image: The file path for the output super-resolved image.
        domain_image: The domain image is used as the template space for the\
            alignment of input images.
        gradient_sigma: The sigma used for calculating the gradient magnitude\
            of input images. If negative, no weighting is applied.
        mesh_size: The size of the mesh used in fitting.
        number_of_levels: The number of resolution levels to process.
        input_image_files: List of paths to input images to be processed for\
            super resolution.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SuperResolution",
        "image_dimension": image_dimension,
        "output_image": output_image,
        "domain_image": domain_image,
        "gradient_sigma": gradient_sigma,
        "mesh_size": mesh_size,
        "number_of_levels": number_of_levels,
        "input_image_files": input_image_files,
    }
    return params


def super_resolution_cargs(
    params: SuperResolutionParameters,
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
    cargs.append("SuperResolution")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(params.get("output_image"))
    cargs.append(execution.input_file(params.get("domain_image")))
    cargs.append(str(params.get("gradient_sigma")))
    cargs.append(str(params.get("mesh_size")))
    cargs.append(str(params.get("number_of_levels")))
    cargs.extend([execution.input_file(f) for f in params.get("input_image_files")])
    return cargs


def super_resolution_outputs(
    params: SuperResolutionParameters,
    execution: Execution,
) -> SuperResolutionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SuperResolutionOutputs(
        root=execution.output_file("."),
        super_resolved_image=execution.output_file(params.get("output_image")),
    )
    return ret


def super_resolution_execute(
    params: SuperResolutionParameters,
    execution: Execution,
) -> SuperResolutionOutputs:
    """
    The SuperResolution tool enhances the spatial resolution of input images. The
    'gradientSigma' parameter is used in calculating the gradient magnitude of the
    input images for weighting the voxel points during fitting. If a negative
    'gradient' sigma is specified then no weighting is used.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SuperResolutionOutputs`).
    """
    cargs = super_resolution_cargs(params, execution)
    ret = super_resolution_outputs(params, execution)
    execution.run(cargs)
    return ret


def super_resolution(
    image_dimension: int,
    output_image: str,
    domain_image: InputPathType,
    gradient_sigma: float,
    mesh_size: float,
    number_of_levels: int,
    input_image_files: list[InputPathType],
    runner: Runner | None = None,
) -> SuperResolutionOutputs:
    """
    The SuperResolution tool enhances the spatial resolution of input images. The
    'gradientSigma' parameter is used in calculating the gradient magnitude of the
    input images for weighting the voxel points during fitting. If a negative
    'gradient' sigma is specified then no weighting is used.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Specifies the dimensionality of the input images\
            (e.g., 2 for 2D images, 3 for 3D images).
        output_image: The file path for the output super-resolved image.
        domain_image: The domain image is used as the template space for the\
            alignment of input images.
        gradient_sigma: The sigma used for calculating the gradient magnitude\
            of input images. If negative, no weighting is applied.
        mesh_size: The size of the mesh used in fitting.
        number_of_levels: The number of resolution levels to process.
        input_image_files: List of paths to input images to be processed for\
            super resolution.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SuperResolutionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUPER_RESOLUTION_METADATA)
    params = super_resolution_params(image_dimension=image_dimension, output_image=output_image, domain_image=domain_image, gradient_sigma=gradient_sigma, mesh_size=mesh_size, number_of_levels=number_of_levels, input_image_files=input_image_files)
    return super_resolution_execute(params, execution)


__all__ = [
    "SUPER_RESOLUTION_METADATA",
    "SuperResolutionOutputs",
    "SuperResolutionParameters",
    "super_resolution",
    "super_resolution_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_FUSE_INTENSITY_IMAGES_METADATA = Metadata(
    id="22ecf33c78a1fc7ec78703d7b49001464fb5a595.boutiques",
    name="mri_fuse_intensity_images",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriFuseIntensityImagesParameters = typing.TypedDict('MriFuseIntensityImagesParameters', {
    "__STYX_TYPE__": typing.Literal["mri_fuse_intensity_images"],
    "longitudinal_time_point_file": InputPathType,
    "input_volume": InputPathType,
    "transform_file": InputPathType,
    "output_volume": str,
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
        "mri_fuse_intensity_images": mri_fuse_intensity_images_cargs,
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
        "mri_fuse_intensity_images": mri_fuse_intensity_images_outputs,
    }.get(t)


class MriFuseIntensityImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fuse_intensity_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fused_intensity_image: OutputPathType
    """The resulting fused intensity image"""


def mri_fuse_intensity_images_params(
    longitudinal_time_point_file: InputPathType,
    input_volume: InputPathType,
    transform_file: InputPathType,
    output_volume: str,
) -> MriFuseIntensityImagesParameters:
    """
    Build parameters.
    
    Args:
        longitudinal_time_point_file: File containing the longitudinal time\
            points.
        input_volume: Input volume to be fused.
        transform_file: File containing the transforms.
        output_volume: Output fused volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_fuse_intensity_images",
        "longitudinal_time_point_file": longitudinal_time_point_file,
        "input_volume": input_volume,
        "transform_file": transform_file,
        "output_volume": output_volume,
    }
    return params


def mri_fuse_intensity_images_cargs(
    params: MriFuseIntensityImagesParameters,
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
    cargs.append("mri_fuse_intensity_images")
    cargs.append(execution.input_file(params.get("longitudinal_time_point_file")))
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("transform_file")))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_fuse_intensity_images_outputs(
    params: MriFuseIntensityImagesParameters,
    execution: Execution,
) -> MriFuseIntensityImagesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFuseIntensityImagesOutputs(
        root=execution.output_file("."),
        fused_intensity_image=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_fuse_intensity_images_execute(
    params: MriFuseIntensityImagesParameters,
    execution: Execution,
) -> MriFuseIntensityImagesOutputs:
    """
    Fuses intensity images based on given transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFuseIntensityImagesOutputs`).
    """
    params = execution.params(params)
    cargs = mri_fuse_intensity_images_cargs(params, execution)
    ret = mri_fuse_intensity_images_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_fuse_intensity_images(
    longitudinal_time_point_file: InputPathType,
    input_volume: InputPathType,
    transform_file: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriFuseIntensityImagesOutputs:
    """
    Fuses intensity images based on given transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        longitudinal_time_point_file: File containing the longitudinal time\
            points.
        input_volume: Input volume to be fused.
        transform_file: File containing the transforms.
        output_volume: Output fused volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFuseIntensityImagesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FUSE_INTENSITY_IMAGES_METADATA)
    params = mri_fuse_intensity_images_params(
        longitudinal_time_point_file=longitudinal_time_point_file,
        input_volume=input_volume,
        transform_file=transform_file,
        output_volume=output_volume,
    )
    return mri_fuse_intensity_images_execute(params, execution)


__all__ = [
    "MRI_FUSE_INTENSITY_IMAGES_METADATA",
    "MriFuseIntensityImagesOutputs",
    "MriFuseIntensityImagesParameters",
    "mri_fuse_intensity_images",
    "mri_fuse_intensity_images_params",
]

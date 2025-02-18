# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_CAPTURE_PLANE_METADATA = Metadata(
    id="b2bfd3d4513396540148947511ec229d0418fc44.boutiques",
    name="volume-capture-plane",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeCapturePlaneParameters = typing.TypedDict('VolumeCapturePlaneParameters', {
    "__STYX_TYPE__": typing.Literal["volume-capture-plane"],
    "volume": InputPathType,
    "subvolume": str,
    "interp": str,
    "h_dim": int,
    "v_dim": int,
    "scale_min": float,
    "scale_max": float,
    "bottom_left_x": float,
    "bottom_left_y": float,
    "bottom_left_z": float,
    "bottom_right_x": float,
    "bottom_right_y": float,
    "bottom_right_z": float,
    "top_left_x": float,
    "top_left_y": float,
    "top_left_z": float,
    "image": str,
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
        "volume-capture-plane": volume_capture_plane_cargs,
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
    }.get(t)


class VolumeCapturePlaneOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_capture_plane(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_capture_plane_params(
    volume: InputPathType,
    subvolume: str,
    interp: str,
    h_dim: int,
    v_dim: int,
    scale_min: float,
    scale_max: float,
    bottom_left_x: float,
    bottom_left_y: float,
    bottom_left_z: float,
    bottom_right_x: float,
    bottom_right_y: float,
    bottom_right_z: float,
    top_left_x: float,
    top_left_y: float,
    top_left_z: float,
    image: str,
) -> VolumeCapturePlaneParameters:
    """
    Build parameters.
    
    Args:
        volume: the volume file to interpolate from.
        subvolume: the name or number of the subvolume to use.
        interp: interpolation type.
        h_dim: width of output image, in pixels.
        v_dim: height of output image, in pixels.
        scale_min: value to render as black.
        scale_max: value to render as white.
        bottom_left_x: x-coordinate of the bottom left of the output image.
        bottom_left_y: y-coordinate of the bottom left of the output image.
        bottom_left_z: z-coordinate of the bottom left of the output image.
        bottom_right_x: x-coordinate of the bottom right of the output image.
        bottom_right_y: y-coordinate of the bottom right of the output image.
        bottom_right_z: z-coordinate of the bottom right of the output image.
        top_left_x: x-coordinate of the top left of the output image.
        top_left_y: y-coordinate of the top left of the output image.
        top_left_z: z-coordinate of the top left of the output image.
        image: output - the output image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-capture-plane",
        "volume": volume,
        "subvolume": subvolume,
        "interp": interp,
        "h_dim": h_dim,
        "v_dim": v_dim,
        "scale_min": scale_min,
        "scale_max": scale_max,
        "bottom_left_x": bottom_left_x,
        "bottom_left_y": bottom_left_y,
        "bottom_left_z": bottom_left_z,
        "bottom_right_x": bottom_right_x,
        "bottom_right_y": bottom_right_y,
        "bottom_right_z": bottom_right_z,
        "top_left_x": top_left_x,
        "top_left_y": top_left_y,
        "top_left_z": top_left_z,
        "image": image,
    }
    return params


def volume_capture_plane_cargs(
    params: VolumeCapturePlaneParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-capture-plane")
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(params.get("subvolume"))
    cargs.append(params.get("interp"))
    cargs.append(str(params.get("h_dim")))
    cargs.append(str(params.get("v_dim")))
    cargs.append(str(params.get("scale_min")))
    cargs.append(str(params.get("scale_max")))
    cargs.append(str(params.get("bottom_left_x")))
    cargs.append(str(params.get("bottom_left_y")))
    cargs.append(str(params.get("bottom_left_z")))
    cargs.append(str(params.get("bottom_right_x")))
    cargs.append(str(params.get("bottom_right_y")))
    cargs.append(str(params.get("bottom_right_z")))
    cargs.append(str(params.get("top_left_x")))
    cargs.append(str(params.get("top_left_y")))
    cargs.append(str(params.get("top_left_z")))
    cargs.append(params.get("image"))
    return cargs


def volume_capture_plane_outputs(
    params: VolumeCapturePlaneParameters,
    execution: Execution,
) -> VolumeCapturePlaneOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeCapturePlaneOutputs(
        root=execution.output_file("."),
    )
    return ret


def volume_capture_plane_execute(
    params: VolumeCapturePlaneParameters,
    execution: Execution,
) -> VolumeCapturePlaneOutputs:
    """
    Interpolate image from plane through volume.
    
    NOTE: If you want to generate an image with all of the capabilities of the
    GUI rendering, see -show-scene.
    
    Renders an image of an arbitrary plane through the volume file, with a
    simple linear grayscale palette. The parameter <interp> must be one of:
    
    CUBIC
    ENCLOSING_VOXEL
    TRILINEAR.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeCapturePlaneOutputs`).
    """
    cargs = volume_capture_plane_cargs(params, execution)
    ret = volume_capture_plane_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def volume_capture_plane(
    volume: InputPathType,
    subvolume: str,
    interp: str,
    h_dim: int,
    v_dim: int,
    scale_min: float,
    scale_max: float,
    bottom_left_x: float,
    bottom_left_y: float,
    bottom_left_z: float,
    bottom_right_x: float,
    bottom_right_y: float,
    bottom_right_z: float,
    top_left_x: float,
    top_left_y: float,
    top_left_z: float,
    image: str,
    runner: Runner | None = None,
) -> VolumeCapturePlaneOutputs:
    """
    Interpolate image from plane through volume.
    
    NOTE: If you want to generate an image with all of the capabilities of the
    GUI rendering, see -show-scene.
    
    Renders an image of an arbitrary plane through the volume file, with a
    simple linear grayscale palette. The parameter <interp> must be one of:
    
    CUBIC
    ENCLOSING_VOXEL
    TRILINEAR.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume: the volume file to interpolate from.
        subvolume: the name or number of the subvolume to use.
        interp: interpolation type.
        h_dim: width of output image, in pixels.
        v_dim: height of output image, in pixels.
        scale_min: value to render as black.
        scale_max: value to render as white.
        bottom_left_x: x-coordinate of the bottom left of the output image.
        bottom_left_y: y-coordinate of the bottom left of the output image.
        bottom_left_z: z-coordinate of the bottom left of the output image.
        bottom_right_x: x-coordinate of the bottom right of the output image.
        bottom_right_y: y-coordinate of the bottom right of the output image.
        bottom_right_z: z-coordinate of the bottom right of the output image.
        top_left_x: x-coordinate of the top left of the output image.
        top_left_y: y-coordinate of the top left of the output image.
        top_left_z: z-coordinate of the top left of the output image.
        image: output - the output image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeCapturePlaneOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_CAPTURE_PLANE_METADATA)
    params = volume_capture_plane_params(volume=volume, subvolume=subvolume, interp=interp, h_dim=h_dim, v_dim=v_dim, scale_min=scale_min, scale_max=scale_max, bottom_left_x=bottom_left_x, bottom_left_y=bottom_left_y, bottom_left_z=bottom_left_z, bottom_right_x=bottom_right_x, bottom_right_y=bottom_right_y, bottom_right_z=bottom_right_z, top_left_x=top_left_x, top_left_y=top_left_y, top_left_z=top_left_z, image=image)
    return volume_capture_plane_execute(params, execution)


__all__ = [
    "VOLUME_CAPTURE_PLANE_METADATA",
    "VolumeCapturePlaneOutputs",
    "VolumeCapturePlaneParameters",
    "volume_capture_plane",
    "volume_capture_plane_params",
]

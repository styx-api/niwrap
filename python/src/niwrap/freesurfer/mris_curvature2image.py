# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_CURVATURE2IMAGE_METADATA = Metadata(
    id="39d168b98aa409f7185978cb8e4d30fc3f31b37b.boutiques",
    name="mris_curvature2image",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisCurvature2imageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_curvature2image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlay_img: OutputPathType
    """Generated overlay image file."""
    output_distance_img: OutputPathType
    """Generated distance image file."""


def mris_curvature2image(
    surface: InputPathType,
    mask: InputPathType,
    output_overlay: str,
    output_distance: str,
    overlay: InputPathType,
    label: InputPathType,
    radius: float,
    invert_flag: bool = False,
    runner: Runner | None = None,
) -> MrisCurvature2imageOutputs:
    """
    Tool to convert surface curvature data to an image using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface file.
        mask: Input mask file.
        output_overlay: Output overlay image file.
        output_distance: Output distance image file.
        overlay: Overlay file.
        label: Label file.
        radius: Radius value for processing.
        invert_flag: Flag to invert the curvature values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCurvature2imageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CURVATURE2IMAGE_METADATA)
    cargs = []
    cargs.append("mris_curvature2image")
    cargs.extend([
        "-s",
        execution.input_file(surface)
    ])
    cargs.extend([
        "-m",
        execution.input_file(mask)
    ])
    cargs.extend([
        "-o",
        output_overlay
    ])
    cargs.extend([
        "-d",
        output_distance
    ])
    cargs.extend([
        "-c",
        execution.input_file(overlay)
    ])
    cargs.extend([
        "-l",
        execution.input_file(label)
    ])
    if invert_flag:
        cargs.append("-inv")
    cargs.extend([
        "-r",
        str(radius)
    ])
    ret = MrisCurvature2imageOutputs(
        root=execution.output_file("."),
        output_overlay_img=execution.output_file(output_overlay),
        output_distance_img=execution.output_file(output_distance),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_CURVATURE2IMAGE_METADATA",
    "MrisCurvature2imageOutputs",
    "mris_curvature2image",
]

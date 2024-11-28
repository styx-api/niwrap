# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_PAINT_METADATA = Metadata(
    id="7a8b84ee3337bcd66c42781ab9453c54416612bb.boutiques",
    name="mri_paint",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriPaintOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_paint(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_float: OutputPathType
    """The output .float file resulting from the painting process"""


def mri_paint(
    input_volume: InputPathType,
    input_surface: InputPathType,
    registration_file: InputPathType,
    output_float_file: str,
    image_offset: float | None = None,
    paint_surf_coords: bool = False,
    runner: Runner | None = None,
) -> MriPaintOutputs:
    """
    This program will paint average Talairach stats onto a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: The input volume file.
        input_surface: The input surface file.
        registration_file: The registration file.
        output_float_file: The output .float file.
        image_offset: Set offset to use.
        paint_surf_coords: Paint using surface coordinates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriPaintOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PAINT_METADATA)
    cargs = []
    cargs.append("mri_paint")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(input_surface))
    cargs.append(execution.input_file(registration_file))
    cargs.append(output_float_file)
    if image_offset is not None:
        cargs.extend([
            "-imageoffset",
            str(image_offset)
        ])
    if paint_surf_coords:
        cargs.append("-S")
    ret = MriPaintOutputs(
        root=execution.output_file("."),
        output_float=execution.output_file(output_float_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_PAINT_METADATA",
    "MriPaintOutputs",
    "mri_paint",
]

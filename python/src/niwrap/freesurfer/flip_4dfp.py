# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FLIP_4DFP_METADATA = Metadata(
    id="98f6070d26bce59316ac68755d93cf8ab88b930d.boutiques",
    name="flip_4dfp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Flip4dfpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flip_4dfp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    flipped_image: OutputPathType | None
    """Flipped output 4dfp image"""


def flip_4dfp(
    input_image: InputPathType,
    output_image: str | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    endianness: typing.Literal["b", "l"] | None = None,
    runner: Runner | None = None,
) -> Flip4dfpOutputs:
    """
    A tool to flip 4dfp images along specified axes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input 4dfp image file.
        output_image: Output 4dfp image file. Default is input image root with\
            '_flip' suffix.
        flip_x: Flip along x-axis.
        flip_y: Flip along y-axis.
        flip_z: Flip along z-axis.
        endianness: Specify output endianness: 'b' for big endian, 'l' for\
            little endian. Default is input endianness.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Flip4dfpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FLIP_4DFP_METADATA)
    cargs = []
    cargs.append("flip_4dfp")
    cargs.append(execution.input_file(input_image))
    if output_image is not None:
        cargs.append(output_image)
    if flip_x:
        cargs.append("-x")
    if flip_y:
        cargs.append("-y")
    if flip_z:
        cargs.append("-z")
    if endianness is not None:
        cargs.extend([
            "-@",
            endianness
        ])
    ret = Flip4dfpOutputs(
        root=execution.output_file("."),
        flipped_image=execution.output_file(output_image + ".4dfp.img") if (output_image is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FLIP_4DFP_METADATA",
    "Flip4dfpOutputs",
    "flip_4dfp",
]

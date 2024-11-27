# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_DCT_ALIGN_BINARY_METADATA = Metadata(
    id="fab87434d0987de7a7173eb733caa67e1aaa56b5.boutiques",
    name="mri_dct_align_binary",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriDctAlignBinaryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_dct_align_binary(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transformation_file: OutputPathType
    """The resulting transformation from the alignment"""


def mri_dct_align_binary(
    source_image: InputPathType,
    destination_image: InputPathType,
    output_transformation: str,
    runner: Runner | None = None,
) -> MriDctAlignBinaryOutputs:
    """
    A binary tool for aligning MRI images using DCT.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_image: Source image for alignment.
        destination_image: Destination image for alignment.
        output_transformation: Output transformation file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDctAlignBinaryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DCT_ALIGN_BINARY_METADATA)
    cargs = []
    cargs.append("mri_dct_align_binary")
    cargs.append(execution.input_file(source_image))
    cargs.append(execution.input_file(destination_image))
    cargs.append(output_transformation)
    ret = MriDctAlignBinaryOutputs(
        root=execution.output_file("."),
        output_transformation_file=execution.output_file("[OUTPUT_XFORM]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_DCT_ALIGN_BINARY_METADATA",
    "MriDctAlignBinaryOutputs",
    "mri_dct_align_binary",
]

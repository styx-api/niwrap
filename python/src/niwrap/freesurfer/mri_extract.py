# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_EXTRACT_METADATA = Metadata(
    id="8ea8492114a69493e6fb6d2e1d9f2b2b63d51237.boutiques",
    name="mri_extract",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriExtractOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_extract(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_extracted_volume: OutputPathType
    """Output file with extracted MRI data."""


def mri_extract(
    src_volume: InputPathType,
    dst_volume: InputPathType,
    like_template: InputPathType | None = None,
    coordinates: list[float] | None = None,
    runner: Runner | None = None,
) -> MriExtractOutputs:
    """
    MRI data extraction tool for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_volume: Source MRI volume file from which data will be extracted.
        dst_volume: The destination file where the extracted data will be\
            saved.
        like_template: Extract region like the given template volume.
        coordinates: Coordinates and size of the extraction box: x0 y0 z0 dx dy\
            dz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriExtractOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EXTRACT_METADATA)
    cargs = []
    cargs.append("mri_extract")
    if like_template is not None:
        cargs.extend([
            "-like",
            execution.input_file(like_template)
        ])
    cargs.append(execution.input_file(src_volume))
    cargs.append(execution.input_file(dst_volume))
    if coordinates is not None:
        cargs.extend(map(str, coordinates))
    ret = MriExtractOutputs(
        root=execution.output_file("."),
        output_extracted_volume=execution.output_file(pathlib.Path(dst_volume).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_EXTRACT_METADATA",
    "MriExtractOutputs",
    "mri_extract",
]

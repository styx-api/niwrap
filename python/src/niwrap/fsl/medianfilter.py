# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MEDIANFILTER_METADATA = Metadata(
    id="78b38d971dc71365ed3894d5bb7f83c2dee92ce5.boutiques",
    name="medianfilter",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class MedianfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `medianfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_file: OutputPathType
    """Output file containing the median filtered image"""


def medianfilter(
    infile: InputPathType,
    outfile: InputPathType,
    runner: Runner | None = None,
) -> MedianfilterOutputs:
    """
    A tool to perform 26 neighbourhood median filtering on an input image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input image file to be filtered (e.g., img.nii.gz).
        outfile: Output file to store the filtered image (e.g.,\
            img_filtered.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MedianfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MEDIANFILTER_METADATA)
    cargs = []
    cargs.append("medianfilter")
    cargs.append(execution.input_file(infile))
    cargs.append(execution.input_file(outfile))
    ret = MedianfilterOutputs(
        root=execution.output_file("."),
        filtered_file=execution.output_file(pathlib.Path(outfile).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MEDIANFILTER_METADATA",
    "MedianfilterOutputs",
    "medianfilter",
]

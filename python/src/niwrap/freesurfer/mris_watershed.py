# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_WATERSHED_METADATA = Metadata(
    id="9a83ea93f5a076342b24e15d530ba987b9017a6b.boutiques",
    name="mris_watershed",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisWatershedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_watershed(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_annotation_file: OutputPathType
    """The resulting annotation file from the watershed transform"""


def mris_watershed(
    input_surface: InputPathType,
    input_gradient_field: InputPathType,
    output_annotation: str,
    max_clusters: float | None = None,
    mask_label: str | None = None,
    runner: Runner | None = None,
) -> MrisWatershedOutputs:
    """
    This program computes the watershed transform on the surface of an intensity
    gradient and writes the resulting measurement into a .annot file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        input_gradient_field: Input gradient field file.
        output_annotation: Output annotation file.
        max_clusters: Set the number of maximum clusters.
        mask_label: Read in and mask the input volume that is not in the\
            specified label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisWatershedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_WATERSHED_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mris_watershed")
    cargs.append(execution.input_file(input_surface))
    cargs.append(execution.input_file(input_gradient_field))
    cargs.append(output_annotation)
    if max_clusters is not None:
        cargs.extend([
            "-M",
            str(max_clusters)
        ])
    if mask_label is not None:
        cargs.extend([
            "-mask_label",
            mask_label
        ])
    ret = MrisWatershedOutputs(
        root=execution.output_file("."),
        output_annotation_file=execution.output_file(output_annotation),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_WATERSHED_METADATA",
    "MrisWatershedOutputs",
    "mris_watershed",
]

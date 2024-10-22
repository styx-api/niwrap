# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_COMPUTE_OVERLAP_METADATA = Metadata(
    id="b8c7267b48763a28db58a035190b786e4ca3ba1c.boutiques",
    name="mri_compute_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriComputeOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_compute_overlap(
    volumes: list[InputPathType],
    label_numbers: list[str] | None = None,
    all_labels: bool = False,
    show_label: bool = False,
    total_overlap: bool = False,
    no_summary: bool = False,
    mask: InputPathType | None = None,
    output_file: str | None = None,
    quiet_mode: bool = False,
    translate_label: list[float] | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriComputeOverlapOutputs:
    """
    Computes three different types of overlap measures for labels in input volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volumes: Input volume files for which overlap measures are computed.
        label_numbers: List of specific label numbers for which to compute\
            overlap measures. If not specified, all labels are considered if -a is\
            provided.
        all_labels: Compute overlap for all labels.
        show_label: Show label name for segmentation.
        total_overlap: Compute the total overlap, which is the number of voxels\
            that are the same among all labels.
        no_summary: Do not compute total label summary.
        mask: Limit the domain of the calculation to the nonzero voxels in\
            specified volume.
        output_file: Filename to write results to.
        quiet_mode: Do not display results on standard display. If -l is\
            specified, this flag is automatically set.
        translate_label: Translate label l1 to label l2.
        help_: Print help.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_OVERLAP_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_compute_overlap")
    cargs.extend([execution.input_file(f) for f in volumes])
    if label_numbers is not None:
        cargs.extend(label_numbers)
    if all_labels:
        cargs.append("-a")
    if show_label:
        cargs.append("-s")
    if total_overlap:
        cargs.append("-total")
    if no_summary:
        cargs.append("-nosummary")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if output_file is not None:
        cargs.extend([
            "-l",
            output_file
        ])
    if quiet_mode:
        cargs.append("-q")
    if translate_label is not None:
        cargs.extend([
            "-t",
            *map(str, translate_label)
        ])
    if help_:
        cargs.append("-h")
    ret = MriComputeOverlapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_COMPUTE_OVERLAP_METADATA",
    "MriComputeOverlapOutputs",
    "mri_compute_overlap",
]

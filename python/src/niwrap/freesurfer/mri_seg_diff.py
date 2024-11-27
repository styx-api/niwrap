# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SEG_DIFF_METADATA = Metadata(
    id="71504722501dfa1ec92d8dd0c51d3ee7e1c9740c.boutiques",
    name="mri_seg_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSegDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_seg_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    diff_output: OutputPathType
    """Output diff segmentation file."""
    merged_output: OutputPathType | None
    """Output merged segmentation file."""


def mri_seg_diff(
    diff: str,
    seg1: InputPathType | None = None,
    seg2: InputPathType | None = None,
    seg: InputPathType | None = None,
    merged: str | None = None,
    diff_force: bool = False,
    debug: bool = False,
    checkopts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriSegDiffOutputs:
    """
    This program computes and merges differences in segmentation volumes, primarily
    for managing manual edits in FreeSurfer's aseg.mgz.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        diff: Output diff segmentation volume.
        seg1: First segmentation file (e.g., unedited).
        seg2: Second segmentation file (e.g., edited).
        seg: Source segmentation file (e.g., unedited).
        merged: Merged output, combining unedited with diff.
        diff_force: Force creation of a diff even if no diff is detected.
        debug: Turn on debugging.
        checkopts: Check options and exit without running.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEG_DIFF_METADATA)
    cargs = []
    cargs.append("mri_seg_diff")
    if seg1 is not None:
        cargs.extend([
            "--seg1",
            execution.input_file(seg1)
        ])
    if seg2 is not None:
        cargs.extend([
            "--seg2",
            execution.input_file(seg2)
        ])
    if seg is not None:
        cargs.extend([
            "--seg",
            execution.input_file(seg)
        ])
    cargs.extend([
        "--diff",
        diff
    ])
    if merged is not None:
        cargs.extend([
            "--merged",
            merged
        ])
    if diff_force:
        cargs.append("--diff-force")
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    if version:
        cargs.append("--version")
    ret = MriSegDiffOutputs(
        root=execution.output_file("."),
        diff_output=execution.output_file(diff),
        merged_output=execution.output_file(merged) if (merged is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SEG_DIFF_METADATA",
    "MriSegDiffOutputs",
    "mri_seg_diff",
]

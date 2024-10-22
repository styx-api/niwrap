# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_STATS2SEG_METADATA = Metadata(
    id="236e7b62048530381f4a8663a82ee18cb02c54b4.boutiques",
    name="mri_stats2seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriStats2segOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_stats2seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_output: OutputPathType
    """Output segmented file."""


def mri_stats2seg(
    stat_file: InputPathType,
    segmentation_volume: InputPathType,
    output_file: str,
    debug: bool = False,
    check_opts: bool = False,
    runner: Runner | None = None,
) -> MriStats2segOutputs:
    """
    A command-line tool for converting MRI statistical maps to segmented volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        stat_file: Stat file in an MRI format.
        segmentation_volume: Segmentation volume file.
        output_file: Output file.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriStats2segOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_STATS2SEG_METADATA)
    cargs = []
    cargs.append("mri_stats2seg")
    cargs.append("--stat")
    cargs.extend([
        "--stat",
        execution.input_file(stat_file)
    ])
    cargs.append("--seg")
    cargs.extend([
        "--seg",
        execution.input_file(segmentation_volume)
    ])
    cargs.append("--o")
    cargs.extend([
        "--o",
        output_file
    ])
    if debug:
        cargs.append("--debug")
    if check_opts:
        cargs.append("--checkopts")
    ret = MriStats2segOutputs(
        root=execution.output_file("."),
        segmented_output=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_STATS2SEG_METADATA",
    "MriStats2segOutputs",
    "mri_stats2seg",
]

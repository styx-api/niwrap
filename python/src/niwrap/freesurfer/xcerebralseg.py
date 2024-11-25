# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

XCEREBRALSEG_METADATA = Metadata(
    id="8185c238aec4ffe8f3eb70e8bcbb83f8e7a0af6b.boutiques",
    name="xcerebralseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class XcerebralsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xcerebralseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Output volume file for the whole head segmentation"""


def xcerebralseg(
    subject: str,
    output_volume: str | None = "apas+head.mgz",
    atlas: str | None = "/usr/local/freesurfer/average/aseg+spmhead+vermis+pons.ixi.gca",
    mergevol: str | None = "aparc+aseg.mgz",
    source_volume: str | None = "nu.mgz",
    no_stats: bool = False,
    seg1_name: str | None = None,
    no_pons: bool = False,
    no_vermis: bool = False,
    threads: float | None = None,
    runner: Runner | None = None,
) -> XcerebralsegOutputs:
    """
    Tool for labeling extracerebral structures including sulcal CSF, skull/bone,
    head soft tissue, and air inside the head, merged with aparc+aseg.mgz
    segmentation for a whole head segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier (required).
        output_volume: Output volume file (default: apas+head.mgz).
        atlas: Atlas file path (default:\
            /usr/local/freesurfer/average/aseg+spmhead+vermis+pons.ixi.gca).
        mergevol: Merge with mergevol (default: aparc+aseg.mgz).
        source_volume: Source intensity volume (default: nu.mgz).
        no_stats: Do not run mri_segstats.
        seg1_name: Full-head segmentation name (usually computed with\
            mri_ca_label).
        no_pons: Exclude pons segmentation.
        no_vermis: Exclude vermis segmentation.
        threads: Set number of OPENMP threads.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XcerebralsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XCEREBRALSEG_METADATA)
    cargs = []
    cargs.append("xcerebralseg")
    cargs.extend([
        "--s",
        subject
    ])
    if output_volume is not None:
        cargs.extend([
            "--o",
            output_volume
        ])
    if atlas is not None:
        cargs.extend([
            "--atlas",
            atlas
        ])
    if mergevol is not None:
        cargs.extend([
            "--m",
            mergevol
        ])
    if source_volume is not None:
        cargs.extend([
            "--srcvol",
            source_volume
        ])
    if no_stats:
        cargs.append("--no-stats")
    if seg1_name is not None:
        cargs.extend([
            "--seg1",
            seg1_name
        ])
    if no_pons:
        cargs.append("--no-pons")
    if no_vermis:
        cargs.append("--no-vermis")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    ret = XcerebralsegOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file("apas+head.mgz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XCEREBRALSEG_METADATA",
    "XcerebralsegOutputs",
    "xcerebralseg",
]

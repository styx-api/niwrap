# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_SUMA_FS_ROI_INFO_METADATA = Metadata(
    id="671e6ddb16b18d728e86051ee9166763f6d74855.boutiques",
    name="adjunct_suma_fs_roi_info",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctSumaFsRoiInfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_suma_fs_roi_info(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    rois_2000_ft: OutputPathType
    """Info for the '2000' parcellation."""
    rois_2009_ft: OutputPathType
    """Info for the '2009' parcellation."""
    segs_2000_ft: OutputPathType
    """Info for the '2000' parcellation brain mask and tissue/segmentations."""
    segs_2009_ft: OutputPathType
    """Info for the '2009' parcellation brain mask and tissue/segmentations."""


def adjunct_suma_fs_roi_info(
    subject_id: str,
    suma_directory: str,
    help_: bool = False,
    hview: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AdjunctSumaFsRoiInfoOutputs:
    """
    Script for making ROI stats for the SUMA/ directory created by
    @SUMA_Make_Spec_FS after running FreeSurfer's recon-all.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_suma_fs_roi_info.html
    
    Args:
        subject_id: Subject ID.
        suma_directory: SUMA directory output by AFNI's @SUMA_Make_Spec_FS.
        help_: Show help.
        hview: Show help in text editor.
        version: Show version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSumaFsRoiInfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SUMA_FS_ROI_INFO_METADATA)
    cargs = []
    cargs.append("adjunct_suma_fs_roi_info")
    cargs.extend([
        "-sid",
        subject_id
    ])
    cargs.extend([
        "-suma_dir",
        suma_directory
    ])
    if help_:
        cargs.append("-help")
    if hview:
        cargs.append("-hview")
    if version:
        cargs.append("-ver")
    ret = AdjunctSumaFsRoiInfoOutputs(
        root=execution.output_file("."),
        rois_2000_ft=execution.output_file("stats_fs_rois_2000_FT.1D"),
        rois_2009_ft=execution.output_file("stats_fs_rois_2009_FT.1D"),
        segs_2000_ft=execution.output_file("stats_fs_segs_2000_FT.1D"),
        segs_2009_ft=execution.output_file("stats_fs_segs_2009_FT.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_SUMA_FS_ROI_INFO_METADATA",
    "AdjunctSumaFsRoiInfoOutputs",
    "adjunct_suma_fs_roi_info",
]

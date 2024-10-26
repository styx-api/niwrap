# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VOL2LABEL_METADATA = Metadata(
    id="bcab966f1de6a06d8fe875c4cab580bdeaafabb3.boutiques",
    name="mri_vol2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriVol2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_vol2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Generated label file."""
    output_volume_file: OutputPathType | None
    """Generated label volume file."""


def mri_vol2label(
    input_: InputPathType,
    label_file: str,
    label_id: float | None = None,
    threshold: float | None = None,
    vol_file: str | None = None,
    surf_subject_hemi: str | None = None,
    surf_path: str | None = None,
    opt_params: str | None = None,
    remove_holes: bool = False,
    dilations: float | None = None,
    erosions: float | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriVol2labelOutputs:
    """
    Converts values in a volume or surface overlay to a label using specified
    parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_: Input volume or surface overlay.
        label_file: Name of output label file.
        label_id: Value to match in the input.
        threshold: Threshold the input to make label (i.e., input > threshold)\
            instead of using Label ID.
        vol_file: Write label volume in this file.
        surf_subject_hemi: Interpret input as surface overlay with the given\
            subject and hemisphere (optionally with surface).
        surf_path: Specify surface path instead of subject/hemi.
        opt_params: Treats input as a probability map. Format: target delta\
            valmap.
        remove_holes: Remove holes in label and islands (with --surf only).
        dilations: Dilate label (with --surf only).
        erosions: Erode label (with --surf only).
        help_: Print out help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVol2labelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOL2LABEL_METADATA)
    cargs = []
    cargs.append("mri_vol2label")
    cargs.append("--i")
    cargs.extend([
        "--i",
        execution.input_file(input_)
    ])
    cargs.append("--id")
    if label_id is not None:
        cargs.extend([
            "--id",
            str(label_id)
        ])
    cargs.append("--thresh")
    if threshold is not None:
        cargs.extend([
            "--thresh",
            str(threshold)
        ])
    cargs.append("--l")
    cargs.extend([
        "--l",
        label_file
    ])
    cargs.append("--v")
    if vol_file is not None:
        cargs.extend([
            "--v",
            vol_file
        ])
    cargs.append("--surf")
    if surf_subject_hemi is not None:
        cargs.extend([
            "--surf",
            surf_subject_hemi
        ])
    cargs.append("--surf-path")
    if surf_path is not None:
        cargs.extend([
            "--surf-path",
            surf_path
        ])
    cargs.append("--opt")
    if opt_params is not None:
        cargs.extend([
            "--opt",
            opt_params
        ])
    cargs.append("--remove-holes-islands")
    if remove_holes:
        cargs.append("--remove-holes-islands")
    cargs.append("--dilate")
    if dilations is not None:
        cargs.extend([
            "--dilate",
            str(dilations)
        ])
    cargs.append("--erode")
    if erosions is not None:
        cargs.extend([
            "--erode",
            str(erosions)
        ])
    if help_:
        cargs.append("--help")
    ret = MriVol2labelOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(label_file),
        output_volume_file=execution.output_file(vol_file) if (vol_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_VOL2LABEL_METADATA",
    "MriVol2labelOutputs",
    "mri_vol2label",
]

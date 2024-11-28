# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_LABEL_AREA_METADATA = Metadata(
    id="af4ae64d94b43274563c0c9b58c9131bb1103886.boutiques",
    name="mris_label_area",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisLabelAreaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label_area(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_label_area(
    subject_name: str,
    hemi: str,
    surf_name: str,
    annot_name: str,
    labels: list[str],
    pct_flag: bool = False,
    log_file: str | None = None,
    brain_vol: str | None = None,
    runner: Runner | None = None,
) -> MrisLabelAreaOutputs:
    """
    Compute the area of specific labels on a surface of a brain hemisphere in
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemi: Hemisphere, typically 'lh' or 'rh'.
        surf_name: Surface name.
        annot_name: Annotation name.
        labels: Labels to calculate area for.
        pct_flag: Compute brain area as a percentage of all brain labels.
        log_file: Log results to file (use %d to include label number).
        brain_vol: Load brain volume and use it to normalize areas.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabelAreaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL_AREA_METADATA)
    cargs = []
    cargs.append("mris_label_area")
    if pct_flag:
        cargs.append("-p")
    if log_file is not None:
        cargs.extend([
            "-l",
            log_file
        ])
    if brain_vol is not None:
        cargs.extend([
            "-b",
            brain_vol
        ])
    cargs.append(subject_name)
    cargs.append(hemi)
    cargs.append(surf_name)
    cargs.append(annot_name)
    cargs.extend(labels)
    ret = MrisLabelAreaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_LABEL_AREA_METADATA",
    "MrisLabelAreaOutputs",
    "mris_label_area",
]

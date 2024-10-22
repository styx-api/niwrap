# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_COMPUTE_ACORR_METADATA = Metadata(
    id="8d79067612b7c7c1a02eda210109a56f5c751d45.boutiques",
    name="mris_compute_acorr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisComputeAcorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_acorr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_compute_acorr(
    output_subject: str,
    hemi: str,
    surf: InputPathType,
    curv: InputPathType,
    c1_subjects: list[str],
    c2_subjects: list[str],
    runner: Runner | None = None,
) -> MrisComputeAcorrOutputs:
    """
    Compute the autocorrelation function of a curvature file on a spherical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_subject: The output subject file.
        hemi: Specify the hemisphere for processing.
        surf: The surface file which must be a spherical surface suitable for\
            computing geodesics.
        curv: The input curvature file.
        c1_subjects: List of subjects from one class.
        c2_subjects: List of subjects from another class.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeAcorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_ACORR_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mris_compute_acorr")
    cargs.append("-o")
    cargs.extend([
        "-o",
        output_subject
    ])
    cargs.append(hemi)
    cargs.append(execution.input_file(surf))
    cargs.append(execution.input_file(curv))
    cargs.extend(c1_subjects)
    cargs.append(":")
    cargs.extend(c2_subjects)
    ret = MrisComputeAcorrOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_COMPUTE_ACORR_METADATA",
    "MrisComputeAcorrOutputs",
    "mris_compute_acorr",
]

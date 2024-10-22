# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MULTISCALE_STATS_METADATA = Metadata(
    id="b5c8f81f66bfdfad08f197f106b3125b31c02eac.boutiques",
    name="mris_multiscale_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisMultiscaleStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_multiscale_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_multiscale_stats(
    output_subject: str,
    hemi: str,
    surf: InputPathType,
    curv: InputPathType,
    class1_subjects: list[str],
    class2_subjects: list[str],
    runner: Runner | None = None,
) -> MrisMultiscaleStatsOutputs:
    """
    Compute the autocorrelation function of a curvature file using multiscale
    statistical techniques.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_subject: The output subject identifier.
        hemi: Specify which hemisphere to use.
        surf: A spherical surface file suitable for computing geodesics.
        curv: The curvature file to be processed.
        class1_subjects: List of subjects from one class.
        class2_subjects: List of subjects from another class.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMultiscaleStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MULTISCALE_STATS_METADATA)
    cargs = []
    cargs.append("mris_multiscale_stats")
    cargs.append("-o")
    cargs.extend([
        "-o",
        output_subject
    ])
    cargs.append("[OPTIONS]")
    cargs.append(hemi)
    cargs.append(execution.input_file(surf))
    cargs.append(execution.input_file(curv))
    cargs.extend(class1_subjects)
    cargs.append(":")
    cargs.extend(class2_subjects)
    ret = MrisMultiscaleStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_MULTISCALE_STATS_METADATA",
    "MrisMultiscaleStatsOutputs",
    "mris_multiscale_stats",
]

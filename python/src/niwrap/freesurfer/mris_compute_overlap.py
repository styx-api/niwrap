# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_COMPUTE_OVERLAP_METADATA = Metadata(
    id="b1711e8a9fdbab9fd171b5b8a201396b8d6f1ceb.boutiques",
    name="mris_compute_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisComputeOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_compute_overlap(
    subject: str,
    hemi: str,
    surface: str,
    annotation: str,
    labels: list[str],
    percentage: bool = False,
    log_file: str | None = None,
    brain_volume: InputPathType | None = None,
    runner: Runner | None = None,
) -> MrisComputeOverlapOutputs:
    """
    Tool to compute the overlap between two or more labels on a cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject name.
        hemi: Hemisphere (e.g. lh or rh).
        surface: Surface name.
        annotation: Annotation name.
        labels: Labels to compute overlap for.
        percentage: Compute brain area as a percentage of all brain labels.
        log_file: Log results to file, where %d will include label number.
        brain_volume: Load brain volume and use it to normalize areas.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_OVERLAP_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mris_compute_overlap")
    cargs.append(subject)
    cargs.append(hemi)
    cargs.append(surface)
    cargs.append(annotation)
    cargs.extend(labels)
    if percentage:
        cargs.append("-p")
    if log_file is not None:
        cargs.extend([
            "-l",
            log_file
        ])
    if brain_volume is not None:
        cargs.extend([
            "-b",
            execution.input_file(brain_volume)
        ])
    ret = MrisComputeOverlapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_COMPUTE_OVERLAP_METADATA",
    "MrisComputeOverlapOutputs",
    "mris_compute_overlap",
]

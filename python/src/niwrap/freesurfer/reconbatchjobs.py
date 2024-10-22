# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RECONBATCHJOBS_METADATA = Metadata(
    id="3b88343e632e9bbafdf43ea3df14e2cf0c3f34d1.boutiques",
    name="reconbatchjobs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ReconbatchjobsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reconbatchjobs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def reconbatchjobs(
    logfile: str,
    cmdfiles: list[str],
    runner: Runner | None = None,
) -> ReconbatchjobsOutputs:
    """
    Batch job processor for reconstruction scripts.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        logfile: Log file to capture output of batch jobs.
        cmdfiles: Command files for batch processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconbatchjobsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECONBATCHJOBS_METADATA)
    cargs = []
    cargs.append("reconbatchjobs")
    cargs.append(logfile)
    cargs.extend(cmdfiles)
    ret = ReconbatchjobsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RECONBATCHJOBS_METADATA",
    "ReconbatchjobsOutputs",
    "reconbatchjobs",
]

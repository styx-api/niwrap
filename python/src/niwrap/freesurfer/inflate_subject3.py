# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INFLATE_SUBJECT3_METADATA = Metadata(
    id="a274d70311c1a539bade6099eed3c3f3614e2009.boutiques",
    name="inflate_subject3",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class InflateSubject3Outputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject3(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def inflate_subject3(
    subjects_dir: str,
    script_name: str,
    runner: Runner | None = None,
) -> InflateSubject3Outputs:
    """
    A tool related to subject inflation in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: The directory where FreeSurfer subjects are stored.
        script_name: The name of the script to be executed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubject3Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT3_METADATA)
    cargs = []
    cargs.append("inflate_subject3")
    cargs.append(subjects_dir)
    cargs.append(script_name)
    ret = InflateSubject3Outputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INFLATE_SUBJECT3_METADATA",
    "InflateSubject3Outputs",
    "inflate_subject3",
]

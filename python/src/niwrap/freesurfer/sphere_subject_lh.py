# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SPHERE_SUBJECT_LH_METADATA = Metadata(
    id="6cb29acf4c0a72caae7b4c3b000c37495ed423e6.boutiques",
    name="sphere_subject-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SphereSubjectLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sphere_subject_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def sphere_subject_lh(
    license_file: InputPathType,
    runner: Runner | None = None,
) -> SphereSubjectLhOutputs:
    """
    Tool for processing spherical representations in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        license_file: Path to the FreeSurfer license file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SphereSubjectLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPHERE_SUBJECT_LH_METADATA)
    cargs = []
    cargs.extend([
        "-lh",
        "sphere_subject" + execution.input_file(license_file)
    ])
    ret = SphereSubjectLhOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SPHERE_SUBJECT_LH_METADATA",
    "SphereSubjectLhOutputs",
    "sphere_subject_lh",
]

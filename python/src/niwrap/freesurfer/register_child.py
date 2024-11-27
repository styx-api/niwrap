# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REGISTER_CHILD_METADATA = Metadata(
    id="605dca8f2351a2947069059787f2878020583ef2.boutiques",
    name="register_child",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RegisterChildOutputs(typing.NamedTuple):
    """
    Output object returned when calling `register_child(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_control_points: OutputPathType
    """File where transformed control points are written."""
    intensity_normalized_volume: OutputPathType
    """File where intensity normalized volume is written."""


def register_child(
    input_volume: InputPathType,
    output_directory: str,
    runner: Runner | None = None,
) -> RegisterChildOutputs:
    """
    A tool used for registering MR volumes with a child's atlas in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input MR volume to be used for registration.
        output_directory: Directory where output files will be written.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegisterChildOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REGISTER_CHILD_METADATA)
    cargs = []
    cargs.append("register_child")
    cargs.append(execution.input_file(input_volume))
    cargs.append(output_directory)
    ret = RegisterChildOutputs(
        root=execution.output_file("."),
        transformed_control_points=execution.output_file("[OUTPUT_DIR]/fsamples"),
        intensity_normalized_volume=execution.output_file("[OUTPUT_DIR]/norm"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REGISTER_CHILD_METADATA",
    "RegisterChildOutputs",
    "register_child",
]

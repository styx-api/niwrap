# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RIGID_REGISTER_METADATA = Metadata(
    id="01ab99672586fbc77fecc88ed31ad35e50033472.boutiques",
    name="mri_rigid_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRigidRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rigid_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transform_file: OutputPathType
    """Output file for transform matrix"""


def mri_rigid_register(
    source_volume: InputPathType,
    target_volume: InputPathType,
    transform_output: str,
    runner: Runner | None = None,
) -> MriRigidRegisterOutputs:
    """
    Rigid registration tool for MRI volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_volume: Source volume file for registration.
        target_volume: Target volume file for registration.
        transform_output: Output file name for the transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRigidRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RIGID_REGISTER_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_rigid_register")
    cargs.append(execution.input_file(source_volume))
    cargs.append(execution.input_file(target_volume))
    cargs.append(transform_output)
    ret = MriRigidRegisterOutputs(
        root=execution.output_file("."),
        transform_file=execution.output_file(transform_output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_RIGID_REGISTER_METADATA",
    "MriRigidRegisterOutputs",
    "mri_rigid_register",
]

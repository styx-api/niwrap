# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_GRADIENT_METADATA = Metadata(
    id="8a3963a5286efe9681117c3b59f9af7c79a97b6e.boutiques",
    name="mris_gradient",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_gradient: OutputPathType
    """The resulting gradient measurement written into a .mgz file."""


def mris_gradient(
    input_surface: InputPathType,
    input_vector_field: InputPathType,
    output_gradient_file: str,
    runner: Runner | None = None,
) -> MrisGradientOutputs:
    """
    This program computes the gradient of an intensity profile of the cortical
    ribbon and writes the resulting measurement into a .mgz file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Path to the input surface file.
        input_vector_field: Path to the input vector field file.
        output_gradient_file: Path to the output gradient file ending with\
            .mgz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_GRADIENT_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mris_gradient")
    cargs.append(execution.input_file(input_surface))
    cargs.append(execution.input_file(input_vector_field))
    cargs.append(output_gradient_file)
    ret = MrisGradientOutputs(
        root=execution.output_file("."),
        output_gradient=execution.output_file(output_gradient_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_GRADIENT_METADATA",
    "MrisGradientOutputs",
    "mris_gradient",
]

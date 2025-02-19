# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_GRADIENT_METADATA = Metadata(
    id="4e76ee59424b712977309da37bac35a8195a7230.boutiques",
    name="mris_gradient",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisGradientParameters = typing.TypedDict('MrisGradientParameters', {
    "__STYX_TYPE__": typing.Literal["mris_gradient"],
    "input_surface": InputPathType,
    "input_vector_field": InputPathType,
    "output_gradient_file": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mris_gradient": mris_gradient_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mris_gradient": mris_gradient_outputs,
    }.get(t)


class MrisGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_gradient: OutputPathType
    """The resulting gradient measurement written into a .mgz file."""


def mris_gradient_params(
    input_surface: InputPathType,
    input_vector_field: InputPathType,
    output_gradient_file: str,
) -> MrisGradientParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Path to the input surface file.
        input_vector_field: Path to the input vector field file.
        output_gradient_file: Path to the output gradient file ending with\
            .mgz.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_gradient",
        "input_surface": input_surface,
        "input_vector_field": input_vector_field,
        "output_gradient_file": output_gradient_file,
    }
    return params


def mris_gradient_cargs(
    params: MrisGradientParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mris_gradient")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("input_vector_field")))
    cargs.append(params.get("output_gradient_file"))
    return cargs


def mris_gradient_outputs(
    params: MrisGradientParameters,
    execution: Execution,
) -> MrisGradientOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisGradientOutputs(
        root=execution.output_file("."),
        output_gradient=execution.output_file(params.get("output_gradient_file")),
    )
    return ret


def mris_gradient_execute(
    params: MrisGradientParameters,
    execution: Execution,
) -> MrisGradientOutputs:
    """
    This program computes the gradient of an intensity profile of the cortical
    ribbon and writes the resulting measurement into a .mgz file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisGradientOutputs`).
    """
    params = execution.params(params)
    cargs = mris_gradient_cargs(params, execution)
    ret = mris_gradient_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = mris_gradient_params(
        input_surface=input_surface,
        input_vector_field=input_vector_field,
        output_gradient_file=output_gradient_file,
    )
    return mris_gradient_execute(params, execution)


__all__ = [
    "MRIS_GRADIENT_METADATA",
    "MrisGradientOutputs",
    "MrisGradientParameters",
    "mris_gradient",
    "mris_gradient_params",
]

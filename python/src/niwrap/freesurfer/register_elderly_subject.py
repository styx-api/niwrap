# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REGISTER_ELDERLY_SUBJECT_METADATA = Metadata(
    id="537220baa60ce5febcf14be16d4b791c3cbbebb9.boutiques",
    name="register_elderly_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


RegisterElderlySubjectParameters = typing.TypedDict('RegisterElderlySubjectParameters', {
    "__STYX_TYPE__": typing.Literal["register_elderly_subject"],
    "sampling_percentage": typing.NotRequired[float | None],
    "output_fsamples": str,
    "output_norm": str,
    "input_volume": InputPathType,
    "gca_file": InputPathType,
    "transform_file": InputPathType,
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
        "register_elderly_subject": register_elderly_subject_cargs,
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
        "register_elderly_subject": register_elderly_subject_outputs,
    }.get(t)


class RegisterElderlySubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `register_elderly_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_fsamples_output: OutputPathType
    """Transformed control points output"""
    normalized_volume_output: OutputPathType
    """Intensity normalized volume"""


def register_elderly_subject_params(
    output_fsamples: str,
    output_norm: str,
    input_volume: InputPathType,
    gca_file: InputPathType,
    transform_file: InputPathType,
    sampling_percentage: float | None = 0.5,
) -> RegisterElderlySubjectParameters:
    """
    Build parameters.
    
    Args:
        output_fsamples: Output path for transformed control points.
        output_norm: Output path for intensity normalized volume.
        input_volume: Input MRI volume to register.
        gca_file: GCA file for registration.
        transform_file: Output transform file.
        sampling_percentage: Percentage of white matter points to use as\
            control points.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "register_elderly_subject",
        "output_fsamples": output_fsamples,
        "output_norm": output_norm,
        "input_volume": input_volume,
        "gca_file": gca_file,
        "transform_file": transform_file,
    }
    if sampling_percentage is not None:
        params["sampling_percentage"] = sampling_percentage
    return params


def register_elderly_subject_cargs(
    params: RegisterElderlySubjectParameters,
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
    cargs.append("mri_em_register")
    if params.get("sampling_percentage") is not None:
        cargs.extend([
            "-p",
            str(params.get("sampling_percentage"))
        ])
    cargs.extend([
        "-fsamples",
        params.get("output_fsamples")
    ])
    cargs.extend([
        "-norm",
        params.get("output_norm")
    ])
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("gca_file")))
    cargs.append(execution.input_file(params.get("transform_file")))
    return cargs


def register_elderly_subject_outputs(
    params: RegisterElderlySubjectParameters,
    execution: Execution,
) -> RegisterElderlySubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegisterElderlySubjectOutputs(
        root=execution.output_file("."),
        transformed_fsamples_output=execution.output_file(params.get("output_fsamples")),
        normalized_volume_output=execution.output_file(params.get("output_norm")),
    )
    return ret


def register_elderly_subject_execute(
    params: RegisterElderlySubjectParameters,
    execution: Execution,
) -> RegisterElderlySubjectOutputs:
    """
    Tool for registering MRI images of elderly subjects using Freesurfer's
    mri_em_register.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegisterElderlySubjectOutputs`).
    """
    params = execution.params(params)
    cargs = register_elderly_subject_cargs(params, execution)
    ret = register_elderly_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def register_elderly_subject(
    output_fsamples: str,
    output_norm: str,
    input_volume: InputPathType,
    gca_file: InputPathType,
    transform_file: InputPathType,
    sampling_percentage: float | None = 0.5,
    runner: Runner | None = None,
) -> RegisterElderlySubjectOutputs:
    """
    Tool for registering MRI images of elderly subjects using Freesurfer's
    mri_em_register.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_fsamples: Output path for transformed control points.
        output_norm: Output path for intensity normalized volume.
        input_volume: Input MRI volume to register.
        gca_file: GCA file for registration.
        transform_file: Output transform file.
        sampling_percentage: Percentage of white matter points to use as\
            control points.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegisterElderlySubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REGISTER_ELDERLY_SUBJECT_METADATA)
    params = register_elderly_subject_params(
        sampling_percentage=sampling_percentage,
        output_fsamples=output_fsamples,
        output_norm=output_norm,
        input_volume=input_volume,
        gca_file=gca_file,
        transform_file=transform_file,
    )
    return register_elderly_subject_execute(params, execution)


__all__ = [
    "REGISTER_ELDERLY_SUBJECT_METADATA",
    "RegisterElderlySubjectOutputs",
    "RegisterElderlySubjectParameters",
    "register_elderly_subject",
    "register_elderly_subject_params",
]

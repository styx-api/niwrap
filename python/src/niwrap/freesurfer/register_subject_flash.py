# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REGISTER_SUBJECT_FLASH_METADATA = Metadata(
    id="9a7a639d778167b266b2e9f5c9a4ba404e0ced41.boutiques",
    name="register_subject_flash",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RegisterSubjectFlashParameters = typing.TypedDict('RegisterSubjectFlashParameters', {
    "__STYX_TYPE__": typing.Literal["register_subject_flash"],
    "input_volumes": list[InputPathType],
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
        "register_subject_flash": register_subject_flash_cargs,
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
        "register_subject_flash": register_subject_flash_outputs,
    }.get(t)


class RegisterSubjectFlashOutputs(typing.NamedTuple):
    """
    Output object returned when calling `register_subject_flash(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    log_file: OutputPathType
    """Log file output with registration results."""


def register_subject_flash_params(
    input_volumes: list[InputPathType],
) -> RegisterSubjectFlashParameters:
    """
    Build parameters.
    
    Args:
        input_volumes: Input volumes to register.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "register_subject_flash",
        "input_volumes": input_volumes,
    }
    return params


def register_subject_flash_cargs(
    params: RegisterSubjectFlashParameters,
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
    cargs.append("register_subject_flash")
    cargs.extend([execution.input_file(f) for f in params.get("input_volumes")])
    return cargs


def register_subject_flash_outputs(
    params: RegisterSubjectFlashParameters,
    execution: Execution,
) -> RegisterSubjectFlashOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegisterSubjectFlashOutputs(
        root=execution.output_file("."),
        log_file=execution.output_file("talairach.log"),
    )
    return ret


def register_subject_flash_execute(
    params: RegisterSubjectFlashParameters,
    execution: Execution,
) -> RegisterSubjectFlashOutputs:
    """
    Register subject using the FLASH forward model to predict intensity values.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegisterSubjectFlashOutputs`).
    """
    cargs = register_subject_flash_cargs(params, execution)
    ret = register_subject_flash_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def register_subject_flash(
    input_volumes: list[InputPathType],
    runner: Runner | None = None,
) -> RegisterSubjectFlashOutputs:
    """
    Register subject using the FLASH forward model to predict intensity values.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volumes: Input volumes to register.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegisterSubjectFlashOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REGISTER_SUBJECT_FLASH_METADATA)
    params = register_subject_flash_params(input_volumes=input_volumes)
    return register_subject_flash_execute(params, execution)


__all__ = [
    "REGISTER_SUBJECT_FLASH_METADATA",
    "RegisterSubjectFlashOutputs",
    "RegisterSubjectFlashParameters",
    "register_subject_flash",
    "register_subject_flash_params",
]

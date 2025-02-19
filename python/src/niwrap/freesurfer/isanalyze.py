# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ISANALYZE_METADATA = Metadata(
    id="3d8f8ed4f2f6a0e189b0b47b6a3b1fc896553e24.boutiques",
    name="isanalyze",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


IsanalyzeParameters = typing.TypedDict('IsanalyzeParameters', {
    "__STYX_TYPE__": typing.Literal["isanalyze"],
    "input_file": InputPathType,
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
        "isanalyze": isanalyze_cargs,
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
    }.get(t)


class IsanalyzeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `isanalyze(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def isanalyze_params(
    input_file: InputPathType,
) -> IsanalyzeParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file for IS analysis.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "isanalyze",
        "input_file": input_file,
    }
    return params


def isanalyze_cargs(
    params: IsanalyzeParameters,
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
    cargs.append("isanalyze")
    cargs.append(execution.input_file(params.get("input_file")))
    return cargs


def isanalyze_outputs(
    params: IsanalyzeParameters,
    execution: Execution,
) -> IsanalyzeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IsanalyzeOutputs(
        root=execution.output_file("."),
    )
    return ret


def isanalyze_execute(
    params: IsanalyzeParameters,
    execution: Execution,
) -> IsanalyzeOutputs:
    """
    A tool to analyze and process IS files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IsanalyzeOutputs`).
    """
    params = execution.params(params)
    cargs = isanalyze_cargs(params, execution)
    ret = isanalyze_outputs(params, execution)
    execution.run(cargs)
    return ret


def isanalyze(
    input_file: InputPathType,
    runner: Runner | None = None,
) -> IsanalyzeOutputs:
    """
    A tool to analyze and process IS files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input file for IS analysis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsanalyzeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISANALYZE_METADATA)
    params = isanalyze_params(
        input_file=input_file,
    )
    return isanalyze_execute(params, execution)


__all__ = [
    "ISANALYZE_METADATA",
    "IsanalyzeOutputs",
    "IsanalyzeParameters",
    "isanalyze",
    "isanalyze_params",
]

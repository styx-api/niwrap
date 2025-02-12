# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INFLATE_SUBJECT_METADATA = Metadata(
    id="0f453fc5ea15ce4839c856ec25b28572898bd123.boutiques",
    name="inflate_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
InflateSubjectParameters = typing.TypedDict('InflateSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["inflate_subject"],
    "args": typing.NotRequired[str | None],
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
        "inflate_subject": inflate_subject_cargs,
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
        "inflate_subject": inflate_subject_outputs,
    }.get(t)


class InflateSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output of inflate_subject command"""


def inflate_subject_params(
    args: str | None = None,
) -> InflateSubjectParameters:
    """
    Build parameters.
    
    Args:
        args: Arguments for the inflate_subject command.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inflate_subject",
    }
    if args is not None:
        params["args"] = args
    return params


def inflate_subject_cargs(
    params: InflateSubjectParameters,
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
    cargs.append("inflate_subject")
    if params.get("args") is not None:
        cargs.append(params.get("args"))
    return cargs


def inflate_subject_outputs(
    params: InflateSubjectParameters,
    execution: Execution,
) -> InflateSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InflateSubjectOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("args") + "_output.txt") if (params.get("args") is not None) else None,
    )
    return ret


def inflate_subject_execute(
    params: InflateSubjectParameters,
    execution: Execution,
) -> InflateSubjectOutputs:
    """
    Inflate subject script for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectOutputs`).
    """
    cargs = inflate_subject_cargs(params, execution)
    ret = inflate_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def inflate_subject(
    args: str | None = None,
    runner: Runner | None = None,
) -> InflateSubjectOutputs:
    """
    Inflate subject script for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        args: Arguments for the inflate_subject command.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_METADATA)
    params = inflate_subject_params(args=args)
    return inflate_subject_execute(params, execution)


__all__ = [
    "INFLATE_SUBJECT_METADATA",
    "InflateSubjectOutputs",
    "InflateSubjectParameters",
    "inflate_subject",
    "inflate_subject_params",
]

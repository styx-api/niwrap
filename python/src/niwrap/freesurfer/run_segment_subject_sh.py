# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_SEGMENT_SUBJECT_SH_METADATA = Metadata(
    id="3bee4c6b7ffa07b5a4e27cd0261d6a71efb4387a.boutiques",
    name="run_SegmentSubject.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RunSegmentSubjectShParameters = typing.TypedDict('RunSegmentSubjectShParameters', {
    "__STYX_TYPE__": typing.Literal["run_SegmentSubject.sh"],
    "deployedMCRroot": str,
    "arguments": typing.NotRequired[str | None],
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
        "run_SegmentSubject.sh": run_segment_subject_sh_cargs,
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
        "run_SegmentSubject.sh": run_segment_subject_sh_outputs,
    }.get(t)


class RunSegmentSubjectShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_segment_subject_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """The generated output file from the segmentation process."""


def run_segment_subject_sh_params(
    deployed_mcrroot: str,
    arguments: str | None = None,
) -> RunSegmentSubjectShParameters:
    """
    Build parameters.
    
    Args:
        deployed_mcrroot: The root directory of the deployed MATLAB Compiler\
            Runtime.
        arguments: Additional arguments to be passed to the SegmentSubject\
            script.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_SegmentSubject.sh",
        "deployedMCRroot": deployed_mcrroot,
    }
    if arguments is not None:
        params["arguments"] = arguments
    return params


def run_segment_subject_sh_cargs(
    params: RunSegmentSubjectShParameters,
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
    cargs.append("run_SegmentSubject.sh")
    cargs.append(params.get("deployedMCRroot"))
    if params.get("arguments") is not None:
        cargs.append(params.get("arguments"))
    return cargs


def run_segment_subject_sh_outputs(
    params: RunSegmentSubjectShParameters,
    execution: Execution,
) -> RunSegmentSubjectShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunSegmentSubjectShOutputs(
        root=execution.output_file("."),
        output=execution.output_file("outputFileName"),
    )
    return ret


def run_segment_subject_sh_execute(
    params: RunSegmentSubjectShParameters,
    execution: Execution,
) -> RunSegmentSubjectShOutputs:
    """
    A command-line tool for subject segmentation in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunSegmentSubjectShOutputs`).
    """
    cargs = run_segment_subject_sh_cargs(params, execution)
    ret = run_segment_subject_sh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def run_segment_subject_sh(
    deployed_mcrroot: str,
    arguments: str | None = None,
    runner: Runner | None = None,
) -> RunSegmentSubjectShOutputs:
    """
    A command-line tool for subject segmentation in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        deployed_mcrroot: The root directory of the deployed MATLAB Compiler\
            Runtime.
        arguments: Additional arguments to be passed to the SegmentSubject\
            script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunSegmentSubjectShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_SEGMENT_SUBJECT_SH_METADATA)
    params = run_segment_subject_sh_params(deployed_mcrroot=deployed_mcrroot, arguments=arguments)
    return run_segment_subject_sh_execute(params, execution)


__all__ = [
    "RUN_SEGMENT_SUBJECT_SH_METADATA",
    "RunSegmentSubjectShOutputs",
    "RunSegmentSubjectShParameters",
    "run_segment_subject_sh",
    "run_segment_subject_sh_params",
]

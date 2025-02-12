# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_SEGMENT_SUBFIELDS_T1_LONGITUDINAL_SH_METADATA = Metadata(
    id="06a7bfba6231f999f1b4d6fa26f1a22c4fe4eb12.boutiques",
    name="run_SegmentSubfieldsT1Longitudinal.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RunSegmentSubfieldsT1LongitudinalShParameters = typing.TypedDict('RunSegmentSubfieldsT1LongitudinalShParameters', {
    "__STYX_TYPE__": typing.Literal["run_SegmentSubfieldsT1Longitudinal.sh"],
    "deployed_mcr_root": str,
    "additional_args": typing.NotRequired[str | None],
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
        "run_SegmentSubfieldsT1Longitudinal.sh": run_segment_subfields_t1_longitudinal_sh_cargs,
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


class RunSegmentSubfieldsT1LongitudinalShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_segment_subfields_t1_longitudinal_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def run_segment_subfields_t1_longitudinal_sh_params(
    deployed_mcr_root: str,
    additional_args: str | None = None,
) -> RunSegmentSubfieldsT1LongitudinalShParameters:
    """
    Build parameters.
    
    Args:
        deployed_mcr_root: Root directory for the deployed MATLAB Runtime\
            environment.
        additional_args: Additional arguments for the script.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_SegmentSubfieldsT1Longitudinal.sh",
        "deployed_mcr_root": deployed_mcr_root,
    }
    if additional_args is not None:
        params["additional_args"] = additional_args
    return params


def run_segment_subfields_t1_longitudinal_sh_cargs(
    params: RunSegmentSubfieldsT1LongitudinalShParameters,
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
    cargs.append("run_SegmentSubfieldsT1Longitudinal.sh")
    cargs.append(params.get("deployed_mcr_root"))
    if params.get("additional_args") is not None:
        cargs.append(params.get("additional_args"))
    return cargs


def run_segment_subfields_t1_longitudinal_sh_outputs(
    params: RunSegmentSubfieldsT1LongitudinalShParameters,
    execution: Execution,
) -> RunSegmentSubfieldsT1LongitudinalShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunSegmentSubfieldsT1LongitudinalShOutputs(
        root=execution.output_file("."),
    )
    return ret


def run_segment_subfields_t1_longitudinal_sh_execute(
    params: RunSegmentSubfieldsT1LongitudinalShParameters,
    execution: Execution,
) -> RunSegmentSubfieldsT1LongitudinalShOutputs:
    """
    Script for segmenting subfields from T1-weighted longitudinal data using
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunSegmentSubfieldsT1LongitudinalShOutputs`).
    """
    cargs = run_segment_subfields_t1_longitudinal_sh_cargs(params, execution)
    ret = run_segment_subfields_t1_longitudinal_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def run_segment_subfields_t1_longitudinal_sh(
    deployed_mcr_root: str,
    additional_args: str | None = None,
    runner: Runner | None = None,
) -> RunSegmentSubfieldsT1LongitudinalShOutputs:
    """
    Script for segmenting subfields from T1-weighted longitudinal data using
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        deployed_mcr_root: Root directory for the deployed MATLAB Runtime\
            environment.
        additional_args: Additional arguments for the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunSegmentSubfieldsT1LongitudinalShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_SEGMENT_SUBFIELDS_T1_LONGITUDINAL_SH_METADATA)
    params = run_segment_subfields_t1_longitudinal_sh_params(deployed_mcr_root=deployed_mcr_root, additional_args=additional_args)
    return run_segment_subfields_t1_longitudinal_sh_execute(params, execution)


__all__ = [
    "RUN_SEGMENT_SUBFIELDS_T1_LONGITUDINAL_SH_METADATA",
    "RunSegmentSubfieldsT1LongitudinalShOutputs",
    "RunSegmentSubfieldsT1LongitudinalShParameters",
    "run_segment_subfields_t1_longitudinal_sh",
    "run_segment_subfields_t1_longitudinal_sh_params",
]

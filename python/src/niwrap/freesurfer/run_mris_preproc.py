# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_MRIS_PREPROC_METADATA = Metadata(
    id="3629333e45a8eb1987148cec6b9546163e9cda0d.boutiques",
    name="run_mris_preproc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RunMrisPreprocParameters = typing.TypedDict('RunMrisPreprocParameters', {
    "__STYX_TYPE__": typing.Literal["run_mris_preproc"],
    "qdec_table": InputPathType,
    "target_average": typing.NotRequired[str | None],
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
        "run_mris_preproc": run_mris_preproc_cargs,
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


class RunMrisPreprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_mris_preproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def run_mris_preproc_params(
    qdec_table: InputPathType,
    target_average: str | None = None,
) -> RunMrisPreprocParameters:
    """
    Build parameters.
    
    Args:
        qdec_table: Text file of subject data used by qdec.
        target_average: Specify a target average, default is fsaverage.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_mris_preproc",
        "qdec_table": qdec_table,
    }
    if target_average is not None:
        params["target_average"] = target_average
    return params


def run_mris_preproc_cargs(
    params: RunMrisPreprocParameters,
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
    cargs.append("run_mris_preproc")
    cargs.append(execution.input_file(params.get("qdec_table")))
    if params.get("target_average") is not None:
        cargs.append(params.get("target_average"))
    return cargs


def run_mris_preproc_outputs(
    params: RunMrisPreprocParameters,
    execution: Execution,
) -> RunMrisPreprocOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunMrisPreprocOutputs(
        root=execution.output_file("."),
    )
    return ret


def run_mris_preproc_execute(
    params: RunMrisPreprocParameters,
    execution: Execution,
) -> RunMrisPreprocOutputs:
    """
    Utility to create pre-smoothed surface data on a target average subject for Qdec
    application.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunMrisPreprocOutputs`).
    """
    cargs = run_mris_preproc_cargs(params, execution)
    ret = run_mris_preproc_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def run_mris_preproc(
    qdec_table: InputPathType,
    target_average: str | None = None,
    runner: Runner | None = None,
) -> RunMrisPreprocOutputs:
    """
    Utility to create pre-smoothed surface data on a target average subject for Qdec
    application.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec_table: Text file of subject data used by qdec.
        target_average: Specify a target average, default is fsaverage.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunMrisPreprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_MRIS_PREPROC_METADATA)
    params = run_mris_preproc_params(qdec_table=qdec_table, target_average=target_average)
    return run_mris_preproc_execute(params, execution)


__all__ = [
    "RUN_MRIS_PREPROC_METADATA",
    "RunMrisPreprocOutputs",
    "RunMrisPreprocParameters",
    "run_mris_preproc",
    "run_mris_preproc_params",
]

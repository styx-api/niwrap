# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FS_TUTORIAL_DATA_METADATA = Metadata(
    id="80182cd74220da19e2c55dc09c1599b0b78de72e.boutiques",
    name="fs_tutorial_data",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FsTutorialDataParameters = typing.TypedDict('FsTutorialDataParameters', {
    "__STYX_TYPE__": typing.Literal["fs_tutorial_data"],
    "rsync_options": typing.NotRequired[list[str] | None],
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
        "fs_tutorial_data": fs_tutorial_data_cargs,
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
        "fs_tutorial_data": fs_tutorial_data_outputs,
    }.get(t)


class FsTutorialDataOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_tutorial_data(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tutorial_data_dir: OutputPathType
    """Directory where tutorial data will be downloaded and installed."""


def fs_tutorial_data_params(
    rsync_options: list[str] | None = None,
) -> FsTutorialDataParameters:
    """
    Build parameters.
    
    Args:
        rsync_options: Additional rsync options for downloading tutorial data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs_tutorial_data",
    }
    if rsync_options is not None:
        params["rsync_options"] = rsync_options
    return params


def fs_tutorial_data_cargs(
    params: FsTutorialDataParameters,
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
    cargs.append("fs_tutorial_data")
    if params.get("rsync_options") is not None:
        cargs.extend(params.get("rsync_options"))
    return cargs


def fs_tutorial_data_outputs(
    params: FsTutorialDataParameters,
    execution: Execution,
) -> FsTutorialDataOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsTutorialDataOutputs(
        root=execution.output_file("."),
        tutorial_data_dir=execution.output_file("/usr/local/freesurfer/subjects/tutorial_data"),
    )
    return ret


def fs_tutorial_data_execute(
    params: FsTutorialDataParameters,
    execution: Execution,
) -> FsTutorialDataOutputs:
    """
    Tool to download and install FreeSurfer tutorial data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsTutorialDataOutputs`).
    """
    cargs = fs_tutorial_data_cargs(params, execution)
    ret = fs_tutorial_data_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_tutorial_data(
    rsync_options: list[str] | None = None,
    runner: Runner | None = None,
) -> FsTutorialDataOutputs:
    """
    Tool to download and install FreeSurfer tutorial data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        rsync_options: Additional rsync options for downloading tutorial data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsTutorialDataOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_TUTORIAL_DATA_METADATA)
    params = fs_tutorial_data_params(rsync_options=rsync_options)
    return fs_tutorial_data_execute(params, execution)


__all__ = [
    "FS_TUTORIAL_DATA_METADATA",
    "FsTutorialDataOutputs",
    "FsTutorialDataParameters",
    "fs_tutorial_data",
    "fs_tutorial_data_params",
]

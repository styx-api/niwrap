# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UNPACKSDCMDIR_METADATA = Metadata(
    id="874ca0580e83acbaad099d815a81e39d50b1ac26.boutiques",
    name="unpacksdcmdir",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
UnpacksdcmdirParameters = typing.TypedDict('UnpacksdcmdirParameters', {
    "__STYX_TYPE__": typing.Literal["unpacksdcmdir"],
    "input_directory": str,
    "output_directory": str,
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
        "unpacksdcmdir": unpacksdcmdir_cargs,
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
        "unpacksdcmdir": unpacksdcmdir_outputs,
    }.get(t)


class UnpacksdcmdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpacksdcmdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unpacked_data: OutputPathType
    """The directory that will contain the unpacked data."""


def unpacksdcmdir_params(
    input_directory: str,
    output_directory: str,
) -> UnpacksdcmdirParameters:
    """
    Build parameters.
    
    Args:
        input_directory: The directory containing SD card data to be unpacked.
        output_directory: The output directory where unpacked data will be\
            stored.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "unpacksdcmdir",
        "input_directory": input_directory,
        "output_directory": output_directory,
    }
    return params


def unpacksdcmdir_cargs(
    params: UnpacksdcmdirParameters,
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
    cargs.append("unpacksdcmdir")
    cargs.append(params.get("input_directory"))
    cargs.append(params.get("output_directory"))
    return cargs


def unpacksdcmdir_outputs(
    params: UnpacksdcmdirParameters,
    execution: Execution,
) -> UnpacksdcmdirOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UnpacksdcmdirOutputs(
        root=execution.output_file("."),
        unpacked_data=execution.output_file(params.get("output_directory") + "/unpacked_data"),
    )
    return ret


def unpacksdcmdir_execute(
    params: UnpacksdcmdirParameters,
    execution: Execution,
) -> UnpacksdcmdirOutputs:
    """
    A tool for unpacking SD card directories, typically used in neuroimaging
    workflows. It seems to have a dependency on Tcl, as indicated by the error
    messages.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UnpacksdcmdirOutputs`).
    """
    cargs = unpacksdcmdir_cargs(params, execution)
    ret = unpacksdcmdir_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def unpacksdcmdir(
    input_directory: str,
    output_directory: str,
    runner: Runner | None = None,
) -> UnpacksdcmdirOutputs:
    """
    A tool for unpacking SD card directories, typically used in neuroimaging
    workflows. It seems to have a dependency on Tcl, as indicated by the error
    messages.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_directory: The directory containing SD card data to be unpacked.
        output_directory: The output directory where unpacked data will be\
            stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpacksdcmdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACKSDCMDIR_METADATA)
    params = unpacksdcmdir_params(input_directory=input_directory, output_directory=output_directory)
    return unpacksdcmdir_execute(params, execution)


__all__ = [
    "UNPACKSDCMDIR_METADATA",
    "UnpacksdcmdirOutputs",
    "UnpacksdcmdirParameters",
    "unpacksdcmdir",
    "unpacksdcmdir_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_4SWAP_METADATA = Metadata(
    id="b931a726528adf5a726f46c604f9851351673fb9.boutiques",
    name="4swap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V4swapParameters = typing.TypedDict('V4swapParameters', {
    "__STYX_TYPE__": typing.Literal["4swap"],
    "files": list[InputPathType],
    "quiet": bool,
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
        "4swap": v_4swap_cargs,
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


class V4swapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_4swap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_4swap_params(
    files: list[InputPathType],
    quiet: bool = False,
) -> V4swapParameters:
    """
    Build parameters.
    
    Args:
        files: List of files to process.
        quiet: Work quietly; suppress output messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "4swap",
        "files": files,
        "quiet": quiet,
    }
    return params


def v_4swap_cargs(
    params: V4swapParameters,
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
    cargs.append("4swap")
    cargs.extend([execution.input_file(f) for f in params.get("files")])
    if params.get("quiet"):
        cargs.append("-q")
    return cargs


def v_4swap_outputs(
    params: V4swapParameters,
    execution: Execution,
) -> V4swapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V4swapOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_4swap_execute(
    params: V4swapParameters,
    execution: Execution,
) -> V4swapOutputs:
    """
    Swaps byte quadruples on the listed files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V4swapOutputs`).
    """
    params = execution.params(params)
    cargs = v_4swap_cargs(params, execution)
    ret = v_4swap_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_4swap(
    files: list[InputPathType],
    quiet: bool = False,
    runner: Runner | None = None,
) -> V4swapOutputs:
    """
    Swaps byte quadruples on the listed files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        files: List of files to process.
        quiet: Work quietly; suppress output messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V4swapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_4SWAP_METADATA)
    params = v_4swap_params(
        files=files,
        quiet=quiet,
    )
    return v_4swap_execute(params, execution)


__all__ = [
    "V4swapOutputs",
    "V4swapParameters",
    "V_4SWAP_METADATA",
    "v_4swap",
    "v_4swap_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMRM_METADATA = Metadata(
    id="2912eb712fa3a6125fef5aa4f51d0229fb833f90.boutiques",
    name="imrm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
ImrmParameters = typing.TypedDict('ImrmParameters', {
    "__STYX_TYPE__": typing.Literal["imrm"],
    "images_to_remove": list[str],
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
        "imrm": imrm_cargs,
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


class ImrmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imrm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def imrm_params(
    images_to_remove: list[str],
) -> ImrmParameters:
    """
    Build parameters.
    
    Args:
        images_to_remove: List of image names to remove. Filenames can be\
            basenames or full names.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imrm",
        "images_to_remove": images_to_remove,
    }
    return params


def imrm_cargs(
    params: ImrmParameters,
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
    cargs.append("imrm")
    cargs.extend(params.get("images_to_remove"))
    return cargs


def imrm_outputs(
    params: ImrmParameters,
    execution: Execution,
) -> ImrmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImrmOutputs(
        root=execution.output_file("."),
    )
    return ret


def imrm_execute(
    params: ImrmParameters,
    execution: Execution,
) -> ImrmOutputs:
    """
    Remove specified image files.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImrmOutputs`).
    """
    cargs = imrm_cargs(params, execution)
    ret = imrm_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def imrm(
    images_to_remove: list[str],
    runner: Runner | None = None,
) -> ImrmOutputs:
    """
    Remove specified image files.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        images_to_remove: List of image names to remove. Filenames can be\
            basenames or full names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImrmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMRM_METADATA)
    params = imrm_params(images_to_remove=images_to_remove)
    return imrm_execute(params, execution)


__all__ = [
    "IMRM_METADATA",
    "ImrmOutputs",
    "ImrmParameters",
    "imrm",
    "imrm_params",
]

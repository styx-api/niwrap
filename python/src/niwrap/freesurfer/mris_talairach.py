# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_TALAIRACH_METADATA = Metadata(
    id="2a27ec50232d56f8e8e079035c459f747d644292.boutiques",
    name="mris_talairach",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisTalairachParameters = typing.TypedDict('MrisTalairachParameters', {
    "__STYX_TYPE__": typing.Literal["mris_talairach"],
    "input_image": InputPathType,
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
        "mris_talairach": mris_talairach_cargs,
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


class MrisTalairachOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_talairach(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_talairach_params(
    input_image: InputPathType,
) -> MrisTalairachParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image file to be transformed into Talairach space.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_talairach",
        "input_image": input_image,
    }
    return params


def mris_talairach_cargs(
    params: MrisTalairachParameters,
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
    cargs.append("mris_talairach")
    cargs.append(execution.input_file(params.get("input_image")))
    return cargs


def mris_talairach_outputs(
    params: MrisTalairachParameters,
    execution: Execution,
) -> MrisTalairachOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisTalairachOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_talairach_execute(
    params: MrisTalairachParameters,
    execution: Execution,
) -> MrisTalairachOutputs:
    """
    Transforms an MRI surface into Talairach space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisTalairachOutputs`).
    """
    cargs = mris_talairach_cargs(params, execution)
    ret = mris_talairach_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_talairach(
    input_image: InputPathType,
    runner: Runner | None = None,
) -> MrisTalairachOutputs:
    """
    Transforms an MRI surface into Talairach space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input image file to be transformed into Talairach space.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisTalairachOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_TALAIRACH_METADATA)
    params = mris_talairach_params(input_image=input_image)
    return mris_talairach_execute(params, execution)


__all__ = [
    "MRIS_TALAIRACH_METADATA",
    "MrisTalairachOutputs",
    "MrisTalairachParameters",
    "mris_talairach",
    "mris_talairach_params",
]

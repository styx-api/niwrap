# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

HIAM_REGISTER_METADATA = Metadata(
    id="44d0a11f2a96d3babdb3cdeabdf7fd3e2408cf2f.boutiques",
    name="hiam_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
HiamRegisterParameters = typing.TypedDict('HiamRegisterParameters', {
    "__STYX_TYPE__": typing.Literal["hiam_register"],
    "input_surface": InputPathType,
    "average_surface": InputPathType,
    "output_surface": str,
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
        "hiam_register": hiam_register_cargs,
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
        "hiam_register": hiam_register_outputs,
    }.get(t)


class HiamRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `hiam_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_surface: OutputPathType
    """The output surface after registration."""


def hiam_register_params(
    input_surface: InputPathType,
    average_surface: InputPathType,
    output_surface: str,
) -> HiamRegisterParameters:
    """
    Build parameters.
    
    Args:
        input_surface: The input surface to be registered.
        average_surface: The average surface to register against.
        output_surface: The path where the output registered surface will be\
            saved.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "hiam_register",
        "input_surface": input_surface,
        "average_surface": average_surface,
        "output_surface": output_surface,
    }
    return params


def hiam_register_cargs(
    params: HiamRegisterParameters,
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
    cargs.append("hiam_register")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("average_surface")))
    cargs.append(params.get("output_surface"))
    return cargs


def hiam_register_outputs(
    params: HiamRegisterParameters,
    execution: Execution,
) -> HiamRegisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = HiamRegisterOutputs(
        root=execution.output_file("."),
        registered_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def hiam_register_execute(
    params: HiamRegisterParameters,
    execution: Execution,
) -> HiamRegisterOutputs:
    """
    This program registers a surface with an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `HiamRegisterOutputs`).
    """
    cargs = hiam_register_cargs(params, execution)
    ret = hiam_register_outputs(params, execution)
    execution.run(cargs)
    return ret


def hiam_register(
    input_surface: InputPathType,
    average_surface: InputPathType,
    output_surface: str,
    runner: Runner | None = None,
) -> HiamRegisterOutputs:
    """
    This program registers a surface with an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: The input surface to be registered.
        average_surface: The average surface to register against.
        output_surface: The path where the output registered surface will be\
            saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HiamRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HIAM_REGISTER_METADATA)
    params = hiam_register_params(input_surface=input_surface, average_surface=average_surface, output_surface=output_surface)
    return hiam_register_execute(params, execution)


__all__ = [
    "HIAM_REGISTER_METADATA",
    "HiamRegisterOutputs",
    "HiamRegisterParameters",
    "hiam_register",
    "hiam_register_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CLUST_EXP_RUN_SHINY_METADATA = Metadata(
    id="fda3a7d2925f29a17f3a4aecaecf82a67d6aa1fc.boutiques",
    name="@ClustExp_run_shiny",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VClustExpRunShinyParameters = typing.TypedDict('VClustExpRunShinyParameters', {
    "__STYX_TYPE__": typing.Literal["@ClustExp_run_shiny"],
    "directory": str,
    "help": bool,
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
        "@ClustExp_run_shiny": v__clust_exp_run_shiny_cargs,
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


class VClustExpRunShinyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__clust_exp_run_shiny(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__clust_exp_run_shiny_params(
    directory: str,
    help_: bool = False,
) -> VClustExpRunShinyParameters:
    """
    Build parameters.
    
    Args:
        directory: Folder created by ClustExp_StatParse.py.
        help_: Show help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ClustExp_run_shiny",
        "directory": directory,
        "help": help_,
    }
    return params


def v__clust_exp_run_shiny_cargs(
    params: VClustExpRunShinyParameters,
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
    cargs.append("@ClustExp_run_shiny")
    cargs.append(params.get("directory"))
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__clust_exp_run_shiny_outputs(
    params: VClustExpRunShinyParameters,
    execution: Execution,
) -> VClustExpRunShinyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VClustExpRunShinyOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__clust_exp_run_shiny_execute(
    params: VClustExpRunShinyParameters,
    execution: Execution,
) -> VClustExpRunShinyOutputs:
    """
    Launch a shiny app that was created by ClustExp_StatParse.py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VClustExpRunShinyOutputs`).
    """
    cargs = v__clust_exp_run_shiny_cargs(params, execution)
    ret = v__clust_exp_run_shiny_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__clust_exp_run_shiny(
    directory: str,
    help_: bool = False,
    runner: Runner | None = None,
) -> VClustExpRunShinyOutputs:
    """
    Launch a shiny app that was created by ClustExp_StatParse.py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        directory: Folder created by ClustExp_StatParse.py.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VClustExpRunShinyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CLUST_EXP_RUN_SHINY_METADATA)
    params = v__clust_exp_run_shiny_params(directory=directory, help_=help_)
    return v__clust_exp_run_shiny_execute(params, execution)


__all__ = [
    "VClustExpRunShinyOutputs",
    "VClustExpRunShinyParameters",
    "V__CLUST_EXP_RUN_SHINY_METADATA",
    "v__clust_exp_run_shiny",
    "v__clust_exp_run_shiny_params",
]

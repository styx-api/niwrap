# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ADD_TEMPLATE_METADATA = Metadata(
    id="cad5f1397d4979ef787014fa2412a1f0a10cfe8b.boutiques",
    name="mris_add_template",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisAddTemplateParameters = typing.TypedDict('MrisAddTemplateParameters', {
    "__STYX_TYPE__": typing.Literal["mris_add_template"],
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
        "mris_add_template": mris_add_template_cargs,
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
        "mris_add_template": mris_add_template_outputs,
    }.get(t)


class MrisAddTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_add_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    placeholder_output: OutputPathType
    """No outputs available as the tool has been removed."""


def mris_add_template_params(
) -> MrisAddTemplateParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_add_template",
    }
    return params


def mris_add_template_cargs(
    params: MrisAddTemplateParameters,
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
    cargs.append("mris_add_template")
    return cargs


def mris_add_template_outputs(
    params: MrisAddTemplateParameters,
    execution: Execution,
) -> MrisAddTemplateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisAddTemplateOutputs(
        root=execution.output_file("."),
        placeholder_output=execution.output_file("[PLACEHOLDER_OUTPUT]"),
    )
    return ret


def mris_add_template_execute(
    params: MrisAddTemplateParameters,
    execution: Execution,
) -> MrisAddTemplateOutputs:
    """
    This tool has been removed from the current version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisAddTemplateOutputs`).
    """
    params = execution.params(params)
    cargs = mris_add_template_cargs(params, execution)
    ret = mris_add_template_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_add_template(
    runner: Runner | None = None,
) -> MrisAddTemplateOutputs:
    """
    This tool has been removed from the current version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisAddTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ADD_TEMPLATE_METADATA)
    params = mris_add_template_params(
    )
    return mris_add_template_execute(params, execution)


__all__ = [
    "MRIS_ADD_TEMPLATE_METADATA",
    "MrisAddTemplateOutputs",
    "MrisAddTemplateParameters",
    "mris_add_template",
    "mris_add_template_params",
]

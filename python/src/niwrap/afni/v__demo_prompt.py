# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DEMO_PROMPT_METADATA = Metadata(
    id="28759d07ed8faa73243bb8713758a156bb9ca999.boutiques",
    name="@demo_prompt",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDemoPromptParameters = typing.TypedDict('VDemoPromptParameters', {
    "__STYX_TYPE__": typing.Literal["@demo_prompt"],
    "message": str,
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
        "@demo_prompt": v__demo_prompt_cargs,
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
        "@demo_prompt": v__demo_prompt_outputs,
    }.get(t)


class VDemoPromptOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__demo_prompt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    status: OutputPathType
    """Status output: 0 if user presses OK, 1 if user cancels"""


def v__demo_prompt_params(
    message: str,
) -> VDemoPromptParameters:
    """
    Build parameters.
    
    Args:
        message: The message to display in the prompt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@demo_prompt",
        "message": message,
    }
    return params


def v__demo_prompt_cargs(
    params: VDemoPromptParameters,
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
    cargs.append("@demo_prompt")
    cargs.append(params.get("message"))
    return cargs


def v__demo_prompt_outputs(
    params: VDemoPromptParameters,
    execution: Execution,
) -> VDemoPromptOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDemoPromptOutputs(
        root=execution.output_file("."),
        status=execution.output_file("status"),
    )
    return ret


def v__demo_prompt_execute(
    params: VDemoPromptParameters,
    execution: Execution,
) -> VDemoPromptOutputs:
    """
    Prompts user with a message and waits for acknowledgment.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDemoPromptOutputs`).
    """
    cargs = v__demo_prompt_cargs(params, execution)
    ret = v__demo_prompt_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__demo_prompt(
    message: str,
    runner: Runner | None = None,
) -> VDemoPromptOutputs:
    """
    Prompts user with a message and waits for acknowledgment.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        message: The message to display in the prompt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDemoPromptOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DEMO_PROMPT_METADATA)
    params = v__demo_prompt_params(message=message)
    return v__demo_prompt_execute(params, execution)


__all__ = [
    "VDemoPromptOutputs",
    "VDemoPromptParameters",
    "V__DEMO_PROMPT_METADATA",
    "v__demo_prompt",
    "v__demo_prompt_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_FIX_TEXT_METADATA = Metadata(
    id="a220cb697a269f6545c026e4c1c455f141351c48.boutiques",
    name="fslFixText",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslFixTextParameters = typing.TypedDict('FslFixTextParameters', {
    "__STYX_TYPE__": typing.Literal["fslFixText"],
    "input_text_file": InputPathType,
    "output_text_file": str,
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
        "fslFixText": fsl_fix_text_cargs,
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
        "fslFixText": fsl_fix_text_outputs,
    }.get(t)


class FslFixTextOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_fix_text(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_text_file: OutputPathType
    """Output text file with standard UNIX line endings"""


def fsl_fix_text_params(
    input_text_file: InputPathType,
    output_text_file: str,
) -> FslFixTextParameters:
    """
    Build parameters.
    
    Args:
        input_text_file: Input text file.
        output_text_file: Output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslFixText",
        "input_text_file": input_text_file,
        "output_text_file": output_text_file,
    }
    return params


def fsl_fix_text_cargs(
    params: FslFixTextParameters,
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
    cargs.append("fslFixText")
    cargs.append(execution.input_file(params.get("input_text_file")))
    cargs.append(params.get("output_text_file"))
    return cargs


def fsl_fix_text_outputs(
    params: FslFixTextParameters,
    execution: Execution,
) -> FslFixTextOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslFixTextOutputs(
        root=execution.output_file("."),
        output_text_file=execution.output_file(params.get("output_text_file")),
    )
    return ret


def fsl_fix_text_execute(
    params: FslFixTextParameters,
    execution: Execution,
) -> FslFixTextOutputs:
    """
    Ensures standard UNIX line endings in the output text file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslFixTextOutputs`).
    """
    cargs = fsl_fix_text_cargs(params, execution)
    ret = fsl_fix_text_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fsl_fix_text(
    input_text_file: InputPathType,
    output_text_file: str,
    runner: Runner | None = None,
) -> FslFixTextOutputs:
    """
    Ensures standard UNIX line endings in the output text file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_text_file: Input text file.
        output_text_file: Output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslFixTextOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_FIX_TEXT_METADATA)
    params = fsl_fix_text_params(input_text_file=input_text_file, output_text_file=output_text_file)
    return fsl_fix_text_execute(params, execution)


__all__ = [
    "FSL_FIX_TEXT_METADATA",
    "FslFixTextOutputs",
    "FslFixTextParameters",
    "fsl_fix_text",
    "fsl_fix_text_params",
]

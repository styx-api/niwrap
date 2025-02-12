# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLVAL_METADATA = Metadata(
    id="8a100481b1c8accf8862e7e516017aa7a9142b94.boutiques",
    name="fslval",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslvalParameters = typing.TypedDict('FslvalParameters', {
    "__STYX_TYPE__": typing.Literal["fslval"],
    "input_file": InputPathType,
    "keyword": str,
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
        "fslval": fslval_cargs,
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
        "fslval": fslval_outputs,
    }.get(t)


class FslvalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout: OutputPathType
    """Output printed to standard out"""


def fslval_params(
    input_file: InputPathType,
    keyword_: str,
) -> FslvalParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input NIfTI image file.
        keyword_: Keyword to query from the NIfTI header.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslval",
        "input_file": input_file,
        "keyword": keyword_,
    }
    return params


def fslval_cargs(
    params: FslvalParameters,
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
    cargs.append("fslval")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("keyword"))
    return cargs


def fslval_outputs(
    params: FslvalParameters,
    execution: Execution,
) -> FslvalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslvalOutputs(
        root=execution.output_file("."),
        stdout=execution.output_file("stdout"),
    )
    return ret


def fslval_execute(
    params: FslvalParameters,
    execution: Execution,
) -> FslvalOutputs:
    """
    Tool for printing out header information from NIfTI image files.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslvalOutputs`).
    """
    cargs = fslval_cargs(params, execution)
    ret = fslval_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslval(
    input_file: InputPathType,
    keyword_: str,
    runner: Runner | None = None,
) -> FslvalOutputs:
    """
    Tool for printing out header information from NIfTI image files.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input NIfTI image file.
        keyword_: Keyword to query from the NIfTI header.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslvalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVAL_METADATA)
    params = fslval_params(input_file=input_file, keyword_=keyword_)
    return fslval_execute(params, execution)


__all__ = [
    "FSLVAL_METADATA",
    "FslvalOutputs",
    "FslvalParameters",
    "fslval",
    "fslval_params",
]

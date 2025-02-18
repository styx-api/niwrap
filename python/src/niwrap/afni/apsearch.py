# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APSEARCH_METADATA = Metadata(
    id="d759bc178b2620ea44d398387e0405f577daa6c5.boutiques",
    name="apsearch",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ApsearchParameters = typing.TypedDict('ApsearchParameters', {
    "__STYX_TYPE__": typing.Literal["apsearch"],
    "search_term": str,
    "file_output": typing.NotRequired[str | None],
    "verbose": bool,
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
        "apsearch": apsearch_cargs,
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
        "apsearch": apsearch_outputs,
    }.get(t)


class ApsearchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apsearch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """File containing search results"""


def apsearch_params(
    search_term: str,
    file_output: str | None = None,
    verbose: bool = False,
) -> ApsearchParameters:
    """
    Build parameters.
    
    Args:
        search_term: Term to search.
        file_output: File to save the search results.
        verbose: Print detailed information during search.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "apsearch",
        "search_term": search_term,
        "verbose": verbose,
    }
    if file_output is not None:
        params["file_output"] = file_output
    return params


def apsearch_cargs(
    params: ApsearchParameters,
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
    cargs.append("apsearch")
    cargs.append(params.get("search_term"))
    if params.get("file_output") is not None:
        cargs.append(params.get("file_output"))
    if params.get("verbose"):
        cargs.append("-v")
    return cargs


def apsearch_outputs(
    params: ApsearchParameters,
    execution: Execution,
) -> ApsearchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ApsearchOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("file_output")) if (params.get("file_output") is not None) else None,
    )
    return ret


def apsearch_execute(
    params: ApsearchParameters,
    execution: Execution,
) -> ApsearchOutputs:
    """
    A tool for searching applications.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ApsearchOutputs`).
    """
    cargs = apsearch_cargs(params, execution)
    ret = apsearch_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def apsearch(
    search_term: str,
    file_output: str | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> ApsearchOutputs:
    """
    A tool for searching applications.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        search_term: Term to search.
        file_output: File to save the search results.
        verbose: Print detailed information during search.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApsearchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APSEARCH_METADATA)
    params = apsearch_params(search_term=search_term, file_output=file_output, verbose=verbose)
    return apsearch_execute(params, execution)


__all__ = [
    "APSEARCH_METADATA",
    "ApsearchOutputs",
    "ApsearchParameters",
    "apsearch",
    "apsearch_params",
]

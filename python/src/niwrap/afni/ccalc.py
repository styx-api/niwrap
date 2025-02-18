# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CCALC_METADATA = Metadata(
    id="858c935b6b57b9962c3e64fe8202799fde8e6c22.boutiques",
    name="ccalc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
CcalcParameters = typing.TypedDict('CcalcParameters', {
    "__STYX_TYPE__": typing.Literal["ccalc"],
    "format": typing.NotRequired[str | None],
    "expr": str,
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
        "ccalc": ccalc_cargs,
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


class CcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ccalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ccalc_params(
    expr: str,
    format_: str | None = None,
) -> CcalcParameters:
    """
    Build parameters.
    
    Args:
        expr: Evaluate an expression specified on command line, return answer\
            and quit.
        format_: Format output in a nice form. Choose from 'double', 'nice',\
            'int', 'rint', 'cint', 'fint', or custom format string (e.g., %n.mf).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ccalc",
        "expr": expr,
    }
    if format_ is not None:
        params["format"] = format_
    return params


def ccalc_cargs(
    params: CcalcParameters,
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
    cargs.append("ccalc")
    if params.get("format") is not None:
        cargs.extend([
            "-form",
            params.get("format")
        ])
    cargs.extend([
        "-eval",
        params.get("expr")
    ])
    return cargs


def ccalc_outputs(
    params: CcalcParameters,
    execution: Execution,
) -> CcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CcalcOutputs(
        root=execution.output_file("."),
    )
    return ret


def ccalc_execute(
    params: CcalcParameters,
    execution: Execution,
) -> CcalcOutputs:
    """
    Command line calculator with formatted output options.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CcalcOutputs`).
    """
    cargs = ccalc_cargs(params, execution)
    ret = ccalc_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def ccalc(
    expr: str,
    format_: str | None = None,
    runner: Runner | None = None,
) -> CcalcOutputs:
    """
    Command line calculator with formatted output options.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        expr: Evaluate an expression specified on command line, return answer\
            and quit.
        format_: Format output in a nice form. Choose from 'double', 'nice',\
            'int', 'rint', 'cint', 'fint', or custom format string (e.g., %n.mf).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CCALC_METADATA)
    params = ccalc_params(format_=format_, expr=expr)
    return ccalc_execute(params, execution)


__all__ = [
    "CCALC_METADATA",
    "CcalcOutputs",
    "CcalcParameters",
    "ccalc",
    "ccalc_params",
]

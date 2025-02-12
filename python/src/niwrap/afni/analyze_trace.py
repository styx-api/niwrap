# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANALYZE_TRACE_METADATA = Metadata(
    id="3d880a6da4a3639545433e9f6739d09c2df6cf76.boutiques",
    name="AnalyzeTrace",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AnalyzeTraceParameters = typing.TypedDict('AnalyzeTraceParameters', {
    "__STYX_TYPE__": typing.Literal["AnalyzeTrace"],
    "tracefile": InputPathType,
    "max_func_lines": typing.NotRequired[int | None],
    "suma_c": typing.NotRequired[InputPathType | None],
    "max_err": typing.NotRequired[int | None],
    "novolreg": bool,
    "noxform": bool,
    "setenv": typing.NotRequired[str | None],
    "trace": bool,
    "extreme_trace": bool,
    "nomall": bool,
    "yesmall": bool,
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
        "AnalyzeTrace": analyze_trace_cargs,
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


class AnalyzeTraceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `analyze_trace(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def analyze_trace_params(
    tracefile: InputPathType,
    max_func_lines: int | None = None,
    suma_c: InputPathType | None = None,
    max_err: int | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
) -> AnalyzeTraceParameters:
    """
    Build parameters.
    
    Args:
        tracefile: Trace output file obtained by redirecting the program’s\
            trace output.
        max_func_lines: Set the maximum number of code lines before a function\
            returns. Default is no limit.
        suma_c: FILE is a SUMA_*.c file. It is analyzed for functions that use\
            SUMA_RETURN without ENTRY.
        max_err: Stop after encountering MAX_ERR errors reported in log.\
            Default is 5. Error key terms are: 'Error', 'error', 'corruption'.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        setenv: Set environment variable ENVname to be ENVvalue. Quotes are\
            necessary.
        trace_: Turns on In/Out debug and Memory tracing.
        extreme_trace: Turns on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "AnalyzeTrace",
        "tracefile": tracefile,
        "novolreg": novolreg,
        "noxform": noxform,
        "trace": trace_,
        "extreme_trace": extreme_trace,
        "nomall": nomall,
        "yesmall": yesmall,
    }
    if max_func_lines is not None:
        params["max_func_lines"] = max_func_lines
    if suma_c is not None:
        params["suma_c"] = suma_c
    if max_err is not None:
        params["max_err"] = max_err
    if setenv is not None:
        params["setenv"] = setenv
    return params


def analyze_trace_cargs(
    params: AnalyzeTraceParameters,
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
    cargs.append("AnalyzeTrace")
    cargs.append(execution.input_file(params.get("tracefile")))
    if params.get("max_func_lines") is not None:
        cargs.extend([
            "-max_func_lines",
            str(params.get("max_func_lines"))
        ])
    if params.get("suma_c") is not None:
        cargs.extend([
            "-suma_c",
            execution.input_file(params.get("suma_c"))
        ])
    if params.get("max_err") is not None:
        cargs.extend([
            "-max_err",
            str(params.get("max_err"))
        ])
    if params.get("novolreg"):
        cargs.append("-novolreg")
    if params.get("noxform"):
        cargs.append("-noxform")
    if params.get("setenv") is not None:
        cargs.extend([
            "-setenv",
            params.get("setenv")
        ])
    if params.get("trace"):
        cargs.append("-trace")
    if params.get("extreme_trace"):
        cargs.append("-TRACE")
    if params.get("nomall"):
        cargs.append("-nomall")
    if params.get("yesmall"):
        cargs.append("-yesmall")
    return cargs


def analyze_trace_outputs(
    params: AnalyzeTraceParameters,
    execution: Execution,
) -> AnalyzeTraceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AnalyzeTraceOutputs(
        root=execution.output_file("."),
    )
    return ret


def analyze_trace_execute(
    params: AnalyzeTraceParameters,
    execution: Execution,
) -> AnalyzeTraceOutputs:
    """
    A program to analyze SUMA (and AFNI's perhaps) stack output for functions that
    return with RETURN without bothering to go on the stack.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AnalyzeTraceOutputs`).
    """
    cargs = analyze_trace_cargs(params, execution)
    ret = analyze_trace_outputs(params, execution)
    execution.run(cargs)
    return ret


def analyze_trace(
    tracefile: InputPathType,
    max_func_lines: int | None = None,
    suma_c: InputPathType | None = None,
    max_err: int | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    runner: Runner | None = None,
) -> AnalyzeTraceOutputs:
    """
    A program to analyze SUMA (and AFNI's perhaps) stack output for functions that
    return with RETURN without bothering to go on the stack.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        tracefile: Trace output file obtained by redirecting the program’s\
            trace output.
        max_func_lines: Set the maximum number of code lines before a function\
            returns. Default is no limit.
        suma_c: FILE is a SUMA_*.c file. It is analyzed for functions that use\
            SUMA_RETURN without ENTRY.
        max_err: Stop after encountering MAX_ERR errors reported in log.\
            Default is 5. Error key terms are: 'Error', 'error', 'corruption'.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        setenv: Set environment variable ENVname to be ENVvalue. Quotes are\
            necessary.
        trace_: Turns on In/Out debug and Memory tracing.
        extreme_trace: Turns on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AnalyzeTraceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANALYZE_TRACE_METADATA)
    params = analyze_trace_params(tracefile=tracefile, max_func_lines=max_func_lines, suma_c=suma_c, max_err=max_err, novolreg=novolreg, noxform=noxform, setenv=setenv, trace_=trace_, extreme_trace=extreme_trace, nomall=nomall, yesmall=yesmall)
    return analyze_trace_execute(params, execution)


__all__ = [
    "ANALYZE_TRACE_METADATA",
    "AnalyzeTraceOutputs",
    "AnalyzeTraceParameters",
    "analyze_trace",
    "analyze_trace_params",
]

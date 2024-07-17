# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ANALYZE_TRACE_METADATA = Metadata(
    id="a53039294138a46c8ab585e7247bfbd8f066fa8a",
    name="AnalyzeTrace",
)


class AnalyzeTraceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `analyze_trace(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


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
    AnalyzeTrace by Ziad S. Saad SSCC/NIMH/NIH.
    
    A program to analyze SUMA (and AFNI's perhaps) stack output for functions
    that return with RETURN without bothering to go on the stack.
    
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
    cargs = []
    cargs.append("AnalyzeTrace")
    cargs.append("[OPTIONAL_PARAMETERS]")
    cargs.append("FILE")
    ret = AnalyzeTraceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANALYZE_TRACE_METADATA",
    "AnalyzeTraceOutputs",
    "analyze_trace",
]

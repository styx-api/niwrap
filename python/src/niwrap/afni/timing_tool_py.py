# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TIMING_TOOL_PY_METADATA = Metadata(
    id="e72448a163610156059a44280593b8076536b24a.boutiques",
    name="timing_tool.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
TimingToolPyParameters = typing.TypedDict('TimingToolPyParameters', {
    "__STYX_TYPE__": typing.Literal["timing_tool.py"],
    "timing_file": typing.NotRequired[InputPathType | None],
    "output_file": typing.NotRequired[str | None],
    "run_length": typing.NotRequired[list[float] | None],
    "tr": typing.NotRequired[float | None],
    "offset": typing.NotRequired[float | None],
    "extend_file": typing.NotRequired[InputPathType | None],
    "sort": bool,
    "scale_data": typing.NotRequired[float | None],
    "shift_to_run_offset": typing.NotRequired[float | None],
    "timing_to_1D_file": typing.NotRequired[str | None],
    "stim_duration": typing.NotRequired[float | None],
    "multi_timing_files": typing.NotRequired[list[InputPathType] | None],
    "multi_show_isi_stats": bool,
    "multi_show_timing": bool,
    "show_timing": bool,
    "multi_stim_duration": typing.NotRequired[list[float] | None],
    "round_times_frac": typing.NotRequired[float | None],
    "truncate_times": bool,
    "multi_timing_event_list": typing.NotRequired[str | None],
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
        "timing_tool.py": timing_tool_py_cargs,
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
        "timing_tool.py": timing_tool_py_outputs,
    }.get(t)


class TimingToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `timing_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_timing_file: OutputPathType | None
    """Output timing file as specified"""
    timing_to_1_d_output: OutputPathType | None
    """Output 1D formatted stimulus data"""


def timing_tool_py_params(
    timing_file: InputPathType | None = None,
    output_file: str | None = None,
    run_length: list[float] | None = None,
    tr: float | None = None,
    offset: float | None = None,
    extend_file: InputPathType | None = None,
    sort: bool = False,
    scale_data: float | None = None,
    shift_to_run_offset: float | None = None,
    timing_to_1_d_file: str | None = None,
    stim_duration: float | None = None,
    multi_timing_files: list[InputPathType] | None = None,
    multi_show_isi_stats: bool = False,
    multi_show_timing: bool = False,
    show_timing: bool = False,
    multi_stim_duration: list[float] | None = None,
    round_times_frac: float | None = None,
    truncate_times: bool = False,
    multi_timing_event_list: str | None = None,
) -> TimingToolPyParameters:
    """
    Build parameters.
    
    Args:
        timing_file: Specify a stimulus timing file to load.
        output_file: Specify the output timing file.
        run_length: Specify the run duration(s), in seconds.
        tr: Specify the time resolution in 1D output (in seconds).
        offset: Add OFFSET to every time in the main element.
        extend_file: Extend timing rows with those in NEW_FILE.
        sort: Sort the times, per row (run).
        scale_data: Multiply every stim time by SCALAR.
        shift_to_run_offset: Shift times so first event is at start of run.
        timing_to_1_d_file: Convert stim_times format to stim_file.
        stim_duration: Specify the stimulus duration, in seconds.
        multi_timing_files: Specify multiple timing files to load.
        multi_show_isi_stats: Display timing and ISI statistics for the\
            multiple timing files.
        multi_show_timing: Display info on multiple timing elements.
        show_timing: Display info on the main timing element.
        multi_stim_duration: Specify stimulus duration(s), in seconds, for\
            multiple timing elements.
        round_times_frac: Round times to multiples of the TR (0.0 <= FRAC <=\
            1.0).
        truncate_times: Truncate times to multiples of the TR.
        multi_timing_event_list: Create an event list file from multiple timing\
            files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "timing_tool.py",
        "sort": sort,
        "multi_show_isi_stats": multi_show_isi_stats,
        "multi_show_timing": multi_show_timing,
        "show_timing": show_timing,
        "truncate_times": truncate_times,
    }
    if timing_file is not None:
        params["timing_file"] = timing_file
    if output_file is not None:
        params["output_file"] = output_file
    if run_length is not None:
        params["run_length"] = run_length
    if tr is not None:
        params["tr"] = tr
    if offset is not None:
        params["offset"] = offset
    if extend_file is not None:
        params["extend_file"] = extend_file
    if scale_data is not None:
        params["scale_data"] = scale_data
    if shift_to_run_offset is not None:
        params["shift_to_run_offset"] = shift_to_run_offset
    if timing_to_1_d_file is not None:
        params["timing_to_1D_file"] = timing_to_1_d_file
    if stim_duration is not None:
        params["stim_duration"] = stim_duration
    if multi_timing_files is not None:
        params["multi_timing_files"] = multi_timing_files
    if multi_stim_duration is not None:
        params["multi_stim_duration"] = multi_stim_duration
    if round_times_frac is not None:
        params["round_times_frac"] = round_times_frac
    if multi_timing_event_list is not None:
        params["multi_timing_event_list"] = multi_timing_event_list
    return params


def timing_tool_py_cargs(
    params: TimingToolPyParameters,
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
    cargs.append("timing_tool.py")
    if params.get("timing_file") is not None:
        cargs.extend([
            "-timing",
            execution.input_file(params.get("timing_file"))
        ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-write_timing",
            params.get("output_file")
        ])
    if params.get("run_length") is not None:
        cargs.extend([
            "-run_len",
            *map(str, params.get("run_length"))
        ])
    if params.get("tr") is not None:
        cargs.extend([
            "-tr",
            str(params.get("tr"))
        ])
    if params.get("offset") is not None:
        cargs.extend([
            "-add_offset",
            str(params.get("offset"))
        ])
    if params.get("extend_file") is not None:
        cargs.extend([
            "-extend",
            execution.input_file(params.get("extend_file"))
        ])
    if params.get("sort"):
        cargs.append("-sort")
    if params.get("scale_data") is not None:
        cargs.extend([
            "-scale_data",
            str(params.get("scale_data"))
        ])
    if params.get("shift_to_run_offset") is not None:
        cargs.extend([
            "-shift_to_run_offset",
            str(params.get("shift_to_run_offset"))
        ])
    if params.get("timing_to_1D_file") is not None:
        cargs.extend([
            "-timing_to_1D",
            params.get("timing_to_1D_file")
        ])
    if params.get("stim_duration") is not None:
        cargs.extend([
            "-stim_dur",
            str(params.get("stim_duration"))
        ])
    if params.get("multi_timing_files") is not None:
        cargs.extend([
            "-multi_timing",
            *[execution.input_file(f) for f in params.get("multi_timing_files")]
        ])
    if params.get("multi_show_isi_stats"):
        cargs.append("-multi_show_isi_stats")
    if params.get("multi_show_timing"):
        cargs.append("-multi_show_timing_ele")
    if params.get("show_timing"):
        cargs.append("-show_timing_ele")
    if params.get("multi_stim_duration") is not None:
        cargs.extend([
            "-multi_stim_dur",
            *map(str, params.get("multi_stim_duration"))
        ])
    if params.get("round_times_frac") is not None:
        cargs.extend([
            "-round_times",
            str(params.get("round_times_frac"))
        ])
    if params.get("truncate_times"):
        cargs.append("-truncate_times")
    if params.get("multi_timing_event_list") is not None:
        cargs.extend([
            "-multi_timing_to_event_list",
            params.get("multi_timing_event_list")
        ])
    return cargs


def timing_tool_py_outputs(
    params: TimingToolPyParameters,
    execution: Execution,
) -> TimingToolPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TimingToolPyOutputs(
        root=execution.output_file("."),
        output_timing_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
        timing_to_1_d_output=execution.output_file(params.get("timing_to_1D_file")) if (params.get("timing_to_1D_file") is not None) else None,
    )
    return ret


def timing_tool_py_execute(
    params: TimingToolPyParameters,
    execution: Execution,
) -> TimingToolPyOutputs:
    """
    Tool for manipulating and evaluating stimulus timing files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TimingToolPyOutputs`).
    """
    cargs = timing_tool_py_cargs(params, execution)
    ret = timing_tool_py_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def timing_tool_py(
    timing_file: InputPathType | None = None,
    output_file: str | None = None,
    run_length: list[float] | None = None,
    tr: float | None = None,
    offset: float | None = None,
    extend_file: InputPathType | None = None,
    sort: bool = False,
    scale_data: float | None = None,
    shift_to_run_offset: float | None = None,
    timing_to_1_d_file: str | None = None,
    stim_duration: float | None = None,
    multi_timing_files: list[InputPathType] | None = None,
    multi_show_isi_stats: bool = False,
    multi_show_timing: bool = False,
    show_timing: bool = False,
    multi_stim_duration: list[float] | None = None,
    round_times_frac: float | None = None,
    truncate_times: bool = False,
    multi_timing_event_list: str | None = None,
    runner: Runner | None = None,
) -> TimingToolPyOutputs:
    """
    Tool for manipulating and evaluating stimulus timing files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        timing_file: Specify a stimulus timing file to load.
        output_file: Specify the output timing file.
        run_length: Specify the run duration(s), in seconds.
        tr: Specify the time resolution in 1D output (in seconds).
        offset: Add OFFSET to every time in the main element.
        extend_file: Extend timing rows with those in NEW_FILE.
        sort: Sort the times, per row (run).
        scale_data: Multiply every stim time by SCALAR.
        shift_to_run_offset: Shift times so first event is at start of run.
        timing_to_1_d_file: Convert stim_times format to stim_file.
        stim_duration: Specify the stimulus duration, in seconds.
        multi_timing_files: Specify multiple timing files to load.
        multi_show_isi_stats: Display timing and ISI statistics for the\
            multiple timing files.
        multi_show_timing: Display info on multiple timing elements.
        show_timing: Display info on the main timing element.
        multi_stim_duration: Specify stimulus duration(s), in seconds, for\
            multiple timing elements.
        round_times_frac: Round times to multiples of the TR (0.0 <= FRAC <=\
            1.0).
        truncate_times: Truncate times to multiples of the TR.
        multi_timing_event_list: Create an event list file from multiple timing\
            files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TimingToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TIMING_TOOL_PY_METADATA)
    params = timing_tool_py_params(timing_file=timing_file, output_file=output_file, run_length=run_length, tr=tr, offset=offset, extend_file=extend_file, sort=sort, scale_data=scale_data, shift_to_run_offset=shift_to_run_offset, timing_to_1_d_file=timing_to_1_d_file, stim_duration=stim_duration, multi_timing_files=multi_timing_files, multi_show_isi_stats=multi_show_isi_stats, multi_show_timing=multi_show_timing, show_timing=show_timing, multi_stim_duration=multi_stim_duration, round_times_frac=round_times_frac, truncate_times=truncate_times, multi_timing_event_list=multi_timing_event_list)
    return timing_tool_py_execute(params, execution)


__all__ = [
    "TIMING_TOOL_PY_METADATA",
    "TimingToolPyOutputs",
    "TimingToolPyParameters",
    "timing_tool_py",
    "timing_tool_py_params",
]

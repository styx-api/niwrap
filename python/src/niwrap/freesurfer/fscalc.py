# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSCALC_METADATA = Metadata(
    id="8980bc90eda2781be7235010d28f030a03b7741c.boutiques",
    name="fscalc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FscalcParameters = typing.TypedDict('FscalcParameters', {
    "__STYX_TYPE__": typing.Literal["fscalc"],
    "input1": str,
    "operation": str,
    "input2": typing.NotRequired[str | None],
    "output_file": str,
    "output_data_type": typing.NotRequired[str | None],
    "debug": bool,
    "tmpdir": typing.NotRequired[str | None],
    "nocleanup": bool,
    "log_file": typing.NotRequired[str | None],
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
        "fscalc": fscalc_cargs,
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
        "fscalc": fscalc_outputs,
    }.get(t)


class FscalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fscalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_vol: OutputPathType
    """Resulting output volume from the operations specified."""


def fscalc_params(
    input1: str,
    operation: str,
    output_file: str,
    input2: str | None = None,
    output_data_type: str | None = None,
    debug: bool = False,
    tmpdir: str | None = None,
    nocleanup: bool = False,
    log_file: str | None = None,
) -> FscalcParameters:
    """
    Build parameters.
    
    Args:
        input1: First input image or constant.
        operation: Operation to perform between input volumes.
        output_file: Output volume file.
        input2: Second input image or constant. Optional for some unary\
            operations.
        output_data_type: Specify output data type (uchar, short, int, float).
        debug: Enable debug mode.
        tmpdir: Temporary directory for processing.
        nocleanup: Prevent cleanup of temporary files.
        log_file: Specify a log file for operation log.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fscalc",
        "input1": input1,
        "operation": operation,
        "output_file": output_file,
        "debug": debug,
        "nocleanup": nocleanup,
    }
    if input2 is not None:
        params["input2"] = input2
    if output_data_type is not None:
        params["output_data_type"] = output_data_type
    if tmpdir is not None:
        params["tmpdir"] = tmpdir
    if log_file is not None:
        params["log_file"] = log_file
    return params


def fscalc_cargs(
    params: FscalcParameters,
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
    cargs.append("fscalc")
    cargs.append(params.get("input1"))
    cargs.append(params.get("operation"))
    if params.get("input2") is not None:
        cargs.append(params.get("input2"))
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    if params.get("output_data_type") is not None:
        cargs.extend([
            "--odt",
            params.get("output_data_type")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("tmpdir") is not None:
        cargs.extend([
            "--tmpdir",
            params.get("tmpdir")
        ])
    if params.get("nocleanup"):
        cargs.append("--nocleanup")
    if params.get("log_file") is not None:
        cargs.extend([
            "--log",
            params.get("log_file")
        ])
    return cargs


def fscalc_outputs(
    params: FscalcParameters,
    execution: Execution,
) -> FscalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FscalcOutputs(
        root=execution.output_file("."),
        result_vol=execution.output_file(params.get("output_file")),
    )
    return ret


def fscalc_execute(
    params: FscalcParameters,
    execution: Execution,
) -> FscalcOutputs:
    """
    A frontend tool to perform mathematical operations on volumes/surfaces of data
    using mris_calc.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FscalcOutputs`).
    """
    cargs = fscalc_cargs(params, execution)
    ret = fscalc_outputs(params, execution)
    execution.run(cargs)
    return ret


def fscalc(
    input1: str,
    operation: str,
    output_file: str,
    input2: str | None = None,
    output_data_type: str | None = None,
    debug: bool = False,
    tmpdir: str | None = None,
    nocleanup: bool = False,
    log_file: str | None = None,
    runner: Runner | None = None,
) -> FscalcOutputs:
    """
    A frontend tool to perform mathematical operations on volumes/surfaces of data
    using mris_calc.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input1: First input image or constant.
        operation: Operation to perform between input volumes.
        output_file: Output volume file.
        input2: Second input image or constant. Optional for some unary\
            operations.
        output_data_type: Specify output data type (uchar, short, int, float).
        debug: Enable debug mode.
        tmpdir: Temporary directory for processing.
        nocleanup: Prevent cleanup of temporary files.
        log_file: Specify a log file for operation log.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FscalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSCALC_METADATA)
    params = fscalc_params(input1=input1, operation=operation, input2=input2, output_file=output_file, output_data_type=output_data_type, debug=debug, tmpdir=tmpdir, nocleanup=nocleanup, log_file=log_file)
    return fscalc_execute(params, execution)


__all__ = [
    "FSCALC_METADATA",
    "FscalcOutputs",
    "FscalcParameters",
    "fscalc",
    "fscalc_params",
]

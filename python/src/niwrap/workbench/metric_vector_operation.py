# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_VECTOR_OPERATION_METADATA = Metadata(
    id="a16a3d5eebe016ff6fd5576142114de6719372bd.boutiques",
    name="metric-vector-operation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricVectorOperationParameters = typing.TypedDict('MetricVectorOperationParameters', {
    "__STYX_TYPE__": typing.Literal["metric-vector-operation"],
    "vectors_a": InputPathType,
    "vectors_b": InputPathType,
    "operation": str,
    "metric_out": str,
    "opt_normalize_a": bool,
    "opt_normalize_b": bool,
    "opt_normalize_output": bool,
    "opt_magnitude": bool,
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
        "metric-vector-operation": metric_vector_operation_cargs,
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
        "metric-vector-operation": metric_vector_operation_outputs,
    }.get(t)


class MetricVectorOperationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_vector_operation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output file"""


def metric_vector_operation_params(
    vectors_a: InputPathType,
    vectors_b: InputPathType,
    operation: str,
    metric_out: str,
    opt_normalize_a: bool = False,
    opt_normalize_b: bool = False,
    opt_normalize_output: bool = False,
    opt_magnitude: bool = False,
) -> MetricVectorOperationParameters:
    """
    Build parameters.
    
    Args:
        vectors_a: first vector input file.
        vectors_b: second vector input file.
        operation: what vector operation to do.
        metric_out: the output file.
        opt_normalize_a: normalize vectors of first input.
        opt_normalize_b: normalize vectors of second input.
        opt_normalize_output: normalize output vectors (not valid for dot\
            product).
        opt_magnitude: output the magnitude of the result (not valid for dot\
            product).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-vector-operation",
        "vectors_a": vectors_a,
        "vectors_b": vectors_b,
        "operation": operation,
        "metric_out": metric_out,
        "opt_normalize_a": opt_normalize_a,
        "opt_normalize_b": opt_normalize_b,
        "opt_normalize_output": opt_normalize_output,
        "opt_magnitude": opt_magnitude,
    }
    return params


def metric_vector_operation_cargs(
    params: MetricVectorOperationParameters,
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
    cargs.append("wb_command")
    cargs.append("-metric-vector-operation")
    cargs.append(execution.input_file(params.get("vectors_a")))
    cargs.append(execution.input_file(params.get("vectors_b")))
    cargs.append(params.get("operation"))
    cargs.append(params.get("metric_out"))
    if params.get("opt_normalize_a"):
        cargs.append("-normalize-a")
    if params.get("opt_normalize_b"):
        cargs.append("-normalize-b")
    if params.get("opt_normalize_output"):
        cargs.append("-normalize-output")
    if params.get("opt_magnitude"):
        cargs.append("-magnitude")
    return cargs


def metric_vector_operation_outputs(
    params: MetricVectorOperationParameters,
    execution: Execution,
) -> MetricVectorOperationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricVectorOperationOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_vector_operation_execute(
    params: MetricVectorOperationParameters,
    execution: Execution,
) -> MetricVectorOperationOutputs:
    """
    Do a vector operation on metric files.
    
    Does a vector operation on two metric files (that must have a multiple of 3
    columns). Either of the inputs may have multiple vectors (more than 3
    columns), but not both (at least one must have exactly 3 columns). The
    -magnitude and -normalize-output options may not be specified together, or
    with an operation that returns a scalar (dot product). The <operation>
    parameter must be one of the following:
    
    DOT
    CROSS
    ADD
    SUBTRACT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricVectorOperationOutputs`).
    """
    cargs = metric_vector_operation_cargs(params, execution)
    ret = metric_vector_operation_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def metric_vector_operation(
    vectors_a: InputPathType,
    vectors_b: InputPathType,
    operation: str,
    metric_out: str,
    opt_normalize_a: bool = False,
    opt_normalize_b: bool = False,
    opt_normalize_output: bool = False,
    opt_magnitude: bool = False,
    runner: Runner | None = None,
) -> MetricVectorOperationOutputs:
    """
    Do a vector operation on metric files.
    
    Does a vector operation on two metric files (that must have a multiple of 3
    columns). Either of the inputs may have multiple vectors (more than 3
    columns), but not both (at least one must have exactly 3 columns). The
    -magnitude and -normalize-output options may not be specified together, or
    with an operation that returns a scalar (dot product). The <operation>
    parameter must be one of the following:
    
    DOT
    CROSS
    ADD
    SUBTRACT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        vectors_a: first vector input file.
        vectors_b: second vector input file.
        operation: what vector operation to do.
        metric_out: the output file.
        opt_normalize_a: normalize vectors of first input.
        opt_normalize_b: normalize vectors of second input.
        opt_normalize_output: normalize output vectors (not valid for dot\
            product).
        opt_magnitude: output the magnitude of the result (not valid for dot\
            product).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricVectorOperationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_VECTOR_OPERATION_METADATA)
    params = metric_vector_operation_params(vectors_a=vectors_a, vectors_b=vectors_b, operation=operation, metric_out=metric_out, opt_normalize_a=opt_normalize_a, opt_normalize_b=opt_normalize_b, opt_normalize_output=opt_normalize_output, opt_magnitude=opt_magnitude)
    return metric_vector_operation_execute(params, execution)


__all__ = [
    "METRIC_VECTOR_OPERATION_METADATA",
    "MetricVectorOperationOutputs",
    "MetricVectorOperationParameters",
    "metric_vector_operation",
    "metric_vector_operation_params",
]

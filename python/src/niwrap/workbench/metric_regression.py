# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_REGRESSION_METADATA = Metadata(
    id="ed3451cc9b4382fc2c1eefb297b008ce34410f5e.boutiques",
    name="metric-regression",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricRegressionRemoveParameters = typing.TypedDict('MetricRegressionRemoveParameters', {
    "__STYX_TYPE__": typing.Literal["remove"],
    "metric": InputPathType,
    "opt_remove_column_column": typing.NotRequired[str | None],
})
MetricRegressionKeepParameters = typing.TypedDict('MetricRegressionKeepParameters', {
    "__STYX_TYPE__": typing.Literal["keep"],
    "metric": InputPathType,
    "opt_keep_column_column": typing.NotRequired[str | None],
})
MetricRegressionParameters = typing.TypedDict('MetricRegressionParameters', {
    "__STYX_TYPE__": typing.Literal["metric-regression"],
    "metric_in": InputPathType,
    "metric_out": str,
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "remove": typing.NotRequired[list[MetricRegressionRemoveParameters] | None],
    "keep": typing.NotRequired[list[MetricRegressionKeepParameters] | None],
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
        "metric-regression": metric_regression_cargs,
        "remove": metric_regression_remove_cargs,
        "keep": metric_regression_keep_cargs,
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
        "metric-regression": metric_regression_outputs,
    }.get(t)


def metric_regression_remove_params(
    metric: InputPathType,
    opt_remove_column_column: str | None = None,
) -> MetricRegressionRemoveParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric file to use.
        opt_remove_column_column: select a column to use, rather than all: the\
            column number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "remove",
        "metric": metric,
    }
    if opt_remove_column_column is not None:
        params["opt_remove_column_column"] = opt_remove_column_column
    return params


def metric_regression_remove_cargs(
    params: MetricRegressionRemoveParameters,
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
    cargs.append("-remove")
    cargs.append(execution.input_file(params.get("metric")))
    if params.get("opt_remove_column_column") is not None:
        cargs.extend([
            "-remove-column",
            params.get("opt_remove_column_column")
        ])
    return cargs


def metric_regression_keep_params(
    metric: InputPathType,
    opt_keep_column_column: str | None = None,
) -> MetricRegressionKeepParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric file to use.
        opt_keep_column_column: select a column to use, rather than all: the\
            column number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "keep",
        "metric": metric,
    }
    if opt_keep_column_column is not None:
        params["opt_keep_column_column"] = opt_keep_column_column
    return params


def metric_regression_keep_cargs(
    params: MetricRegressionKeepParameters,
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
    cargs.append("-keep")
    cargs.append(execution.input_file(params.get("metric")))
    if params.get("opt_keep_column_column") is not None:
        cargs.extend([
            "-keep-column",
            params.get("opt_keep_column_column")
        ])
    return cargs


class MetricRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_regression_params(
    metric_in: InputPathType,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    remove: list[MetricRegressionRemoveParameters] | None = None,
    keep: list[MetricRegressionKeepParameters] | None = None,
) -> MetricRegressionParameters:
    """
    Build parameters.
    
    Args:
        metric_in: the metric to regress from.
        metric_out: the output metric.
        opt_roi_roi_metric: only regress inside an roi: the area to use for\
            regression, as a metric.
        opt_column_column: select a single column to regress from: the column\
            number or name.
        remove: specify a metric to regress out.
        keep: specify a metric to include in regression, but not remove.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-regression",
        "metric_in": metric_in,
        "metric_out": metric_out,
    }
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if remove is not None:
        params["remove"] = remove
    if keep is not None:
        params["keep"] = keep
    return params


def metric_regression_cargs(
    params: MetricRegressionParameters,
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
    cargs.append("-metric-regression")
    cargs.append(execution.input_file(params.get("metric_in")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("remove") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("remove")] for a in c])
    if params.get("keep") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("keep")] for a in c])
    return cargs


def metric_regression_outputs(
    params: MetricRegressionParameters,
    execution: Execution,
) -> MetricRegressionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricRegressionOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_regression_execute(
    params: MetricRegressionParameters,
    execution: Execution,
) -> MetricRegressionOutputs:
    """
    Regress spatial map out of a metric file.
    
    For each regressor, its mean across the surface is subtracted from its data.
    Each input map is then regressed against these, and a constant term. The
    resulting regressed slopes of all regressors specified with -remove are
    multiplied with their respective regressor maps, and these are subtracted
    from the input map.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricRegressionOutputs`).
    """
    cargs = metric_regression_cargs(params, execution)
    ret = metric_regression_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def metric_regression(
    metric_in: InputPathType,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    remove: list[MetricRegressionRemoveParameters] | None = None,
    keep: list[MetricRegressionKeepParameters] | None = None,
    runner: Runner | None = None,
) -> MetricRegressionOutputs:
    """
    Regress spatial map out of a metric file.
    
    For each regressor, its mean across the surface is subtracted from its data.
    Each input map is then regressed against these, and a constant term. The
    resulting regressed slopes of all regressors specified with -remove are
    multiplied with their respective regressor maps, and these are subtracted
    from the input map.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric_in: the metric to regress from.
        metric_out: the output metric.
        opt_roi_roi_metric: only regress inside an roi: the area to use for\
            regression, as a metric.
        opt_column_column: select a single column to regress from: the column\
            number or name.
        remove: specify a metric to regress out.
        keep: specify a metric to include in regression, but not remove.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricRegressionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_REGRESSION_METADATA)
    params = metric_regression_params(metric_in=metric_in, metric_out=metric_out, opt_roi_roi_metric=opt_roi_roi_metric, opt_column_column=opt_column_column, remove=remove, keep=keep)
    return metric_regression_execute(params, execution)


__all__ = [
    "METRIC_REGRESSION_METADATA",
    "MetricRegressionKeepParameters",
    "MetricRegressionOutputs",
    "MetricRegressionParameters",
    "MetricRegressionRemoveParameters",
    "metric_regression",
    "metric_regression_keep_params",
    "metric_regression_params",
    "metric_regression_remove_params",
]

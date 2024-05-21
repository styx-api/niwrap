# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


METRIC_REGRESSION_METADATA = Metadata(
    id="bb46e14755be94cec9d43617e4229190f26a0183",
    name="metric-regression",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_regression(
    runner: Runner,
    metric_in: InputPathType,
    metric_out: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_remove_metric: InputPathType | None = None,
    opt_keep_metric: InputPathType | None = None,
) -> MetricRegressionOutputs:
    """
    metric-regression by Washington University School of Medicin.
    
    REGRESS SPATIAL MAP OUT OF A METRIC FILE.
    
    For each regressor, its mean across the surface is subtracted from its data.
    Each input map is then regressed against these, and a constant term. The
    resulting regressed slopes of all regressors specified with -remove are
    multiplied with their respective regressor maps, and these are subtracted
    from the input map.
    
    Args:
        runner: Command runner
        metric_in: the metric to regress from
        metric_out: the output metric
        opt_roi_roi_metric: only regress inside an roi: the area to use for
            regression, as a metric
        opt_column_column: select a single column to regress from: the column
            number or name
        opt_remove_metric: specify a metric to regress out: the metric file to
            use
        opt_keep_metric: specify a metric to include in regression, but not
            remove: the metric file to use
    Returns:
        NamedTuple of outputs (described in `MetricRegressionOutputs`).
    """
    execution = runner.start_execution(METRIC_REGRESSION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-regression")
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_remove_metric is not None:
        cargs.extend(["-remove", execution.input_file(opt_remove_metric)])
    if opt_keep_metric is not None:
        cargs.extend(["-keep", execution.input_file(opt_keep_metric)])
    ret = MetricRegressionOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret

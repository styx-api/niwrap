# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_WEIGHTED_STATS_METADATA = Metadata(
    id="db2a150409d1a471dfc038782f82192d9cbfe592.boutiques",
    name="metric-weighted-stats",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class MetricWeightedStatsRoi:
    """
    only consider data inside an roi.
    """
    roi_metric: InputPathType
    """the roi, as a metric file"""
    opt_match_maps: bool = False
    """each column of input uses the corresponding column from the roi file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-roi")
        cargs.append(execution.input_file(self.roi_metric))
        if self.opt_match_maps:
            cargs.append("-match-maps")
        return cargs


class MetricWeightedStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_weighted_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_weighted_stats(
    metric_in: InputPathType,
    opt_area_surface_area_surface: InputPathType | None = None,
    opt_weight_metric_weight_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    roi: MetricWeightedStatsRoi | None = None,
    opt_mean: bool = False,
    opt_stdev: bool = False,
    opt_sample: bool = False,
    opt_percentile_percent: float | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
    runner: Runner | None = None,
) -> MetricWeightedStatsOutputs:
    """
    Weighted spatial statistics on a metric file.
    
    For each column of the input, a line of text is printed, resulting from the
    specified operation. You must specify exactly one of -area-surface or
    -weight-metric. Use -column to only give output for a single column. If the
    -roi option is used without -match-maps, then each line will contain as many
    numbers as there are maps in the ROI file, separated by tab characters.
    Exactly one of -mean, -stdev, -percentile or -sum must be specified.
    
    Using -sum with -area-surface (or -weight-metric with a metric containing
    similar data) is equivalent to integrating with respect to surface area. For
    example, if you want to find the surface area within an roi, do this:
    
    $ wb_command -metric-weighted-stats roi.func.gii -sum -area-surface
    midthickness.surf.gii.
    
    Author: Washington University School of Medicin
    
    Args:
        metric_in: the input metric.
        opt_area_surface_area_surface: use vertex areas as weights: the surface\
            to use for vertex areas.
        opt_weight_metric_weight_metric: use weights from a metric file: metric\
            file containing the weights.
        opt_column_column: only display output for one column: the column\
            number or name.
        roi: only consider data inside an roi.
        opt_mean: compute weighted mean.
        opt_stdev: compute weighted standard deviation.
        opt_sample: estimate population stdev from the sample.
        opt_percentile_percent: compute weighted percentile: the percentile to\
            find, must be between 0 and 100.
        opt_sum: compute weighted sum.
        opt_show_map_name: print map index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricWeightedStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_WEIGHTED_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-weighted-stats")
    cargs.append(execution.input_file(metric_in))
    if opt_area_surface_area_surface is not None:
        cargs.extend([
            "-area-surface",
            execution.input_file(opt_area_surface_area_surface)
        ])
    if opt_weight_metric_weight_metric is not None:
        cargs.extend([
            "-weight-metric",
            execution.input_file(opt_weight_metric_weight_metric)
        ])
    if opt_column_column is not None:
        cargs.extend([
            "-column",
            opt_column_column
        ])
    if roi is not None:
        cargs.extend(roi.run(execution))
    if opt_mean:
        cargs.append("-mean")
    if opt_stdev:
        cargs.append("-stdev")
    if opt_sample:
        cargs.append("-sample")
    if opt_percentile_percent is not None:
        cargs.extend([
            "-percentile",
            str(opt_percentile_percent)
        ])
    if opt_sum:
        cargs.append("-sum")
    if opt_show_map_name:
        cargs.append("-show-map-name")
    ret = MetricWeightedStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_WEIGHTED_STATS_METADATA",
    "MetricWeightedStatsOutputs",
    "MetricWeightedStatsRoi",
    "metric_weighted_stats",
]

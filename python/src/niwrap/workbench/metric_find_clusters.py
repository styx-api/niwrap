# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_FIND_CLUSTERS_METADATA = Metadata(
    id="907a04357923661b73b475f443d3ac00387700fc.boutiques",
    name="metric-find-clusters",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricFindClustersParameters = typing.TypedDict('MetricFindClustersParameters', {
    "__STYX_TYPE__": typing.Literal["metric-find-clusters"],
    "surface": InputPathType,
    "metric_in": InputPathType,
    "value_threshold": float,
    "minimum_area": float,
    "metric_out": str,
    "opt_less_than": bool,
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_size_ratio_ratio": typing.NotRequired[float | None],
    "opt_distance_distance": typing.NotRequired[float | None],
    "opt_start_startval": typing.NotRequired[int | None],
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
        "metric-find-clusters": metric_find_clusters_cargs,
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
        "metric-find-clusters": metric_find_clusters_outputs,
    }.get(t)


class MetricFindClustersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_find_clusters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_find_clusters_params(
    surface: InputPathType,
    metric_in: InputPathType,
    value_threshold: float,
    minimum_area: float,
    metric_out: str,
    opt_less_than: bool = False,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_size_ratio_ratio: float | None = None,
    opt_distance_distance: float | None = None,
    opt_start_startval: int | None = None,
) -> MetricFindClustersParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to compute on.
        metric_in: the input metric.
        value_threshold: threshold for data values.
        minimum_area: threshold for cluster area, in mm^2.
        metric_out: the output metric.
        opt_less_than: find values less than <value-threshold>, rather than\
            greater.
        opt_roi_roi_metric: select a region of interest: the roi, as a metric.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_column_column: select a single column: the column number or name.
        opt_size_ratio_ratio: ignore clusters smaller than a given fraction of\
            the largest cluster in map: fraction of the largest cluster's area.
        opt_distance_distance: ignore clusters further than a given distance\
            from the largest cluster: how far from the largest cluster a cluster\
            can be, edge to edge, in mm.
        opt_start_startval: start labeling clusters from a value other than 1:\
            the value to give the first cluster found.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-find-clusters",
        "surface": surface,
        "metric_in": metric_in,
        "value_threshold": value_threshold,
        "minimum_area": minimum_area,
        "metric_out": metric_out,
        "opt_less_than": opt_less_than,
    }
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_size_ratio_ratio is not None:
        params["opt_size_ratio_ratio"] = opt_size_ratio_ratio
    if opt_distance_distance is not None:
        params["opt_distance_distance"] = opt_distance_distance
    if opt_start_startval is not None:
        params["opt_start_startval"] = opt_start_startval
    return params


def metric_find_clusters_cargs(
    params: MetricFindClustersParameters,
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
    cargs.append("-metric-find-clusters")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric_in")))
    cargs.append(str(params.get("value_threshold")))
    cargs.append(str(params.get("minimum_area")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_less_than"):
        cargs.append("-less-than")
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_size_ratio_ratio") is not None:
        cargs.extend([
            "-size-ratio",
            str(params.get("opt_size_ratio_ratio"))
        ])
    if params.get("opt_distance_distance") is not None:
        cargs.extend([
            "-distance",
            str(params.get("opt_distance_distance"))
        ])
    if params.get("opt_start_startval") is not None:
        cargs.extend([
            "-start",
            str(params.get("opt_start_startval"))
        ])
    return cargs


def metric_find_clusters_outputs(
    params: MetricFindClustersParameters,
    execution: Execution,
) -> MetricFindClustersOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricFindClustersOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_find_clusters_execute(
    params: MetricFindClustersParameters,
    execution: Execution,
) -> MetricFindClustersOutputs:
    """
    Filter clusters by surface area.
    
    Outputs a metric with nonzero integers for all vertices within a large
    enough cluster, and zeros elsewhere. The integers denote cluster membership
    (by default, first cluster found will use value 1, second cluster 2, etc).
    Cluster values are not reused across maps of the output, but instead keep
    counting up. By default, values greater than <value-threshold> are
    considered to be in a cluster, use -less-than to test for values less than
    the threshold. To apply this as a mask to the data, or to do more
    complicated thresholding, see -metric-math.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricFindClustersOutputs`).
    """
    cargs = metric_find_clusters_cargs(params, execution)
    ret = metric_find_clusters_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_find_clusters(
    surface: InputPathType,
    metric_in: InputPathType,
    value_threshold: float,
    minimum_area: float,
    metric_out: str,
    opt_less_than: bool = False,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_size_ratio_ratio: float | None = None,
    opt_distance_distance: float | None = None,
    opt_start_startval: int | None = None,
    runner: Runner | None = None,
) -> MetricFindClustersOutputs:
    """
    Filter clusters by surface area.
    
    Outputs a metric with nonzero integers for all vertices within a large
    enough cluster, and zeros elsewhere. The integers denote cluster membership
    (by default, first cluster found will use value 1, second cluster 2, etc).
    Cluster values are not reused across maps of the output, but instead keep
    counting up. By default, values greater than <value-threshold> are
    considered to be in a cluster, use -less-than to test for values less than
    the threshold. To apply this as a mask to the data, or to do more
    complicated thresholding, see -metric-math.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to compute on.
        metric_in: the input metric.
        value_threshold: threshold for data values.
        minimum_area: threshold for cluster area, in mm^2.
        metric_out: the output metric.
        opt_less_than: find values less than <value-threshold>, rather than\
            greater.
        opt_roi_roi_metric: select a region of interest: the roi, as a metric.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_column_column: select a single column: the column number or name.
        opt_size_ratio_ratio: ignore clusters smaller than a given fraction of\
            the largest cluster in map: fraction of the largest cluster's area.
        opt_distance_distance: ignore clusters further than a given distance\
            from the largest cluster: how far from the largest cluster a cluster\
            can be, edge to edge, in mm.
        opt_start_startval: start labeling clusters from a value other than 1:\
            the value to give the first cluster found.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricFindClustersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_FIND_CLUSTERS_METADATA)
    params = metric_find_clusters_params(surface=surface, metric_in=metric_in, value_threshold=value_threshold, minimum_area=minimum_area, metric_out=metric_out, opt_less_than=opt_less_than, opt_roi_roi_metric=opt_roi_roi_metric, opt_corrected_areas_area_metric=opt_corrected_areas_area_metric, opt_column_column=opt_column_column, opt_size_ratio_ratio=opt_size_ratio_ratio, opt_distance_distance=opt_distance_distance, opt_start_startval=opt_start_startval)
    return metric_find_clusters_execute(params, execution)


__all__ = [
    "METRIC_FIND_CLUSTERS_METADATA",
    "MetricFindClustersOutputs",
    "MetricFindClustersParameters",
    "metric_find_clusters",
    "metric_find_clusters_params",
]

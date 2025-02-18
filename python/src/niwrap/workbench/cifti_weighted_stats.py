# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_WEIGHTED_STATS_METADATA = Metadata(
    id="0c4c1a860d6333e14904c17da15583cc5bc1a9b4.boutiques",
    name="cifti-weighted-stats",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiWeightedStatsSpatialWeightsParameters = typing.TypedDict('CiftiWeightedStatsSpatialWeightsParameters', {
    "__STYX_TYPE__": typing.Literal["spatial_weights"],
    "opt_left_area_surf_left_surf": typing.NotRequired[InputPathType | None],
    "opt_right_area_surf_right_surf": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_area_surf_cerebellum_surf": typing.NotRequired[InputPathType | None],
    "opt_left_area_metric_left_metric": typing.NotRequired[InputPathType | None],
    "opt_right_area_metric_right_metric": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_area_metric_cerebellum_metric": typing.NotRequired[InputPathType | None],
})
CiftiWeightedStatsRoiParameters = typing.TypedDict('CiftiWeightedStatsRoiParameters', {
    "__STYX_TYPE__": typing.Literal["roi"],
    "roi_cifti": InputPathType,
    "opt_match_maps": bool,
})
CiftiWeightedStatsStdevParameters = typing.TypedDict('CiftiWeightedStatsStdevParameters', {
    "__STYX_TYPE__": typing.Literal["stdev"],
    "opt_sample": bool,
})
CiftiWeightedStatsParameters = typing.TypedDict('CiftiWeightedStatsParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-weighted-stats"],
    "cifti_in": InputPathType,
    "spatial_weights": typing.NotRequired[CiftiWeightedStatsSpatialWeightsParameters | None],
    "opt_cifti_weights_weight_cifti": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[int | None],
    "roi": typing.NotRequired[CiftiWeightedStatsRoiParameters | None],
    "opt_mean": bool,
    "stdev": typing.NotRequired[CiftiWeightedStatsStdevParameters | None],
    "opt_percentile_percent": typing.NotRequired[float | None],
    "opt_sum": bool,
    "opt_show_map_name": bool,
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
        "cifti-weighted-stats": cifti_weighted_stats_cargs,
        "spatial_weights": cifti_weighted_stats_spatial_weights_cargs,
        "roi": cifti_weighted_stats_roi_cargs,
        "stdev": cifti_weighted_stats_stdev_cargs,
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


def cifti_weighted_stats_spatial_weights_params(
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    opt_left_area_metric_left_metric: InputPathType | None = None,
    opt_right_area_metric_right_metric: InputPathType | None = None,
    opt_cerebellum_area_metric_cerebellum_metric: InputPathType | None = None,
) -> CiftiWeightedStatsSpatialWeightsParameters:
    """
    Build parameters.
    
    Args:
        opt_left_area_surf_left_surf: use a surface for left vertex areas: the\
            left surface to use, areas are in mm^2.
        opt_right_area_surf_right_surf: use a surface for right vertex areas:\
            the right surface to use, areas are in mm^2.
        opt_cerebellum_area_surf_cerebellum_surf: use a surface for cerebellum\
            vertex areas: the cerebellum surface to use, areas are in mm^2.
        opt_left_area_metric_left_metric: use a metric file for left vertex\
            areas: metric file containing left vertex areas.
        opt_right_area_metric_right_metric: use a metric file for right vertex\
            areas: metric file containing right vertex areas.
        opt_cerebellum_area_metric_cerebellum_metric: use a metric file for\
            cerebellum vertex areas: metric file containing cerebellum vertex areas.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "spatial_weights",
    }
    if opt_left_area_surf_left_surf is not None:
        params["opt_left_area_surf_left_surf"] = opt_left_area_surf_left_surf
    if opt_right_area_surf_right_surf is not None:
        params["opt_right_area_surf_right_surf"] = opt_right_area_surf_right_surf
    if opt_cerebellum_area_surf_cerebellum_surf is not None:
        params["opt_cerebellum_area_surf_cerebellum_surf"] = opt_cerebellum_area_surf_cerebellum_surf
    if opt_left_area_metric_left_metric is not None:
        params["opt_left_area_metric_left_metric"] = opt_left_area_metric_left_metric
    if opt_right_area_metric_right_metric is not None:
        params["opt_right_area_metric_right_metric"] = opt_right_area_metric_right_metric
    if opt_cerebellum_area_metric_cerebellum_metric is not None:
        params["opt_cerebellum_area_metric_cerebellum_metric"] = opt_cerebellum_area_metric_cerebellum_metric
    return params


def cifti_weighted_stats_spatial_weights_cargs(
    params: CiftiWeightedStatsSpatialWeightsParameters,
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
    cargs.append("-spatial-weights")
    if params.get("opt_left_area_surf_left_surf") is not None:
        cargs.extend([
            "-left-area-surf",
            execution.input_file(params.get("opt_left_area_surf_left_surf"))
        ])
    if params.get("opt_right_area_surf_right_surf") is not None:
        cargs.extend([
            "-right-area-surf",
            execution.input_file(params.get("opt_right_area_surf_right_surf"))
        ])
    if params.get("opt_cerebellum_area_surf_cerebellum_surf") is not None:
        cargs.extend([
            "-cerebellum-area-surf",
            execution.input_file(params.get("opt_cerebellum_area_surf_cerebellum_surf"))
        ])
    if params.get("opt_left_area_metric_left_metric") is not None:
        cargs.extend([
            "-left-area-metric",
            execution.input_file(params.get("opt_left_area_metric_left_metric"))
        ])
    if params.get("opt_right_area_metric_right_metric") is not None:
        cargs.extend([
            "-right-area-metric",
            execution.input_file(params.get("opt_right_area_metric_right_metric"))
        ])
    if params.get("opt_cerebellum_area_metric_cerebellum_metric") is not None:
        cargs.extend([
            "-cerebellum-area-metric",
            execution.input_file(params.get("opt_cerebellum_area_metric_cerebellum_metric"))
        ])
    return cargs


def cifti_weighted_stats_roi_params(
    roi_cifti: InputPathType,
    opt_match_maps: bool = False,
) -> CiftiWeightedStatsRoiParameters:
    """
    Build parameters.
    
    Args:
        roi_cifti: the roi, as a cifti file.
        opt_match_maps: each column of input uses the corresponding column from\
            the roi file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "roi",
        "roi_cifti": roi_cifti,
        "opt_match_maps": opt_match_maps,
    }
    return params


def cifti_weighted_stats_roi_cargs(
    params: CiftiWeightedStatsRoiParameters,
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
    cargs.append("-roi")
    cargs.append(execution.input_file(params.get("roi_cifti")))
    if params.get("opt_match_maps"):
        cargs.append("-match-maps")
    return cargs


def cifti_weighted_stats_stdev_params(
    opt_sample: bool = False,
) -> CiftiWeightedStatsStdevParameters:
    """
    Build parameters.
    
    Args:
        opt_sample: estimate population stdev from the sample.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "stdev",
        "opt_sample": opt_sample,
    }
    return params


def cifti_weighted_stats_stdev_cargs(
    params: CiftiWeightedStatsStdevParameters,
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
    cargs.append("-stdev")
    if params.get("opt_sample"):
        cargs.append("-sample")
    return cargs


class CiftiWeightedStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_weighted_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_weighted_stats_params(
    cifti_in: InputPathType,
    spatial_weights: CiftiWeightedStatsSpatialWeightsParameters | None = None,
    opt_cifti_weights_weight_cifti: InputPathType | None = None,
    opt_column_column: int | None = None,
    roi: CiftiWeightedStatsRoiParameters | None = None,
    opt_mean: bool = False,
    stdev: CiftiWeightedStatsStdevParameters | None = None,
    opt_percentile_percent: float | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
) -> CiftiWeightedStatsParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the input cifti.
        spatial_weights: use vertex area and voxel volume as weights.
        opt_cifti_weights_weight_cifti: use a cifti file containing weights:\
            the weights to use, as a cifti file.
        opt_column_column: only display output for one column: the column to\
            use (1-based).
        roi: only consider data inside an roi.
        opt_mean: compute weighted mean.
        stdev: compute weighted standard deviation.
        opt_percentile_percent: compute weighted percentile: the percentile to\
            find, must be between 0 and 100.
        opt_sum: compute weighted sum.
        opt_show_map_name: print map index and name before each output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-weighted-stats",
        "cifti_in": cifti_in,
        "opt_mean": opt_mean,
        "opt_sum": opt_sum,
        "opt_show_map_name": opt_show_map_name,
    }
    if spatial_weights is not None:
        params["spatial_weights"] = spatial_weights
    if opt_cifti_weights_weight_cifti is not None:
        params["opt_cifti_weights_weight_cifti"] = opt_cifti_weights_weight_cifti
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if roi is not None:
        params["roi"] = roi
    if stdev is not None:
        params["stdev"] = stdev
    if opt_percentile_percent is not None:
        params["opt_percentile_percent"] = opt_percentile_percent
    return params


def cifti_weighted_stats_cargs(
    params: CiftiWeightedStatsParameters,
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
    cargs.append("-cifti-weighted-stats")
    cargs.append(execution.input_file(params.get("cifti_in")))
    if params.get("spatial_weights") is not None:
        cargs.extend(dyn_cargs(params.get("spatial_weights")["__STYXTYPE__"])(params.get("spatial_weights"), execution))
    if params.get("opt_cifti_weights_weight_cifti") is not None:
        cargs.extend([
            "-cifti-weights",
            execution.input_file(params.get("opt_cifti_weights_weight_cifti"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            str(params.get("opt_column_column"))
        ])
    if params.get("roi") is not None:
        cargs.extend(dyn_cargs(params.get("roi")["__STYXTYPE__"])(params.get("roi"), execution))
    if params.get("opt_mean"):
        cargs.append("-mean")
    if params.get("stdev") is not None:
        cargs.extend(dyn_cargs(params.get("stdev")["__STYXTYPE__"])(params.get("stdev"), execution))
    if params.get("opt_percentile_percent") is not None:
        cargs.extend([
            "-percentile",
            str(params.get("opt_percentile_percent"))
        ])
    if params.get("opt_sum"):
        cargs.append("-sum")
    if params.get("opt_show_map_name"):
        cargs.append("-show-map-name")
    return cargs


def cifti_weighted_stats_outputs(
    params: CiftiWeightedStatsParameters,
    execution: Execution,
) -> CiftiWeightedStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiWeightedStatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_weighted_stats_execute(
    params: CiftiWeightedStatsParameters,
    execution: Execution,
) -> CiftiWeightedStatsOutputs:
    """
    Weighted statistics along cifti columns.
    
    If the mapping along column is brain models, for each column of the input,
    the specified operation is done on each surface and across all voxels, and
    the results are printed on separate lines. For other mapping types, the
    operation is done on each column, and one line per map is printed. Exactly
    one of -spatial-weights or -cifti-weights must be specified. Use -column to
    only give output for a single column. If the -roi option is used without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Exactly one of -mean, -stdev,
    -percentile or -sum must be specified.
    
    Using -sum with -spatial-weights (or with -cifti-weights and a cifti
    containing weights of similar meaning) is equivalent to integrating with
    respect to area and volume. When the input is binary ROIs, this will
    therefore output the area or volume of each ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiWeightedStatsOutputs`).
    """
    cargs = cifti_weighted_stats_cargs(params, execution)
    ret = cifti_weighted_stats_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def cifti_weighted_stats(
    cifti_in: InputPathType,
    spatial_weights: CiftiWeightedStatsSpatialWeightsParameters | None = None,
    opt_cifti_weights_weight_cifti: InputPathType | None = None,
    opt_column_column: int | None = None,
    roi: CiftiWeightedStatsRoiParameters | None = None,
    opt_mean: bool = False,
    stdev: CiftiWeightedStatsStdevParameters | None = None,
    opt_percentile_percent: float | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
    runner: Runner | None = None,
) -> CiftiWeightedStatsOutputs:
    """
    Weighted statistics along cifti columns.
    
    If the mapping along column is brain models, for each column of the input,
    the specified operation is done on each surface and across all voxels, and
    the results are printed on separate lines. For other mapping types, the
    operation is done on each column, and one line per map is printed. Exactly
    one of -spatial-weights or -cifti-weights must be specified. Use -column to
    only give output for a single column. If the -roi option is used without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Exactly one of -mean, -stdev,
    -percentile or -sum must be specified.
    
    Using -sum with -spatial-weights (or with -cifti-weights and a cifti
    containing weights of similar meaning) is equivalent to integrating with
    respect to area and volume. When the input is binary ROIs, this will
    therefore output the area or volume of each ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the input cifti.
        spatial_weights: use vertex area and voxel volume as weights.
        opt_cifti_weights_weight_cifti: use a cifti file containing weights:\
            the weights to use, as a cifti file.
        opt_column_column: only display output for one column: the column to\
            use (1-based).
        roi: only consider data inside an roi.
        opt_mean: compute weighted mean.
        stdev: compute weighted standard deviation.
        opt_percentile_percent: compute weighted percentile: the percentile to\
            find, must be between 0 and 100.
        opt_sum: compute weighted sum.
        opt_show_map_name: print map index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiWeightedStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_WEIGHTED_STATS_METADATA)
    params = cifti_weighted_stats_params(cifti_in=cifti_in, spatial_weights=spatial_weights, opt_cifti_weights_weight_cifti=opt_cifti_weights_weight_cifti, opt_column_column=opt_column_column, roi=roi, opt_mean=opt_mean, stdev=stdev, opt_percentile_percent=opt_percentile_percent, opt_sum=opt_sum, opt_show_map_name=opt_show_map_name)
    return cifti_weighted_stats_execute(params, execution)


__all__ = [
    "CIFTI_WEIGHTED_STATS_METADATA",
    "CiftiWeightedStatsOutputs",
    "CiftiWeightedStatsParameters",
    "CiftiWeightedStatsRoiParameters",
    "CiftiWeightedStatsSpatialWeightsParameters",
    "CiftiWeightedStatsStdevParameters",
    "cifti_weighted_stats",
    "cifti_weighted_stats_params",
    "cifti_weighted_stats_roi_params",
    "cifti_weighted_stats_spatial_weights_params",
    "cifti_weighted_stats_stdev_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_CREATE_DENSE_TIMESERIES_METADATA = Metadata(
    id="71533feafcaa802cef4d42e37ca6ad2a75119da8.boutiques",
    name="cifti-create-dense-timeseries",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiCreateDenseTimeseriesVolumeParameters = typing.TypedDict('CiftiCreateDenseTimeseriesVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["volume"],
    "volume_data": InputPathType,
    "structure_label_volume": InputPathType,
})
CiftiCreateDenseTimeseriesLeftMetricParameters = typing.TypedDict('CiftiCreateDenseTimeseriesLeftMetricParameters', {
    "__STYX_TYPE__": typing.Literal["left_metric"],
    "metric": InputPathType,
    "opt_roi_left_roi_metric": typing.NotRequired[InputPathType | None],
})
CiftiCreateDenseTimeseriesRightMetricParameters = typing.TypedDict('CiftiCreateDenseTimeseriesRightMetricParameters', {
    "__STYX_TYPE__": typing.Literal["right_metric"],
    "metric": InputPathType,
    "opt_roi_right_roi_metric": typing.NotRequired[InputPathType | None],
})
CiftiCreateDenseTimeseriesCerebellumMetricParameters = typing.TypedDict('CiftiCreateDenseTimeseriesCerebellumMetricParameters', {
    "__STYX_TYPE__": typing.Literal["cerebellum_metric"],
    "metric": InputPathType,
    "opt_roi_cerebellum_roi_metric": typing.NotRequired[InputPathType | None],
})
CiftiCreateDenseTimeseriesParameters = typing.TypedDict('CiftiCreateDenseTimeseriesParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-create-dense-timeseries"],
    "cifti_out": str,
    "volume": typing.NotRequired[CiftiCreateDenseTimeseriesVolumeParameters | None],
    "left_metric": typing.NotRequired[CiftiCreateDenseTimeseriesLeftMetricParameters | None],
    "right_metric": typing.NotRequired[CiftiCreateDenseTimeseriesRightMetricParameters | None],
    "cerebellum_metric": typing.NotRequired[CiftiCreateDenseTimeseriesCerebellumMetricParameters | None],
    "opt_timestep_interval": typing.NotRequired[float | None],
    "opt_timestart_start": typing.NotRequired[float | None],
    "opt_unit_unit": typing.NotRequired[str | None],
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
        "cifti-create-dense-timeseries": cifti_create_dense_timeseries_cargs,
        "volume": cifti_create_dense_timeseries_volume_cargs,
        "left_metric": cifti_create_dense_timeseries_left_metric_cargs,
        "right_metric": cifti_create_dense_timeseries_right_metric_cargs,
        "cerebellum_metric": cifti_create_dense_timeseries_cerebellum_metric_cargs,
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
        "cifti-create-dense-timeseries": cifti_create_dense_timeseries_outputs,
    }.get(t)


def cifti_create_dense_timeseries_volume_params(
    volume_data: InputPathType,
    structure_label_volume: InputPathType,
) -> CiftiCreateDenseTimeseriesVolumeParameters:
    """
    Build parameters.
    
    Args:
        volume_data: volume file containing all voxel data for all volume\
            structures.
        structure_label_volume: label volume file containing labels for cifti\
            structures.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume",
        "volume_data": volume_data,
        "structure_label_volume": structure_label_volume,
    }
    return params


def cifti_create_dense_timeseries_volume_cargs(
    params: CiftiCreateDenseTimeseriesVolumeParameters,
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
    cargs.append("-volume")
    cargs.append(execution.input_file(params.get("volume_data")))
    cargs.append(execution.input_file(params.get("structure_label_volume")))
    return cargs


def cifti_create_dense_timeseries_left_metric_params(
    metric: InputPathType,
    opt_roi_left_roi_metric: InputPathType | None = None,
) -> CiftiCreateDenseTimeseriesLeftMetricParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric file.
        opt_roi_left_roi_metric: roi of vertices to use from left surface: the\
            ROI as a metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "left_metric",
        "metric": metric,
    }
    if opt_roi_left_roi_metric is not None:
        params["opt_roi_left_roi_metric"] = opt_roi_left_roi_metric
    return params


def cifti_create_dense_timeseries_left_metric_cargs(
    params: CiftiCreateDenseTimeseriesLeftMetricParameters,
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
    cargs.append("-left-metric")
    cargs.append(execution.input_file(params.get("metric")))
    if params.get("opt_roi_left_roi_metric") is not None:
        cargs.extend([
            "-roi-left",
            execution.input_file(params.get("opt_roi_left_roi_metric"))
        ])
    return cargs


def cifti_create_dense_timeseries_right_metric_params(
    metric: InputPathType,
    opt_roi_right_roi_metric: InputPathType | None = None,
) -> CiftiCreateDenseTimeseriesRightMetricParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric file.
        opt_roi_right_roi_metric: roi of vertices to use from right surface:\
            the ROI as a metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "right_metric",
        "metric": metric,
    }
    if opt_roi_right_roi_metric is not None:
        params["opt_roi_right_roi_metric"] = opt_roi_right_roi_metric
    return params


def cifti_create_dense_timeseries_right_metric_cargs(
    params: CiftiCreateDenseTimeseriesRightMetricParameters,
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
    cargs.append("-right-metric")
    cargs.append(execution.input_file(params.get("metric")))
    if params.get("opt_roi_right_roi_metric") is not None:
        cargs.extend([
            "-roi-right",
            execution.input_file(params.get("opt_roi_right_roi_metric"))
        ])
    return cargs


def cifti_create_dense_timeseries_cerebellum_metric_params(
    metric: InputPathType,
    opt_roi_cerebellum_roi_metric: InputPathType | None = None,
) -> CiftiCreateDenseTimeseriesCerebellumMetricParameters:
    """
    Build parameters.
    
    Args:
        metric: the metric file.
        opt_roi_cerebellum_roi_metric: roi of vertices to use from right\
            surface: the ROI as a metric file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cerebellum_metric",
        "metric": metric,
    }
    if opt_roi_cerebellum_roi_metric is not None:
        params["opt_roi_cerebellum_roi_metric"] = opt_roi_cerebellum_roi_metric
    return params


def cifti_create_dense_timeseries_cerebellum_metric_cargs(
    params: CiftiCreateDenseTimeseriesCerebellumMetricParameters,
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
    cargs.append("-cerebellum-metric")
    cargs.append(execution.input_file(params.get("metric")))
    if params.get("opt_roi_cerebellum_roi_metric") is not None:
        cargs.extend([
            "-roi-cerebellum",
            execution.input_file(params.get("opt_roi_cerebellum_roi_metric"))
        ])
    return cargs


class CiftiCreateDenseTimeseriesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_dense_timeseries(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_dense_timeseries_params(
    cifti_out: str,
    volume: CiftiCreateDenseTimeseriesVolumeParameters | None = None,
    left_metric: CiftiCreateDenseTimeseriesLeftMetricParameters | None = None,
    right_metric: CiftiCreateDenseTimeseriesRightMetricParameters | None = None,
    cerebellum_metric: CiftiCreateDenseTimeseriesCerebellumMetricParameters | None = None,
    opt_timestep_interval: float | None = None,
    opt_timestart_start: float | None = None,
    opt_unit_unit: str | None = None,
) -> CiftiCreateDenseTimeseriesParameters:
    """
    Build parameters.
    
    Args:
        cifti_out: the output cifti file.
        volume: volume component.
        left_metric: metric for left surface.
        right_metric: metric for left surface.
        cerebellum_metric: metric for the cerebellum.
        opt_timestep_interval: set the timestep: the timestep, in seconds\
            (default 1.0).
        opt_timestart_start: set the start time: the time at the first frame,\
            in seconds (default 0.0).
        opt_unit_unit: use a unit other than time: unit identifier (default\
            SECOND).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-create-dense-timeseries",
        "cifti_out": cifti_out,
    }
    if volume is not None:
        params["volume"] = volume
    if left_metric is not None:
        params["left_metric"] = left_metric
    if right_metric is not None:
        params["right_metric"] = right_metric
    if cerebellum_metric is not None:
        params["cerebellum_metric"] = cerebellum_metric
    if opt_timestep_interval is not None:
        params["opt_timestep_interval"] = opt_timestep_interval
    if opt_timestart_start is not None:
        params["opt_timestart_start"] = opt_timestart_start
    if opt_unit_unit is not None:
        params["opt_unit_unit"] = opt_unit_unit
    return params


def cifti_create_dense_timeseries_cargs(
    params: CiftiCreateDenseTimeseriesParameters,
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
    cargs.append("-cifti-create-dense-timeseries")
    cargs.append(params.get("cifti_out"))
    if params.get("volume") is not None:
        cargs.extend(dyn_cargs(params.get("volume")["__STYXTYPE__"])(params.get("volume"), execution))
    if params.get("left_metric") is not None:
        cargs.extend(dyn_cargs(params.get("left_metric")["__STYXTYPE__"])(params.get("left_metric"), execution))
    if params.get("right_metric") is not None:
        cargs.extend(dyn_cargs(params.get("right_metric")["__STYXTYPE__"])(params.get("right_metric"), execution))
    if params.get("cerebellum_metric") is not None:
        cargs.extend(dyn_cargs(params.get("cerebellum_metric")["__STYXTYPE__"])(params.get("cerebellum_metric"), execution))
    if params.get("opt_timestep_interval") is not None:
        cargs.extend([
            "-timestep",
            str(params.get("opt_timestep_interval"))
        ])
    if params.get("opt_timestart_start") is not None:
        cargs.extend([
            "-timestart",
            str(params.get("opt_timestart_start"))
        ])
    if params.get("opt_unit_unit") is not None:
        cargs.extend([
            "-unit",
            params.get("opt_unit_unit")
        ])
    return cargs


def cifti_create_dense_timeseries_outputs(
    params: CiftiCreateDenseTimeseriesParameters,
    execution: Execution,
) -> CiftiCreateDenseTimeseriesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiCreateDenseTimeseriesOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_create_dense_timeseries_execute(
    params: CiftiCreateDenseTimeseriesParameters,
    execution: Execution,
) -> CiftiCreateDenseTimeseriesOutputs:
    """
    Create a cifti dense timeseries.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti. At least one component
    must be specified.
    
    See -volume-label-import and -volume-help for format details of label volume
    files. The structure-label-volume should have some of the label names from
    this list, all other label names will be ignored:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT
    
    The -unit option accepts these values:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseTimeseriesOutputs`).
    """
    cargs = cifti_create_dense_timeseries_cargs(params, execution)
    ret = cifti_create_dense_timeseries_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def cifti_create_dense_timeseries(
    cifti_out: str,
    volume: CiftiCreateDenseTimeseriesVolumeParameters | None = None,
    left_metric: CiftiCreateDenseTimeseriesLeftMetricParameters | None = None,
    right_metric: CiftiCreateDenseTimeseriesRightMetricParameters | None = None,
    cerebellum_metric: CiftiCreateDenseTimeseriesCerebellumMetricParameters | None = None,
    opt_timestep_interval: float | None = None,
    opt_timestart_start: float | None = None,
    opt_unit_unit: str | None = None,
    runner: Runner | None = None,
) -> CiftiCreateDenseTimeseriesOutputs:
    """
    Create a cifti dense timeseries.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti. At least one component
    must be specified.
    
    See -volume-label-import and -volume-help for format details of label volume
    files. The structure-label-volume should have some of the label names from
    this list, all other label names will be ignored:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT
    
    The -unit option accepts these values:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_out: the output cifti file.
        volume: volume component.
        left_metric: metric for left surface.
        right_metric: metric for left surface.
        cerebellum_metric: metric for the cerebellum.
        opt_timestep_interval: set the timestep: the timestep, in seconds\
            (default 1.0).
        opt_timestart_start: set the start time: the time at the first frame,\
            in seconds (default 0.0).
        opt_unit_unit: use a unit other than time: unit identifier (default\
            SECOND).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseTimeseriesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_DENSE_TIMESERIES_METADATA)
    params = cifti_create_dense_timeseries_params(cifti_out=cifti_out, volume=volume, left_metric=left_metric, right_metric=right_metric, cerebellum_metric=cerebellum_metric, opt_timestep_interval=opt_timestep_interval, opt_timestart_start=opt_timestart_start, opt_unit_unit=opt_unit_unit)
    return cifti_create_dense_timeseries_execute(params, execution)


__all__ = [
    "CIFTI_CREATE_DENSE_TIMESERIES_METADATA",
    "CiftiCreateDenseTimeseriesCerebellumMetricParameters",
    "CiftiCreateDenseTimeseriesLeftMetricParameters",
    "CiftiCreateDenseTimeseriesOutputs",
    "CiftiCreateDenseTimeseriesParameters",
    "CiftiCreateDenseTimeseriesRightMetricParameters",
    "CiftiCreateDenseTimeseriesVolumeParameters",
    "cifti_create_dense_timeseries",
    "cifti_create_dense_timeseries_cerebellum_metric_params",
    "cifti_create_dense_timeseries_left_metric_params",
    "cifti_create_dense_timeseries_params",
    "cifti_create_dense_timeseries_right_metric_params",
    "cifti_create_dense_timeseries_volume_params",
]

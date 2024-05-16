# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.837597

import typing

from ..styxdefs import *


METRIC_REMOVE_ISLANDS_METADATA = Metadata(
    id="79634688a80a1736433ce9a53813d562c5934b6c",
    name="metric-remove-islands",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricRemoveIslandsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_remove_islands(...)`.
    """
    metric_out: OutputPathType
    """the output ROI metric"""


def metric_remove_islands(
    runner: Runner,
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: InputPathType,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> MetricRemoveIslandsOutputs:
    """
    REMOVE ISLANDS FROM AN ROI METRIC.
    
    Finds all connected areas in the ROI, and zeros out all but the largest one,
    in terms of surface area.
    
    Args:
        runner: Command runner
        surface: the surface to use for neighbor information
        metric_in: the input ROI metric
        metric_out: the output ROI metric
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
    Returns:
        NamedTuple of outputs (described in `MetricRemoveIslandsOutputs`).
    """
    execution = runner.start_execution(METRIC_REMOVE_ISLANDS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-remove-islands")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricRemoveIslandsOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret

# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


METRIC_CONVERT_METADATA = Metadata(
    id="f0fabfb25b533140bc29d5cf32ad79c4238482a8",
    name="metric-convert",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_convert(...)`.
    """


def metric_convert(
    runner: Runner,
    opt_to_nifti_metric_in: InputPathType | None = None,
) -> MetricConvertOutputs:
    """
    CONVERT METRIC FILE TO FAKE NIFTI.
    
    The purpose of this command is to convert between metric files and nifti1 so
    that gifti-unaware programs can operate on the data. You must specify
    exactly one of the options.
    
    Args:
        runner: Command runner
        opt_to_nifti_metric_in: convert metric to nifti: the metric to convert
    Returns:
        NamedTuple of outputs (described in `MetricConvertOutputs`).
    """
    execution = runner.start_execution(METRIC_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-convert")
    if opt_to_nifti_metric_in is not None:
        cargs.extend(["-to-nifti", execution.input_file(opt_to_nifti_metric_in)])
    ret = MetricConvertOutputs(
    )
    execution.run(cargs)
    return ret

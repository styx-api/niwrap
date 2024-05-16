# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.896027

import typing

from ..styxdefs import *


BACKEND_AVERAGE_ROI_CORRELATION_METADATA = Metadata(
    id="b2b0ca6503fe3f9ce6b2130d105d269329e5ed51",
    name="backend-average-roi-correlation",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class BackendAverageRoiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `backend_average_roi_correlation(...)`.
    """


def backend_average_roi_correlation(
    runner: Runner,
    index_list: str,
    out_file: str,
) -> BackendAverageRoiCorrelationOutputs:
    """
    CONNECTOME DB BACKEND COMMAND FOR CIFTI AVERAGE ROI CORRELATION.
    
    This command is probably not the one you are looking for, try
    -cifti-average-roi-correlation. It takes the list of cifti files to average
    from standard input, and writes its output as little endian, 32-bit integer
    of row size followed by the row as 32-bit floats.
    
    Args:
        runner: Command runner
        index_list: comma separated list of cifti indexes to average and then
            correlate
        out_file: file to write the average row to
    Returns:
        NamedTuple of outputs (described in `BackendAverageRoiCorrelationOutputs`).
    """
    execution = runner.start_execution(BACKEND_AVERAGE_ROI_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-backend-average-roi-correlation")
    cargs.append(index_list)
    cargs.append(out_file)
    ret = BackendAverageRoiCorrelationOutputs(
    )
    execution.run(cargs)
    return ret

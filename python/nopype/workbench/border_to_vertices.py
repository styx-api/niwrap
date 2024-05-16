# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.788782

import typing

from ..styxdefs import *


BORDER_TO_VERTICES_METADATA = Metadata(
    id="24a3f15dca88742390d15f07372b429dec2dcb1a",
    name="border-to-vertices",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class BorderToVerticesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_to_vertices(...)`.
    """
    metric_out: OutputPathType
    """the output metric file"""


def border_to_vertices(
    runner: Runner,
    surface: InputPathType,
    border_file: InputPathType,
    metric_out: InputPathType,
    opt_border_name: str | None = None,
) -> BorderToVerticesOutputs:
    """
    DRAW BORDERS AS VERTICES IN A METRIC FILE.
    
    Outputs a metric with 1s on vertices that follow a border, and 0s elsewhere.
    By default, a separate metric column is created for each border.
    
    Args:
        runner: Command runner
        surface: the surface the borders are drawn on
        border_file: the border file
        metric_out: the output metric file
        opt_border_name: create ROI for only one border: the name of the border
    Returns:
        NamedTuple of outputs (described in `BorderToVerticesOutputs`).
    """
    execution = runner.start_execution(BORDER_TO_VERTICES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-to-vertices")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(border_file))
    cargs.append(execution.input_file(metric_out))
    if opt_border_name is not None:
        cargs.extend(["-border", opt_border_name])
    ret = BorderToVerticesOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret

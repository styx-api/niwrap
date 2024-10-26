# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_COORDINATES_TO_METRIC_METADATA = Metadata(
    id="3cc68c4335af3e1f6f59a9bcb7fcf07acdca4680.boutiques",
    name="surface-coordinates-to-metric",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceCoordinatesToMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_coordinates_to_metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_coordinates_to_metric(
    surface: InputPathType,
    metric_out: str,
    runner: Runner | None = None,
) -> SurfaceCoordinatesToMetricOutputs:
    """
    Make metric file of surface coordinates.
    
    Puts the coordinates of the surface into a 3-map metric file, as x, y, z.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to use the coordinates of.
        metric_out: the output metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCoordinatesToMetricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_COORDINATES_TO_METRIC_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-coordinates-to-metric")
    cargs.append(execution.input_file(surface))
    cargs.append(metric_out)
    ret = SurfaceCoordinatesToMetricOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_COORDINATES_TO_METRIC_METADATA",
    "SurfaceCoordinatesToMetricOutputs",
    "surface_coordinates_to_metric",
]

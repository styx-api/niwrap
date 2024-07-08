# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_VERTEX_AREAS_METADATA = Metadata(
    id="9df3ecefa233171160b65871e3f998ca64717f3e",
    name="surface-vertex-areas",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceVertexAreasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_vertex_areas(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric: OutputPathType
    """the output metric"""


def surface_vertex_areas(
    surface: InputPathType,
    metric: str,
    runner: Runner = None,
) -> SurfaceVertexAreasOutputs:
    """
    surface-vertex-areas by Washington University School of Medicin.
    
    Measure surface area each vertex is responsible for.
    
    Each vertex gets one third of the area of each triangle it is a part of.
    Units are mm^2.
    
    Args:
        surface: the surface to measure.
        metric: the output metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceVertexAreasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_VERTEX_AREAS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-vertex-areas")
    cargs.append(execution.input_file(surface))
    cargs.append(metric)
    ret = SurfaceVertexAreasOutputs(
        root=execution.output_file("."),
        metric=execution.output_file(f"{metric}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_VERTEX_AREAS_METADATA",
    "SurfaceVertexAreasOutputs",
    "surface_vertex_areas",
]

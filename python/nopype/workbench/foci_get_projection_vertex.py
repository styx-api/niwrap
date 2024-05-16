# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.876059

import typing

from ..styxdefs import *


FOCI_GET_PROJECTION_VERTEX_METADATA = Metadata(
    id="da581877c7476ef3dbd273038f43c39da155df28",
    name="foci-get-projection-vertex",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class FociGetProjectionVertexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_get_projection_vertex(...)`.
    """
    metric_out: OutputPathType
    """the output metric file"""


def foci_get_projection_vertex(
    runner: Runner,
    foci: InputPathType,
    surface: InputPathType,
    metric_out: InputPathType,
    opt_name_name: str | None = None,
) -> FociGetProjectionVertexOutputs:
    """
    GET PROJECTION VERTEX FOR FOCI.
    
    For each focus, a column is created in <metric-out>, and the vertex with the
    most influence on its projection is assigned a value of 1 in that column,
    with all other vertices 0. If -name is used, only one focus will be used.
    
    Args:
        runner: Command runner
        foci: the foci file
        surface: the surface related to the foci file
        metric_out: the output metric file
        opt_name_name: select a focus by name: the name of the focus
    Returns:
        NamedTuple of outputs (described in `FociGetProjectionVertexOutputs`).
    """
    execution = runner.start_execution(FOCI_GET_PROJECTION_VERTEX_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-foci-get-projection-vertex")
    cargs.append(execution.input_file(foci))
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_out))
    if opt_name_name is not None:
        cargs.extend(["-name", opt_name_name])
    ret = FociGetProjectionVertexOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret

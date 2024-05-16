# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.987975

import typing

from ..styxdefs import *


SURFACE_GEODESIC_ROIS_METADATA = Metadata(
    id="8bd2210a884c1c571e67c04abb4bf8fe42875515",
    name="surface-geodesic-rois",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceGeodesicRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_geodesic_rois(...)`.
    """
    metric_out: OutputPathType
    """the output metric"""


def surface_geodesic_rois(
    runner: Runner,
    surface: InputPathType,
    limit: float | int,
    vertex_list_file: str,
    metric_out: InputPathType,
    opt_gaussian_sigma: float | int | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_names_name_list_file: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> SurfaceGeodesicRoisOutputs:
    """
    DRAW GEODESIC LIMITED ROIS AT VERTICES.
    
    For each vertex in the list file, a column in the output metric is created,
    and an ROI around that vertex is drawn in that column. Each metric column
    will have zeros outside the geodesic distance spacified by <limit>, and by
    default will have a value of 1.0 inside it. If the -gaussian option is
    specified, the values inside the ROI will instead form a gaussian with the
    specified value of sigma, normalized so that the sum of the nonzero values
    in the metric column is 1.0. The <method> argument to -overlap-logic must be
    one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means that ROIs
    are treated independently and may overlap. CLOSEST means that ROIs may not
    overlap, and that no ROI contains vertices that are closer to a different
    seed vertex. EXCLUDE means that ROIs may not overlap, and that any vertex
    within range of more than one ROI does not belong to any ROI.
    
    Args:
        runner: Command runner
        surface: the surface to draw on
        limit: geodesic distance limit from vertex, in mm
        vertex_list_file: a text file containing the vertices to draw ROIs
            around
        metric_out: the output metric
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:
            the sigma for the gaussian kernel, in mm
        opt_overlap_logic_method: how to handle overlapping ROIs, default ALLOW:
            the method of resolving overlaps
        opt_names_name_list_file: name the columns from text file: a text file
            containing column names, one per line
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicRoisOutputs`).
    """
    execution = runner.start_execution(SURFACE_GEODESIC_ROIS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-geodesic-rois")
    cargs.append(execution.input_file(surface))
    cargs.append(str(limit))
    cargs.append(vertex_list_file)
    cargs.append(execution.input_file(metric_out))
    if opt_gaussian_sigma is not None:
        cargs.extend(["-gaussian", str(opt_gaussian_sigma)])
    if opt_overlap_logic_method is not None:
        cargs.extend(["-overlap-logic", opt_overlap_logic_method])
    if opt_names_name_list_file is not None:
        cargs.extend(["-names", opt_names_name_list_file])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = SurfaceGeodesicRoisOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret

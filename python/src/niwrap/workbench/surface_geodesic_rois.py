# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_GEODESIC_ROIS_METADATA = Metadata(
    id="9cf06e2ba1e176d35fb90dbd3ef3e83aff71c2fe.boutiques",
    name="surface-geodesic-rois",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceGeodesicRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_geodesic_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_geodesic_rois(
    surface: InputPathType,
    limit: float,
    vertex_list_file: str,
    metric_out: str,
    opt_gaussian_sigma: float | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_names_name_list_file: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfaceGeodesicRoisOutputs:
    """
    Draw geodesic limited rois at vertices.
    
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
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to draw on.
        limit: geodesic distance limit from vertex, in mm.
        vertex_list_file: a text file containing the vertices to draw ROIs\
            around.
        metric_out: the output metric.
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:\
            the sigma for the gaussian kernel, in mm.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_names_name_list_file: name the columns from text file: a text file\
            containing column names, one per line.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicRoisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_GEODESIC_ROIS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-geodesic-rois")
    cargs.append(execution.input_file(surface))
    cargs.append(str(limit))
    cargs.append(vertex_list_file)
    cargs.append(metric_out)
    if opt_gaussian_sigma is not None:
        cargs.extend([
            "-gaussian",
            str(opt_gaussian_sigma)
        ])
    if opt_overlap_logic_method is not None:
        cargs.extend([
            "-overlap-logic",
            opt_overlap_logic_method
        ])
    if opt_names_name_list_file is not None:
        cargs.extend([
            "-names",
            opt_names_name_list_file
        ])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(opt_corrected_areas_area_metric)
        ])
    ret = SurfaceGeodesicRoisOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_GEODESIC_ROIS_METADATA",
    "SurfaceGeodesicRoisOutputs",
    "surface_geodesic_rois",
]

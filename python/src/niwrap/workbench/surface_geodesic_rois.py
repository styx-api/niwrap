# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_GEODESIC_ROIS_METADATA = Metadata(
    id="e84a10dd4b7742d06a2cc82bdf785c2ce3993f10.boutiques",
    name="surface-geodesic-rois",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceGeodesicRoisParameters = typing.TypedDict('SurfaceGeodesicRoisParameters', {
    "__STYX_TYPE__": typing.Literal["surface-geodesic-rois"],
    "surface": InputPathType,
    "limit": float,
    "vertex_list_file": str,
    "metric_out": str,
    "opt_gaussian_sigma": typing.NotRequired[float | None],
    "opt_overlap_logic_method": typing.NotRequired[str | None],
    "opt_names_name_list_file": typing.NotRequired[str | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
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
        "surface-geodesic-rois": surface_geodesic_rois_cargs,
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
        "surface-geodesic-rois": surface_geodesic_rois_outputs,
    }.get(t)


class SurfaceGeodesicRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_geodesic_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_geodesic_rois_params(
    surface: InputPathType,
    limit: float,
    vertex_list_file: str,
    metric_out: str,
    opt_gaussian_sigma: float | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_names_name_list_file: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> SurfaceGeodesicRoisParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-geodesic-rois",
        "surface": surface,
        "limit": limit,
        "vertex_list_file": vertex_list_file,
        "metric_out": metric_out,
    }
    if opt_gaussian_sigma is not None:
        params["opt_gaussian_sigma"] = opt_gaussian_sigma
    if opt_overlap_logic_method is not None:
        params["opt_overlap_logic_method"] = opt_overlap_logic_method
    if opt_names_name_list_file is not None:
        params["opt_names_name_list_file"] = opt_names_name_list_file
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def surface_geodesic_rois_cargs(
    params: SurfaceGeodesicRoisParameters,
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
    cargs.append("-surface-geodesic-rois")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(str(params.get("limit")))
    cargs.append(params.get("vertex_list_file"))
    cargs.append(params.get("metric_out"))
    if params.get("opt_gaussian_sigma") is not None:
        cargs.extend([
            "-gaussian",
            str(params.get("opt_gaussian_sigma"))
        ])
    if params.get("opt_overlap_logic_method") is not None:
        cargs.extend([
            "-overlap-logic",
            params.get("opt_overlap_logic_method")
        ])
    if params.get("opt_names_name_list_file") is not None:
        cargs.extend([
            "-names",
            params.get("opt_names_name_list_file")
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    return cargs


def surface_geodesic_rois_outputs(
    params: SurfaceGeodesicRoisParameters,
    execution: Execution,
) -> SurfaceGeodesicRoisOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceGeodesicRoisOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def surface_geodesic_rois_execute(
    params: SurfaceGeodesicRoisParameters,
    execution: Execution,
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
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicRoisOutputs`).
    """
    cargs = surface_geodesic_rois_cargs(params, execution)
    ret = surface_geodesic_rois_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = surface_geodesic_rois_params(surface=surface, limit=limit, vertex_list_file=vertex_list_file, metric_out=metric_out, opt_gaussian_sigma=opt_gaussian_sigma, opt_overlap_logic_method=opt_overlap_logic_method, opt_names_name_list_file=opt_names_name_list_file, opt_corrected_areas_area_metric=opt_corrected_areas_area_metric)
    return surface_geodesic_rois_execute(params, execution)


__all__ = [
    "SURFACE_GEODESIC_ROIS_METADATA",
    "SurfaceGeodesicRoisOutputs",
    "SurfaceGeodesicRoisParameters",
    "surface_geodesic_rois",
    "surface_geodesic_rois_params",
]

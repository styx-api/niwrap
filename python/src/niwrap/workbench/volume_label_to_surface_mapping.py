# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA = Metadata(
    id="9bc6b682807328e6a1b0c7145d97a8a86f72e627.boutiques",
    name="volume-label-to-surface-mapping",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


VolumeLabelToSurfaceMappingRibbonConstrainedParameters = typing.TypedDict('VolumeLabelToSurfaceMappingRibbonConstrainedParameters', {
    "__STYX_TYPE__": typing.Literal["ribbon_constrained"],
    "inner_surf": InputPathType,
    "outer_surf": InputPathType,
    "opt_volume_roi_roi_volume": typing.NotRequired[InputPathType | None],
    "opt_voxel_subdiv_subdiv_num": typing.NotRequired[int | None],
    "opt_thin_columns": bool,
})


VolumeLabelToSurfaceMappingParameters = typing.TypedDict('VolumeLabelToSurfaceMappingParameters', {
    "__STYX_TYPE__": typing.Literal["volume-label-to-surface-mapping"],
    "volume": InputPathType,
    "surface": InputPathType,
    "label_out": str,
    "ribbon_constrained": typing.NotRequired[VolumeLabelToSurfaceMappingRibbonConstrainedParameters | None],
    "opt_subvol_select_subvol": typing.NotRequired[str | None],
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
        "volume-label-to-surface-mapping": volume_label_to_surface_mapping_cargs,
        "ribbon_constrained": volume_label_to_surface_mapping_ribbon_constrained_cargs,
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
        "volume-label-to-surface-mapping": volume_label_to_surface_mapping_outputs,
    }.get(t)


def volume_label_to_surface_mapping_ribbon_constrained_params(
    inner_surf: InputPathType,
    outer_surf: InputPathType,
    opt_volume_roi_roi_volume: InputPathType | None = None,
    opt_voxel_subdiv_subdiv_num: int | None = None,
    opt_thin_columns: bool = False,
) -> VolumeLabelToSurfaceMappingRibbonConstrainedParameters:
    """
    Build parameters.
    
    Args:
        inner_surf: the inner surface of the ribbon.
        outer_surf: the outer surface of the ribbon.
        opt_volume_roi_roi_volume: use a volume roi: the volume file.
        opt_voxel_subdiv_subdiv_num: voxel divisions while estimating voxel\
            weights: number of subdivisions, default 3.
        opt_thin_columns: use non-overlapping polyhedra.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ribbon_constrained",
        "inner_surf": inner_surf,
        "outer_surf": outer_surf,
        "opt_thin_columns": opt_thin_columns,
    }
    if opt_volume_roi_roi_volume is not None:
        params["opt_volume_roi_roi_volume"] = opt_volume_roi_roi_volume
    if opt_voxel_subdiv_subdiv_num is not None:
        params["opt_voxel_subdiv_subdiv_num"] = opt_voxel_subdiv_subdiv_num
    return params


def volume_label_to_surface_mapping_ribbon_constrained_cargs(
    params: VolumeLabelToSurfaceMappingRibbonConstrainedParameters,
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
    cargs.append("-ribbon-constrained")
    cargs.append(execution.input_file(params.get("inner_surf")))
    cargs.append(execution.input_file(params.get("outer_surf")))
    if params.get("opt_volume_roi_roi_volume") is not None:
        cargs.extend([
            "-volume-roi",
            execution.input_file(params.get("opt_volume_roi_roi_volume"))
        ])
    if params.get("opt_voxel_subdiv_subdiv_num") is not None:
        cargs.extend([
            "-voxel-subdiv",
            str(params.get("opt_voxel_subdiv_subdiv_num"))
        ])
    if params.get("opt_thin_columns"):
        cargs.append("-thin-columns")
    return cargs


class VolumeLabelToSurfaceMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_to_surface_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output gifti label file"""


def volume_label_to_surface_mapping_params(
    volume: InputPathType,
    surface: InputPathType,
    label_out: str,
    ribbon_constrained: VolumeLabelToSurfaceMappingRibbonConstrainedParameters | None = None,
    opt_subvol_select_subvol: str | None = None,
) -> VolumeLabelToSurfaceMappingParameters:
    """
    Build parameters.
    
    Args:
        volume: the volume to map data from.
        surface: the surface to map the data onto.
        label_out: the output gifti label file.
        ribbon_constrained: use ribbon constrained mapping algorithm.
        opt_subvol_select_subvol: select a single subvolume to map: the\
            subvolume number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-label-to-surface-mapping",
        "volume": volume,
        "surface": surface,
        "label_out": label_out,
    }
    if ribbon_constrained is not None:
        params["ribbon_constrained"] = ribbon_constrained
    if opt_subvol_select_subvol is not None:
        params["opt_subvol_select_subvol"] = opt_subvol_select_subvol
    return params


def volume_label_to_surface_mapping_cargs(
    params: VolumeLabelToSurfaceMappingParameters,
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
    cargs.append("-volume-label-to-surface-mapping")
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("label_out"))
    if params.get("ribbon_constrained") is not None:
        cargs.extend(dyn_cargs(params.get("ribbon_constrained")["__STYXTYPE__"])(params.get("ribbon_constrained"), execution))
    if params.get("opt_subvol_select_subvol") is not None:
        cargs.extend([
            "-subvol-select",
            params.get("opt_subvol_select_subvol")
        ])
    return cargs


def volume_label_to_surface_mapping_outputs(
    params: VolumeLabelToSurfaceMappingParameters,
    execution: Execution,
) -> VolumeLabelToSurfaceMappingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeLabelToSurfaceMappingOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
    )
    return ret


def volume_label_to_surface_mapping_execute(
    params: VolumeLabelToSurfaceMappingParameters,
    execution: Execution,
) -> VolumeLabelToSurfaceMappingOutputs:
    """
    Map a label volume to a surface label file.
    
    Map label volume data to a surface. If -ribbon-constrained is not specified,
    uses the enclosing voxel method. The ribbon mapping method constructs a
    polyhedron from the vertex's neighbors on each surface, and estimates the
    amount of this polyhedron's volume that falls inside any nearby voxels, to
    use as the weights for a popularity comparison. If -thin-columns is
    specified, the polyhedron uses the edge midpoints and triangle centroids, so
    that neighboring vertices do not have overlapping polyhedra. This may
    require increasing -voxel-subdiv to get enough samples in each voxel to
    reliably land inside these smaller polyhedra. The volume ROI is useful to
    exclude partial volume effects of voxels the surfaces pass through, and will
    cause the mapping to ignore voxels that don't have a positive value in the
    mask. The subdivision number specifies how it approximates the amount of the
    volume the polyhedron intersects, by splitting each voxel into NxNxN pieces,
    and checking whether the center of each piece is inside the polyhedron. If
    you have very large voxels, consider increasing this if you get unexpected
    unlabeled vertices in your output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelToSurfaceMappingOutputs`).
    """
    params = execution.params(params)
    cargs = volume_label_to_surface_mapping_cargs(params, execution)
    ret = volume_label_to_surface_mapping_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_label_to_surface_mapping(
    volume: InputPathType,
    surface: InputPathType,
    label_out: str,
    ribbon_constrained: VolumeLabelToSurfaceMappingRibbonConstrainedParameters | None = None,
    opt_subvol_select_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeLabelToSurfaceMappingOutputs:
    """
    Map a label volume to a surface label file.
    
    Map label volume data to a surface. If -ribbon-constrained is not specified,
    uses the enclosing voxel method. The ribbon mapping method constructs a
    polyhedron from the vertex's neighbors on each surface, and estimates the
    amount of this polyhedron's volume that falls inside any nearby voxels, to
    use as the weights for a popularity comparison. If -thin-columns is
    specified, the polyhedron uses the edge midpoints and triangle centroids, so
    that neighboring vertices do not have overlapping polyhedra. This may
    require increasing -voxel-subdiv to get enough samples in each voxel to
    reliably land inside these smaller polyhedra. The volume ROI is useful to
    exclude partial volume effects of voxels the surfaces pass through, and will
    cause the mapping to ignore voxels that don't have a positive value in the
    mask. The subdivision number specifies how it approximates the amount of the
    volume the polyhedron intersects, by splitting each voxel into NxNxN pieces,
    and checking whether the center of each piece is inside the polyhedron. If
    you have very large voxels, consider increasing this if you get unexpected
    unlabeled vertices in your output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume: the volume to map data from.
        surface: the surface to map the data onto.
        label_out: the output gifti label file.
        ribbon_constrained: use ribbon constrained mapping algorithm.
        opt_subvol_select_subvol: select a single subvolume to map: the\
            subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelToSurfaceMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA)
    params = volume_label_to_surface_mapping_params(
        volume=volume,
        surface=surface,
        label_out=label_out,
        ribbon_constrained=ribbon_constrained,
        opt_subvol_select_subvol=opt_subvol_select_subvol,
    )
    return volume_label_to_surface_mapping_execute(params, execution)


__all__ = [
    "VOLUME_LABEL_TO_SURFACE_MAPPING_METADATA",
    "VolumeLabelToSurfaceMappingOutputs",
    "VolumeLabelToSurfaceMappingParameters",
    "VolumeLabelToSurfaceMappingRibbonConstrainedParameters",
    "volume_label_to_surface_mapping",
    "volume_label_to_surface_mapping_params",
    "volume_label_to_surface_mapping_ribbon_constrained_params",
]

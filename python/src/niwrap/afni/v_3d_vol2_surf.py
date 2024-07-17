# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_VOL2_SURF_METADATA = Metadata(
    id="26cf7cda8bf500a49e3c0d9ad8a518d4bc40695e",
    name="3dVol2Surf",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dVol2SurfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_vol2_surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_1d_file: OutputPathType | None
    """1D output file"""
    out_niml_file: OutputPathType | None
    """NIML output file"""
    seg_coords_file: OutputPathType | None
    """Segment coordinates output file"""


def v_3d_vol2_surf(
    spec_file: InputPathType,
    sv: InputPathType,
    grid_parent: InputPathType,
    map_func: str,
    surf_a: str,
    surf_b: str | None = None,
    out_1_d: str | None = None,
    out_niml: str | None = None,
    use_norms: bool = False,
    norm_len: float | int | None = None,
    first_node: float | int | None = None,
    last_node: float | int | None = None,
    debug_level: float | int | None = None,
    dnode: float | int | None = None,
    f_steps: float | int | None = None,
    f_index: str | None = None,
    f_p1_mm: float | int | None = None,
    f_pn_mm: float | int | None = None,
    f_p1_fr: float | int | None = None,
    f_pn_fr: float | int | None = None,
    skip_col_nodes: bool = False,
    skip_col_1dindex: bool = False,
    skip_col_i: bool = False,
    skip_col_j: bool = False,
    skip_col_k: bool = False,
    skip_col_vals: bool = False,
    no_headers: bool = False,
    save_seg_coords: str | None = None,
    cmask: str | None = None,
    gp_index: float | int | None = None,
    oob_index: float | int | None = None,
    oob_value: float | int | None = None,
    oom_value: float | int | None = None,
    outcols_afni_nsd: bool = False,
    outcols_1_result: bool = False,
    outcols_results: bool = False,
    outcols_nsd_format: bool = False,
    help_: bool = False,
    hist: bool = False,
    version: bool = False,
    keep_norm_dir: bool = False,
    reverse_norm_dir: bool = False,
    runner: Runner | None = None,
) -> V3dVol2SurfOutputs:
    """
    3dVol2Surf by R. Reynolds.
    
    Map data from a volume domain to a surface domain.
    
    More information: https://afni.nimh.nih.gov
    
    Args:
        spec_file: SUMA spec file.
        sv: AFNI volume dataset mapped by the surface.
        grid_parent: AFNI volume dataset used as a grid and orientation master\
            for output.
        map_func: Filter for values along the segment.
        surf_a: Name of surface A from the spec file.
        surf_b: Name of surface B from the spec file.
        out_1_d: Specify a 1D file for the output.
        out_niml: Specify a niml file for the output.
        use_norms: Use normals for second surface.
        norm_len: Length for node normals.
        first_node: Skip all previous nodes.
        last_node: Skip all following nodes.
        debug_level: Verbose output level.
        dnode: Node for debug.
        f_steps: Number of steps along each segment (defines the number of\
            evenly spaced points along each segment).
        f_index: Whether to use all segment point values or only those\
            corresponding to unique volume voxels.
        f_p1_mm: Distance in millimeters to add to the first point of each line\
            segment.
        f_pn_mm: Distance in millimeters to add to the second point of each\
            line segment.
        f_p1_fr: Fractional distance to add to the first point of each line\
            segment.
        f_pn_fr: Fractional distance to add to the second point of each line\
            segment.
        skip_col_nodes: Do not output node column.
        skip_col_1dindex: Do not output 1dindex column.
        skip_col_i: Do not output i column.
        skip_col_j: Do not output j column.
        skip_col_k: Do not output k column.
        skip_col_vals: Do not output vals column.
        no_headers: Do not output column headers.
        save_seg_coords: Save segment coordinates to a file.
        cmask: Command for dataset mask.
        gp_index: Choose grid_parent sub-brick.
        oob_index: Specify default index for out of bounds nodes.
        oob_value: Specify default value for out of bounds nodes.
        oom_value: Specify default value for out of mask nodes.
        outcols_afni_nsd: Output nodes and one result column.
        outcols_1_result: Output only one result column.
        outcols_results: Output only all result columns.
        outcols_nsd_format: Output nodes and all results (NI_SURF_DSET format).
        help_: Show this help.
        hist: Show revision history.
        version: Show version information.
        keep_norm_dir: Keep the direction of the normals.
        reverse_norm_dir: Reverse the normal directions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dVol2SurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_VOL2_SURF_METADATA)
    cargs = []
    cargs.append("3dVol2Surf")
    cargs.append(execution.input_file(spec_file))
    cargs.extend(["-sv", execution.input_file(sv)])
    cargs.extend(["-grid_parent", execution.input_file(grid_parent)])
    cargs.extend(["-map_func", map_func])
    cargs.extend(["-surf_A", surf_a])
    if surf_b is not None:
        cargs.extend(["-surf_B", surf_b])
    if out_1_d is not None:
        cargs.extend(["-out_1D", out_1_d])
    if out_niml is not None:
        cargs.extend(["-out_niml", out_niml])
    if use_norms:
        cargs.append("-use_norms")
    if norm_len is not None:
        cargs.extend(["-norm_len", str(norm_len)])
    if first_node is not None:
        cargs.extend(["-first_node", str(first_node)])
    if last_node is not None:
        cargs.extend(["-last_node", str(last_node)])
    if debug_level is not None:
        cargs.extend(["-debug", str(debug_level)])
    if dnode is not None:
        cargs.extend(["-dnode", str(dnode)])
    if f_steps is not None:
        cargs.extend(["-f_steps", str(f_steps)])
    if f_index is not None:
        cargs.extend(["-f_index", f_index])
    if f_p1_mm is not None:
        cargs.extend(["-f_p1_mm", str(f_p1_mm)])
    if f_pn_mm is not None:
        cargs.extend(["-f_pn_mm", str(f_pn_mm)])
    if f_p1_fr is not None:
        cargs.extend(["-f_p1_fr", str(f_p1_fr)])
    if f_pn_fr is not None:
        cargs.extend(["-f_pn_fr", str(f_pn_fr)])
    if skip_col_nodes:
        cargs.append("-skip_col_nodes")
    if skip_col_1dindex:
        cargs.append("-skip_col_1dindex")
    if skip_col_i:
        cargs.append("-skip_col_i")
    if skip_col_j:
        cargs.append("-skip_col_j")
    if skip_col_k:
        cargs.append("-skip_col_k")
    if skip_col_vals:
        cargs.append("-skip_col_vals")
    if no_headers:
        cargs.append("-no_headers")
    if save_seg_coords is not None:
        cargs.extend(["-save_seg_coords", save_seg_coords])
    if cmask is not None:
        cargs.extend(["-cmask", cmask])
    if gp_index is not None:
        cargs.extend(["-gp_index", str(gp_index)])
    if oob_index is not None:
        cargs.extend(["-oob_index", str(oob_index)])
    if oob_value is not None:
        cargs.extend(["-oob_value", str(oob_value)])
    if oom_value is not None:
        cargs.extend(["-oom_value", str(oom_value)])
    if outcols_afni_nsd:
        cargs.append("-outcols_afni_NSD")
    if outcols_1_result:
        cargs.append("-outcols_1_result")
    if outcols_results:
        cargs.append("-outcols_results")
    if outcols_nsd_format:
        cargs.append("-outcols_NSD_format")
    if help_:
        cargs.append("-help")
    if hist:
        cargs.append("-hist")
    if version:
        cargs.append("-version")
    if keep_norm_dir:
        cargs.append("-keep_norm_dir")
    if reverse_norm_dir:
        cargs.append("-reverse_norm_dir")
    ret = V3dVol2SurfOutputs(
        root=execution.output_file("."),
        out_1d_file=execution.output_file(f"{out_1_d}", optional=True) if out_1_d is not None else None,
        out_niml_file=execution.output_file(f"{out_niml}", optional=True) if out_niml is not None else None,
        seg_coords_file=execution.output_file(f"{save_seg_coords}", optional=True) if save_seg_coords is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dVol2SurfOutputs",
    "V_3D_VOL2_SURF_METADATA",
    "v_3d_vol2_surf",
]

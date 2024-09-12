# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_RE_HO_METADATA = Metadata(
    id="4907b9dfed49d3b0df7f50cea93389d02339c14e.boutiques",
    name="3dReHo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dReHoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_re_ho(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reho_output: OutputPathType
    """Output file containing ReHo/Kendall's W value per voxel."""
    roi_reho_vals: OutputPathType
    """List of ROI ReHo values."""
    chi_square: OutputPathType
    """Optional output subbrick containing Friedman chi-square value per
    voxel."""
    roi_chi_vals: OutputPathType
    """ROI Chi-square values file."""


def v_3d_re_ho(
    prefix: str,
    inset: InputPathType,
    nneigh: str | None = None,
    chi_sq: bool = False,
    mask: InputPathType | None = None,
    neigh_rad: float | None = None,
    neigh_x: float | None = None,
    neigh_y: float | None = None,
    neigh_z: float | None = None,
    box_rad: float | None = None,
    box_x: float | None = None,
    box_y: float | None = None,
    box_z: float | None = None,
    in_rois: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dReHoOutputs:
    """
    3dReHo calculates Kendall's W per voxel using neighborhood voxels from 4D time
    series data set.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dReHo.html
    
    Args:
        prefix: Output file name part.
        inset: Time series input file.
        nneigh: Number of voxels in neighborhood, inclusive; can be 7 (for\
            facewise neighbors), 19 (for face- and edge-wise neighbors), 27 (for\
            face-, edge-, and node-wise neighbors). Default is 27.
        chi_sq: Switch to output Friedman chi-square value per voxel as a\
            subbrick.
        mask: Include a whole brain mask within which to calculate ReHo.\
            Otherwise, data should be masked already.
        neigh_rad: Radius R of a desired neighborhood for voxelwise control,\
            must be a floating point number >1. Examples: R=2.0 -> V=33, R=2.3 ->\
            V=57, etc.
        neigh_x: Semi-radius length A for ellipsoidal neighborhood.
        neigh_y: Semi-radius length B for ellipsoidal neighborhood.
        neigh_z: Semi-radius length C for ellipsoidal neighborhood.
        box_rad: Cubic box radius BR centered on a given voxel for neighborhood\
            control. Examples: BR=1 -> V=27, BR=2 -> V=125, etc.
        box_x: Box volume neighborhood dimension X. Values put in get added in\
            the +/- directions of each axis.
        box_y: Box volume neighborhood dimension Y. Values put in get added in\
            the +/- directions of each axis.
        box_z: Box volume neighborhood dimension Z. Values put in get added in\
            the +/- directions of each axis.
        in_rois: Input a set of ROIs, each labeled with distinct integers. ReHo\
            will be calculated per ROI.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dReHoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_RE_HO_METADATA)
    cargs = []
    cargs.append("3dReHo")
    cargs.append("-prefix")
    cargs.append(prefix)
    cargs.append("-inset")
    cargs.append(execution.input_file(inset))
    if nneigh is not None:
        cargs.extend([
            "-nneigh",
            nneigh
        ])
    if chi_sq:
        cargs.append("-chi_sq")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if neigh_rad is not None:
        cargs.extend([
            "-neigh_RAD",
            str(neigh_rad)
        ])
    if neigh_x is not None:
        cargs.extend([
            "-neigh_X",
            str(neigh_x)
        ])
    if neigh_y is not None:
        cargs.extend([
            "-neigh_Y",
            str(neigh_y)
        ])
    if neigh_z is not None:
        cargs.extend([
            "-neigh_Z",
            str(neigh_z)
        ])
    if box_rad is not None:
        cargs.extend([
            "-box_RAD",
            str(box_rad)
        ])
    if box_x is not None:
        cargs.extend([
            "-box_X",
            str(box_x)
        ])
    if box_y is not None:
        cargs.extend([
            "-box_Y",
            str(box_y)
        ])
    if box_z is not None:
        cargs.extend([
            "-box_Z",
            str(box_z)
        ])
    if in_rois is not None:
        cargs.extend([
            "-in_rois",
            execution.input_file(in_rois)
        ])
    ret = V3dReHoOutputs(
        root=execution.output_file("."),
        reho_output=execution.output_file(prefix + "+orig.BRIK"),
        roi_reho_vals=execution.output_file(prefix + "_ROI_reho.vals"),
        chi_square=execution.output_file(prefix + "+orig.BRIK[1]"),
        roi_chi_vals=execution.output_file(prefix + "_ROI_reho.chi"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dReHoOutputs",
    "V_3D_RE_HO_METADATA",
    "v_3d_re_ho",
]

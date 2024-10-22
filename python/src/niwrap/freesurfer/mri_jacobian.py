# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_JACOBIAN_METADATA = Metadata(
    id="02ae4a187b42fcf3963ac202dc1a7655d9264dee.boutiques",
    name="mri_jacobian",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriJacobianOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_jacobian(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_vol: OutputPathType
    """Resulting volume file after Jacobian computation"""


def mri_jacobian(
    morph_file: InputPathType,
    template_vol: InputPathType,
    output_vol: str,
    atlas_coord: bool = False,
    write_area_vols: bool = False,
    log_jacobian: bool = False,
    smooth_sigma: float | None = None,
    zero_mean_log: bool = False,
    tm3d: bool = False,
    help2: bool = False,
    dt: bool = False,
    debug_voxel: list[float] | None = None,
    remove: bool = False,
    runner: Runner | None = None,
) -> MriJacobianOutputs:
    """
    Compute the Jacobian of a morph with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        morph_file: 3D morph input file.
        template_vol: Template volume file.
        output_vol: Output volume file.
        atlas_coord: Output is written in atlas coordinate system.
        write_area_vols: Writing area volumes.
        log_jacobian: Taking log of Jacobian values before saving.
        smooth_sigma: Smoothing Jacobian volume with sigma.
        zero_mean_log: Make log Jacobian zero mean.
        tm3d: The input morph (m3z) originated from tm3d (mri_cvs_register).
        help2: Writing out help.
        dt: DT option (description not provided in help text).
        debug_voxel: Debug voxel with specified Gx, Gy, Gz coordinates.
        remove: Remove option (description not provided in help text).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriJacobianOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_JACOBIAN_METADATA)
    cargs = []
    cargs.append("mri_jacobian")
    cargs.append(execution.input_file(morph_file))
    cargs.append(execution.input_file(template_vol))
    cargs.append(output_vol)
    if atlas_coord:
        cargs.append("-a")
    if write_area_vols:
        cargs.append("-w")
    if log_jacobian:
        cargs.append("-l")
    if smooth_sigma is not None:
        cargs.extend([
            "-s",
            str(smooth_sigma)
        ])
    if zero_mean_log:
        cargs.append("-z")
    if tm3d:
        cargs.append("-tm3d")
    if help2:
        cargs.append("-u")
    if dt:
        cargs.append("-dt")
    if debug_voxel is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, debug_voxel)
        ])
    if remove:
        cargs.append("-remove")
    ret = MriJacobianOutputs(
        root=execution.output_file("."),
        result_vol=execution.output_file(output_vol),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_JACOBIAN_METADATA",
    "MriJacobianOutputs",
    "mri_jacobian",
]

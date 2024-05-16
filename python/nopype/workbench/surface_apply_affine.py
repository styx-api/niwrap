# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.785804

import typing

from ..styxdefs import *


SURFACE_APPLY_AFFINE_METADATA = Metadata(
    id="2b82bc65555d62f9156abd7f9df88009c91024b9",
    name="surface-apply-affine",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceApplyAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_apply_affine(...)`.
    """
    out_surf: OutputPathType
    """the output transformed surface"""


def surface_apply_affine(
    runner: Runner,
    in_surf: InputPathType,
    affine: str,
    out_surf: InputPathType,
) -> SurfaceApplyAffineOutputs:
    """
    APPLY AFFINE TRANSFORM TO SURFACE FILE.
    
    For flirt matrices, you must use the -flirt option, because flirt matrices
    are not a complete description of the coordinate transform they represent.
    If the -flirt option is not present, the affine must be a nifti 'world'
    affine, which can be obtained with the -convert-affine command, or aff_conv
    from the 4dfp suite.
    
    Args:
        runner: Command runner
        in_surf: the surface to transform
        affine: the affine file
        out_surf: the output transformed surface
    Returns:
        NamedTuple of outputs (described in `SurfaceApplyAffineOutputs`).
    """
    execution = runner.start_execution(SURFACE_APPLY_AFFINE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-apply-affine")
    cargs.append(execution.input_file(in_surf))
    cargs.append(affine)
    cargs.append(execution.input_file(out_surf))
    ret = SurfaceApplyAffineOutputs(
        out_surf=execution.output_file(f"{out_surf}"),
    )
    execution.run(cargs)
    return ret

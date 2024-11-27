# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_SPACE_TIME_CORR_METADATA = Metadata(
    id="4814bf096ff466e54811cb676a4fbe4de1173bcf.boutiques",
    name="3dSpaceTimeCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dSpaceTimeCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_space_time_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """Output data set with space-time correlation coefficients."""


def v_3d_space_time_corr(
    inset_a: InputPathType,
    inset_b: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    out_zcorr: bool = False,
    freeze_inset_a_ijk: list[float] | None = None,
    freeze_inset_a_xyz: list[float] | None = None,
    runner: Runner | None = None,
) -> V3dSpaceTimeCorrOutputs:
    """
    Calculates correlation coefficients between two 4D datasets using space+time
    patterns.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset_a: First 4D data set.
        inset_b: Second 4D data set. Must have the same spatial dimensions and\
            number of time points as insetA.
        prefix: Output filename/base.
        mask: Optional mask for calculations. Recommended for speed and\
            interpretability.
        out_zcorr: Switch to output Fisher Z transform of spatial map\
            correlation instead of Pearson r values.
        freeze_inset_a_ijk: Freeze the seed voxel location in the insetA data\
            set using ijk indices while the seed location in insetB moves\
            throughout the volume or mask. Provide three ijk values.
        freeze_inset_a_xyz: Freeze the seed voxel location in the insetA data\
            set using xyz coordinates while the seed location in insetB moves\
            throughout the volume or mask. Provide three xyz values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSpaceTimeCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SPACE_TIME_CORR_METADATA)
    cargs = []
    cargs.append("3dSpaceTimeCorr")
    cargs.extend([
        "-insetA",
        execution.input_file(inset_a)
    ])
    cargs.extend([
        "-insetB",
        execution.input_file(inset_b)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if out_zcorr:
        cargs.append("-out_Zcorr")
    if freeze_inset_a_ijk is not None:
        cargs.extend([
            "-freeze_insetA_ijk",
            *map(str, freeze_inset_a_ijk)
        ])
    if freeze_inset_a_xyz is not None:
        cargs.extend([
            "-freeze_insetA_xyz",
            *map(str, freeze_inset_a_xyz)
        ])
    ret = V3dSpaceTimeCorrOutputs(
        root=execution.output_file("."),
        output=execution.output_file("[OUTPUT_PREFIX].nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSpaceTimeCorrOutputs",
    "V_3D_SPACE_TIME_CORR_METADATA",
    "v_3d_space_time_corr",
]

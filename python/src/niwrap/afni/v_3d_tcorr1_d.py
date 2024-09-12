# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TCORR1_D_METADATA = Metadata(
    id="53f15459103ea70fcda0ae8a21f3ca2a54b306a0.boutiques",
    name="3dTcorr1D",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTcorr1DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcorr1_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output filename prefix."""
    out_file_: OutputPathType
    """Output file containing correlations."""


def v_3d_tcorr1_d(
    xset: InputPathType,
    y_1d: InputPathType,
    spearman: bool = False,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    runner: Runner | None = None,
) -> V3dTcorr1DOutputs:
    """
    Computes the correlation coefficient between each voxel time series in the input
    3D+time dataset.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTcorr1D.html
    
    Args:
        xset: 3d+time dataset input.
        y_1d: 1d time series file input.
        spearman: Correlation is the spearman (rank) correlation coefficient.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTcorr1DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCORR1_D_METADATA)
    cargs = []
    cargs.append("3dTcorr1D")
    cargs.append(execution.input_file(xset))
    if spearman:
        cargs.append("-spearman")
    cargs.append(execution.input_file(y_1d))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dTcorr1DOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(xset).name + "_correlation.nii.gz"),
        out_file_=execution.output_file("out_file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTcorr1DOutputs",
    "V_3D_TCORR1_D_METADATA",
    "v_3d_tcorr1_d",
]

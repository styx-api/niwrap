# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TCORR1_D_METADATA = Metadata(
    id="28502a6e2b45dfa6629df5e5bdaf7c4dde7d82f6.boutiques",
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
    ktaub: bool = False,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    pearson: bool = False,
    quadrant: bool = False,
    spearman: bool = False,
    runner: Runner | None = None,
) -> V3dTcorr1DOutputs:
    """
    Computes the correlation coefficient between each voxel time series in the input
    3D+time dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        xset: 3d+time dataset input.
        y_1d: 1d time series file input.
        ktaub: Correlation is the kendall's tau_b correlation coefficient.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        pearson: Correlation is the normal pearson correlation coefficient.
        quadrant: Correlation is the quadrant correlation coefficient.
        spearman: Correlation is the spearman (rank) correlation coefficient.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTcorr1DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCORR1_D_METADATA)
    cargs = []
    cargs.append("3dTcorr1D")
    if ktaub:
        cargs.append("-ktaub")
    if num_threads is not None:
        cargs.append(str(num_threads))
    if outputtype is not None:
        cargs.append(outputtype)
    if pearson:
        cargs.append("-pearson")
    if quadrant:
        cargs.append("-quadrant")
    if spearman:
        cargs.append("-spearman")
    cargs.append(execution.input_file(xset))
    cargs.append(execution.input_file(y_1d))
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

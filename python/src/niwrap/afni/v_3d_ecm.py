# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ECM_METADATA = Metadata(
    id="91d8d58fa4639faaf4600f4e74c107adf466aacc.boutiques",
    name="3dECM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dEcmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_ecm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_ecm(
    in_file: InputPathType,
    autoclip: bool = False,
    automask: bool = False,
    eps: float | None = None,
    fecm: bool = False,
    full: bool = False,
    mask: InputPathType | None = None,
    max_iter: int | None = None,
    memory: float | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    polort: int | None = None,
    scale: float | None = None,
    shift: float | None = None,
    sparsity: float | None = None,
    thresh: float | None = None,
    runner: Runner | None = None,
) -> V3dEcmOutputs:
    """
    Performs degree centrality on a dataset using a given maskfile via the 3dECM
    command.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3decm.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Mask the dataset to target brain-only voxels.
        eps: Sets the stopping criterion for the power iteration;\
            :math:`l2\\|v_\\text{old} - v_\\text{new}\\| < eps\\|v_\\text{old}\\|`;\
            default = 0.001.
        fecm: Fast centrality method; substantial speed increase but cannot\
            accommodate thresholding; automatically selected if -thresh or\
            -sparsity are not set.
        full: Full power method; enables thresholding; automatically selected\
            if -thresh or -sparsity are set.
        mask: Mask file to mask input data.
        max_iter: Sets the maximum number of iterations to use in the power\
            iteration; default = 1000.
        memory: Limit memory consumption on system by setting the amount of gb\
            to limit the algorithm to; default = 2gb.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        polort: No description provided.
        scale: Scale correlation coefficients in similarity matrix to after\
            shifting, x >= 0.0; default = 1.0 for -full, 0.5 for -fecm.
        shift: Shift correlation coefficients in similarity matrix to enforce\
            non-negativity, s >= 0.0; default = 0.0 for -full, 1.0 for -fecm.
        sparsity: Only take the top percent of connections.
        thresh: Threshold to exclude connections where corr <= thresh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEcmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ECM_METADATA)
    cargs = []
    cargs.append("3dECM")
    cargs.append(execution.input_file(in_file))
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if eps is not None:
        cargs.extend([
            "-eps",
            str(eps)
        ])
    if fecm:
        cargs.append("-fecm")
    if full:
        cargs.append("-full")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if max_iter is not None:
        cargs.extend([
            "-max_iter",
            str(max_iter)
        ])
    if memory is not None:
        cargs.extend([
            "-memory",
            str(memory)
        ])
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if polort is not None:
        cargs.extend([
            "-polort",
            str(polort)
        ])
    if scale is not None:
        cargs.extend([
            "-scale",
            str(scale)
        ])
    if shift is not None:
        cargs.extend([
            "-shift",
            str(shift)
        ])
    if sparsity is not None:
        cargs.extend([
            "-sparsity",
            str(sparsity)
        ])
    if thresh is not None:
        cargs.extend([
            "-thresh",
            str(thresh)
        ])
    ret = V3dEcmOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(in_file).name + "_afni"),
        out_file_=execution.output_file("out_file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dEcmOutputs",
    "V_3D_ECM_METADATA",
    "v_3d_ecm",
]

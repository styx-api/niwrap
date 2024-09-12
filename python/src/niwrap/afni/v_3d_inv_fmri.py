# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_INV_FMRI_METADATA = Metadata(
    id="cb27e0de727e2a1295bb09c0a66d6ab3481186c2.boutiques",
    name="3dInvFMRI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dInvFmriOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_inv_fmri(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """The output 1D file."""


def v_3d_inv_fmri(
    input_file: InputPathType,
    activation_map: InputPathType,
    map_weight: InputPathType | None = None,
    mask: InputPathType | None = None,
    baseline_file: list[InputPathType] | None = None,
    polynom_order: float | None = None,
    output_file: str | None = None,
    method: str | None = None,
    alpha: float | None = None,
    smooth_fir: bool = False,
    smooth_median: bool = False,
    runner: Runner | None = None,
) -> V3dInvFmriOutputs:
    """
    Program to compute stimulus time series, given a 3D+time dataset and an
    activation map (the inverse of the usual FMRI analysis problem).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dInvFMRI.html
    
    Args:
        input_file: Input 3D+time dataset.
        activation_map: Defines activation map; should be a bucket dataset\
            where each sub-brick defines the beta weight map for an unknown\
            stimulus time series.
        map_weight: Defines a weighting factor for the map. Dataset can have\
            either 1 sub-brick or the same number as in the -map dataset.
        mask: Defines a mask dataset to restrict input voxels from -data and\
            -map.
        baseline_file: Baseline time series file. Each column of the file\
            defines a baseline time series.
        polynom_order: Adds polynomials of specified order to the baseline\
            collection.
        output_file: Name of the 1D output file.
        method: Determines the method to use: C for least squares fit to data\
            matrix (default) or K for least squares fit to activation matrix.
        alpha: Set the alpha factor to penalize large values of the output\
            vectors.
        smooth_fir: Smooth the results with a 5 point lowpass FIR filter.
        smooth_median: Smooth the results with a 5 point median filter.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dInvFmriOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_INV_FMRI_METADATA)
    cargs = []
    cargs.append("3dInvFMRI")
    cargs.extend([
        "-data",
        execution.input_file(input_file)
    ])
    cargs.extend([
        "-map",
        execution.input_file(activation_map)
    ])
    if map_weight is not None:
        cargs.extend([
            "-mapwt",
            execution.input_file(map_weight)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if baseline_file is not None:
        cargs.extend([
            "-base",
            *[execution.input_file(f) for f in baseline_file]
        ])
    if polynom_order is not None:
        cargs.extend([
            "-polort",
            str(polynom_order)
        ])
    if output_file is not None:
        cargs.extend([
            "-out",
            output_file
        ])
    if method is not None:
        cargs.extend([
            "-method",
            method
        ])
    if alpha is not None:
        cargs.extend([
            "-alpha",
            str(alpha)
        ])
    if smooth_fir:
        cargs.append("-fir5")
    if smooth_median:
        cargs.append("-median5")
    ret = V3dInvFmriOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(output_file) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dInvFmriOutputs",
    "V_3D_INV_FMRI_METADATA",
    "v_3d_inv_fmri",
]

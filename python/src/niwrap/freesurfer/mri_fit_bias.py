# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_FIT_BIAS_METADATA = Metadata(
    id="cf8d10003f869e3e7ca124a53deaebc1f5c089d0.boutiques",
    name="mri_fit_bias",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriFitBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fit_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_output: OutputPathType
    """Bias corrected output volume"""
    generated_bias_field: OutputPathType
    """Generated bias field"""


def mri_fit_bias(
    inputvol: InputPathType,
    segvol: InputPathType,
    maskvol: InputPathType,
    outvol: str,
    biasfield: str,
    lpf_cutoff: float | None = 23.0,
    dctvol: str | None = None,
    threshold: float | None = None,
    nerode: float | None = 1,
    nthreads: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriFitBiasOutputs:
    """
    A tool for intensity normalization and bias correction in MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inputvol: Input volume for intensity normalization.
        segvol: Segmentation volume to define WM and Cortex (e.g.,\
            aseg.presurf.mgz).
        maskvol: Mask volume; zero everything outside of the mask (e.g.,\
            brainmask.mgz).
        outvol: Bias corrected output volume.
        biasfield: Output bias field.
        lpf_cutoff: Low-pass filter cutoff in mm (default is 23.000000).
        dctvol: DCT fields file for debugging.
        threshold: Mask out anything <= threshold value.
        nerode: 3D erode segmentation by n steps (default is 1).
        nthreads: Number of threads to use.
        debug: Turn on debugging mode.
        checkopts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFitBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FIT_BIAS_METADATA)
    cargs = []
    cargs.append("mri_fit_bias")
    cargs.append("--i")
    cargs.extend([
        "--i",
        execution.input_file(inputvol)
    ])
    cargs.append("--cutoff")
    if lpf_cutoff is not None:
        cargs.extend([
            "--cutoff",
            str(lpf_cutoff)
        ])
    cargs.append("--seg")
    cargs.extend([
        "--seg",
        execution.input_file(segvol)
    ])
    cargs.append("--mask")
    cargs.extend([
        "--mask",
        execution.input_file(maskvol)
    ])
    cargs.append("--o")
    cargs.extend([
        "--o",
        outvol
    ])
    cargs.append("--bias")
    cargs.extend([
        "--bias",
        biasfield
    ])
    cargs.append("--dct")
    if dctvol is not None:
        cargs.extend([
            "--dct",
            dctvol
        ])
    cargs.append("--thresh")
    if threshold is not None:
        cargs.extend([
            "--thresh",
            str(threshold)
        ])
    cargs.append("--erode")
    if nerode is not None:
        cargs.extend([
            "--erode",
            str(nerode)
        ])
    cargs.append("--threads")
    if nthreads is not None:
        cargs.extend([
            "--threads",
            str(nthreads)
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    ret = MriFitBiasOutputs(
        root=execution.output_file("."),
        corrected_output=execution.output_file(outvol),
        generated_bias_field=execution.output_file(biasfield),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_FIT_BIAS_METADATA",
    "MriFitBiasOutputs",
    "mri_fit_bias",
]

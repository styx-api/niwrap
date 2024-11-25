# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEG2RECON_METADATA = Metadata(
    id="44937504fdd7e044c60f695c6e140d947bc3549d.boutiques",
    name="seg2recon",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Seg2reconOutputs(typing.NamedTuple):
    """
    Output object returned when calling `seg2recon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aseg_auto_mgz: OutputPathType
    """Output aseg.auto.mgz file including corpus callosum segmentation"""
    nu_mgz: OutputPathType
    """Bias field corrected output nu.mgz file"""
    brainmask_mgz: OutputPathType
    """Output brainmask.mgz file"""


def seg2recon(
    subject: str,
    segvol: InputPathType,
    inputvol: InputPathType,
    ctab: InputPathType | None = None,
    ndilate: float | None = None,
    threads: float | None = None,
    force_update: bool = False,
    no_cc: bool = False,
    mask: InputPathType | None = None,
    headmask: InputPathType | None = None,
    thresh: float | None = None,
    expert: InputPathType | None = None,
    rca: bool = False,
    no_bias_field_cor: bool = False,
    runner: Runner | None = None,
) -> Seg2reconOutputs:
    """
    Creates and populates a subjects directory from an input image and segmentation
    suitable for running recon-all.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Output subject directory name.
        segvol: Aseg-type volume, e.g., from synthseg, fastsurfer, psacnn,\
            samseg, or aseg.
        inputvol: Input volume as would be passed to recon-all.
        ctab: Color table for the segmentation. Uses embedded table if\
            available, or FreeSurferColorLUT.txt if not specified.
        ndilate: Dilate binarization of segmentation when creating brainmask.\
            Default is 2.
        threads: Number of threads to use for processing.
        force_update: Force regeneration of files whether needed or not.
        no_cc: Do not segment corpus callosum.
        mask: Use this mask as brainmask instead of computing from\
            segmentation.
        headmask: Use this headmask instead of running mri_seghead.
        thresh: Threshold for bias field estimation.
        expert: Path to expert options file.
        rca: Run recon-all on the output.
        no_bias_field_cor: Do not compute or apply bias field correction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Seg2reconOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEG2RECON_METADATA)
    cargs = []
    cargs.append("seg2recon")
    cargs.extend([
        "-s",
        "-" + subject
    ])
    cargs.extend([
        "-seg",
        "-" + execution.input_file(segvol)
    ])
    cargs.extend([
        "-i",
        "-" + execution.input_file(inputvol)
    ])
    if ctab is not None:
        cargs.extend([
            "-ctab",
            "-" + execution.input_file(ctab)
        ])
    if ndilate is not None:
        cargs.extend([
            "--ndilate",
            str(ndilate)
        ])
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if force_update:
        cargs.append("--force-update")
    if no_cc:
        cargs.append("--no-cc")
    if mask is not None:
        cargs.extend([
            "--m",
            execution.input_file(mask)
        ])
    if headmask is not None:
        cargs.extend([
            "--h",
            execution.input_file(headmask)
        ])
    if thresh is not None:
        cargs.extend([
            "--thresh",
            str(thresh)
        ])
    if expert is not None:
        cargs.extend([
            "--expert",
            execution.input_file(expert)
        ])
    if rca:
        cargs.append("--rca")
    if no_bias_field_cor:
        cargs.append("--no-bias-field-cor")
    ret = Seg2reconOutputs(
        root=execution.output_file("."),
        aseg_auto_mgz=execution.output_file(subject + "/aseg.auto.mgz"),
        nu_mgz=execution.output_file(subject + "/nu.mgz"),
        brainmask_mgz=execution.output_file(subject + "/brainmask.mgz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEG2RECON_METADATA",
    "Seg2reconOutputs",
    "seg2recon",
]

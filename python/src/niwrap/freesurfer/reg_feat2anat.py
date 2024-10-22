# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REG_FEAT2ANAT_METADATA = Metadata(
    id="f85ca9bdedc584505f032005f97326ce3f70e7a6.boutiques",
    name="reg-feat2anat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RegFeat2anatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_feat2anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    anat2std_register: OutputPathType
    """Init FS reg from anat to FSL-standard"""
    std2anat_fsl_mat: OutputPathType
    """Init FSL reg from FSL-standard to anat"""
    exf2anat_init_fsl_mat: OutputPathType
    """Init FSL reg from example_func to anat"""
    exf2anat_fsl_mat: OutputPathType
    """Final FSL reg from example_func to anat"""
    anat2exf_register: OutputPathType
    """Final FS reg from example_func to anat"""
    register_dat: OutputPathType
    """Same as anat2exf.register.dat"""
    example_func2standard_mat: OutputPathType
    """Replacement for feat-generated"""
    log_file: OutputPathType
    """Log file for registration"""


def reg_feat2anat(
    feat_dir: str,
    subject_id: str,
    overwrite_exf2std: bool = False,
    manual: bool = False,
    manxfm_type: str | None = None,
    dof: int | None = None,
    bins: int | None = None,
    cost: str | None = None,
    max_angle: float | None = None,
    bet: bool = False,
    title: str | None = None,
    no_bbr: bool = False,
    spm: bool = False,
    no_inorm: bool = False,
    fmov: str | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> RegFeat2anatOutputs:
    """
    Registers FSL-Feat example_func to FreeSurfer anatomical data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_dir: Directory in which to find example_func.
        subject_id: FreeSurfer subject identifier as found in SUBJECTS_DIR.
        overwrite_exf2std: Replace Feat-generated example_func2standard.
        manual: Interactively view/edit registration.
        manxfm_type: Interactively view/edit registration for xfm type. xfmtype\
            can be: func2anat, std2anat, or func2std.
        dof: FLIRT degrees of freedom (default is 6).
        bins: FLIRT number of bins (default is 256).
        cost: FLIRT cost function (default is corratio).
        max_angle: FLIRT maximum search angle (default is 90).
        bet: Run betfunc on example_func (not with FSL 4.0).
        title: Title for tkregister window.
        no_bbr: Do not use boundary-based registration.
        spm: Use SPM instead of FLIRT, 6 dof only.
        no_inorm: Do not inorm when running tkregister2.
        fmov: fmov argument for tkregister2.
        debug: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegFeat2anatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_FEAT2ANAT_METADATA)
    cargs = []
    cargs.append("reg-feat2anat")
    cargs.append("--feat")
    cargs.extend([
        "--feat",
        feat_dir
    ])
    cargs.append("--subject")
    cargs.extend([
        "--subject",
        subject_id
    ])
    if overwrite_exf2std:
        cargs.append("--overwrite-exf2std")
    if manual:
        cargs.append("--manual")
    if manxfm_type is not None:
        cargs.extend([
            "--manxfm",
            manxfm_type
        ])
    if dof is not None:
        cargs.extend([
            "--dof",
            str(dof)
        ])
    if bins is not None:
        cargs.extend([
            "--bins",
            str(bins)
        ])
    if cost is not None:
        cargs.extend([
            "--cost",
            cost
        ])
    if max_angle is not None:
        cargs.extend([
            "--maxangle",
            str(max_angle)
        ])
    if bet:
        cargs.append("--bet")
    if title is not None:
        cargs.extend([
            "--title",
            title
        ])
    if no_bbr:
        cargs.append("--no-bbr")
    if spm:
        cargs.append("--spm")
    if no_inorm:
        cargs.append("--no-inorm")
    if fmov is not None:
        cargs.extend([
            "--fmov",
            fmov
        ])
    if debug:
        cargs.append("--debug")
    ret = RegFeat2anatOutputs(
        root=execution.output_file("."),
        anat2std_register=execution.output_file("featdir/reg/freesurfer/anat2std.register.dat"),
        std2anat_fsl_mat=execution.output_file("featdir/reg/freesurfer/std2anat.fsl.mat"),
        exf2anat_init_fsl_mat=execution.output_file("featdir/reg/freesurfer/exf2anat.init.fsl.mat"),
        exf2anat_fsl_mat=execution.output_file("featdir/reg/freesurfer/exf2anat.fsl.mat"),
        anat2exf_register=execution.output_file("featdir/reg/freesurfer/anat2exf.register.dat"),
        register_dat=execution.output_file("featdir/reg/freesurfer/register.dat"),
        example_func2standard_mat=execution.output_file("featdir/reg/freesurfer/example_func2standard.mat"),
        log_file=execution.output_file("reg/freesurfer/reg-feat2anat.log"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_FEAT2ANAT_METADATA",
    "RegFeat2anatOutputs",
    "reg_feat2anat",
]

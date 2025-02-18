# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_PROC_AXIALIZE_ANAT_METADATA = Metadata(
    id="e138eb56e5029d03d449b78987c687adf3579333.boutiques",
    name="fat_proc_axialize_anat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatProcAxializeAnatParameters = typing.TypedDict('FatProcAxializeAnatParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_axialize_anat"],
    "in_file": InputPathType,
    "ref_file": InputPathType,
    "prefix": str,
    "mode_t2w": bool,
    "mode_t1w": bool,
    "workdir": typing.NotRequired[str | None],
    "out_match_ref": bool,
    "do_ceil_out": bool,
    "extra_al_wtmask": typing.NotRequired[InputPathType | None],
    "extra_al_cost": typing.NotRequired[str | None],
    "extra_al_opts": typing.NotRequired[str | None],
    "focus_mask": typing.NotRequired[InputPathType | None],
    "focus_by_ss": bool,
    "remove_inf_sli": typing.NotRequired[float | None],
    "pre_align_center_mass": bool,
    "pre_center_mass": bool,
    "post_lr_symm": bool,
    "no_pre_lr_symm": bool,
    "no_clean": bool,
    "qc_ulay_range": typing.NotRequired[list[float] | None],
    "no_qc_view": bool,
    "qc_prefix": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fat_proc_axialize_anat": fat_proc_axialize_anat_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fat_proc_axialize_anat": fat_proc_axialize_anat_outputs,
    }.get(t)


class FatProcAxializeAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_axialize_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """An anatomical data set that is regularly situated within its FOV
    volume"""
    working_directory: OutputPathType | None
    """The working directory with intermediate files"""


def fat_proc_axialize_anat_params(
    in_file: InputPathType,
    ref_file: InputPathType,
    prefix: str,
    mode_t2w: bool = False,
    mode_t1w: bool = False,
    workdir: str | None = None,
    out_match_ref: bool = False,
    do_ceil_out: bool = False,
    extra_al_wtmask: InputPathType | None = None,
    extra_al_cost: str | None = None,
    extra_al_opts: str | None = None,
    focus_mask: InputPathType | None = None,
    focus_by_ss: bool = False,
    remove_inf_sli: float | None = None,
    pre_align_center_mass: bool = False,
    pre_center_mass: bool = False,
    post_lr_symm: bool = False,
    no_pre_lr_symm: bool = False,
    no_clean: bool = False,
    qc_ulay_range: list[float] | None = None,
    no_qc_view: bool = False,
    qc_prefix: str | None = None,
) -> FatProcAxializeAnatParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input anatomical volume full name.
        ref_file: Reference volume full name, such as TT or MNI.
        prefix: Output prefix for files and snapshots.
        mode_t2w: Switch for T2-weighted image processing.
        mode_t1w: Switch for T1-weighted image processing.
        workdir: Name of the working subdirectory in the output directory.
        out_match_ref: Match the final output volume space FOV and spatial\
            resolution to the reference file.
        do_ceil_out: Apply a ceiling based on the 98%ile value within an\
            automasked volume.
        extra_al_wtmask: Extra weight mask to emphasize specific parts for\
            alignment.
        extra_al_cost: Specify a cost function for 3dAllineate to use (default\
            'lpa').
        extra_al_opts: Extra options for 3dAllineate when applying the warp.
        focus_mask: Input mask to focus processing and alignment.
        focus_by_ss: Make a mask by simply skullstripping input data set.
        remove_inf_sli: Remove a number of slices from the inferior part of the\
            FOV.
        pre_align_center_mass: Pre-align the centers of mass of the volumes.
        pre_center_mass: Pre-recenter input center of mass to (0, 0, 0).
        post_lr_symm: Apply post-alignment left-right symmetrization.
        no_pre_lr_symm: Turn off pre-alignment left-right symmetrization.
        no_clean: Do not remove working directory '__WORKING_axialize_anat'.
        qc_ulay_range: Provide a min (UMIN) and max (UMAX) range for underlay\
            grayscale bar.
        no_qc_view: Turn off default QC image saving/viewing.
        qc_prefix: Provide a prefix for QC outputs separate from the main\
            prefix.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_axialize_anat",
        "in_file": in_file,
        "ref_file": ref_file,
        "prefix": prefix,
        "mode_t2w": mode_t2w,
        "mode_t1w": mode_t1w,
        "out_match_ref": out_match_ref,
        "do_ceil_out": do_ceil_out,
        "focus_by_ss": focus_by_ss,
        "pre_align_center_mass": pre_align_center_mass,
        "pre_center_mass": pre_center_mass,
        "post_lr_symm": post_lr_symm,
        "no_pre_lr_symm": no_pre_lr_symm,
        "no_clean": no_clean,
        "no_qc_view": no_qc_view,
    }
    if workdir is not None:
        params["workdir"] = workdir
    if extra_al_wtmask is not None:
        params["extra_al_wtmask"] = extra_al_wtmask
    if extra_al_cost is not None:
        params["extra_al_cost"] = extra_al_cost
    if extra_al_opts is not None:
        params["extra_al_opts"] = extra_al_opts
    if focus_mask is not None:
        params["focus_mask"] = focus_mask
    if remove_inf_sli is not None:
        params["remove_inf_sli"] = remove_inf_sli
    if qc_ulay_range is not None:
        params["qc_ulay_range"] = qc_ulay_range
    if qc_prefix is not None:
        params["qc_prefix"] = qc_prefix
    return params


def fat_proc_axialize_anat_cargs(
    params: FatProcAxializeAnatParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("fat_proc_axialize_anat")
    cargs.append(execution.input_file(params.get("in_file")))
    cargs.append(execution.input_file(params.get("ref_file")))
    cargs.append(params.get("prefix"))
    if params.get("mode_t2w"):
        cargs.append("-mode_t2w")
    if params.get("mode_t1w"):
        cargs.append("-mode_t1w")
    if params.get("workdir") is not None:
        cargs.extend([
            "-workdir",
            params.get("workdir")
        ])
    if params.get("out_match_ref"):
        cargs.append("-out_match_ref")
    if params.get("do_ceil_out"):
        cargs.append("-do_ceil_out")
    if params.get("extra_al_wtmask") is not None:
        cargs.extend([
            "-extra_al_wtmask",
            execution.input_file(params.get("extra_al_wtmask"))
        ])
    if params.get("extra_al_cost") is not None:
        cargs.extend([
            "-extra_al_cost",
            params.get("extra_al_cost")
        ])
    if params.get("extra_al_opts") is not None:
        cargs.extend([
            "-extra_al_opts",
            params.get("extra_al_opts")
        ])
    if params.get("focus_mask") is not None:
        cargs.extend([
            "-focus_mask",
            execution.input_file(params.get("focus_mask"))
        ])
    if params.get("focus_by_ss"):
        cargs.append("-focus_by_ss")
    if params.get("remove_inf_sli") is not None:
        cargs.extend([
            "-remove_inf_sli",
            str(params.get("remove_inf_sli"))
        ])
    if params.get("pre_align_center_mass"):
        cargs.append("-pre_align_center_mass")
    if params.get("pre_center_mass"):
        cargs.append("-pre_center_mass")
    if params.get("post_lr_symm"):
        cargs.append("-post_lr_symm")
    if params.get("no_pre_lr_symm"):
        cargs.append("-no_pre_lr_symm")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("qc_ulay_range") is not None:
        cargs.extend([
            "-qc1_ulay_range",
            *map(str, params.get("qc_ulay_range"))
        ])
    if params.get("no_qc_view"):
        cargs.append("-no_qc_view")
    if params.get("qc_prefix") is not None:
        cargs.extend([
            "-qc_prefix",
            params.get("qc_prefix")
        ])
    return cargs


def fat_proc_axialize_anat_outputs(
    params: FatProcAxializeAnatParameters,
    execution: Execution,
) -> FatProcAxializeAnatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcAxializeAnatOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".nii.gz"),
        working_directory=execution.output_file(params.get("workdir")) if (params.get("workdir") is not None) else None,
    )
    return ret


def fat_proc_axialize_anat_execute(
    params: FatProcAxializeAnatParameters,
    execution: Execution,
) -> FatProcAxializeAnatOutputs:
    """
    Helps align the major axes of an anatomical volume to those of the volumetric
    field of view.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcAxializeAnatOutputs`).
    """
    cargs = fat_proc_axialize_anat_cargs(params, execution)
    ret = fat_proc_axialize_anat_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fat_proc_axialize_anat(
    in_file: InputPathType,
    ref_file: InputPathType,
    prefix: str,
    mode_t2w: bool = False,
    mode_t1w: bool = False,
    workdir: str | None = None,
    out_match_ref: bool = False,
    do_ceil_out: bool = False,
    extra_al_wtmask: InputPathType | None = None,
    extra_al_cost: str | None = None,
    extra_al_opts: str | None = None,
    focus_mask: InputPathType | None = None,
    focus_by_ss: bool = False,
    remove_inf_sli: float | None = None,
    pre_align_center_mass: bool = False,
    pre_center_mass: bool = False,
    post_lr_symm: bool = False,
    no_pre_lr_symm: bool = False,
    no_clean: bool = False,
    qc_ulay_range: list[float] | None = None,
    no_qc_view: bool = False,
    qc_prefix: str | None = None,
    runner: Runner | None = None,
) -> FatProcAxializeAnatOutputs:
    """
    Helps align the major axes of an anatomical volume to those of the volumetric
    field of view.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input anatomical volume full name.
        ref_file: Reference volume full name, such as TT or MNI.
        prefix: Output prefix for files and snapshots.
        mode_t2w: Switch for T2-weighted image processing.
        mode_t1w: Switch for T1-weighted image processing.
        workdir: Name of the working subdirectory in the output directory.
        out_match_ref: Match the final output volume space FOV and spatial\
            resolution to the reference file.
        do_ceil_out: Apply a ceiling based on the 98%ile value within an\
            automasked volume.
        extra_al_wtmask: Extra weight mask to emphasize specific parts for\
            alignment.
        extra_al_cost: Specify a cost function for 3dAllineate to use (default\
            'lpa').
        extra_al_opts: Extra options for 3dAllineate when applying the warp.
        focus_mask: Input mask to focus processing and alignment.
        focus_by_ss: Make a mask by simply skullstripping input data set.
        remove_inf_sli: Remove a number of slices from the inferior part of the\
            FOV.
        pre_align_center_mass: Pre-align the centers of mass of the volumes.
        pre_center_mass: Pre-recenter input center of mass to (0, 0, 0).
        post_lr_symm: Apply post-alignment left-right symmetrization.
        no_pre_lr_symm: Turn off pre-alignment left-right symmetrization.
        no_clean: Do not remove working directory '__WORKING_axialize_anat'.
        qc_ulay_range: Provide a min (UMIN) and max (UMAX) range for underlay\
            grayscale bar.
        no_qc_view: Turn off default QC image saving/viewing.
        qc_prefix: Provide a prefix for QC outputs separate from the main\
            prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcAxializeAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_AXIALIZE_ANAT_METADATA)
    params = fat_proc_axialize_anat_params(in_file=in_file, ref_file=ref_file, prefix=prefix, mode_t2w=mode_t2w, mode_t1w=mode_t1w, workdir=workdir, out_match_ref=out_match_ref, do_ceil_out=do_ceil_out, extra_al_wtmask=extra_al_wtmask, extra_al_cost=extra_al_cost, extra_al_opts=extra_al_opts, focus_mask=focus_mask, focus_by_ss=focus_by_ss, remove_inf_sli=remove_inf_sli, pre_align_center_mass=pre_align_center_mass, pre_center_mass=pre_center_mass, post_lr_symm=post_lr_symm, no_pre_lr_symm=no_pre_lr_symm, no_clean=no_clean, qc_ulay_range=qc_ulay_range, no_qc_view=no_qc_view, qc_prefix=qc_prefix)
    return fat_proc_axialize_anat_execute(params, execution)


__all__ = [
    "FAT_PROC_AXIALIZE_ANAT_METADATA",
    "FatProcAxializeAnatOutputs",
    "FatProcAxializeAnatParameters",
    "fat_proc_axialize_anat",
    "fat_proc_axialize_anat_params",
]

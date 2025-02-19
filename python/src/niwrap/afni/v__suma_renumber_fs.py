# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SUMA_RENUMBER_FS_METADATA = Metadata(
    id="c19b88d98568eb300b3deddf6a92cffe231ec7b8.boutiques",
    name="@SUMA_renumber_FS",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VSumaRenumberFsParameters = typing.TypedDict('VSumaRenumberFsParameters', {
    "__STYX_TYPE__": typing.Literal["@SUMA_renumber_FS"],
    "sumadir": str,
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
        "@SUMA_renumber_FS": v__suma_renumber_fs_cargs,
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
        "@SUMA_renumber_FS": v__suma_renumber_fs_outputs,
    }.get(t)


class VSumaRenumberFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_renumber_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    ren_all: OutputPathType
    """Whole parcellation/segmentation file with renumbered ROIs."""
    ren_gm: OutputPathType
    """Gray matter tissue segmentation map."""
    ren_wmat: OutputPathType
    """White matter tissue segmentation map."""
    ren_csf: OutputPathType
    """Cerebrospinal fluid tissue segmentation map."""
    ren_vent: OutputPathType
    """Ventricles and choroid plexus tissue segmentation map."""
    ren_othr: OutputPathType
    """Other tissue segmentation map (optic chiasm, non-WM-hypointens, etc.)."""
    ren_unkn: OutputPathType
    """Unknown tissue segmentation map (FS-defined 'unknown', with voxel value
    >0)."""
    ren_gmrois: OutputPathType
    """Gray matter ROIs without '*-Cerebral-Cortex' dots."""
    fs_ap_wm: OutputPathType
    """White matter mask (excluding the dotted part from FS)."""
    fs_ap_latvent: OutputPathType
    """Lateral ventricles mask ('*-Lateral-Ventricle')."""
    ren_lbl_table: OutputPathType
    """Labeltable of the new ROI values."""


def v__suma_renumber_fs_params(
    sumadir: str,
) -> VSumaRenumberFsParameters:
    """
    Build parameters.
    
    Args:
        sumadir: Path to the 'SUMA/' directory created by @SUMA_Make_Spec_FS.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@SUMA_renumber_FS",
        "sumadir": sumadir,
    }
    return params


def v__suma_renumber_fs_cargs(
    params: VSumaRenumberFsParameters,
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
    cargs.append("@SUMA_renumber_FS")
    cargs.append(params.get("sumadir"))
    return cargs


def v__suma_renumber_fs_outputs(
    params: VSumaRenumberFsParameters,
    execution: Execution,
) -> VSumaRenumberFsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSumaRenumberFsOutputs(
        root=execution.output_file("."),
        ren_all=execution.output_file("*_REN_all.nii.gz"),
        ren_gm=execution.output_file("*_REN_gm.nii.gz"),
        ren_wmat=execution.output_file("*_REN_wmat.nii.gz"),
        ren_csf=execution.output_file("*_REN_csf.nii.gz"),
        ren_vent=execution.output_file("*_REN_vent.nii.gz"),
        ren_othr=execution.output_file("*_REN_othr.nii.gz"),
        ren_unkn=execution.output_file("*_REN_unkn.nii.gz"),
        ren_gmrois=execution.output_file("*_REN_gmrois.nii.gz"),
        fs_ap_wm=execution.output_file("fs_ap_wm.nii.gz"),
        fs_ap_latvent=execution.output_file("fs_ap_latvent.nii.gz"),
        ren_lbl_table=execution.output_file("*_REN_all.niml.lt"),
    )
    return ret


def v__suma_renumber_fs_execute(
    params: VSumaRenumberFsParameters,
    execution: Execution,
) -> VSumaRenumberFsOutputs:
    """
    This script processes FreeSurfer-generated parcellation files and produces
    various derived datasets and segmentation maps.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSumaRenumberFsOutputs`).
    """
    params = execution.params(params)
    cargs = v__suma_renumber_fs_cargs(params, execution)
    ret = v__suma_renumber_fs_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__suma_renumber_fs(
    sumadir: str,
    runner: Runner | None = None,
) -> VSumaRenumberFsOutputs:
    """
    This script processes FreeSurfer-generated parcellation files and produces
    various derived datasets and segmentation maps.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        sumadir: Path to the 'SUMA/' directory created by @SUMA_Make_Spec_FS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaRenumberFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_RENUMBER_FS_METADATA)
    params = v__suma_renumber_fs_params(
        sumadir=sumadir,
    )
    return v__suma_renumber_fs_execute(params, execution)


__all__ = [
    "VSumaRenumberFsOutputs",
    "VSumaRenumberFsParameters",
    "V__SUMA_RENUMBER_FS_METADATA",
    "v__suma_renumber_fs",
    "v__suma_renumber_fs_params",
]

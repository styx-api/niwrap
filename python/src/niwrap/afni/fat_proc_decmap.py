# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_PROC_DECMAP_METADATA = Metadata(
    id="a736dc72fa9ccb8800e84305855b09096c833b1d.boutiques",
    name="fat_proc_decmap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatProcDecmapParameters = typing.TypedDict('FatProcDecmapParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_decmap"],
    "in_fa": InputPathType,
    "in_v1": InputPathType,
    "prefix": str,
    "mask": typing.NotRequired[InputPathType | None],
    "fa_thr": typing.NotRequired[float | None],
    "fa_sca": typing.NotRequired[float | None],
    "workdir": typing.NotRequired[str | None],
    "no_clean": bool,
    "qc_prefix": typing.NotRequired[str | None],
    "no_cmd_out": bool,
    "no_qc_view": bool,
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
        "fat_proc_decmap": fat_proc_decmap_cargs,
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
        "fat_proc_decmap": fat_proc_decmap_outputs,
    }.get(t)


class FatProcDecmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_decmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_dec_rgb: OutputPathType
    """Single file of type 'rgb' for RGB coloration display."""
    outfile_dec_unwt_thr: OutputPathType
    """Single file of type 'rgb' without FA weighting but using FA to threshold
    where DEC values are calculated."""
    outfile_dec_sca: OutputPathType
    """DEC file additionally scaled by a value (such as 0.7)."""
    qc_dec_images: OutputPathType
    """Set of cor, axi, and sag images (each a 5x3 montage) of the DEC data."""
    qc_dec_unwt_thrx_images: OutputPathType
    """Set of cor, axi, and sag images (each a 5x3 montage) of the DEC
    unweighted thresholded data."""
    qc_dec_sca_images: OutputPathType
    """Set of cor, axi, and sag images (each a 5x3 montage) of the DEC scaled
    data."""


def fat_proc_decmap_params(
    in_fa: InputPathType,
    in_v1: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    fa_thr: float | None = None,
    fa_sca: float | None = None,
    workdir: str | None = None,
    no_clean: bool = False,
    qc_prefix: str | None = None,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
) -> FatProcDecmapParameters:
    """
    Build parameters.
    
    Args:
        in_fa: Input FA (scalar) map.
        in_v1: Input first eigenvector (3-vector) map.
        prefix: Set prefix (and path) for output DWI data.
        mask: Optional mask for picking out a region. Otherwise, only places\
            with FA>0 are given coloration.
        fa_thr: For QC1 type of DEC images, use FFF to threshold where DEC\
            values are calculated (default: 0.2).
        fa_sca: For QC2 type of DEC images, use SSS to scale the FA weighting\
            of what would otherwise be a 'classical' DEC map (default: 0.7).
        workdir: Specify a working directory, which can be removed (default:\
            '__WORKING_decmap').
        no_clean: Do not delete temporary files when finishing.
        qc_prefix: Set the prefix of the QC image files (default: 'PREFIX').
        no_cmd_out: Do not save the command line call of this program and\
            location where it was run.
        no_qc_view: Turn off generating QC image files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_decmap",
        "in_fa": in_fa,
        "in_v1": in_v1,
        "prefix": prefix,
        "no_clean": no_clean,
        "no_cmd_out": no_cmd_out,
        "no_qc_view": no_qc_view,
    }
    if mask is not None:
        params["mask"] = mask
    if fa_thr is not None:
        params["fa_thr"] = fa_thr
    if fa_sca is not None:
        params["fa_sca"] = fa_sca
    if workdir is not None:
        params["workdir"] = workdir
    if qc_prefix is not None:
        params["qc_prefix"] = qc_prefix
    return params


def fat_proc_decmap_cargs(
    params: FatProcDecmapParameters,
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
    cargs.append("fat_proc_decmap")
    cargs.extend([
        "-in_fa",
        execution.input_file(params.get("in_fa"))
    ])
    cargs.extend([
        "-in_v1",
        execution.input_file(params.get("in_v1"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("fa_thr") is not None:
        cargs.extend([
            "-fa_thr",
            str(params.get("fa_thr"))
        ])
    if params.get("fa_sca") is not None:
        cargs.extend([
            "-fa_sca",
            str(params.get("fa_sca"))
        ])
    if params.get("workdir") is not None:
        cargs.extend([
            "-workdir",
            params.get("workdir")
        ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("qc_prefix") is not None:
        cargs.extend([
            "-qc_prefix",
            params.get("qc_prefix")
        ])
    if params.get("no_cmd_out"):
        cargs.append("-no_cmd_out")
    if params.get("no_qc_view"):
        cargs.append("-no_qc_view")
    return cargs


def fat_proc_decmap_outputs(
    params: FatProcDecmapParameters,
    execution: Execution,
) -> FatProcDecmapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcDecmapOutputs(
        root=execution.output_file("."),
        outfile_dec_rgb=execution.output_file(params.get("prefix") + "_dec.nii.gz"),
        outfile_dec_unwt_thr=execution.output_file(params.get("prefix") + "_dec_unwt_thr.nii.gz"),
        outfile_dec_sca=execution.output_file(params.get("prefix") + "_dec_sca*.nii.gz"),
        qc_dec_images=execution.output_file(params.get("prefix") + "_qc_dec*.png"),
        qc_dec_unwt_thrx_images=execution.output_file(params.get("prefix") + "_qc_dec_unwt_thrx*.png"),
        qc_dec_sca_images=execution.output_file(params.get("prefix") + "_qc_dec_sca*.png"),
    )
    return ret


def fat_proc_decmap_execute(
    params: FatProcDecmapParameters,
    execution: Execution,
) -> FatProcDecmapOutputs:
    """
    This program makes a directionally encoded color (DEC) map for DTI results.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcDecmapOutputs`).
    """
    cargs = fat_proc_decmap_cargs(params, execution)
    ret = fat_proc_decmap_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fat_proc_decmap(
    in_fa: InputPathType,
    in_v1: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    fa_thr: float | None = None,
    fa_sca: float | None = None,
    workdir: str | None = None,
    no_clean: bool = False,
    qc_prefix: str | None = None,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    runner: Runner | None = None,
) -> FatProcDecmapOutputs:
    """
    This program makes a directionally encoded color (DEC) map for DTI results.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_fa: Input FA (scalar) map.
        in_v1: Input first eigenvector (3-vector) map.
        prefix: Set prefix (and path) for output DWI data.
        mask: Optional mask for picking out a region. Otherwise, only places\
            with FA>0 are given coloration.
        fa_thr: For QC1 type of DEC images, use FFF to threshold where DEC\
            values are calculated (default: 0.2).
        fa_sca: For QC2 type of DEC images, use SSS to scale the FA weighting\
            of what would otherwise be a 'classical' DEC map (default: 0.7).
        workdir: Specify a working directory, which can be removed (default:\
            '__WORKING_decmap').
        no_clean: Do not delete temporary files when finishing.
        qc_prefix: Set the prefix of the QC image files (default: 'PREFIX').
        no_cmd_out: Do not save the command line call of this program and\
            location where it was run.
        no_qc_view: Turn off generating QC image files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcDecmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_DECMAP_METADATA)
    params = fat_proc_decmap_params(in_fa=in_fa, in_v1=in_v1, prefix=prefix, mask=mask, fa_thr=fa_thr, fa_sca=fa_sca, workdir=workdir, no_clean=no_clean, qc_prefix=qc_prefix, no_cmd_out=no_cmd_out, no_qc_view=no_qc_view)
    return fat_proc_decmap_execute(params, execution)


__all__ = [
    "FAT_PROC_DECMAP_METADATA",
    "FatProcDecmapOutputs",
    "FatProcDecmapParameters",
    "fat_proc_decmap",
    "fat_proc_decmap_params",
]

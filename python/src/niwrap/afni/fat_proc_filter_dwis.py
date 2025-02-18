# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_PROC_FILTER_DWIS_METADATA = Metadata(
    id="f1ab079defa2b7a6a0437c119ce099f8d81cc812.boutiques",
    name="fat_proc_filter_dwis",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatProcFilterDwisParameters = typing.TypedDict('FatProcFilterDwisParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_filter_dwis"],
    "input_dwi": InputPathType,
    "input_gradient": InputPathType,
    "select_string": str,
    "select_file": typing.NotRequired[InputPathType | None],
    "output_prefix": str,
    "input_bvals": typing.NotRequired[InputPathType | None],
    "unit_mag_out": bool,
    "qc_prefix": typing.NotRequired[str | None],
    "no_qc_view": bool,
    "no_cmd_out": bool,
    "do_movie": typing.NotRequired[typing.Literal["AGIF", "MPEG"] | None],
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
        "fat_proc_filter_dwis": fat_proc_filter_dwis_cargs,
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
        "fat_proc_filter_dwis": fat_proc_filter_dwis_outputs,
    }.get(t)


class FatProcFilterDwisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_filter_dwis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_dwi: OutputPathType
    """Filtered 4D DWI dataset."""
    filtered_bvecs: OutputPathType
    """Filtered gradient file matching input format."""
    filtered_bvals: OutputPathType
    """Filtered b-values file, if provided."""


def fat_proc_filter_dwis_params(
    input_dwi: InputPathType,
    input_gradient: InputPathType,
    select_string: str,
    output_prefix: str,
    select_file: InputPathType | None = None,
    input_bvals: InputPathType | None = None,
    unit_mag_out: bool = False,
    qc_prefix: str | None = None,
    no_qc_view: bool = False,
    no_cmd_out: bool = False,
    do_movie: typing.Literal["AGIF", "MPEG"] | None = None,
) -> FatProcFilterDwisParameters:
    """
    Build parameters.
    
    Args:
        input_dwi: Name of a 4D file of DWIs (required).
        input_gradient: Bvec/bmat file from the gradients. Required. One of\
            these options must be used: -in_col_matA, -in_col_matT, -in_col_vec,\
            -in_row_vec.
        select_string: A string of indices and index ranges for selecting which\
            volumes/grads/bvals to keep. This string gets applied to the volume,\
            bval|bvec|bmat files for an input set. Either this or -select_file is\
            required.
        output_prefix: Output prefix for all the volumes and text files.\
            Required.
        select_file: A file containing a string of indices and index ranges for\
            selecting which volumes/grads/bvals to keep. This string gets applied\
            to the volume, bval|bvec|bmat files for an input set. Either this or\
            -select is required.
        input_bvals: If the bvec/bmat is a file of unit-magnitude values, then\
            the bvalues can be input.
        unit_mag_out: Ensure that the output grad information is unit\
            magnitude.
        qc_prefix: Set the prefix of the QC image files separately.
        no_qc_view: Turn off generating QC image files.
        no_cmd_out: Don't save the command line call of this program and the\
            location where it was run.
        do_movie: Output a movie of the newly created dataset (AGIF or MPEG).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_filter_dwis",
        "input_dwi": input_dwi,
        "input_gradient": input_gradient,
        "select_string": select_string,
        "output_prefix": output_prefix,
        "unit_mag_out": unit_mag_out,
        "no_qc_view": no_qc_view,
        "no_cmd_out": no_cmd_out,
    }
    if select_file is not None:
        params["select_file"] = select_file
    if input_bvals is not None:
        params["input_bvals"] = input_bvals
    if qc_prefix is not None:
        params["qc_prefix"] = qc_prefix
    if do_movie is not None:
        params["do_movie"] = do_movie
    return params


def fat_proc_filter_dwis_cargs(
    params: FatProcFilterDwisParameters,
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
    cargs.append("fat_proc_filter_dwis")
    cargs.extend([
        "-in_dwi",
        execution.input_file(params.get("input_dwi"))
    ])
    cargs.extend([
        "-in_col_matA|-in_col_matT|-in_col_vec|-in_row_vec",
        execution.input_file(params.get("input_gradient"))
    ])
    cargs.extend([
        "-select",
        params.get("select_string")
    ])
    if params.get("select_file") is not None:
        cargs.extend([
            "-select_file",
            execution.input_file(params.get("select_file"))
        ])
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    if params.get("input_bvals") is not None:
        cargs.extend([
            "-in_bvals",
            execution.input_file(params.get("input_bvals"))
        ])
    if params.get("unit_mag_out"):
        cargs.append("-unit_mag_out")
    if params.get("qc_prefix") is not None:
        cargs.extend([
            "-qc_prefix",
            params.get("qc_prefix")
        ])
    if params.get("no_qc_view"):
        cargs.append("-no_qc_view")
    if params.get("no_cmd_out"):
        cargs.append("-no_cmd_out")
    if params.get("do_movie") is not None:
        cargs.extend([
            "-do_movie",
            params.get("do_movie")
        ])
    return cargs


def fat_proc_filter_dwis_outputs(
    params: FatProcFilterDwisParameters,
    execution: Execution,
) -> FatProcFilterDwisOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcFilterDwisOutputs(
        root=execution.output_file("."),
        filtered_dwi=execution.output_file(params.get("output_prefix") + "_filtered.nii.gz"),
        filtered_bvecs=execution.output_file(params.get("output_prefix") + "_filtered.bvecs"),
        filtered_bvals=execution.output_file(params.get("output_prefix") + "_filtered.bvals"),
    )
    return ret


def fat_proc_filter_dwis_execute(
    params: FatProcFilterDwisParameters,
    execution: Execution,
) -> FatProcFilterDwisOutputs:
    """
    Filter out user-found and user-defined bad volumes from DWI data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcFilterDwisOutputs`).
    """
    cargs = fat_proc_filter_dwis_cargs(params, execution)
    ret = fat_proc_filter_dwis_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fat_proc_filter_dwis(
    input_dwi: InputPathType,
    input_gradient: InputPathType,
    select_string: str,
    output_prefix: str,
    select_file: InputPathType | None = None,
    input_bvals: InputPathType | None = None,
    unit_mag_out: bool = False,
    qc_prefix: str | None = None,
    no_qc_view: bool = False,
    no_cmd_out: bool = False,
    do_movie: typing.Literal["AGIF", "MPEG"] | None = None,
    runner: Runner | None = None,
) -> FatProcFilterDwisOutputs:
    """
    Filter out user-found and user-defined bad volumes from DWI data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dwi: Name of a 4D file of DWIs (required).
        input_gradient: Bvec/bmat file from the gradients. Required. One of\
            these options must be used: -in_col_matA, -in_col_matT, -in_col_vec,\
            -in_row_vec.
        select_string: A string of indices and index ranges for selecting which\
            volumes/grads/bvals to keep. This string gets applied to the volume,\
            bval|bvec|bmat files for an input set. Either this or -select_file is\
            required.
        output_prefix: Output prefix for all the volumes and text files.\
            Required.
        select_file: A file containing a string of indices and index ranges for\
            selecting which volumes/grads/bvals to keep. This string gets applied\
            to the volume, bval|bvec|bmat files for an input set. Either this or\
            -select is required.
        input_bvals: If the bvec/bmat is a file of unit-magnitude values, then\
            the bvalues can be input.
        unit_mag_out: Ensure that the output grad information is unit\
            magnitude.
        qc_prefix: Set the prefix of the QC image files separately.
        no_qc_view: Turn off generating QC image files.
        no_cmd_out: Don't save the command line call of this program and the\
            location where it was run.
        do_movie: Output a movie of the newly created dataset (AGIF or MPEG).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcFilterDwisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_FILTER_DWIS_METADATA)
    params = fat_proc_filter_dwis_params(input_dwi=input_dwi, input_gradient=input_gradient, select_string=select_string, select_file=select_file, output_prefix=output_prefix, input_bvals=input_bvals, unit_mag_out=unit_mag_out, qc_prefix=qc_prefix, no_qc_view=no_qc_view, no_cmd_out=no_cmd_out, do_movie=do_movie)
    return fat_proc_filter_dwis_execute(params, execution)


__all__ = [
    "FAT_PROC_FILTER_DWIS_METADATA",
    "FatProcFilterDwisOutputs",
    "FatProcFilterDwisParameters",
    "fat_proc_filter_dwis",
    "fat_proc_filter_dwis_params",
]

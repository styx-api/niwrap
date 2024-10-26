# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_FILTER_DWIS_METADATA = Metadata(
    id="f1ab079defa2b7a6a0437c119ce099f8d81cc812.boutiques",
    name="fat_proc_filter_dwis",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


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
    cargs = []
    cargs.append("fat_proc_filter_dwis")
    cargs.extend([
        "-in_dwi",
        execution.input_file(input_dwi)
    ])
    cargs.extend([
        "-in_col_matA|-in_col_matT|-in_col_vec|-in_row_vec",
        execution.input_file(input_gradient)
    ])
    cargs.extend([
        "-select",
        select_string
    ])
    if select_file is not None:
        cargs.extend([
            "-select_file",
            execution.input_file(select_file)
        ])
    cargs.extend([
        "-prefix",
        output_prefix
    ])
    if input_bvals is not None:
        cargs.extend([
            "-in_bvals",
            execution.input_file(input_bvals)
        ])
    if unit_mag_out:
        cargs.append("-unit_mag_out")
    if qc_prefix is not None:
        cargs.extend([
            "-qc_prefix",
            qc_prefix
        ])
    if no_qc_view:
        cargs.append("-no_qc_view")
    if no_cmd_out:
        cargs.append("-no_cmd_out")
    if do_movie is not None:
        cargs.extend([
            "-do_movie",
            do_movie
        ])
    ret = FatProcFilterDwisOutputs(
        root=execution.output_file("."),
        filtered_dwi=execution.output_file(output_prefix + "_filtered.nii.gz"),
        filtered_bvecs=execution.output_file(output_prefix + "_filtered.bvecs"),
        filtered_bvals=execution.output_file(output_prefix + "_filtered.bvals"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_FILTER_DWIS_METADATA",
    "FatProcFilterDwisOutputs",
    "fat_proc_filter_dwis",
]

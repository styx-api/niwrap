# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_SELECT_VOLS_METADATA = Metadata(
    id="423b3bdef1ce58c3541799a5887c14712d5adc04.boutiques",
    name="fat_proc_select_vols",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatProcSelectVolsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_select_vols(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_selector_string: OutputPathType
    """Text file with AFNI-usable selector string"""


def fat_proc_select_vols(
    dwi_input: InputPathType,
    img_input: InputPathType,
    prefix: str,
    in_bads: InputPathType | None = None,
    apply_to_vols: bool = False,
    do_movie: str | None = None,
    workdir: str | None = None,
    no_cmd_out: bool = False,
    runner: Runner | None = None,
) -> FatProcSelectVolsOutputs:
    """
    Tool for building a selector string for AFNI subbricks and/or 1D text files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dwi_input: Input DWI dataset.
        img_input: 2D image of the DWI dataset.
        prefix: Output prefix for files.
        in_bads: A single column file of integers representing bad volumes\
            indices (optional).
        apply_to_vols: Apply the created selection of good volumes to the DWI\
            dataset.
        do_movie: Output a movie of the newly created dataset. Only 'AGIF' or\
            'MPEG' arguments can be used.
        workdir: Specify a working directory.
        no_cmd_out: Don't save the command line call of this program and the\
            location where it was run.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcSelectVolsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_SELECT_VOLS_METADATA)
    cargs = []
    cargs.append("fat_proc_select_vols")
    cargs.append("-in_dwi")
    cargs.append(execution.input_file(dwi_input))
    cargs.append("-in_img")
    cargs.append(execution.input_file(img_input))
    cargs.append("-prefix")
    cargs.append(prefix)
    if in_bads is not None:
        cargs.extend([
            "-in_bads",
            execution.input_file(in_bads)
        ])
    if apply_to_vols:
        cargs.append("-apply_to_vols")
    if do_movie is not None:
        cargs.extend([
            "-do_movie",
            do_movie
        ])
    if workdir is not None:
        cargs.extend([
            "-workdir",
            workdir
        ])
    if no_cmd_out:
        cargs.append("-no_cmd_out")
    ret = FatProcSelectVolsOutputs(
        root=execution.output_file("."),
        output_selector_string=execution.output_file(prefix + "_bads.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_SELECT_VOLS_METADATA",
    "FatProcSelectVolsOutputs",
    "fat_proc_select_vols",
]

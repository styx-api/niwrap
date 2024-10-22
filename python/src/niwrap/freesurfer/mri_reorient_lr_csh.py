# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_REORIENT_LR_CSH_METADATA = Metadata(
    id="6dc1cf350d86e1160d050d18263e1c18fc0d89b6.boutiques",
    name="mri_reorient_LR.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriReorientLrCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_reorient_lr_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reoriented_vol: OutputPathType
    """Reoriented volume"""


def mri_reorient_lr_csh(
    input_vol: InputPathType,
    output_vol: str,
    display_result: bool = False,
    clean_files: bool = False,
    output_registration: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriReorientLrCshOutputs:
    """
    A script to reorient MRI volumes from left-right orientation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input file to be reoriented.
        output_vol: Reoriented input file.
        display_result: Display registration result using FreeView.
        clean_files: Delete all auxiliary and registration files.
        output_registration: Write out the registration file that is applied to\
            the reoriented input file (fslmat or lta).
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriReorientLrCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_REORIENT_LR_CSH_METADATA)
    cargs = []
    cargs.append("mri_reorient_LR")
    cargs.extend([
        "--i",
        execution.input_file(input_vol)
    ])
    cargs.extend([
        "--o",
        output_vol
    ])
    if display_result:
        cargs.append("--disp")
    if clean_files:
        cargs.append("--clean")
    if output_registration:
        cargs.append("--outreg")
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = MriReorientLrCshOutputs(
        root=execution.output_file("."),
        reoriented_vol=execution.output_file(output_vol),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_REORIENT_LR_CSH_METADATA",
    "MriReorientLrCshOutputs",
    "mri_reorient_lr_csh",
]

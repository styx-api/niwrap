# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_NU_CORRECT_MNI_METADATA = Metadata(
    id="cd9d0cddf25451a50015bcc15a19587583722482.boutiques",
    name="mri_nu_correct.mni",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriNuCorrectMniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_nu_correct_mni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_output: OutputPathType
    """Corrected output volume."""


def mri_nu_correct_mni(
    input_volume: InputPathType,
    output_volume: str,
    iterations: float,
    proto_iterations: float | None = None,
    mask_volume: InputPathType | None = None,
    stop_threshold: float | None = None,
    uchar_transform: InputPathType | None = None,
    ants_n3: bool = False,
    ants_n4: bool = False,
    no_uchar: bool = False,
    ants_n4_replace_zeros: bool = False,
    cm_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MriNuCorrectMniOutputs:
    """
    Wrapper for nu_correct, used for correcting intensity non-uniformity (bias
    fields).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume. Can be any format accepted by mri_convert.
        output_volume: Output volume. Can be any format accepted by\
            mri_convert.
        iterations: Number of iterations to run nu_correct. Default is 4.
        proto_iterations: Passes as argument of the -iterations flag of\
            nu_correct.
        mask_volume: Brainmask volume. Can be any format accepted by\
            mri_convert.
        stop_threshold: Threshold for stopping iteration. Suggest values\
            between 0.01 to 0.0001.
        uchar_transform: Use mri_make_uchar instead of conforming.
        ants_n3: Run N3 using ANTS N3BiasFieldCorrection.
        ants_n4: Run N4 using ANTS N4BiasFieldCorrection.
        no_uchar: Do not use mri_make_uchar (default).
        ants_n4_replace_zeros: Replace 0s with small random numbers then remove\
            after nu correction.
        cm_flag: For use with data that is higher than 1mm resolution.
        debug_flag: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNuCorrectMniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NU_CORRECT_MNI_METADATA)
    cargs = []
    cargs.append("mri_nu_correct.mni")
    cargs.extend([
        "--i",
        execution.input_file(input_volume)
    ])
    cargs.extend([
        "--o",
        output_volume
    ])
    cargs.extend([
        "--n",
        str(iterations)
    ])
    if proto_iterations is not None:
        cargs.extend([
            "--proto-iters",
            str(proto_iterations)
        ])
    if mask_volume is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_volume)
        ])
    if stop_threshold is not None:
        cargs.extend([
            "--stop",
            str(stop_threshold)
        ])
    if uchar_transform is not None:
        cargs.extend([
            "--uchar",
            execution.input_file(uchar_transform)
        ])
    if ants_n3:
        cargs.append("--ants-n3")
    if ants_n4:
        cargs.append("--ants-n4")
    if no_uchar:
        cargs.append("--no-uchar")
    if ants_n4_replace_zeros:
        cargs.append("--ants-n4-replace-zeros")
    if cm_flag:
        cargs.append("--cm")
    if debug_flag:
        cargs.append("--debug")
    ret = MriNuCorrectMniOutputs(
        root=execution.output_file("."),
        corrected_output=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_NU_CORRECT_MNI_METADATA",
    "MriNuCorrectMniOutputs",
    "mri_nu_correct_mni",
]

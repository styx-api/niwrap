# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TALAIRACH_AFD_METADATA = Metadata(
    id="72ffaa549b1639dc1447b786e9294b5cadced79c.boutiques",
    name="talairach_afd",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TalairachAfdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `talairach_afd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def talairach_afd(
    subject_name: str | None = None,
    xfm_file: InputPathType | None = None,
    p_value_threshold: float | None = 0.01,
    afd_directory: str | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> TalairachAfdOutputs:
    """
    Detects Talairach alignment failures.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Specify subject's name.
        xfm_file: Specify the talairach.xfm file to check.
        p_value_threshold: Threshold the p-values at #; Talairach transforms\
            for subjects with p-values <= T are considered as very unlikely.
        afd_directory: Specify directory containing .afd data files.
        verbose: Enable verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalairachAfdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALAIRACH_AFD_METADATA)
    cargs = []
    cargs.append("talairach_afd")
    if subject_name is not None:
        cargs.extend([
            "-subj",
            subject_name
        ])
    if xfm_file is not None:
        cargs.extend([
            "-xfm",
            execution.input_file(xfm_file)
        ])
    if p_value_threshold is not None:
        cargs.extend([
            "-T",
            str(p_value_threshold)
        ])
    if afd_directory is not None:
        cargs.extend([
            "-afd",
            afd_directory
        ])
    if verbose:
        cargs.append("-V")
    ret = TalairachAfdOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TALAIRACH_AFD_METADATA",
    "TalairachAfdOutputs",
    "talairach_afd",
]

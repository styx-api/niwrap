# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APARC2FEAT_METADATA = Metadata(
    id="40a686bfd13826d8c5472e46b643ff5ee20464a4.boutiques",
    name="aparc2feat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Aparc2featOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aparc2feat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_aparc_output: OutputPathType
    """Output Left Hemisphere aparc in nifti format."""
    rh_aparc_output: OutputPathType
    """Output Right Hemisphere aparc in nifti format."""


def aparc2feat(
    feat_directories: str,
    featdirfile: InputPathType | None = None,
    hemi: str | None = None,
    annot: str | None = None,
    annot_a2005s_flag: bool = False,
    annot_a2009s_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> Aparc2featOutputs:
    """
    Resamples the FreeSurfer automatic cortical segmentation to the FEAT functional
    space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_directories: FEAT output directory. Multiple --feat arguments can\
            be supplied.
        featdirfile: File with a list of FEAT directories. Multiple\
            --featdirfile flags are allowed.
        hemi: Resample hemisphere only (default is both rh and lh).
        annot: Specify something other than aparc.
        annot_a2005s_flag: Specify annotation = aparc.a2005s.
        annot_a2009s_flag: Specify annotation = aparc.a2009s.
        debug_flag: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Aparc2featOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APARC2FEAT_METADATA)
    cargs = []
    cargs.append("aparc2feat")
    cargs.extend([
        "--feat",
        feat_directories
    ])
    if featdirfile is not None:
        cargs.extend([
            "--featdirfile",
            execution.input_file(featdirfile)
        ])
    if hemi is not None:
        cargs.extend([
            "--hemi",
            hemi
        ])
    if annot is not None:
        cargs.extend([
            "--annot",
            annot
        ])
    if annot_a2005s_flag:
        cargs.append("--a2005s")
    if annot_a2009s_flag:
        cargs.append("--a2009s")
    if debug_flag:
        cargs.append("--debug")
    ret = Aparc2featOutputs(
        root=execution.output_file("."),
        lh_aparc_output=execution.output_file(feat_directories + "/reg/freesurfer/lh.aparc.nii.gz"),
        rh_aparc_output=execution.output_file(feat_directories + "/reg/freesurfer/rh.aparc.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APARC2FEAT_METADATA",
    "Aparc2featOutputs",
    "aparc2feat",
]

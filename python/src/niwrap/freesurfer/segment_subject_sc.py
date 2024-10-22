# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBJECT_SC_METADATA = Metadata(
    id="a2763ec226e679f84ec01530f1c0e3bad1495f0d.boutiques",
    name="segment_subject_sc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SegmentSubjectScOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_sc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_xfm_file: OutputPathType
    """Output transform file (xfm)"""


def segment_subject_sc(
    invol: InputPathType,
    outxfm: InputPathType,
    log: str | None = "outdir/talarach.log",
    debug: bool = False,
    runner: Runner | None = None,
) -> SegmentSubjectScOutputs:
    """
    Front-end for MINC's mritotal. Computes the Talairach transform for mapping the
    input volume to the MNI305 space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        invol: Input volume.
        outxfm: Output xfm file.
        log: Log file. Default is outdir/talarach.log.
        debug: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectScOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_SC_METADATA)
    cargs = []
    cargs.append("mri_nu_correct.mni")
    cargs.append("--i")
    cargs.append(execution.input_file(invol))
    cargs.append("--xfm")
    cargs.append(execution.input_file(outxfm))
    if log is not None:
        cargs.extend([
            "--log",
            log
        ])
    if debug:
        cargs.append("--debug")
    ret = SegmentSubjectScOutputs(
        root=execution.output_file("."),
        output_xfm_file=execution.output_file(pathlib.Path(outxfm).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEGMENT_SUBJECT_SC_METADATA",
    "SegmentSubjectScOutputs",
    "segment_subject_sc",
]

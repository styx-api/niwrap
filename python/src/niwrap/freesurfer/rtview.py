# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RTVIEW_METADATA = Metadata(
    id="bbfc6a7778d4c734c212389406f89e8b0c6cbe09.boutiques",
    name="rtview",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RtviewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rtview(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rtview(
    subject: str | None = None,
    right_hemi: bool = False,
    polar: bool = False,
    real_file: InputPathType | None = None,
    imag_file: InputPathType | None = None,
    fsig_file: InputPathType | None = None,
    reg_file: InputPathType | None = None,
    flat_display: bool = False,
    patch: str | None = None,
    tcl_file: InputPathType | None = None,
    no_cleanup: bool = False,
    runner: Runner | None = None,
) -> RtviewOutputs:
    """
    View FSFAST version 5 retinotopy data using the color wheel. This is a front-end
    for tksurfer, setting up the environment for using the color wheel.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject to use as display.
        right_hemi: Display right hemisphere.
        polar: Display polar data.
        real_file: File containing real (cosine) values.
        imag_file: File containing imaginary (sine) values.
        fsig_file: File containing significance values.
        reg_file: Registration file for when real/imag/fsig are volumes.
        flat_display: Display on occip.patch.flat.
        patch: Display on specified patchname.
        tcl_file: Use your own TCL command file.
        no_cleanup: Don't delete temporary directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RtviewOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RTVIEW_METADATA)
    cargs = []
    cargs.append("rtview")
    if subject is not None:
        cargs.extend([
            "--s",
            subject
        ])
    if right_hemi:
        cargs.append("--rh")
    if polar:
        cargs.append("--polar")
    if real_file is not None:
        cargs.extend([
            "--real",
            execution.input_file(real_file)
        ])
    if imag_file is not None:
        cargs.extend([
            "--imag",
            execution.input_file(imag_file)
        ])
    if fsig_file is not None:
        cargs.extend([
            "--fsig",
            execution.input_file(fsig_file)
        ])
    if reg_file is not None:
        cargs.extend([
            "--reg",
            execution.input_file(reg_file)
        ])
    if flat_display:
        cargs.append("--flat")
    if patch is not None:
        cargs.extend([
            "--patch",
            patch
        ])
    if tcl_file is not None:
        cargs.extend([
            "--tcl",
            execution.input_file(tcl_file)
        ])
    if no_cleanup:
        cargs.append("--no-cleanup")
    ret = RtviewOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RTVIEW_METADATA",
    "RtviewOutputs",
    "rtview",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SPMREGISTER_METADATA = Metadata(
    id="48c39df6adb290bff10bc7c09ab9ffe94274c400.boutiques",
    name="spmregister",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SpmregisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spmregister(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registration_file: OutputPathType
    """Output registration file."""
    resampled_mov: OutputPathType | None
    """Resampled mov volume."""


def spmregister(
    subjid: str,
    mov: str,
    reg: str,
    frame: float | None = None,
    mid_frame: bool = False,
    template_out: str | None = None,
    fsvol: str | None = None,
    force_ras: bool = False,
    outvol: str | None = None,
    tmpdir: str | None = None,
    nocleanup: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> SpmregisterOutputs:
    """
    Registers a volume to its FreeSurfer anatomical using SPM's spm_coreg.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjid: Id of the subject as found in SUBJECTS_DIR. This is converted\
            to analyze using mri_convert.
        mov: Volume identifier of the movable volume. Must be specified in a\
            way suitable for mri_convert.
        reg: Output registration file. Maps RAS in the reference to RAS in the\
            movable.
        frame: Use something other than the first frame. Specify the frame\
            number you want.
        mid_frame: Use the middle frame of the mov volume as the template.
        template_out: Save the mov template when template is something other\
            than the first frame.
        fsvol: Use FreeSurfer volid (default brainmask).
        force_ras: Force input geometry to be RAS.
        outvol: Resample mov and save as outvol.
        tmpdir: Temporary directory (implies --nocleanup).
        nocleanup: Do not delete temporary files.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpmregisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPMREGISTER_METADATA)
    cargs = []
    cargs.append("spmregister")
    cargs.extend([
        "--s",
        subjid
    ])
    cargs.extend([
        "--mov",
        mov
    ])
    cargs.extend([
        "--reg",
        reg
    ])
    if frame is not None:
        cargs.extend([
            "--frame",
            str(frame)
        ])
    if mid_frame:
        cargs.append("--mid-frame")
    if template_out is not None:
        cargs.extend([
            "--template-out",
            template_out
        ])
    if fsvol is not None:
        cargs.extend([
            "--fsvol",
            fsvol
        ])
    if force_ras:
        cargs.append("--force-ras")
    if outvol is not None:
        cargs.extend([
            "--o",
            outvol
        ])
    if tmpdir is not None:
        cargs.extend([
            "--tmp",
            tmpdir
        ])
    if nocleanup:
        cargs.append("--nocleanup")
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = SpmregisterOutputs(
        root=execution.output_file("."),
        registration_file=execution.output_file("register.dat"),
        resampled_mov=execution.output_file(outvol) if (outvol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SPMREGISTER_METADATA",
    "SpmregisterOutputs",
    "spmregister",
]

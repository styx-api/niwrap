# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SPH2SURF_METADATA = Metadata(
    id="527b07854c2c693db94b586724ac645153390f46.boutiques",
    name="mri-sph2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSph2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_sph2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output surface data file in the form outstem-lh.w (or rh)."""


def mri_sph2surf(
    instem: str,
    outstem: str,
    hemi: str,
    subject: str,
    offset: float | None = 0,
    svitdir: str | None = "/usr/local/freesurfer/subjects/subject/svit",
    umask: str | None = None,
    verbose: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriSph2surfOutputs:
    """
    Converts spherical functional data to surface data in the FreeSurfer processing
    pipeline.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        instem: Input stem of a bfloat file. The full input file name must take\
            the form instem-lh_000.bfloat (or rh).
        outstem: Output stem for the resulting file. The output file will have\
            the name outstem-lh.w (or rh).
        hemi: Specifies the hemisphere for processing. Acceptable values are\
            'lh' or 'rh'.
        subject: Specifies the subject identifier for the FreeSurfer processing\
            pipeline.
        offset: Zero-based plane/frame number. Default is 0.
        svitdir: Directory for svit. Default is\
            '/usr/local/freesurfer/subjects/subject/svit'.
        umask: Specifies a new user mask.
        verbose: Enable verbose output.
        version: Show version information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSph2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SPH2SURF_METADATA)
    cargs = []
    cargs.append("mri-sph2surf")
    cargs.extend([
        "-i",
        instem
    ])
    cargs.extend([
        "-o",
        outstem
    ])
    cargs.extend([
        "-hemi",
        hemi
    ])
    cargs.extend([
        "-s",
        subject
    ])
    if offset is not None:
        cargs.extend([
            "-offset",
            str(offset)
        ])
    if svitdir is not None:
        cargs.extend([
            "-svitdir",
            svitdir
        ])
    if umask is not None:
        cargs.extend([
            "-umask",
            umask
        ])
    if verbose:
        cargs.append("-verbose")
    if version:
        cargs.append("-version")
    ret = MriSph2surfOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[OUTPUT_STEM]-" + hemi + ".w"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SPH2SURF_METADATA",
    "MriSph2surfOutputs",
    "mri_sph2surf",
]

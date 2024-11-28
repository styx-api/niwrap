# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VOLDIFF_METADATA = Metadata(
    id="ffbb97583e5b1d5df187fa9f9126f53cb96614c1.boutiques",
    name="mri_voldiff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriVoldiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_voldiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_voldiff(
    volume1: InputPathType,
    volume2: InputPathType,
    vox2ras_thresh: float | None = None,
    pix_thresh: float | None = None,
    allow_precision: bool = False,
    allow_resolution: bool = False,
    allow_vox2ras: bool = False,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriVoldiffOutputs:
    """
    Determines whether two volumes are different in terms of pixel data, dimension,
    precision, resolution, or geometry.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume1: First input volume.
        volume2: Second input volume.
        vox2ras_thresh: Vox2RAS threshold value.
        pix_thresh: Pixel threshold value.
        allow_precision: Allow differences in precision.
        allow_resolution: Allow differences in resolution.
        allow_vox2ras: Allow differences in Vox2RAS.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVoldiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOLDIFF_METADATA)
    cargs = []
    cargs.append("mri_voldiff")
    cargs.extend([
        "-v1",
        "-" + execution.input_file(volume1)
    ])
    cargs.extend([
        "-v2",
        "-" + execution.input_file(volume2)
    ])
    if vox2ras_thresh is not None:
        cargs.extend([
            "--vox2ras",
            str(vox2ras_thresh)
        ])
    if pix_thresh is not None:
        cargs.extend([
            "--pix",
            str(pix_thresh)
        ])
    if allow_precision:
        cargs.append("--allow-prec")
    if allow_resolution:
        cargs.append("--allow-res")
    if allow_vox2ras:
        cargs.append("--allow-vox2ras")
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    ret = MriVoldiffOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_VOLDIFF_METADATA",
    "MriVoldiffOutputs",
    "mri_voldiff",
]

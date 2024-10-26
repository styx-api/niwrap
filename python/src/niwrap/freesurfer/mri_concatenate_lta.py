# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CONCATENATE_LTA_METADATA = Metadata(
    id="6bdd2d8b898ad18cca59fea91e0bc86baf92c633.boutiques",
    name="mri_concatenate_lta",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriConcatenateLtaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_concatenate_lta(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_concatenate_lta(
    lta_1: InputPathType,
    lta_2: InputPathType,
    lta_final: str,
    tal_src: InputPathType | None = None,
    tal_template: InputPathType | None = None,
    invert1: bool = False,
    invert2: bool = False,
    invertout: bool = False,
    out_type: float | None = None,
    subject: str | None = None,
    rmsdiff_radius: float | None = None,
    rmsdiff_outputfile: str | None = None,
    runner: Runner | None = None,
) -> MriConcatenateLtaOutputs:
    """
    Concatenates two consecutive LTA transformations into one overall
    transformation, Out = LTA2*LTA1.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        lta_1: File for LTA transformation that maps some src1 to dst1.
        lta_2: File for LTA transformation that maps dst1 (src2) to dst2.
        lta_final: File for the combined LTA maps: src1 to dst2 = LTA2*LTA1.
        tal_src: Specify source (file1) for Talairach transformation.
        tal_template: Specify template (file2) for Talairach transformation.
        invert1: Invert LTA1 before applying it.
        invert2: Invert LTA2 before applying it.
        invertout: Invert output LTA.
        out_type: Set final LTA type: 0 for VOX2VOX (default), 1 for RAS2RAS.
        subject: Set subject in output LTA.
        rmsdiff_radius: Radius used for computing RMS diff between transforms.
        rmsdiff_outputfile: Output file for RMS diff computation. Use 'nofile'\
            to skip output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConcatenateLtaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONCATENATE_LTA_METADATA)
    cargs = []
    cargs.append("mri_concatenate_lta")
    cargs.append(execution.input_file(lta_1))
    cargs.append(execution.input_file(lta_2))
    cargs.append(lta_final)
    if tal_src is not None:
        cargs.extend([
            "-tal",
            execution.input_file(tal_src)
        ])
    if tal_template is not None:
        cargs.append(execution.input_file(tal_template))
    if invert1:
        cargs.append("-invert1")
    if invert2:
        cargs.append("-invert2")
    if invertout:
        cargs.append("-invertout")
    if out_type is not None:
        cargs.extend([
            "-out_type",
            str(out_type)
        ])
    if subject is not None:
        cargs.extend([
            "-subject",
            subject
        ])
    if rmsdiff_radius is not None:
        cargs.extend([
            "-rmsdiff",
            str(rmsdiff_radius)
        ])
    if rmsdiff_outputfile is not None:
        cargs.append(rmsdiff_outputfile)
    ret = MriConcatenateLtaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CONCATENATE_LTA_METADATA",
    "MriConcatenateLtaOutputs",
    "mri_concatenate_lta",
]

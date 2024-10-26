# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLFFT_METADATA = Metadata(
    id="0c7496964edeca751d97ecb126121bfa61f6295b.boutiques",
    name="fslfft",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslfftOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslfft(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output volume result of the Fourier transform"""


def fslfft(
    input_volume: InputPathType,
    output_volume: InputPathType,
    inverse_flag: bool = False,
    runner: Runner | None = None,
) -> FslfftOutputs:
    """
    A tool to compute the Fourier transform of an input volume and save the result
    in an output volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_volume: Input volume file (e.g. invol.nii.gz).
        output_volume: Output volume file (e.g. outvol.nii.gz).
        inverse_flag: Flag to perform the inverse Fourier transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslfftOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLFFT_METADATA)
    cargs = []
    cargs.append("fslfft")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(output_volume))
    if inverse_flag:
        cargs.append("-inv")
    ret = FslfftOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(output_volume).name + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLFFT_METADATA",
    "FslfftOutputs",
    "fslfft",
]

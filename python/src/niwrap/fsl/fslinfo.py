# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLINFO_METADATA = Metadata(
    id="58cca8fed848f7c3b19f49f10179561bb2d86040.boutiques",
    name="fslinfo",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslinfo(
    filename: InputPathType,
    runner: Runner | None = None,
) -> FslinfoOutputs:
    """
    Display information about NIFTI-1 image file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filename: Input NIFTI-1 image file (e.g. img.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLINFO_METADATA)
    cargs = []
    cargs.append("fslinfo")
    cargs.append(execution.input_file(filename))
    ret = FslinfoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLINFO_METADATA",
    "FslinfoOutputs",
    "fslinfo",
]

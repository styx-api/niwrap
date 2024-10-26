# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_ORIENT_SIGN_METADATA = Metadata(
    id="e1bbba0e6f37200e4ecc08d0b497112ae8daf6df.boutiques",
    name="@AfniOrientSign",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VAfniOrientSignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_orient_sign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the orientation signs of the dataset"""


def v__afni_orient_sign(
    infile: InputPathType,
    runner: Runner | None = None,
) -> VAfniOrientSignOutputs:
    """
    A tool within the AFNI suite to determine the orientation signs of datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input image file to determine orientation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniOrientSignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_ORIENT_SIGN_METADATA)
    cargs = []
    cargs.append("@AfniOrientSign")
    cargs.append("-orient")
    cargs.append(execution.input_file(infile))
    ret = VAfniOrientSignOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(pathlib.Path(infile).name + "_orient.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAfniOrientSignOutputs",
    "V__AFNI_ORIENT_SIGN_METADATA",
    "v__afni_orient_sign",
]

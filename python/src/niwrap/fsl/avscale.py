# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AVSCALE_METADATA = Metadata(
    id="b4cf2ddb954800b4fff52e3094c8131c12e16602.boutiques",
    name="avscale",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class AvscaleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `avscale(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output file."""


def avscale(
    matrix_file: InputPathType,
    allparams_flag: bool = False,
    inverteddies_flag: bool = False,
    non_reference_volume: InputPathType | None = None,
    runner: Runner | None = None,
) -> AvscaleOutputs:
    """
    A command line tool for computing affine transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        matrix_file: The path to the matrix file.
        allparams_flag: Flag for all parameters.
        inverteddies_flag: Flag for inverted eddies.
        non_reference_volume: The path to the non-reference volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AvscaleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AVSCALE_METADATA)
    cargs = []
    cargs.append("avscale")
    if allparams_flag:
        cargs.append("--allparams")
    if inverteddies_flag:
        cargs.append("--inverteddies")
    cargs.append(execution.input_file(matrix_file))
    if non_reference_volume is not None:
        cargs.append(execution.input_file(non_reference_volume))
    cargs.append(">")
    cargs.append("output.txt")
    ret = AvscaleOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AVSCALE_METADATA",
    "AvscaleOutputs",
    "avscale",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_TRANSFORM_FILE_METADATA = Metadata(
    id="224c137774aff43d94d1fecb5c8b4a19ae81816c.boutiques",
    name="ConvertTransformFile",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class ConvertTransformFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_transform_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def convert_transform_file(
    dimensions: int,
    input_transform_file: InputPathType,
    output_transform_file: str,
    runner: Runner | None = None,
) -> ConvertTransformFileOutputs:
    """
    Utility to read in a transform file (presumed to be in binary format) and output
    it in various formats. Default output is legacy human-readable text format.
    Without any options, the output filename extension must be .txt or .tfm to
    signify a text-formatted transform file.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimensions: Dimensionality of the transform file.
        input_transform_file: Path to the input transform file.
        output_transform_file: Path for the output transform file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertTransformFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_TRANSFORM_FILE_METADATA)
    cargs = []
    cargs.append("ConvertTransformFile")
    cargs.append(str(dimensions))
    cargs.append(execution.input_file(input_transform_file))
    cargs.append(output_transform_file)
    cargs.append("[OPTIONS]")
    ret = ConvertTransformFileOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_TRANSFORM_FILE_METADATA",
    "ConvertTransformFileOutputs",
    "convert_transform_file",
]

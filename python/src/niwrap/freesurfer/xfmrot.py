# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

XFMROT_METADATA = Metadata(
    id="e68f95765471172c3f4d5eecbc6fc6f118b60ba7.boutiques",
    name="xfmrot",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class XfmrotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xfmrot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_vector: OutputPathType | None
    """The transformed output vector file with the same format as input."""


def xfmrot(
    transform_file: InputPathType,
    input_vector_file: InputPathType,
    output_vector_file: str | None = None,
    runner: Runner | None = None,
) -> XfmrotOutputs:
    """
    Tool to apply a transformation defined in a transform file to an input vector
    file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        transform_file: Transform file, can be an eddy_correct/eddy log file or\
            a .mat file.
        input_vector_file: Input vector file which can be formatted in 3 rows\
            or 3 columns.
        output_vector_file: Output vector file will have the same format as\
            input.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XfmrotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XFMROT_METADATA)
    cargs = []
    cargs.append("xfmrot")
    cargs.append(execution.input_file(transform_file))
    cargs.append(execution.input_file(input_vector_file))
    if output_vector_file is not None:
        cargs.append(output_vector_file)
    ret = XfmrotOutputs(
        root=execution.output_file("."),
        transformed_vector=execution.output_file(output_vector_file) if (output_vector_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XFMROT_METADATA",
    "XfmrotOutputs",
    "xfmrot",
]

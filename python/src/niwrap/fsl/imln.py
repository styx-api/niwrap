# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMLN_METADATA = Metadata(
    id="a4704c5816c7753dcb74f87bd33f7b0717677a74.boutiques",
    name="imln",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class ImlnOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imln(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_link: OutputPathType
    """The created link to the input file"""


def imln(
    input_file: InputPathType,
    link_name: str,
    runner: Runner | None = None,
) -> ImlnOutputs:
    """
    Creates a link (called file2) to file1.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: The source file (file1) to create a link to.
        link_name: The name for the link (file2).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImlnOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMLN_METADATA)
    cargs = []
    cargs.append("imln")
    cargs.append(execution.input_file(input_file))
    cargs.append(link_name)
    ret = ImlnOutputs(
        root=execution.output_file("."),
        output_link=execution.output_file(link_name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMLN_METADATA",
    "ImlnOutputs",
    "imln",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

COLUMN_CAT_METADATA = Metadata(
    id="22f92393a4504948631931c183a528c1437f87dc.boutiques",
    name="column_cat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ColumnCatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `column_cat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Redirect output of concatenation to a file"""


def column_cat(
    input_files: list[InputPathType],
    line_number: float | None = None,
    separator_string: str | None = None,
    runner: Runner | None = None,
) -> ColumnCatOutputs:
    """
    Catenate files horizontally. Each line of output is the concatenation of each
    current line from the input files, all on the same line, separated by a space or
    a user-defined separator.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input files to be concatenated.
        line_number: Print only the specified line number (1-based).
        separator_string: Use the specified string as a separator between\
            columns.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ColumnCatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COLUMN_CAT_METADATA)
    cargs = []
    cargs.append("column_cat")
    if line_number is not None:
        cargs.extend([
            "-line",
            str(line_number)
        ])
    if separator_string is not None:
        cargs.extend([
            "-sep",
            separator_string
        ])
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = ColumnCatOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output_file.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "COLUMN_CAT_METADATA",
    "ColumnCatOutputs",
    "column_cat",
]

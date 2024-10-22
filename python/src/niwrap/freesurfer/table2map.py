# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TABLE2MAP_METADATA = Metadata(
    id="0d6ae0c89d189ffeba6b927be0f918cdb263bd3c.boutiques",
    name="table2map",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Table2mapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `table2map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def table2map(
    input_table: InputPathType,
    output_map: str,
    segmentation: InputPathType | None = None,
    parcellation: InputPathType | None = None,
    columns: list[str] | None = None,
    lookup_table: InputPathType | None = None,
    runner: Runner | None = None,
) -> Table2mapOutputs:
    """
    A tool to map data from a table onto an output map, optionally using
    segmentation or parcellation files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_table: Input table.
        output_map: Output map.
        segmentation: Segmentation to map to.
        parcellation: Parcellation to map to.
        columns: Table columns to map. All are included by default.
        lookup_table: Alternative lookup table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Table2mapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TABLE2MAP_METADATA)
    cargs = []
    cargs.append("table2map")
    cargs.extend([
        "-t",
        execution.input_file(input_table)
    ])
    cargs.extend([
        "-o",
        output_map
    ])
    if segmentation is not None:
        cargs.extend([
            "-s",
            execution.input_file(segmentation)
        ])
    if parcellation is not None:
        cargs.extend([
            "-p",
            execution.input_file(parcellation)
        ])
    if columns is not None:
        cargs.extend([
            "-c",
            *columns
        ])
    if lookup_table is not None:
        cargs.extend([
            "-l",
            execution.input_file(lookup_table)
        ])
    ret = Table2mapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TABLE2MAP_METADATA",
    "Table2mapOutputs",
    "table2map",
]

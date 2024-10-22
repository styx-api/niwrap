# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

QUANTIFY_HASUBREGIONS_SH_METADATA = Metadata(
    id="f13142174113b626afcd17c7d932b4aef8a28755.boutiques",
    name="quantifyHAsubregions.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class QuantifyHasubregionsShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quantify_hasubregions_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """File containing the quantification results of hippocampal subregions."""


def quantify_hasubregions_sh(
    prefix: str,
    suffix: str,
    output_file: str,
    subjects_directory: str | None = None,
    runner: Runner | None = None,
) -> QuantifyHasubregionsShOutputs:
    """
    Tool to quantify hippocampal subregions using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        prefix: Prefix for the files to be processed.
        suffix: Suffix for the files to be processed.
        output_file: Output file name to store the results.
        subjects_directory: Directory containing the subject data. If not\
            provided, the current directory is used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuantifyHasubregionsShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUANTIFY_HASUBREGIONS_SH_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/quantifyHAsubregions.sh")
    cargs.append(prefix)
    cargs.append(suffix)
    cargs.append(output_file)
    if subjects_directory is not None:
        cargs.append(subjects_directory)
    ret = QuantifyHasubregionsShOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QUANTIFY_HASUBREGIONS_SH_METADATA",
    "QuantifyHasubregionsShOutputs",
    "quantify_hasubregions_sh",
]

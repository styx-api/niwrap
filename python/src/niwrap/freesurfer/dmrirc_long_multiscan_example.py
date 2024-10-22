# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRIRC_LONG_MULTISCAN_EXAMPLE_METADATA = Metadata(
    id="27e8e8126ade948919f10de74a69b6d6ae7bde56.boutiques",
    name="dmrirc.long.multiscan.example",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmrircLongMultiscanExampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmrirc_long_multiscan_example(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated by the script, location not specified due to
    script errors."""


def dmrirc_long_multiscan_example(
    subject_list: list[str],
    other_options: str | None = None,
    runner: Runner | None = None,
) -> DmrircLongMultiscanExampleOutputs:
    """
    A multi-scan example script for DMRIRC in longitudinal analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_list: List of subjects for the multiscan analysis. Each subject\
            is separated by a space.
        other_options: Other options for the analysis, as available in the\
            script. These options are unknown due to the script errors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmrircLongMultiscanExampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRIRC_LONG_MULTISCAN_EXAMPLE_METADATA)
    cargs = []
    cargs.append("dmrirc.long.multiscan.example")
    cargs.extend(subject_list)
    if other_options is not None:
        cargs.append(other_options)
    ret = DmrircLongMultiscanExampleOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file("output_dir/{output_file}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRIRC_LONG_MULTISCAN_EXAMPLE_METADATA",
    "DmrircLongMultiscanExampleOutputs",
    "dmrirc_long_multiscan_example",
]

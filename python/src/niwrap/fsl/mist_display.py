# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MIST_DISPLAY_METADATA = Metadata(
    id="15f76552733813373c102cfdca7d604be3b835da.boutiques",
    name="mist_display",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class MistDisplayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mist_display(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mist_display(
    mode: typing.Literal["simple", "pvals", "noscalars"],
    help_: bool = False,
    runner: Runner | None = None,
) -> MistDisplayOutputs:
    """
    Tool to show scalars on mesh.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        mode: Mode for displaying scalars on mesh.
        help_: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MistDisplayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MIST_DISPLAY_METADATA)
    cargs = []
    cargs.append("mist_display")
    cargs.append(mode)
    if help_:
        cargs.append("--help")
    ret = MistDisplayOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MIST_DISPLAY_METADATA",
    "MistDisplayOutputs",
    "mist_display",
]

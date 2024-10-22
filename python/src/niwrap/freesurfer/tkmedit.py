# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TKMEDIT_METADATA = Metadata(
    id="2639ebbb939f13f81bdbee37ec8b0efdfcd62789.boutiques",
    name="tkmedit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TkmeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tkmedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tkmedit(
    input_volume: InputPathType,
    options: str | None = None,
    runner: Runner | None = None,
) -> TkmeditOutputs:
    """
    tkmedit is a multi-functional imaging tool for viewing and editing surface
    models and volumes in FreeSurfer. It provides a GUI representation of volumetric
    data and facilitates modifications in the data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file (e.g., nu.mgz or brain.mgz).
        options: Options for running tkmedit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TkmeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKMEDIT_METADATA)
    cargs = []
    cargs.append("tkmedit")
    cargs.append(execution.input_file(input_volume))
    if options is not None:
        cargs.append(options)
    ret = TkmeditOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TKMEDIT_METADATA",
    "TkmeditOutputs",
    "tkmedit",
]

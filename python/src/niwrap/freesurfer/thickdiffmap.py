# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

THICKDIFFMAP_METADATA = Metadata(
    id="386d35dd120f181e0cd722b783b2ab7dab134ec4.boutiques",
    name="thickdiffmap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ThickdiffmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `thickdiffmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def thickdiffmap(
    subjscan1: InputPathType,
    subjscan2: InputPathType,
    commonsubj: str,
    hemi: str,
    steps: list[str] | None = None,
    runner: Runner | None = None,
) -> ThickdiffmapOutputs:
    """
    Compute and analyze cortical thickness difference maps.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjscan1: First scan of a subject.
        subjscan2: Second (later) scan of the same subject.
        commonsubj: Subject to use as the common template.
        hemi: Hemisphere to process.
        steps: Stages of processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ThickdiffmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(THICKDIFFMAP_METADATA)
    cargs = []
    cargs.append("thickdiffmap")
    cargs.append(execution.input_file(subjscan1))
    cargs.append(execution.input_file(subjscan2))
    cargs.append(commonsubj)
    cargs.append(hemi)
    if steps is not None:
        cargs.extend(steps)
    ret = ThickdiffmapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "THICKDIFFMAP_METADATA",
    "ThickdiffmapOutputs",
    "thickdiffmap",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_BA_SEGMENT_METADATA = Metadata(
    id="b3ec206494aa6dee2d2521daa7c2af2397b82e98.boutiques",
    name="mris_BA_segment",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisBaSegmentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_ba_segment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Output label file"""


def mris_ba_segment(
    surface: InputPathType,
    profiles: InputPathType,
    prior_label: InputPathType,
    output_label: str,
    runner: Runner | None = None,
) -> MrisBaSegmentOutputs:
    """
    Segments a Brodmann area (MT currently) from a laminar intensity profile
    overlay.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface file.
        profiles: Input profiles file.
        prior_label: Input prior label file.
        output_label: Output label file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisBaSegmentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_BA_SEGMENT_METADATA)
    cargs = []
    cargs.append("mris_BA_segment")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(profiles))
    cargs.append(execution.input_file(prior_label))
    cargs.append(output_label)
    ret = MrisBaSegmentOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(output_label),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_BA_SEGMENT_METADATA",
    "MrisBaSegmentOutputs",
    "mris_ba_segment",
]

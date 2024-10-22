# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_MARK_TEMPORAL_LOBE_METADATA = Metadata(
    id="99daa640afa4ba9f38ddfa2098d7d3bb2a7a16a9.boutiques",
    name="mri_mark_temporal_lobe",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriMarkTemporalLobeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mark_temporal_lobe(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Marked temporal lobe output file"""


def mri_mark_temporal_lobe(
    subjects: list[InputPathType],
    output_file: str,
    spacing: str | None = None,
    use_gradient: bool = False,
    runner: Runner | None = None,
) -> MriMarkTemporalLobeOutputs:
    """
    A tool for marking the temporal lobe in MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: Subject MRI images.
        output_file: Output file for marked temporal lobes.
        spacing: The spacing of classifiers in canonical space.
        use_gradient: Flag to use intensity gradient as input to classifier.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMarkTemporalLobeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MARK_TEMPORAL_LOBE_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_mark_temporal_lobe")
    if spacing is not None:
        cargs.extend([
            "-spacing",
            spacing
        ])
    if use_gradient:
        cargs.append("-gradient")
    cargs.extend([execution.input_file(f) for f in subjects])
    cargs.append(output_file)
    ret = MriMarkTemporalLobeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_MARK_TEMPORAL_LOBE_METADATA",
    "MriMarkTemporalLobeOutputs",
    "mri_mark_temporal_lobe",
]

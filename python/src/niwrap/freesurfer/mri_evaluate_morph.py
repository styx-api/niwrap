# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_EVALUATE_MORPH_METADATA = Metadata(
    id="f678f940e17b71a66c4b99ca2e39b996966acffe.boutiques",
    name="mri_evaluate_morph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriEvaluateMorphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_evaluate_morph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlap_file: OutputPathType
    """The output file containing overlap results."""


def mri_evaluate_morph(
    xform_name: InputPathType,
    segmentation_files: list[InputPathType],
    output_file: str,
    runner: Runner | None = None,
) -> MriEvaluateMorphOutputs:
    """
    This program computes the overlap of a set of segmentations for a given morph
    using an xform file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        xform_name: Transformation file name.
        segmentation_files: Input segmentation files.
        output_file: Output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEvaluateMorphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EVALUATE_MORPH_METADATA)
    cargs = []
    cargs.append("mri_evaluate_morph")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(xform_name))
    cargs.extend([execution.input_file(f) for f in segmentation_files])
    cargs.append(output_file)
    ret = MriEvaluateMorphOutputs(
        root=execution.output_file("."),
        output_overlap_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_EVALUATE_MORPH_METADATA",
    "MriEvaluateMorphOutputs",
    "mri_evaluate_morph",
]

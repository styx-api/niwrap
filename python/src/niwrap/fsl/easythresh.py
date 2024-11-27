# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EASYTHRESH_METADATA = Metadata(
    id="98fe51731b5eb29a261a330f299532a959122300.boutiques",
    name="easythresh",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class EasythreshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `easythresh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_thresh_image: OutputPathType
    """Output thresholded image"""


def easythresh(
    raw_zstat_input: InputPathType,
    brain_mask_input: InputPathType,
    cluster_z_thresh_input: float,
    cluster_prob_thresh_input: float,
    background_image_input: InputPathType,
    output_root: str,
    mm_flag: bool = False,
    runner: Runner | None = None,
) -> EasythreshOutputs:
    """
    Cluster-based statistical thresholding tool from FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        raw_zstat_input: Input raw z-statistics image.
        brain_mask_input: Brain mask image.
        cluster_z_thresh_input: Cluster z-threshold.
        cluster_prob_thresh_input: Cluster probability threshold.
        background_image_input: Background image for thresholding.
        output_root: Root of output file names.
        mm_flag: Flag to indicate the use of mm (millimeters).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EasythreshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EASYTHRESH_METADATA)
    cargs = []
    cargs.append("easythresh")
    cargs.append(execution.input_file(raw_zstat_input))
    cargs.append(execution.input_file(brain_mask_input))
    cargs.append(str(cluster_z_thresh_input))
    cargs.append(str(cluster_prob_thresh_input))
    cargs.append(execution.input_file(background_image_input))
    cargs.append(output_root)
    if mm_flag:
        cargs.append("--mm")
    ret = EasythreshOutputs(
        root=execution.output_file("."),
        output_thresh_image=execution.output_file(output_root + "_thresh.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EASYTHRESH_METADATA",
    "EasythreshOutputs",
    "easythresh",
]

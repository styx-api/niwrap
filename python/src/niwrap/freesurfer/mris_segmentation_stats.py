# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SEGMENTATION_STATS_METADATA = Metadata(
    id="c496c4babb272fe5cf304c7413672a6f323ade3f.boutiques",
    name="mris_segmentation_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisSegmentationStatsParameters = typing.TypedDict('MrisSegmentationStatsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_segmentation_stats"],
    "overlay_name": str,
    "segmentation_label_name": str,
    "subjects": list[str],
    "roc_file": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mris_segmentation_stats": mris_segmentation_stats_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mris_segmentation_stats": mris_segmentation_stats_outputs,
    }.get(t)


class MrisSegmentationStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_segmentation_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    roc_output_file: OutputPathType
    """ROC curve file"""


def mris_segmentation_stats_params(
    overlay_name: str,
    segmentation_label_name: str,
    subjects: list[str],
    roc_file: str,
) -> MrisSegmentationStatsParameters:
    """
    Build parameters.
    
    Args:
        overlay_name: Overlay name for segmentation.
        segmentation_label_name: Segmentation label name.
        subjects: List of subjects to process.
        roc_file: File for ROC curve output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_segmentation_stats",
        "overlay_name": overlay_name,
        "segmentation_label_name": segmentation_label_name,
        "subjects": subjects,
        "roc_file": roc_file,
    }
    return params


def mris_segmentation_stats_cargs(
    params: MrisSegmentationStatsParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mris_segmentation_stats")
    cargs.append(params.get("overlay_name"))
    cargs.append(params.get("segmentation_label_name"))
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("roc_file"))
    return cargs


def mris_segmentation_stats_outputs(
    params: MrisSegmentationStatsParameters,
    execution: Execution,
) -> MrisSegmentationStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSegmentationStatsOutputs(
        root=execution.output_file("."),
        roc_output_file=execution.output_file(params.get("roc_file")),
    )
    return ret


def mris_segmentation_stats_execute(
    params: MrisSegmentationStatsParameters,
    execution: Execution,
) -> MrisSegmentationStatsOutputs:
    """
    Tool for calculating segmentation statistics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSegmentationStatsOutputs`).
    """
    params = execution.params(params)
    cargs = mris_segmentation_stats_cargs(params, execution)
    ret = mris_segmentation_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_segmentation_stats(
    overlay_name: str,
    segmentation_label_name: str,
    subjects: list[str],
    roc_file: str,
    runner: Runner | None = None,
) -> MrisSegmentationStatsOutputs:
    """
    Tool for calculating segmentation statistics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        overlay_name: Overlay name for segmentation.
        segmentation_label_name: Segmentation label name.
        subjects: List of subjects to process.
        roc_file: File for ROC curve output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSegmentationStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SEGMENTATION_STATS_METADATA)
    params = mris_segmentation_stats_params(
        overlay_name=overlay_name,
        segmentation_label_name=segmentation_label_name,
        subjects=subjects,
        roc_file=roc_file,
    )
    return mris_segmentation_stats_execute(params, execution)


__all__ = [
    "MRIS_SEGMENTATION_STATS_METADATA",
    "MrisSegmentationStatsOutputs",
    "MrisSegmentationStatsParameters",
    "mris_segmentation_stats",
    "mris_segmentation_stats_params",
]

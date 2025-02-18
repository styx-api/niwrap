# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_HA_T2_SH_METADATA = Metadata(
    id="e35fef1406f0bc21d5d98039621ba41ed9020379.boutiques",
    name="segmentHA_T2.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentHaT2ShParameters = typing.TypedDict('SegmentHaT2ShParameters', {
    "__STYX_TYPE__": typing.Literal["segmentHA_T2.sh"],
    "input_image": InputPathType,
    "output_directory": str,
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
        "segmentHA_T2.sh": segment_ha_t2_sh_cargs,
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
        "segmentHA_T2.sh": segment_ha_t2_sh_outputs,
    }.get(t)


class SegmentHaT2ShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_ha_t2_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    left_hemisphere_labels: OutputPathType
    """Left hemisphere hippocampal and amygdala labels"""
    right_hemisphere_labels: OutputPathType
    """Right hemisphere hippocampal and amygdala labels"""


def segment_ha_t2_sh_params(
    input_image: InputPathType,
    output_directory: str,
) -> SegmentHaT2ShParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input T2-weighted MRI image file.
        output_directory: Output directory for segmented structures.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segmentHA_T2.sh",
        "input_image": input_image,
        "output_directory": output_directory,
    }
    return params


def segment_ha_t2_sh_cargs(
    params: SegmentHaT2ShParameters,
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
    cargs.append("segmentHA_T2.sh")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_directory"))
    return cargs


def segment_ha_t2_sh_outputs(
    params: SegmentHaT2ShParameters,
    execution: Execution,
) -> SegmentHaT2ShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentHaT2ShOutputs(
        root=execution.output_file("."),
        left_hemisphere_labels=execution.output_file(params.get("output_directory") + "/lh.hippoAmygLabels-T2.v21.mgz"),
        right_hemisphere_labels=execution.output_file(params.get("output_directory") + "/rh.hippoAmygLabels-T2.v21.mgz"),
    )
    return ret


def segment_ha_t2_sh_execute(
    params: SegmentHaT2ShParameters,
    execution: Execution,
) -> SegmentHaT2ShOutputs:
    """
    Segments hippocampal and amygdala structures from T2-weighted MRI images using
    the FreeSurfer suite.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentHaT2ShOutputs`).
    """
    cargs = segment_ha_t2_sh_cargs(params, execution)
    ret = segment_ha_t2_sh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def segment_ha_t2_sh(
    input_image: InputPathType,
    output_directory: str,
    runner: Runner | None = None,
) -> SegmentHaT2ShOutputs:
    """
    Segments hippocampal and amygdala structures from T2-weighted MRI images using
    the FreeSurfer suite.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input T2-weighted MRI image file.
        output_directory: Output directory for segmented structures.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentHaT2ShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_HA_T2_SH_METADATA)
    params = segment_ha_t2_sh_params(input_image=input_image, output_directory=output_directory)
    return segment_ha_t2_sh_execute(params, execution)


__all__ = [
    "SEGMENT_HA_T2_SH_METADATA",
    "SegmentHaT2ShOutputs",
    "SegmentHaT2ShParameters",
    "segment_ha_t2_sh",
    "segment_ha_t2_sh_params",
]

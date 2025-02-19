# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_LABEL_HISTO_METADATA = Metadata(
    id="279e3275146be4635a5b307d29d8143bca5b3d20.boutiques",
    name="mri_label_histo",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriLabelHistoParameters = typing.TypedDict('MriLabelHistoParameters', {
    "__STYX_TYPE__": typing.Literal["mri_label_histo"],
    "t1_volume": InputPathType,
    "labeled_volume": InputPathType,
    "label": float,
    "output": str,
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
        "mri_label_histo": mri_label_histo_cargs,
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
        "mri_label_histo": mri_label_histo_outputs,
    }.get(t)


class MriLabelHistoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_label_histo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    histogram_output: OutputPathType
    """Histogram of voxel values for the specified label."""


def mri_label_histo_params(
    t1_volume: InputPathType,
    labeled_volume: InputPathType,
    label: float,
    output: str,
) -> MriLabelHistoParameters:
    """
    Build parameters.
    
    Args:
        t1_volume: Input T1-weighted anatomical volume.
        labeled_volume: Input volume with labeled regions.
        label: Label of the region of interest.
        output: Output file for histogram.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_label_histo",
        "t1_volume": t1_volume,
        "labeled_volume": labeled_volume,
        "label": label,
        "output": output,
    }
    return params


def mri_label_histo_cargs(
    params: MriLabelHistoParameters,
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
    cargs.append("mri_label_histo")
    cargs.append(execution.input_file(params.get("t1_volume")))
    cargs.append(execution.input_file(params.get("labeled_volume")))
    cargs.append(str(params.get("label")))
    cargs.append(params.get("output"))
    return cargs


def mri_label_histo_outputs(
    params: MriLabelHistoParameters,
    execution: Execution,
) -> MriLabelHistoOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriLabelHistoOutputs(
        root=execution.output_file("."),
        histogram_output=execution.output_file(params.get("output")),
    )
    return ret


def mri_label_histo_execute(
    params: MriLabelHistoParameters,
    execution: Execution,
) -> MriLabelHistoOutputs:
    """
    Tool for creating a histogram of voxel values within a specified label.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriLabelHistoOutputs`).
    """
    params = execution.params(params)
    cargs = mri_label_histo_cargs(params, execution)
    ret = mri_label_histo_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_label_histo(
    t1_volume: InputPathType,
    labeled_volume: InputPathType,
    label: float,
    output: str,
    runner: Runner | None = None,
) -> MriLabelHistoOutputs:
    """
    Tool for creating a histogram of voxel values within a specified label.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_volume: Input T1-weighted anatomical volume.
        labeled_volume: Input volume with labeled regions.
        label: Label of the region of interest.
        output: Output file for histogram.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriLabelHistoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_LABEL_HISTO_METADATA)
    params = mri_label_histo_params(
        t1_volume=t1_volume,
        labeled_volume=labeled_volume,
        label=label,
        output=output,
    )
    return mri_label_histo_execute(params, execution)


__all__ = [
    "MRI_LABEL_HISTO_METADATA",
    "MriLabelHistoOutputs",
    "MriLabelHistoParameters",
    "mri_label_histo",
    "mri_label_histo_params",
]

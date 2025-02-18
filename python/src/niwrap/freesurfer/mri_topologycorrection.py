# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_TOPOLOGYCORRECTION_METADATA = Metadata(
    id="fb398c893ff0a9507f05f5c97dc95a403a3121a3.boutiques",
    name="mri_topologycorrection",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriTopologycorrectionParameters = typing.TypedDict('MriTopologycorrectionParameters', {
    "__STYX_TYPE__": typing.Literal["mri_topologycorrection"],
    "input_orig_file": InputPathType,
    "input_segmented_file": InputPathType,
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
        "mri_topologycorrection": mri_topologycorrection_cargs,
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
        "mri_topologycorrection": mri_topologycorrection_outputs,
    }.get(t)


class MriTopologycorrectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_topologycorrection(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_folder: OutputPathType
    """Directory where output files will be stored."""


def mri_topologycorrection_params(
    input_orig_file: InputPathType,
    input_segmented_file: InputPathType,
) -> MriTopologycorrectionParameters:
    """
    Build parameters.
    
    Args:
        input_orig_file: Path to the original image file.
        input_segmented_file: Path to the segmented image file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_topologycorrection",
        "input_orig_file": input_orig_file,
        "input_segmented_file": input_segmented_file,
    }
    return params


def mri_topologycorrection_cargs(
    params: MriTopologycorrectionParameters,
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
    cargs.append("mri_topologycorrection")
    cargs.append(execution.input_file(params.get("input_orig_file")))
    cargs.append(execution.input_file(params.get("input_segmented_file")))
    return cargs


def mri_topologycorrection_outputs(
    params: MriTopologycorrectionParameters,
    execution: Execution,
) -> MriTopologycorrectionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriTopologycorrectionOutputs(
        root=execution.output_file("."),
        output_folder=execution.output_file("[OUTPUT_FOLDER]"),
    )
    return ret


def mri_topologycorrection_execute(
    params: MriTopologycorrectionParameters,
    execution: Execution,
) -> MriTopologycorrectionOutputs:
    """
    Corrects the topology of segmented MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriTopologycorrectionOutputs`).
    """
    cargs = mri_topologycorrection_cargs(params, execution)
    ret = mri_topologycorrection_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_topologycorrection(
    input_orig_file: InputPathType,
    input_segmented_file: InputPathType,
    runner: Runner | None = None,
) -> MriTopologycorrectionOutputs:
    """
    Corrects the topology of segmented MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_orig_file: Path to the original image file.
        input_segmented_file: Path to the segmented image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriTopologycorrectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_TOPOLOGYCORRECTION_METADATA)
    params = mri_topologycorrection_params(input_orig_file=input_orig_file, input_segmented_file=input_segmented_file)
    return mri_topologycorrection_execute(params, execution)


__all__ = [
    "MRI_TOPOLOGYCORRECTION_METADATA",
    "MriTopologycorrectionOutputs",
    "MriTopologycorrectionParameters",
    "mri_topologycorrection",
    "mri_topologycorrection_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_OR_METADATA = Metadata(
    id="23de8af32e672952c619b947417102b41f7a6636.boutiques",
    name="mri_or",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriOrParameters = typing.TypedDict('MriOrParameters', {
    "__STYX_TYPE__": typing.Literal["mri_or"],
    "original_labels": bool,
    "input_files": list[InputPathType],
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
        "mri_or": mri_or_cargs,
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
    }.get(t)


class MriOrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_or(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_or_params(
    input_files: list[InputPathType],
    original_labels: bool = False,
) -> MriOrParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input image files on which to perform the logical OR\
            operation.
        original_labels: Keeps the original label values in the input files\
            when creating the output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_or",
        "original_labels": original_labels,
        "input_files": input_files,
    }
    return params


def mri_or_cargs(
    params: MriOrParameters,
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
    cargs.append("mri_or")
    if params.get("original_labels"):
        cargs.append("-o")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def mri_or_outputs(
    params: MriOrParameters,
    execution: Execution,
) -> MriOrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriOrOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_or_execute(
    params: MriOrParameters,
    execution: Execution,
) -> MriOrOutputs:
    """
    Performs a logical voxel-wise OR on a series of volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriOrOutputs`).
    """
    cargs = mri_or_cargs(params, execution)
    ret = mri_or_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_or(
    input_files: list[InputPathType],
    original_labels: bool = False,
    runner: Runner | None = None,
) -> MriOrOutputs:
    """
    Performs a logical voxel-wise OR on a series of volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input image files on which to perform the logical OR\
            operation.
        original_labels: Keeps the original label values in the input files\
            when creating the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriOrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_OR_METADATA)
    params = mri_or_params(original_labels=original_labels, input_files=input_files)
    return mri_or_execute(params, execution)


__all__ = [
    "MRI_OR_METADATA",
    "MriOrOutputs",
    "MriOrParameters",
    "mri_or",
    "mri_or_params",
]

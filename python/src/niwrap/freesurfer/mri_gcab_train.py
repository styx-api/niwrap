# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_GCAB_TRAIN_METADATA = Metadata(
    id="5b3336956c10bad5fe64ad5c8c726b6429d9bf74.boutiques",
    name="mri_gcab_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriGcabTrainParameters = typing.TypedDict('MriGcabTrainParameters', {
    "__STYX_TYPE__": typing.Literal["mri_gcab_train"],
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
        "mri_gcab_train": mri_gcab_train_cargs,
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


class MriGcabTrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gcab_train(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_gcab_train_params(
) -> MriGcabTrainParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_gcab_train",
    }
    return params


def mri_gcab_train_cargs(
    params: MriGcabTrainParameters,
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
    cargs.append("mri_gcab_train")
    return cargs


def mri_gcab_train_outputs(
    params: MriGcabTrainParameters,
    execution: Execution,
) -> MriGcabTrainOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGcabTrainOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_gcab_train_execute(
    params: MriGcabTrainParameters,
    execution: Execution,
) -> MriGcabTrainOutputs:
    """
    Previously used command in FreeSurfer for training with Gaussian Classifier
    Atlas-based (GCAB) modeling; has been removed in the current version.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGcabTrainOutputs`).
    """
    params = execution.params(params)
    cargs = mri_gcab_train_cargs(params, execution)
    ret = mri_gcab_train_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_gcab_train(
    runner: Runner | None = None,
) -> MriGcabTrainOutputs:
    """
    Previously used command in FreeSurfer for training with Gaussian Classifier
    Atlas-based (GCAB) modeling; has been removed in the current version.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGcabTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GCAB_TRAIN_METADATA)
    params = mri_gcab_train_params(
    )
    return mri_gcab_train_execute(params, execution)


__all__ = [
    "MRI_GCAB_TRAIN_METADATA",
    "MriGcabTrainOutputs",
    "MriGcabTrainParameters",
    "mri_gcab_train",
    "mri_gcab_train_params",
]

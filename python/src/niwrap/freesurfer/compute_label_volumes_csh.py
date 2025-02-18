# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

COMPUTE_LABEL_VOLUMES_CSH_METADATA = Metadata(
    id="82638ae4faa0eb9506df9c2f3a56c833cb5de288.boutiques",
    name="compute_label_volumes.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ComputeLabelVolumesCshParameters = typing.TypedDict('ComputeLabelVolumesCshParameters', {
    "__STYX_TYPE__": typing.Literal["compute_label_volumes.csh"],
    "label_vol": InputPathType,
    "output_file": str,
    "label_l": typing.NotRequired[str | None],
    "version": bool,
    "help": bool,
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
        "compute_label_volumes.csh": compute_label_volumes_csh_cargs,
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
        "compute_label_volumes.csh": compute_label_volumes_csh_outputs,
    }.get(t)


class ComputeLabelVolumesCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `compute_label_volumes_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_file: OutputPathType
    """Text file with the computed number of voxels and volumes"""


def compute_label_volumes_csh_params(
    label_vol: InputPathType,
    output_file: str,
    label_l: str | None = None,
    version: bool = False,
    help_: bool = False,
) -> ComputeLabelVolumesCshParameters:
    """
    Build parameters.
    
    Args:
        label_vol: Label volume to be analyzed.
        output_file: Text file where the results are written.
        label_l: The particular label to be analyzed (case-insensitive option).
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "compute_label_volumes.csh",
        "label_vol": label_vol,
        "output_file": output_file,
        "version": version,
        "help": help_,
    }
    if label_l is not None:
        params["label_l"] = label_l
    return params


def compute_label_volumes_csh_cargs(
    params: ComputeLabelVolumesCshParameters,
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
    cargs.append("compute_label_volumes")
    cargs.extend([
        "--vol",
        execution.input_file(params.get("label_vol"))
    ])
    cargs.extend([
        "--out",
        params.get("output_file")
    ])
    if params.get("label_l") is not None:
        cargs.extend([
            "--l",
            params.get("label_l")
        ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def compute_label_volumes_csh_outputs(
    params: ComputeLabelVolumesCshParameters,
    execution: Execution,
) -> ComputeLabelVolumesCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ComputeLabelVolumesCshOutputs(
        root=execution.output_file("."),
        result_file=execution.output_file(params.get("output_file")),
    )
    return ret


def compute_label_volumes_csh_execute(
    params: ComputeLabelVolumesCshParameters,
    execution: Execution,
) -> ComputeLabelVolumesCshOutputs:
    """
    Computes the number of voxels and the volumes of either all or a particular
    label in the input label volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ComputeLabelVolumesCshOutputs`).
    """
    cargs = compute_label_volumes_csh_cargs(params, execution)
    ret = compute_label_volumes_csh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def compute_label_volumes_csh(
    label_vol: InputPathType,
    output_file: str,
    label_l: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> ComputeLabelVolumesCshOutputs:
    """
    Computes the number of voxels and the volumes of either all or a particular
    label in the input label volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_vol: Label volume to be analyzed.
        output_file: Text file where the results are written.
        label_l: The particular label to be analyzed (case-insensitive option).
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ComputeLabelVolumesCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COMPUTE_LABEL_VOLUMES_CSH_METADATA)
    params = compute_label_volumes_csh_params(label_vol=label_vol, output_file=output_file, label_l=label_l, version=version, help_=help_)
    return compute_label_volumes_csh_execute(params, execution)


__all__ = [
    "COMPUTE_LABEL_VOLUMES_CSH_METADATA",
    "ComputeLabelVolumesCshOutputs",
    "ComputeLabelVolumesCshParameters",
    "compute_label_volumes_csh",
    "compute_label_volumes_csh_params",
]

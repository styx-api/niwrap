# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CENTER_DISTANCE_METADATA = Metadata(
    id="e8ff28117986ef062e78754067cfab3c33d4cd86.boutiques",
    name="@Center_Distance",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VCenterDistanceParameters = typing.TypedDict('VCenterDistanceParameters', {
    "__STYX_TYPE__": typing.Literal["@Center_Distance"],
    "dset1": InputPathType,
    "dset2": InputPathType,
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
        "@Center_Distance": v__center_distance_cargs,
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
        "@Center_Distance": v__center_distance_outputs,
    }.get(t)


class VCenterDistanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__center_distance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    distance_output: OutputPathType
    """The calculated distance between the centers of DSET_1 and DSET_2"""


def v__center_distance_params(
    dset1: InputPathType,
    dset2: InputPathType,
) -> VCenterDistanceParameters:
    """
    Build parameters.
    
    Args:
        dset1: First dataset file (e.g. file1.nii.gz).
        dset2: Second dataset file (e.g. file2.nii.gz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@Center_Distance",
        "dset1": dset1,
        "dset2": dset2,
    }
    return params


def v__center_distance_cargs(
    params: VCenterDistanceParameters,
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
    cargs.append("@Center_Distance")
    cargs.extend([
        "-dset",
        execution.input_file(params.get("dset1"))
    ])
    cargs.append(execution.input_file(params.get("dset2")))
    return cargs


def v__center_distance_outputs(
    params: VCenterDistanceParameters,
    execution: Execution,
) -> VCenterDistanceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VCenterDistanceOutputs(
        root=execution.output_file("."),
        distance_output=execution.output_file("distance.txt"),
    )
    return ret


def v__center_distance_execute(
    params: VCenterDistanceParameters,
    execution: Execution,
) -> VCenterDistanceOutputs:
    """
    Tool to calculate the distance between the centers of two datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VCenterDistanceOutputs`).
    """
    cargs = v__center_distance_cargs(params, execution)
    ret = v__center_distance_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__center_distance(
    dset1: InputPathType,
    dset2: InputPathType,
    runner: Runner | None = None,
) -> VCenterDistanceOutputs:
    """
    Tool to calculate the distance between the centers of two datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset1: First dataset file (e.g. file1.nii.gz).
        dset2: Second dataset file (e.g. file2.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VCenterDistanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CENTER_DISTANCE_METADATA)
    params = v__center_distance_params(dset1=dset1, dset2=dset2)
    return v__center_distance_execute(params, execution)


__all__ = [
    "VCenterDistanceOutputs",
    "VCenterDistanceParameters",
    "V__CENTER_DISTANCE_METADATA",
    "v__center_distance",
    "v__center_distance_params",
]

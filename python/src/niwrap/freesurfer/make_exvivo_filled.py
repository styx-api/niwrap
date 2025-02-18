# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKE_EXVIVO_FILLED_METADATA = Metadata(
    id="ea9e6e6bb03c9eb7e7861ad8386b4df6348f9898.boutiques",
    name="make_exvivo_filled",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MakeExvivoFilledParameters = typing.TypedDict('MakeExvivoFilledParameters', {
    "__STYX_TYPE__": typing.Literal["make_exvivo_filled"],
    "subject_name": str,
    "input_samseg": InputPathType,
    "input_intensity_vol": InputPathType,
    "hemi_both": str,
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
        "make_exvivo_filled": make_exvivo_filled_cargs,
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


class MakeExvivoFilledOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_exvivo_filled(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def make_exvivo_filled_params(
    subject_name: str,
    input_samseg: InputPathType,
    input_intensity_vol: InputPathType,
    hemi_both: str,
) -> MakeExvivoFilledParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        input_samseg: Input SAMSEG (Segmentation Analysis of MRI brain images).
        input_intensity_vol: Input intensity volume.
        hemi_both: Specify hemisphere or both.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "make_exvivo_filled",
        "subject_name": subject_name,
        "input_samseg": input_samseg,
        "input_intensity_vol": input_intensity_vol,
        "hemi_both": hemi_both,
    }
    return params


def make_exvivo_filled_cargs(
    params: MakeExvivoFilledParameters,
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
    cargs.append("make_exvivo_filled")
    cargs.append(params.get("subject_name"))
    cargs.append(execution.input_file(params.get("input_samseg")))
    cargs.append(execution.input_file(params.get("input_intensity_vol")))
    cargs.append(params.get("hemi_both"))
    return cargs


def make_exvivo_filled_outputs(
    params: MakeExvivoFilledParameters,
    execution: Execution,
) -> MakeExvivoFilledOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakeExvivoFilledOutputs(
        root=execution.output_file("."),
    )
    return ret


def make_exvivo_filled_execute(
    params: MakeExvivoFilledParameters,
    execution: Execution,
) -> MakeExvivoFilledOutputs:
    """
    A command-line tool for generating filled ex vivo brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakeExvivoFilledOutputs`).
    """
    cargs = make_exvivo_filled_cargs(params, execution)
    ret = make_exvivo_filled_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def make_exvivo_filled(
    subject_name: str,
    input_samseg: InputPathType,
    input_intensity_vol: InputPathType,
    hemi_both: str,
    runner: Runner | None = None,
) -> MakeExvivoFilledOutputs:
    """
    A command-line tool for generating filled ex vivo brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        input_samseg: Input SAMSEG (Segmentation Analysis of MRI brain images).
        input_intensity_vol: Input intensity volume.
        hemi_both: Specify hemisphere or both.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeExvivoFilledOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_EXVIVO_FILLED_METADATA)
    params = make_exvivo_filled_params(subject_name=subject_name, input_samseg=input_samseg, input_intensity_vol=input_intensity_vol, hemi_both=hemi_both)
    return make_exvivo_filled_execute(params, execution)


__all__ = [
    "MAKE_EXVIVO_FILLED_METADATA",
    "MakeExvivoFilledOutputs",
    "MakeExvivoFilledParameters",
    "make_exvivo_filled",
    "make_exvivo_filled_params",
]

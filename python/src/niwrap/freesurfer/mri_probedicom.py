# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_PROBEDICOM_METADATA = Metadata(
    id="e881c56e43ccca97c6f0346fbb32f30273bb1fbf.boutiques",
    name="mri_probedicom",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriProbedicomParameters = typing.TypedDict('MriProbedicomParameters', {
    "__STYX_TYPE__": typing.Literal["mri_probedicom"],
    "dicom_file": InputPathType,
    "option1": typing.NotRequired[str | None],
    "option2": typing.NotRequired[str | None],
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
        "mri_probedicom": mri_probedicom_cargs,
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
        "mri_probedicom": mri_probedicom_outputs,
    }.get(t)


class MriProbedicomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_probedicom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Text file containing extracted information from DICOM."""


def mri_probedicom_params(
    dicom_file: InputPathType,
    option1: str | None = None,
    option2: str | None = None,
) -> MriProbedicomParameters:
    """
    Build parameters.
    
    Args:
        dicom_file: DICOM file to be probed.
        option1: Description for option1.
        option2: Description for option2.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_probedicom",
        "dicom_file": dicom_file,
    }
    if option1 is not None:
        params["option1"] = option1
    if option2 is not None:
        params["option2"] = option2
    return params


def mri_probedicom_cargs(
    params: MriProbedicomParameters,
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
    cargs.append("mri_probedicom")
    cargs.append(execution.input_file(params.get("dicom_file")))
    if params.get("option1") is not None:
        cargs.extend([
            "-option1",
            params.get("option1")
        ])
    if params.get("option2") is not None:
        cargs.extend([
            "-option2",
            params.get("option2")
        ])
    return cargs


def mri_probedicom_outputs(
    params: MriProbedicomParameters,
    execution: Execution,
) -> MriProbedicomOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriProbedicomOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[OUTPUT].txt"),
    )
    return ret


def mri_probedicom_execute(
    params: MriProbedicomParameters,
    execution: Execution,
) -> MriProbedicomOutputs:
    """
    Utility to probe DICOM files for information.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriProbedicomOutputs`).
    """
    cargs = mri_probedicom_cargs(params, execution)
    ret = mri_probedicom_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_probedicom(
    dicom_file: InputPathType,
    option1: str | None = None,
    option2: str | None = None,
    runner: Runner | None = None,
) -> MriProbedicomOutputs:
    """
    Utility to probe DICOM files for information.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dicom_file: DICOM file to be probed.
        option1: Description for option1.
        option2: Description for option2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriProbedicomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PROBEDICOM_METADATA)
    params = mri_probedicom_params(dicom_file=dicom_file, option1=option1, option2=option2)
    return mri_probedicom_execute(params, execution)


__all__ = [
    "MRI_PROBEDICOM_METADATA",
    "MriProbedicomOutputs",
    "MriProbedicomParameters",
    "mri_probedicom",
    "mri_probedicom_params",
]

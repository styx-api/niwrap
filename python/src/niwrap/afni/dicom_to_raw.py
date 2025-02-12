# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DICOM_TO_RAW_METADATA = Metadata(
    id="7eb027b7c5690d1e6ebc29a721254ed558470f1d.boutiques",
    name="dicom_to_raw",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
DicomToRawParameters = typing.TypedDict('DicomToRawParameters', {
    "__STYX_TYPE__": typing.Literal["dicom_to_raw"],
    "input_dicom": InputPathType,
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
        "dicom_to_raw": dicom_to_raw_cargs,
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
        "dicom_to_raw": dicom_to_raw_outputs,
    }.get(t)


class DicomToRawOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dicom_to_raw(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_raw_file: OutputPathType
    """Output raw file(s)"""


def dicom_to_raw_params(
    input_dicom: InputPathType,
) -> DicomToRawParameters:
    """
    Build parameters.
    
    Args:
        input_dicom: Input DICOM file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dicom_to_raw",
        "input_dicom": input_dicom,
    }
    return params


def dicom_to_raw_cargs(
    params: DicomToRawParameters,
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
    cargs.append("dicom_to_raw")
    cargs.append(execution.input_file(params.get("input_dicom")))
    return cargs


def dicom_to_raw_outputs(
    params: DicomToRawParameters,
    execution: Execution,
) -> DicomToRawOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DicomToRawOutputs(
        root=execution.output_file("."),
        output_raw_file=execution.output_file(pathlib.Path(params.get("input_dicom")).name + ".raw.0001"),
    )
    return ret


def dicom_to_raw_execute(
    params: DicomToRawParameters,
    execution: Execution,
) -> DicomToRawOutputs:
    """
    Reads images from DICOM file and writes them to raw file(s).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DicomToRawOutputs`).
    """
    cargs = dicom_to_raw_cargs(params, execution)
    ret = dicom_to_raw_outputs(params, execution)
    execution.run(cargs)
    return ret


def dicom_to_raw(
    input_dicom: InputPathType,
    runner: Runner | None = None,
) -> DicomToRawOutputs:
    """
    Reads images from DICOM file and writes them to raw file(s).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dicom: Input DICOM file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DicomToRawOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DICOM_TO_RAW_METADATA)
    params = dicom_to_raw_params(input_dicom=input_dicom)
    return dicom_to_raw_execute(params, execution)


__all__ = [
    "DICOM_TO_RAW_METADATA",
    "DicomToRawOutputs",
    "DicomToRawParameters",
    "dicom_to_raw",
    "dicom_to_raw_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIDUCIALS_CALIBRATION_METADATA = Metadata(
    id="445a4b2fe29e36b5286fe1c80268453941ab7144.boutiques",
    name="fiducials_calibration",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FiducialsCalibrationParameters = typing.TypedDict('FiducialsCalibrationParameters', {
    "__STYX_TYPE__": typing.Literal["fiducials_calibration"],
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
        "fiducials_calibration": fiducials_calibration_cargs,
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


class FiducialsCalibrationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fiducials_calibration(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fiducials_calibration_params(
) -> FiducialsCalibrationParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fiducials_calibration",
    }
    return params


def fiducials_calibration_cargs(
    params: FiducialsCalibrationParameters,
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
    cargs.append("fiducials_calibration")
    return cargs


def fiducials_calibration_outputs(
    params: FiducialsCalibrationParameters,
    execution: Execution,
) -> FiducialsCalibrationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FiducialsCalibrationOutputs(
        root=execution.output_file("."),
    )
    return ret


def fiducials_calibration_execute(
    params: FiducialsCalibrationParameters,
    execution: Execution,
) -> FiducialsCalibrationOutputs:
    """
    A tool used for calibrating fiducials.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FiducialsCalibrationOutputs`).
    """
    cargs = fiducials_calibration_cargs(params, execution)
    ret = fiducials_calibration_outputs(params, execution)
    execution.run(cargs)
    return ret


def fiducials_calibration(
    runner: Runner | None = None,
) -> FiducialsCalibrationOutputs:
    """
    A tool used for calibrating fiducials.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FiducialsCalibrationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIDUCIALS_CALIBRATION_METADATA)
    params = fiducials_calibration_params()
    return fiducials_calibration_execute(params, execution)


__all__ = [
    "FIDUCIALS_CALIBRATION_METADATA",
    "FiducialsCalibrationOutputs",
    "FiducialsCalibrationParameters",
    "fiducials_calibration",
    "fiducials_calibration_params",
]

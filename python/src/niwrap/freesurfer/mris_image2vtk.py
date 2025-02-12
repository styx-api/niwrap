# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_IMAGE2VTK_METADATA = Metadata(
    id="67a28ca73b630cb9d69525ca86a737dcf4b40ebe.boutiques",
    name="mris_image2vtk",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisImage2vtkParameters = typing.TypedDict('MrisImage2vtkParameters', {
    "__STYX_TYPE__": typing.Literal["mris_image2vtk"],
    "input_filename": InputPathType,
    "output_filename": str,
    "lower_threshold": float,
    "upper_threshold": float,
    "vtk_smoothing_iters": float,
    "image_smoothing_size": float,
    "reduction_percent": float,
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
        "mris_image2vtk": mris_image2vtk_cargs,
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
        "mris_image2vtk": mris_image2vtk_outputs,
    }.get(t)


class MrisImage2vtkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_image2vtk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vtk_file: OutputPathType
    """Output VTK file generated by the conversion process"""


def mris_image2vtk_params(
    input_filename: InputPathType,
    output_filename: str,
    lower_threshold: float,
    upper_threshold: float,
    vtk_smoothing_iters: float,
    image_smoothing_size: float,
    reduction_percent: float,
) -> MrisImage2vtkParameters:
    """
    Build parameters.
    
    Args:
        input_filename: Input image file name.
        output_filename: Output VTK file name.
        lower_threshold: Lower threshold for image conversion.
        upper_threshold: Upper threshold for image conversion.
        vtk_smoothing_iters: Number of VTK smoothing iterations.
        image_smoothing_size: Image smoothing size.
        reduction_percent: Reduction percentage for the conversion.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_image2vtk",
        "input_filename": input_filename,
        "output_filename": output_filename,
        "lower_threshold": lower_threshold,
        "upper_threshold": upper_threshold,
        "vtk_smoothing_iters": vtk_smoothing_iters,
        "image_smoothing_size": image_smoothing_size,
        "reduction_percent": reduction_percent,
    }
    return params


def mris_image2vtk_cargs(
    params: MrisImage2vtkParameters,
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
    cargs.append("mris_image2vtk")
    cargs.append(execution.input_file(params.get("input_filename")))
    cargs.append(params.get("output_filename"))
    cargs.append(str(params.get("lower_threshold")))
    cargs.append(str(params.get("upper_threshold")))
    cargs.append(str(params.get("vtk_smoothing_iters")))
    cargs.append(str(params.get("image_smoothing_size")))
    cargs.append(str(params.get("reduction_percent")))
    return cargs


def mris_image2vtk_outputs(
    params: MrisImage2vtkParameters,
    execution: Execution,
) -> MrisImage2vtkOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisImage2vtkOutputs(
        root=execution.output_file("."),
        output_vtk_file=execution.output_file(params.get("output_filename")),
    )
    return ret


def mris_image2vtk_execute(
    params: MrisImage2vtkParameters,
    execution: Execution,
) -> MrisImage2vtkOutputs:
    """
    Convert image to VTK format with specified thresholds and smoothing parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisImage2vtkOutputs`).
    """
    cargs = mris_image2vtk_cargs(params, execution)
    ret = mris_image2vtk_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_image2vtk(
    input_filename: InputPathType,
    output_filename: str,
    lower_threshold: float,
    upper_threshold: float,
    vtk_smoothing_iters: float,
    image_smoothing_size: float,
    reduction_percent: float,
    runner: Runner | None = None,
) -> MrisImage2vtkOutputs:
    """
    Convert image to VTK format with specified thresholds and smoothing parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_filename: Input image file name.
        output_filename: Output VTK file name.
        lower_threshold: Lower threshold for image conversion.
        upper_threshold: Upper threshold for image conversion.
        vtk_smoothing_iters: Number of VTK smoothing iterations.
        image_smoothing_size: Image smoothing size.
        reduction_percent: Reduction percentage for the conversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisImage2vtkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_IMAGE2VTK_METADATA)
    params = mris_image2vtk_params(input_filename=input_filename, output_filename=output_filename, lower_threshold=lower_threshold, upper_threshold=upper_threshold, vtk_smoothing_iters=vtk_smoothing_iters, image_smoothing_size=image_smoothing_size, reduction_percent=reduction_percent)
    return mris_image2vtk_execute(params, execution)


__all__ = [
    "MRIS_IMAGE2VTK_METADATA",
    "MrisImage2vtkOutputs",
    "MrisImage2vtkParameters",
    "mris_image2vtk",
    "mris_image2vtk_params",
]

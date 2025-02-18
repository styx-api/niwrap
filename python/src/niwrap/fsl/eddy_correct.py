# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EDDY_CORRECT_METADATA = Metadata(
    id="02952b63ff7a435bc981ecebb28837bbe6e3e7cb.boutiques",
    name="eddy_correct",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
EddyCorrectParameters = typing.TypedDict('EddyCorrectParameters', {
    "__STYX_TYPE__": typing.Literal["eddy_correct"],
    "4d_input": InputPathType,
    "4d_output": str,
    "reference_no": int,
    "interp_method": typing.NotRequired[typing.Literal["trilinear", "spline"] | None],
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
        "eddy_correct": eddy_correct_cargs,
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
        "eddy_correct": eddy_correct_outputs,
    }.get(t)


class EddyCorrectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy_correct(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_4d_output: OutputPathType
    """Corrected 4D output image file"""


def eddy_correct_params(
    v_4d_input: InputPathType,
    v_4d_output: str,
    reference_no: int,
    interp_method: typing.Literal["trilinear", "spline"] | None = "trilinear",
) -> EddyCorrectParameters:
    """
    Build parameters.
    
    Args:
        v_4d_input: Input 4D image file (e.g., dti.nii.gz).
        v_4d_output: Output 4D image file (e.g., dti_corrected.nii.gz).
        reference_no: Reference number.
        interp_method: Interpolation method to use: 'trilinear' or 'spline'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "eddy_correct",
        "4d_input": v_4d_input,
        "4d_output": v_4d_output,
        "reference_no": reference_no,
    }
    if interp_method is not None:
        params["interp_method"] = interp_method
    return params


def eddy_correct_cargs(
    params: EddyCorrectParameters,
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
    cargs.append("eddy_correct")
    cargs.append(execution.input_file(params.get("4d_input")))
    cargs.append(params.get("4d_output"))
    if params.get("interp_method") is not None:
        cargs.append(str(params.get("reference_no")) + params.get("interp_method"))
    return cargs


def eddy_correct_outputs(
    params: EddyCorrectParameters,
    execution: Execution,
) -> EddyCorrectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = EddyCorrectOutputs(
        root=execution.output_file("."),
        corrected_4d_output=execution.output_file(params.get("4d_output") + ".nii.gz"),
    )
    return ret


def eddy_correct_execute(
    params: EddyCorrectParameters,
    execution: Execution,
) -> EddyCorrectOutputs:
    """
    Eddy current correction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `EddyCorrectOutputs`).
    """
    cargs = eddy_correct_cargs(params, execution)
    ret = eddy_correct_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def eddy_correct(
    v_4d_input: InputPathType,
    v_4d_output: str,
    reference_no: int,
    interp_method: typing.Literal["trilinear", "spline"] | None = "trilinear",
    runner: Runner | None = None,
) -> EddyCorrectOutputs:
    """
    Eddy current correction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        v_4d_input: Input 4D image file (e.g., dti.nii.gz).
        v_4d_output: Output 4D image file (e.g., dti_corrected.nii.gz).
        reference_no: Reference number.
        interp_method: Interpolation method to use: 'trilinear' or 'spline'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyCorrectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_CORRECT_METADATA)
    params = eddy_correct_params(v_4d_input=v_4d_input, v_4d_output=v_4d_output, reference_no=reference_no, interp_method=interp_method)
    return eddy_correct_execute(params, execution)


__all__ = [
    "EDDY_CORRECT_METADATA",
    "EddyCorrectOutputs",
    "EddyCorrectParameters",
    "eddy_correct",
    "eddy_correct_params",
]

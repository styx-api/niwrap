# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_SEM_METADATA = Metadata(
    id="22951ac5931e28304cde031a44c651e57c4e4a1e.boutiques",
    name="1dSEM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dSemParameters = typing.TypedDict('V1dSemParameters', {
    "__STYX_TYPE__": typing.Literal["1dSEM"],
    "theta": InputPathType,
    "correlation_matrix": InputPathType,
    "residual_variance": InputPathType,
    "degrees_of_freedom": float,
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
        "1dSEM": v_1d_sem_cargs,
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
        "1dSEM": v_1d_sem_outputs,
    }.get(t)


class V1dSemOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_sem(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output printed to the terminal. This file may be redirected."""


def v_1d_sem_params(
    theta: InputPathType,
    correlation_matrix: InputPathType,
    residual_variance: InputPathType,
    degrees_of_freedom: float,
) -> V1dSemParameters:
    """
    Build parameters.
    
    Args:
        theta: Connection matrix 1D file with initial representation.
        correlation_matrix: Correlation matrix 1D file.
        residual_variance: Residual variance vector 1D file.
        degrees_of_freedom: Degrees of freedom.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dSEM",
        "theta": theta,
        "correlation_matrix": correlation_matrix,
        "residual_variance": residual_variance,
        "degrees_of_freedom": degrees_of_freedom,
    }
    return params


def v_1d_sem_cargs(
    params: V1dSemParameters,
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
    cargs.append("1dSEM")
    cargs.extend([
        "-theta",
        execution.input_file(params.get("theta"))
    ])
    cargs.extend([
        "-C",
        execution.input_file(params.get("correlation_matrix"))
    ])
    cargs.extend([
        "-psi",
        execution.input_file(params.get("residual_variance"))
    ])
    cargs.extend([
        "-DF",
        str(params.get("degrees_of_freedom"))
    ])
    cargs.append("[OPTIONS]")
    return cargs


def v_1d_sem_outputs(
    params: V1dSemParameters,
    execution: Execution,
) -> V1dSemOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dSemOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    return ret


def v_1d_sem_execute(
    params: V1dSemParameters,
    execution: Execution,
) -> V1dSemOutputs:
    """
    Computes path coefficients for connection matrix in Structural Equation Modeling
    (SEM).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dSemOutputs`).
    """
    cargs = v_1d_sem_cargs(params, execution)
    ret = v_1d_sem_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_1d_sem(
    theta: InputPathType,
    correlation_matrix: InputPathType,
    residual_variance: InputPathType,
    degrees_of_freedom: float,
    runner: Runner | None = None,
) -> V1dSemOutputs:
    """
    Computes path coefficients for connection matrix in Structural Equation Modeling
    (SEM).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        theta: Connection matrix 1D file with initial representation.
        correlation_matrix: Correlation matrix 1D file.
        residual_variance: Residual variance vector 1D file.
        degrees_of_freedom: Degrees of freedom.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dSemOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_SEM_METADATA)
    params = v_1d_sem_params(theta=theta, correlation_matrix=correlation_matrix, residual_variance=residual_variance, degrees_of_freedom=degrees_of_freedom)
    return v_1d_sem_execute(params, execution)


__all__ = [
    "V1dSemOutputs",
    "V1dSemParameters",
    "V_1D_SEM_METADATA",
    "v_1d_sem",
    "v_1d_sem_params",
]

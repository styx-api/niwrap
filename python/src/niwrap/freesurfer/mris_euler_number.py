# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_EULER_NUMBER_METADATA = Metadata(
    id="0ad5734919ffe0fbdc78eddad073fdf8082b2ef3.boutiques",
    name="mris_euler_number",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisEulerNumberParameters = typing.TypedDict('MrisEulerNumberParameters', {
    "__STYX_TYPE__": typing.Literal["mris_euler_number"],
    "input_surface": InputPathType,
    "output_file": typing.NotRequired[str | None],
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
        "mris_euler_number": mris_euler_number_cargs,
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
        "mris_euler_number": mris_euler_number_outputs,
    }.get(t)


class MrisEulerNumberOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_euler_number(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """File where the number of holes is written"""


def mris_euler_number_params(
    input_surface: InputPathType,
    output_file: str | None = None,
) -> MrisEulerNumberParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        output_file: Write number of holes to output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_euler_number",
        "input_surface": input_surface,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def mris_euler_number_cargs(
    params: MrisEulerNumberParameters,
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
    cargs.append("mris_euler_number")
    cargs.append(execution.input_file(params.get("input_surface")))
    if params.get("output_file") is not None:
        cargs.extend([
            "-o",
            params.get("output_file")
        ])
    return cargs


def mris_euler_number_outputs(
    params: MrisEulerNumberParameters,
    execution: Execution,
) -> MrisEulerNumberOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisEulerNumberOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def mris_euler_number_execute(
    params: MrisEulerNumberParameters,
    execution: Execution,
) -> MrisEulerNumberOutputs:
    """
    This program computes EulerNumber for a cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisEulerNumberOutputs`).
    """
    cargs = mris_euler_number_cargs(params, execution)
    ret = mris_euler_number_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_euler_number(
    input_surface: InputPathType,
    output_file: str | None = None,
    runner: Runner | None = None,
) -> MrisEulerNumberOutputs:
    """
    This program computes EulerNumber for a cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        output_file: Write number of holes to output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisEulerNumberOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_EULER_NUMBER_METADATA)
    params = mris_euler_number_params(input_surface=input_surface, output_file=output_file)
    return mris_euler_number_execute(params, execution)


__all__ = [
    "MRIS_EULER_NUMBER_METADATA",
    "MrisEulerNumberOutputs",
    "MrisEulerNumberParameters",
    "mris_euler_number",
    "mris_euler_number_params",
]

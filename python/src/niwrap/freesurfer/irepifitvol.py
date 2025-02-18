# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IREPIFITVOL_METADATA = Metadata(
    id="a2bd7dc06ae3c68248647867b862df791e5ba76b.boutiques",
    name="irepifitvol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
IrepifitvolParameters = typing.TypedDict('IrepifitvolParameters', {
    "__STYX_TYPE__": typing.Literal["irepifitvol"],
    "input_file": InputPathType,
    "output_file": str,
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
        "irepifitvol": irepifitvol_cargs,
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
        "irepifitvol": irepifitvol_outputs,
    }.get(t)


class IrepifitvolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `irepifitvol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fitted_output: OutputPathType
    """The resulting volume file after fitting"""


def irepifitvol_params(
    input_file: InputPathType,
    output_file: str = "fitted_output",
) -> IrepifitvolParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input volume file for fitting.
        output_file: Output volume file after fitting.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "irepifitvol",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def irepifitvol_cargs(
    params: IrepifitvolParameters,
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
    cargs.append("irepifitvol")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def irepifitvol_outputs(
    params: IrepifitvolParameters,
    execution: Execution,
) -> IrepifitvolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IrepifitvolOutputs(
        root=execution.output_file("."),
        fitted_output=execution.output_file(params.get("output_file") + ".ext"),
    )
    return ret


def irepifitvol_execute(
    params: IrepifitvolParameters,
    execution: Execution,
) -> IrepifitvolOutputs:
    """
    A tool for 3D volume fitting.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IrepifitvolOutputs`).
    """
    cargs = irepifitvol_cargs(params, execution)
    ret = irepifitvol_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def irepifitvol(
    input_file: InputPathType,
    output_file: str = "fitted_output",
    runner: Runner | None = None,
) -> IrepifitvolOutputs:
    """
    A tool for 3D volume fitting.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input volume file for fitting.
        output_file: Output volume file after fitting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IrepifitvolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IREPIFITVOL_METADATA)
    params = irepifitvol_params(input_file=input_file, output_file=output_file)
    return irepifitvol_execute(params, execution)


__all__ = [
    "IREPIFITVOL_METADATA",
    "IrepifitvolOutputs",
    "IrepifitvolParameters",
    "irepifitvol",
    "irepifitvol_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ISNIFTI_METADATA = Metadata(
    id="0ec07279947545d1155748f4d9a448ee304204a0.boutiques",
    name="isnifti",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
IsniftiParameters = typing.TypedDict('IsniftiParameters', {
    "__STYX_TYPE__": typing.Literal["isnifti"],
    "infile": InputPathType,
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
        "isnifti": isnifti_cargs,
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


class IsniftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `isnifti(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def isnifti_params(
    infile: InputPathType,
) -> IsniftiParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file to be checked if it is a NIfTI image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "isnifti",
        "infile": infile,
    }
    return params


def isnifti_cargs(
    params: IsniftiParameters,
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
    cargs.append("isnifti")
    cargs.append(execution.input_file(params.get("infile")))
    return cargs


def isnifti_outputs(
    params: IsniftiParameters,
    execution: Execution,
) -> IsniftiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IsniftiOutputs(
        root=execution.output_file("."),
    )
    return ret


def isnifti_execute(
    params: IsniftiParameters,
    execution: Execution,
) -> IsniftiOutputs:
    """
    A simple tool to check if a file is a NIfTI image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IsniftiOutputs`).
    """
    cargs = isnifti_cargs(params, execution)
    ret = isnifti_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def isnifti(
    infile: InputPathType,
    runner: Runner | None = None,
) -> IsniftiOutputs:
    """
    A simple tool to check if a file is a NIfTI image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file to be checked if it is a NIfTI image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsniftiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISNIFTI_METADATA)
    params = isnifti_params(infile=infile)
    return isnifti_execute(params, execution)


__all__ = [
    "ISNIFTI_METADATA",
    "IsniftiOutputs",
    "IsniftiParameters",
    "isnifti",
    "isnifti_params",
]

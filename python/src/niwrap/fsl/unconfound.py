# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UNCONFOUND_METADATA = Metadata(
    id="2ccf7c410e301ebdd239b6f4684654f07d566038.boutiques",
    name="unconfound",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
UnconfoundParameters = typing.TypedDict('UnconfoundParameters', {
    "__STYX_TYPE__": typing.Literal["unconfound"],
    "in4d": InputPathType,
    "out4d": str,
    "confound_mat": InputPathType,
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
        "unconfound": unconfound_cargs,
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
        "unconfound": unconfound_outputs,
    }.get(t)


class UnconfoundOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unconfound(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_4d: OutputPathType
    """Output 4D fMRI data after removing confounds"""


def unconfound_params(
    in4d: InputPathType,
    out4d: str,
    confound_mat: InputPathType,
) -> UnconfoundParameters:
    """
    Build parameters.
    
    Args:
        in4d: Input 4D fMRI data (e.g., in4d.nii.gz).
        out4d: Output 4D fMRI data after removing confounds (e.g.,\
            out4d.nii.gz).
        confound_mat: Confound matrix file (e.g., confound.mat).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "unconfound",
        "in4d": in4d,
        "out4d": out4d,
        "confound_mat": confound_mat,
    }
    return params


def unconfound_cargs(
    params: UnconfoundParameters,
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
    cargs.append("unconfound")
    cargs.append(execution.input_file(params.get("in4d")))
    cargs.append(params.get("out4d"))
    cargs.append(execution.input_file(params.get("confound_mat")))
    return cargs


def unconfound_outputs(
    params: UnconfoundParameters,
    execution: Execution,
) -> UnconfoundOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UnconfoundOutputs(
        root=execution.output_file("."),
        output_4d=execution.output_file(params.get("out4d") + ".nii.gz"),
    )
    return ret


def unconfound_execute(
    params: UnconfoundParameters,
    execution: Execution,
) -> UnconfoundOutputs:
    """
    Removing confounds from 4D fMRI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UnconfoundOutputs`).
    """
    cargs = unconfound_cargs(params, execution)
    ret = unconfound_outputs(params, execution)
    execution.run(cargs)
    return ret


def unconfound(
    in4d: InputPathType,
    out4d: str,
    confound_mat: InputPathType,
    runner: Runner | None = None,
) -> UnconfoundOutputs:
    """
    Removing confounds from 4D fMRI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in4d: Input 4D fMRI data (e.g., in4d.nii.gz).
        out4d: Output 4D fMRI data after removing confounds (e.g.,\
            out4d.nii.gz).
        confound_mat: Confound matrix file (e.g., confound.mat).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnconfoundOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNCONFOUND_METADATA)
    params = unconfound_params(in4d=in4d, out4d=out4d, confound_mat=confound_mat)
    return unconfound_execute(params, execution)


__all__ = [
    "UNCONFOUND_METADATA",
    "UnconfoundOutputs",
    "UnconfoundParameters",
    "unconfound",
    "unconfound_params",
]

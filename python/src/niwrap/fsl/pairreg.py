# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PAIRREG_METADATA = Metadata(
    id="b91659121aa50786207f87a814c07e8cbf851fc0.boutiques",
    name="pairreg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PairregParameters = typing.TypedDict('PairregParameters', {
    "__STYX_TYPE__": typing.Literal["pairreg"],
    "brain1": InputPathType,
    "brain2": InputPathType,
    "skull1": InputPathType,
    "skull2": InputPathType,
    "outputmatrix": InputPathType,
    "extra_flirt_args": typing.NotRequired[str | None],
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
        "pairreg": pairreg_cargs,
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
        "pairreg": pairreg_outputs,
    }.get(t)


class PairregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pairreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix: OutputPathType
    """Pairwise registration output transformation matrix file"""


def pairreg_params(
    brain1: InputPathType,
    brain2: InputPathType,
    skull1: InputPathType,
    skull2: InputPathType,
    outputmatrix: InputPathType,
    extra_flirt_args: str | None = None,
) -> PairregParameters:
    """
    Build parameters.
    
    Args:
        brain1: Brain image 1 (used as -ref internally).
        brain2: Brain image 2.
        skull1: Skull image 1 (used as -ref internally).
        skull2: Skull image 2.
        outputmatrix: Output transformation matrix file.
        extra_flirt_args: Extra arguments to pass to flirt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pairreg",
        "brain1": brain1,
        "brain2": brain2,
        "skull1": skull1,
        "skull2": skull2,
        "outputmatrix": outputmatrix,
    }
    if extra_flirt_args is not None:
        params["extra_flirt_args"] = extra_flirt_args
    return params


def pairreg_cargs(
    params: PairregParameters,
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
    cargs.append("pairreg")
    cargs.append(execution.input_file(params.get("brain1")))
    cargs.append(execution.input_file(params.get("brain2")))
    cargs.append(execution.input_file(params.get("skull1")))
    cargs.append(execution.input_file(params.get("skull2")))
    cargs.append(execution.input_file(params.get("outputmatrix")))
    if params.get("extra_flirt_args") is not None:
        cargs.append(params.get("extra_flirt_args"))
    return cargs


def pairreg_outputs(
    params: PairregParameters,
    execution: Execution,
) -> PairregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PairregOutputs(
        root=execution.output_file("."),
        output_matrix=execution.output_file(pathlib.Path(params.get("outputmatrix")).name),
    )
    return ret


def pairreg_execute(
    params: PairregParameters,
    execution: Execution,
) -> PairregOutputs:
    """
    Pairwise registration tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PairregOutputs`).
    """
    cargs = pairreg_cargs(params, execution)
    ret = pairreg_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def pairreg(
    brain1: InputPathType,
    brain2: InputPathType,
    skull1: InputPathType,
    skull2: InputPathType,
    outputmatrix: InputPathType,
    extra_flirt_args: str | None = None,
    runner: Runner | None = None,
) -> PairregOutputs:
    """
    Pairwise registration tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        brain1: Brain image 1 (used as -ref internally).
        brain2: Brain image 2.
        skull1: Skull image 1 (used as -ref internally).
        skull2: Skull image 2.
        outputmatrix: Output transformation matrix file.
        extra_flirt_args: Extra arguments to pass to flirt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PairregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PAIRREG_METADATA)
    params = pairreg_params(brain1=brain1, brain2=brain2, skull1=skull1, skull2=skull2, outputmatrix=outputmatrix, extra_flirt_args=extra_flirt_args)
    return pairreg_execute(params, execution)


__all__ = [
    "PAIRREG_METADATA",
    "PairregOutputs",
    "PairregParameters",
    "pairreg",
    "pairreg_params",
]

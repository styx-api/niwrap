# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1DNORM_METADATA = Metadata(
    id="ea6e83597c9dc8fb3895db8c36d06ddc6f559447.boutiques",
    name="1dnorm",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dnormParameters = typing.TypedDict('V1dnormParameters', {
    "__STYX_TYPE__": typing.Literal["1dnorm"],
    "infile": InputPathType,
    "outfile": str,
    "norm1": bool,
    "normx": bool,
    "demean": bool,
    "demed": bool,
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
        "1dnorm": v_1dnorm_cargs,
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
        "1dnorm": v_1dnorm_outputs,
    }.get(t)


class V1dnormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dnorm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    normalized_output: OutputPathType
    """Normalized output AFNI *.1D file"""


def v_1dnorm_params(
    infile: InputPathType,
    outfile: str,
    norm1: bool = False,
    normx: bool = False,
    demean: bool = False,
    demed: bool = False,
) -> V1dnormParameters:
    """
    Build parameters.
    
    Args:
        infile: Input AFNI *.1D file (ASCII list of numbers arranged in\
            columns); if '-' input will be read from stdin.
        outfile: Output AFNI *.1D file (normalized); if '-' output will be\
            written to stdout.
        norm1: Normalize so sum of absolute values is 1 (L_1 norm).
        normx: Normalize so that max absolute value is 1 (L_infinity norm).
        demean: Subtract each column's mean before normalizing.
        demed: Subtract each column's median before normalizing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dnorm",
        "infile": infile,
        "outfile": outfile,
        "norm1": norm1,
        "normx": normx,
        "demean": demean,
        "demed": demed,
    }
    return params


def v_1dnorm_cargs(
    params: V1dnormParameters,
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
    cargs.append("1dnorm")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(params.get("outfile"))
    if params.get("norm1"):
        cargs.append("-norm1")
    if params.get("normx"):
        cargs.append("-normx")
    if params.get("demean"):
        cargs.append("-demean")
    if params.get("demed"):
        cargs.append("-demed")
    return cargs


def v_1dnorm_outputs(
    params: V1dnormParameters,
    execution: Execution,
) -> V1dnormOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dnormOutputs(
        root=execution.output_file("."),
        normalized_output=execution.output_file(params.get("outfile")),
    )
    return ret


def v_1dnorm_execute(
    params: V1dnormParameters,
    execution: Execution,
) -> V1dnormOutputs:
    """
    Normalize columns of a 1D file (AFNI ASCII list of numbers).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dnormOutputs`).
    """
    cargs = v_1dnorm_cargs(params, execution)
    ret = v_1dnorm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1dnorm(
    infile: InputPathType,
    outfile: str,
    norm1: bool = False,
    normx: bool = False,
    demean: bool = False,
    demed: bool = False,
    runner: Runner | None = None,
) -> V1dnormOutputs:
    """
    Normalize columns of a 1D file (AFNI ASCII list of numbers).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input AFNI *.1D file (ASCII list of numbers arranged in\
            columns); if '-' input will be read from stdin.
        outfile: Output AFNI *.1D file (normalized); if '-' output will be\
            written to stdout.
        norm1: Normalize so sum of absolute values is 1 (L_1 norm).
        normx: Normalize so that max absolute value is 1 (L_infinity norm).
        demean: Subtract each column's mean before normalizing.
        demed: Subtract each column's median before normalizing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dnormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DNORM_METADATA)
    params = v_1dnorm_params(infile=infile, outfile=outfile, norm1=norm1, normx=normx, demean=demean, demed=demed)
    return v_1dnorm_execute(params, execution)


__all__ = [
    "V1dnormOutputs",
    "V1dnormParameters",
    "V_1DNORM_METADATA",
    "v_1dnorm",
    "v_1dnorm_params",
]

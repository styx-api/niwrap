# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SAMP_BIAS_METADATA = Metadata(
    id="6e470934bf7282b84b4830d0577fb44d56bf39e3.boutiques",
    name="SampBias",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SampBiasParameters = typing.TypedDict('SampBiasParameters', {
    "__STYX_TYPE__": typing.Literal["SampBias"],
    "specfile": InputPathType,
    "surfname": str,
    "plimit": typing.NotRequired[float | None],
    "dlimit": typing.NotRequired[float | None],
    "outfile": str,
    "prefix": typing.NotRequired[str | None],
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
        "SampBias": samp_bias_cargs,
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
        "SampBias": samp_bias_outputs,
    }.get(t)


class SampBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `samp_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_1_d: OutputPathType
    """Output results in .1D format"""
    out_prefix: OutputPathType | None
    """Output results in a proper surface-based dataset."""


def samp_bias_params(
    specfile: InputPathType,
    surfname: str,
    outfile: str,
    plimit: float | None = None,
    dlimit: float | None = None,
    prefix: str | None = None,
) -> SampBiasParameters:
    """
    Build parameters.
    
    Args:
        specfile: Spec file containing input surfaces.
        surfname: Name of input surface.
        outfile: Output results in .1D format.
        plimit: Maximum length of path along surface in mm. Default is 50 mm.
        dlimit: Maximum length of euclidean distance in mm. Default is 1000 mm.
        prefix: Output results into a proper surface-based dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SampBias",
        "specfile": specfile,
        "surfname": surfname,
        "outfile": outfile,
    }
    if plimit is not None:
        params["plimit"] = plimit
    if dlimit is not None:
        params["dlimit"] = dlimit
    if prefix is not None:
        params["prefix"] = prefix
    return params


def samp_bias_cargs(
    params: SampBiasParameters,
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
    cargs.append("SampBias")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("specfile"))
    ])
    cargs.extend([
        "-surf",
        params.get("surfname")
    ])
    if params.get("plimit") is not None:
        cargs.extend([
            "-plimit",
            str(params.get("plimit"))
        ])
    if params.get("dlimit") is not None:
        cargs.extend([
            "-dlimit",
            str(params.get("dlimit"))
        ])
    cargs.extend([
        "-out",
        params.get("outfile")
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def samp_bias_outputs(
    params: SampBiasParameters,
    execution: Execution,
) -> SampBiasOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SampBiasOutputs(
        root=execution.output_file("."),
        out_1_d=execution.output_file(params.get("outfile") + ".1D"),
        out_prefix=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def samp_bias_execute(
    params: SampBiasParameters,
    execution: Execution,
) -> SampBiasOutputs:
    """
    SampBias is a tool for sampling bias resultant segments between paired nodes on
    anatomical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SampBiasOutputs`).
    """
    params = execution.params(params)
    cargs = samp_bias_cargs(params, execution)
    ret = samp_bias_outputs(params, execution)
    execution.run(cargs)
    return ret


def samp_bias(
    specfile: InputPathType,
    surfname: str,
    outfile: str,
    plimit: float | None = None,
    dlimit: float | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> SampBiasOutputs:
    """
    SampBias is a tool for sampling bias resultant segments between paired nodes on
    anatomical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        specfile: Spec file containing input surfaces.
        surfname: Name of input surface.
        outfile: Output results in .1D format.
        plimit: Maximum length of path along surface in mm. Default is 50 mm.
        dlimit: Maximum length of euclidean distance in mm. Default is 1000 mm.
        prefix: Output results into a proper surface-based dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SampBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SAMP_BIAS_METADATA)
    params = samp_bias_params(
        specfile=specfile,
        surfname=surfname,
        plimit=plimit,
        dlimit=dlimit,
        outfile=outfile,
        prefix=prefix,
    )
    return samp_bias_execute(params, execution)


__all__ = [
    "SAMP_BIAS_METADATA",
    "SampBiasOutputs",
    "SampBiasParameters",
    "samp_bias",
    "samp_bias_params",
]

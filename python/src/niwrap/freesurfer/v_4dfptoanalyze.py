# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_4DFPTOANALYZE_METADATA = Metadata(
    id="65cd83dce834e4e472f7fa7af8e2201dfe71e3b3.boutiques",
    name="4dfptoanalyze",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
V4dfptoanalyzeParameters = typing.TypedDict('V4dfptoanalyzeParameters', {
    "__STYX_TYPE__": typing.Literal["4dfptoanalyze"],
    "input_file": InputPathType,
    "scale_factor": typing.NotRequired[float | None],
    "output_8bit": bool,
    "spm99": bool,
    "endianness": typing.NotRequired[str | None],
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
        "4dfptoanalyze": v_4dfptoanalyze_cargs,
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
        "4dfptoanalyze": v_4dfptoanalyze_outputs,
    }.get(t)


class V4dfptoanalyzeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_4dfptoanalyze(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    analyze_hdr: OutputPathType
    """Header file of Analyze format output"""
    analyze_img: OutputPathType
    """Image file of Analyze format output"""


def v_4dfptoanalyze_params(
    input_file: InputPathType,
    scale_factor: float | None = None,
    output_8bit: bool = False,
    spm99: bool = False,
    endianness: str | None = None,
) -> V4dfptoanalyzeParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input 4dfp filename.
        scale_factor: Scale output values by specified factor.
        output_8bit: Output 8 bit unsigned char.
        spm99: Include origin and scale in hdr.
        endianness: Output big or little endian (default CPU endian).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "4dfptoanalyze",
        "input_file": input_file,
        "output_8bit": output_8bit,
        "spm99": spm99,
    }
    if scale_factor is not None:
        params["scale_factor"] = scale_factor
    if endianness is not None:
        params["endianness"] = endianness
    return params


def v_4dfptoanalyze_cargs(
    params: V4dfptoanalyzeParameters,
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
    cargs.append("4dfptoanalyze")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("scale_factor") is not None:
        cargs.extend([
            "-c",
            str(params.get("scale_factor"))
        ])
    if params.get("output_8bit"):
        cargs.append("-8")
    if params.get("spm99"):
        cargs.append("-SPM99")
    if params.get("endianness") is not None:
        cargs.extend([
            "-@",
            params.get("endianness")
        ])
    return cargs


def v_4dfptoanalyze_outputs(
    params: V4dfptoanalyzeParameters,
    execution: Execution,
) -> V4dfptoanalyzeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V4dfptoanalyzeOutputs(
        root=execution.output_file("."),
        analyze_hdr=execution.output_file(pathlib.Path(params.get("input_file")).name + "_analyze.hdr"),
        analyze_img=execution.output_file(pathlib.Path(params.get("input_file")).name + "_analyze.img"),
    )
    return ret


def v_4dfptoanalyze_execute(
    params: V4dfptoanalyzeParameters,
    execution: Execution,
) -> V4dfptoanalyzeOutputs:
    """
    Converts 4dfp formatted files to Analyze format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V4dfptoanalyzeOutputs`).
    """
    cargs = v_4dfptoanalyze_cargs(params, execution)
    ret = v_4dfptoanalyze_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_4dfptoanalyze(
    input_file: InputPathType,
    scale_factor: float | None = None,
    output_8bit: bool = False,
    spm99: bool = False,
    endianness: str | None = None,
    runner: Runner | None = None,
) -> V4dfptoanalyzeOutputs:
    """
    Converts 4dfp formatted files to Analyze format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input 4dfp filename.
        scale_factor: Scale output values by specified factor.
        output_8bit: Output 8 bit unsigned char.
        spm99: Include origin and scale in hdr.
        endianness: Output big or little endian (default CPU endian).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V4dfptoanalyzeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_4DFPTOANALYZE_METADATA)
    params = v_4dfptoanalyze_params(input_file=input_file, scale_factor=scale_factor, output_8bit=output_8bit, spm99=spm99, endianness=endianness)
    return v_4dfptoanalyze_execute(params, execution)


__all__ = [
    "V4dfptoanalyzeOutputs",
    "V4dfptoanalyzeParameters",
    "V_4DFPTOANALYZE_METADATA",
    "v_4dfptoanalyze",
    "v_4dfptoanalyze_params",
]

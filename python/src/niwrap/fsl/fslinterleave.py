# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLINTERLEAVE_METADATA = Metadata(
    id="93b8da65cc073c4d0bd4a959fb87a8823f01227a.boutiques",
    name="fslinterleave",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslinterleaveParameters = typing.TypedDict('FslinterleaveParameters', {
    "__STYX_TYPE__": typing.Literal["fslinterleave"],
    "infile1": InputPathType,
    "infile2": InputPathType,
    "outfile": str,
    "reverse_slice_order_flag": bool,
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
        "fslinterleave": fslinterleave_cargs,
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
        "fslinterleave": fslinterleave_outputs,
    }.get(t)


class FslinterleaveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslinterleave(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    interleaved_output: OutputPathType
    """Interleaved output image"""


def fslinterleave_params(
    infile1: InputPathType,
    infile2: InputPathType,
    outfile: str,
    reverse_slice_order_flag: bool = False,
) -> FslinterleaveParameters:
    """
    Build parameters.
    
    Args:
        infile1: First input image.
        infile2: Second input image.
        outfile: Output interleaved image.
        reverse_slice_order_flag: Reverse slice order.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslinterleave",
        "infile1": infile1,
        "infile2": infile2,
        "outfile": outfile,
        "reverse_slice_order_flag": reverse_slice_order_flag,
    }
    return params


def fslinterleave_cargs(
    params: FslinterleaveParameters,
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
    cargs.append("fslinterleave")
    cargs.append(execution.input_file(params.get("infile1")))
    cargs.append(execution.input_file(params.get("infile2")))
    cargs.append(params.get("outfile"))
    if params.get("reverse_slice_order_flag"):
        cargs.append("-i")
    return cargs


def fslinterleave_outputs(
    params: FslinterleaveParameters,
    execution: Execution,
) -> FslinterleaveOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslinterleaveOutputs(
        root=execution.output_file("."),
        interleaved_output=execution.output_file(params.get("outfile") + ".nii.gz"),
    )
    return ret


def fslinterleave_execute(
    params: FslinterleaveParameters,
    execution: Execution,
) -> FslinterleaveOutputs:
    """
    Interleaves two input images slice-by-slice to produce an output image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslinterleaveOutputs`).
    """
    cargs = fslinterleave_cargs(params, execution)
    ret = fslinterleave_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslinterleave(
    infile1: InputPathType,
    infile2: InputPathType,
    outfile: str,
    reverse_slice_order_flag: bool = False,
    runner: Runner | None = None,
) -> FslinterleaveOutputs:
    """
    Interleaves two input images slice-by-slice to produce an output image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile1: First input image.
        infile2: Second input image.
        outfile: Output interleaved image.
        reverse_slice_order_flag: Reverse slice order.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslinterleaveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLINTERLEAVE_METADATA)
    params = fslinterleave_params(infile1=infile1, infile2=infile2, outfile=outfile, reverse_slice_order_flag=reverse_slice_order_flag)
    return fslinterleave_execute(params, execution)


__all__ = [
    "FSLINTERLEAVE_METADATA",
    "FslinterleaveOutputs",
    "FslinterleaveParameters",
    "fslinterleave",
    "fslinterleave_params",
]

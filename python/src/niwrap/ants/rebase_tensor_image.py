# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REBASE_TENSOR_IMAGE_METADATA = Metadata(
    id="cb7dc4431e44610b96f7d5021a64651fd63ad535.boutiques",
    name="RebaseTensorImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
RebaseTensorImageParameters = typing.TypedDict('RebaseTensorImageParameters', {
    "__STYX_TYPE__": typing.Literal["RebaseTensorImage"],
    "dimension": int,
    "infile": InputPathType,
    "outfile": InputPathType,
    "method": typing.Literal["PHYSICAL", "LOCAL"],
    "reference": typing.NotRequired[InputPathType | None],
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
        "RebaseTensorImage": rebase_tensor_image_cargs,
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
        "RebaseTensorImage": rebase_tensor_image_outputs,
    }.get(t)


class RebaseTensorImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rebase_tensor_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    rebased_image: OutputPathType
    """The rebased tensor image."""


def rebase_tensor_image_params(
    dimension: int,
    infile: InputPathType,
    outfile: InputPathType,
    method: typing.Literal["PHYSICAL", "LOCAL"],
    reference: InputPathType | None = None,
) -> RebaseTensorImageParameters:
    """
    Build parameters.
    
    Args:
        dimension: The dimensionality of the input image.
        infile: The input image file.
        outfile: The output image file.
        method: Method of rebasing the tensor image.
        reference: Reference image file (required if PHYSICAL or LOCAL method\
            is chosen).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "RebaseTensorImage",
        "dimension": dimension,
        "infile": infile,
        "outfile": outfile,
        "method": method,
    }
    if reference is not None:
        params["reference"] = reference
    return params


def rebase_tensor_image_cargs(
    params: RebaseTensorImageParameters,
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
    cargs.append("RebaseTensorImage")
    cargs.append(str(params.get("dimension")))
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(execution.input_file(params.get("outfile")))
    cargs.append(params.get("method"))
    if params.get("reference") is not None:
        cargs.append(execution.input_file(params.get("reference")))
    return cargs


def rebase_tensor_image_outputs(
    params: RebaseTensorImageParameters,
    execution: Execution,
) -> RebaseTensorImageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RebaseTensorImageOutputs(
        root=execution.output_file("."),
        rebased_image=execution.output_file(pathlib.Path(params.get("outfile")).name),
    )
    return ret


def rebase_tensor_image_execute(
    params: RebaseTensorImageParameters,
    execution: Execution,
) -> RebaseTensorImageOutputs:
    """
    Rebase Tensor Image using specified dimensionality and method.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RebaseTensorImageOutputs`).
    """
    cargs = rebase_tensor_image_cargs(params, execution)
    ret = rebase_tensor_image_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def rebase_tensor_image(
    dimension: int,
    infile: InputPathType,
    outfile: InputPathType,
    method: typing.Literal["PHYSICAL", "LOCAL"],
    reference: InputPathType | None = None,
    runner: Runner | None = None,
) -> RebaseTensorImageOutputs:
    """
    Rebase Tensor Image using specified dimensionality and method.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimension: The dimensionality of the input image.
        infile: The input image file.
        outfile: The output image file.
        method: Method of rebasing the tensor image.
        reference: Reference image file (required if PHYSICAL or LOCAL method\
            is chosen).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RebaseTensorImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REBASE_TENSOR_IMAGE_METADATA)
    params = rebase_tensor_image_params(dimension=dimension, infile=infile, outfile=outfile, method=method, reference=reference)
    return rebase_tensor_image_execute(params, execution)


__all__ = [
    "REBASE_TENSOR_IMAGE_METADATA",
    "RebaseTensorImageOutputs",
    "RebaseTensorImageParameters",
    "rebase_tensor_image",
    "rebase_tensor_image_params",
]

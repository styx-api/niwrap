# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ORIENT_LAS_METADATA = Metadata(
    id="c8cbae7a0ae48bc5ff23e10ecc70110ddd8919ae.boutiques",
    name="orientLAS",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
OrientLasParameters = typing.TypedDict('OrientLasParameters', {
    "__STYX_TYPE__": typing.Literal["orientLAS"],
    "input_image": InputPathType,
    "output_image": str,
    "check": bool,
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
        "orientLAS": orient_las_cargs,
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
        "orientLAS": orient_las_outputs,
    }.get(t)


class OrientLasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `orient_las(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_las_image: OutputPathType
    """Output image with LAS orientation"""


def orient_las_params(
    input_image: InputPathType,
    output_image: str,
    check: bool = False,
) -> OrientLasParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image in NIfTI format.
        output_image: Output image in NIfTI format with LAS orientation.
        check: Check the match of input and output images using tkregister, and\
            for diffusion data, run dtifit and show tensors with fslview.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "orientLAS",
        "input_image": input_image,
        "output_image": output_image,
        "check": check,
    }
    return params


def orient_las_cargs(
    params: OrientLasParameters,
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
    cargs.append("orientLAS")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    if params.get("check"):
        cargs.append("--check")
    return cargs


def orient_las_outputs(
    params: OrientLasParameters,
    execution: Execution,
) -> OrientLasOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = OrientLasOutputs(
        root=execution.output_file("."),
        output_las_image=execution.output_file(params.get("output_image")),
    )
    return ret


def orient_las_execute(
    params: OrientLasParameters,
    execution: Execution,
) -> OrientLasOutputs:
    """
    Convert image to LAS orientation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `OrientLasOutputs`).
    """
    cargs = orient_las_cargs(params, execution)
    ret = orient_las_outputs(params, execution)
    execution.run(cargs)
    return ret


def orient_las(
    input_image: InputPathType,
    output_image: str,
    check: bool = False,
    runner: Runner | None = None,
) -> OrientLasOutputs:
    """
    Convert image to LAS orientation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input image in NIfTI format.
        output_image: Output image in NIfTI format with LAS orientation.
        check: Check the match of input and output images using tkregister, and\
            for diffusion data, run dtifit and show tensors with fslview.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OrientLasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ORIENT_LAS_METADATA)
    params = orient_las_params(input_image=input_image, output_image=output_image, check=check)
    return orient_las_execute(params, execution)


__all__ = [
    "ORIENT_LAS_METADATA",
    "OrientLasOutputs",
    "OrientLasParameters",
    "orient_las",
    "orient_las_params",
]

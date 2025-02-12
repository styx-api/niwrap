# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIRST_MULT_BCORR_METADATA = Metadata(
    id="a7d6c8e2e8974e5facac9a650b214397ba549860.boutiques",
    name="first_mult_bcorr",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FirstMultBcorrParameters = typing.TypedDict('FirstMultBcorrParameters', {
    "__STYX_TYPE__": typing.Literal["first_mult_bcorr"],
    "input_image": InputPathType,
    "corrected_4d_labels": InputPathType,
    "uncorrected_4d_labels": InputPathType,
    "output_image": str,
    "verbose_flag": bool,
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
        "first_mult_bcorr": first_mult_bcorr_cargs,
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
        "first_mult_bcorr": first_mult_bcorr_outputs,
    }.get(t)


class FirstMultBcorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first_mult_bcorr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output image name (3D label image)"""


def first_mult_bcorr_params(
    input_image: InputPathType,
    corrected_4d_labels: InputPathType,
    uncorrected_4d_labels: InputPathType,
    output_image: str,
    verbose_flag: bool = False,
) -> FirstMultBcorrParameters:
    """
    Build parameters.
    
    Args:
        input_image: Filename of original T1 input image.
        corrected_4d_labels: Filename of 4D image of individually corrected\
            labels.
        uncorrected_4d_labels: Filename of 4D image of uncorrected labels (with\
            boundaries).
        output_image: Output image name (3D label image).
        verbose_flag: Output F-stats to standard out.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "first_mult_bcorr",
        "input_image": input_image,
        "corrected_4d_labels": corrected_4d_labels,
        "uncorrected_4d_labels": uncorrected_4d_labels,
        "output_image": output_image,
        "verbose_flag": verbose_flag,
    }
    return params


def first_mult_bcorr_cargs(
    params: FirstMultBcorrParameters,
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
    cargs.append("first_mult_bcorr")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    cargs.extend([
        "-c",
        execution.input_file(params.get("corrected_4d_labels"))
    ])
    cargs.extend([
        "-u",
        execution.input_file(params.get("uncorrected_4d_labels"))
    ])
    cargs.extend([
        "-o",
        params.get("output_image")
    ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def first_mult_bcorr_outputs(
    params: FirstMultBcorrParameters,
    execution: Execution,
) -> FirstMultBcorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FirstMultBcorrOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_image")),
    )
    return ret


def first_mult_bcorr_execute(
    params: FirstMultBcorrParameters,
    execution: Execution,
) -> FirstMultBcorrOutputs:
    """
    Part of FSL (ID: 6.0.5:9e026117), first_mult_bcorr converts label images to an
    output image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FirstMultBcorrOutputs`).
    """
    cargs = first_mult_bcorr_cargs(params, execution)
    ret = first_mult_bcorr_outputs(params, execution)
    execution.run(cargs)
    return ret


def first_mult_bcorr(
    input_image: InputPathType,
    corrected_4d_labels: InputPathType,
    uncorrected_4d_labels: InputPathType,
    output_image: str,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> FirstMultBcorrOutputs:
    """
    Part of FSL (ID: 6.0.5:9e026117), first_mult_bcorr converts label images to an
    output image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Filename of original T1 input image.
        corrected_4d_labels: Filename of 4D image of individually corrected\
            labels.
        uncorrected_4d_labels: Filename of 4D image of uncorrected labels (with\
            boundaries).
        output_image: Output image name (3D label image).
        verbose_flag: Output F-stats to standard out.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstMultBcorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_MULT_BCORR_METADATA)
    params = first_mult_bcorr_params(input_image=input_image, corrected_4d_labels=corrected_4d_labels, uncorrected_4d_labels=uncorrected_4d_labels, output_image=output_image, verbose_flag=verbose_flag)
    return first_mult_bcorr_execute(params, execution)


__all__ = [
    "FIRST_MULT_BCORR_METADATA",
    "FirstMultBcorrOutputs",
    "FirstMultBcorrParameters",
    "first_mult_bcorr",
    "first_mult_bcorr_params",
]

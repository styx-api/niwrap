# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_INTRODUCTION_SH_METADATA = Metadata(
    id="ea6433a22b9e7d78a34c893edf721a839a07cf99.boutiques",
    name="antsIntroduction.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsIntroductionShParameters = typing.TypedDict('AntsIntroductionShParameters', {
    "__STYX_TYPE__": typing.Literal["antsIntroduction.sh"],
    "image_dimension": typing.Literal[2, 3],
    "reference_image": InputPathType,
    "input_image": InputPathType,
    "force": typing.NotRequired[typing.Literal[0, 1] | None],
    "labels_in_fixed_image_space": typing.NotRequired[str | None],
    "max_iterations": typing.NotRequired[int | None],
    "n4_bias_field_correction": typing.NotRequired[typing.Literal[0, 1] | None],
    "outprefix": typing.NotRequired[str | None],
    "quality_check": typing.NotRequired[typing.Literal[0, 1] | None],
    "similarity_metric": typing.NotRequired[str | None],
    "transformation_model": typing.NotRequired[str | None],
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
        "antsIntroduction.sh": ants_introduction_sh_cargs,
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


class AntsIntroductionShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_introduction_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ants_introduction_sh_params(
    image_dimension: typing.Literal[2, 3],
    reference_image: InputPathType,
    input_image: InputPathType,
    force: typing.Literal[0, 1] | None = 1,
    labels_in_fixed_image_space: str | None = None,
    max_iterations: int | None = None,
    n4_bias_field_correction: typing.Literal[0, 1] | None = 0,
    outprefix: str | None = None,
    quality_check: typing.Literal[0, 1] | None = 0,
    similarity_metric: str | None = None,
    transformation_model: str | None = None,
) -> AntsIntroductionShParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Image dimension for registration: 2 or 3.
        reference_image: Reference image for registration.
        input_image: Input image to be registered.
        force: Force script to proceed even if headers may be incompatible.
        labels_in_fixed_image_space: Labels in fixed image space to deform to\
            moving image.
        max_iterations: Maximum number of iterations.
        n4_bias_field_correction: N4 Bias Field Correction of moving image: 0\
            for off, 1 for on.
        outprefix: A prefix that is prepended to all output files.
        quality_check: Perform a Quality Check (QC) of the result: 0 for off, 1\
            for on.
        similarity_metric: Type of similarity metric used for registration.
        transformation_model: Type of transformation model used for\
            registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsIntroduction.sh",
        "image_dimension": image_dimension,
        "reference_image": reference_image,
        "input_image": input_image,
    }
    if force is not None:
        params["force"] = force
    if labels_in_fixed_image_space is not None:
        params["labels_in_fixed_image_space"] = labels_in_fixed_image_space
    if max_iterations is not None:
        params["max_iterations"] = max_iterations
    if n4_bias_field_correction is not None:
        params["n4_bias_field_correction"] = n4_bias_field_correction
    if outprefix is not None:
        params["outprefix"] = outprefix
    if quality_check is not None:
        params["quality_check"] = quality_check
    if similarity_metric is not None:
        params["similarity_metric"] = similarity_metric
    if transformation_model is not None:
        params["transformation_model"] = transformation_model
    return params


def ants_introduction_sh_cargs(
    params: AntsIntroductionShParameters,
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
    cargs.append("antsIntroduction.sh")
    cargs.extend([
        "-d",
        str(params.get("image_dimension"))
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("reference_image"))
    ])
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    if params.get("force") is not None:
        cargs.extend([
            "-f",
            str(params.get("force"))
        ])
    if params.get("labels_in_fixed_image_space") is not None:
        cargs.extend([
            "-l",
            params.get("labels_in_fixed_image_space")
        ])
    if params.get("max_iterations") is not None:
        cargs.extend([
            "-m",
            str(params.get("max_iterations"))
        ])
    if params.get("n4_bias_field_correction") is not None:
        cargs.extend([
            "-n",
            str(params.get("n4_bias_field_correction"))
        ])
    if params.get("outprefix") is not None:
        cargs.extend([
            "-o",
            params.get("outprefix")
        ])
    if params.get("quality_check") is not None:
        cargs.extend([
            "-q",
            str(params.get("quality_check"))
        ])
    if params.get("similarity_metric") is not None:
        cargs.extend([
            "-s",
            params.get("similarity_metric")
        ])
    if params.get("transformation_model") is not None:
        cargs.extend([
            "-t",
            params.get("transformation_model")
        ])
    return cargs


def ants_introduction_sh_outputs(
    params: AntsIntroductionShParameters,
    execution: Execution,
) -> AntsIntroductionShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsIntroductionShOutputs(
        root=execution.output_file("."),
    )
    return ret


def ants_introduction_sh_execute(
    params: AntsIntroductionShParameters,
    execution: Execution,
) -> AntsIntroductionShOutputs:
    """
    Script for registration using ANTS with compulsory and optional arguments.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsIntroductionShOutputs`).
    """
    cargs = ants_introduction_sh_cargs(params, execution)
    ret = ants_introduction_sh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def ants_introduction_sh(
    image_dimension: typing.Literal[2, 3],
    reference_image: InputPathType,
    input_image: InputPathType,
    force: typing.Literal[0, 1] | None = 1,
    labels_in_fixed_image_space: str | None = None,
    max_iterations: int | None = None,
    n4_bias_field_correction: typing.Literal[0, 1] | None = 0,
    outprefix: str | None = None,
    quality_check: typing.Literal[0, 1] | None = 0,
    similarity_metric: str | None = None,
    transformation_model: str | None = None,
    runner: Runner | None = None,
) -> AntsIntroductionShOutputs:
    """
    Script for registration using ANTS with compulsory and optional arguments.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Image dimension for registration: 2 or 3.
        reference_image: Reference image for registration.
        input_image: Input image to be registered.
        force: Force script to proceed even if headers may be incompatible.
        labels_in_fixed_image_space: Labels in fixed image space to deform to\
            moving image.
        max_iterations: Maximum number of iterations.
        n4_bias_field_correction: N4 Bias Field Correction of moving image: 0\
            for off, 1 for on.
        outprefix: A prefix that is prepended to all output files.
        quality_check: Perform a Quality Check (QC) of the result: 0 for off, 1\
            for on.
        similarity_metric: Type of similarity metric used for registration.
        transformation_model: Type of transformation model used for\
            registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsIntroductionShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_INTRODUCTION_SH_METADATA)
    params = ants_introduction_sh_params(image_dimension=image_dimension, reference_image=reference_image, input_image=input_image, force=force, labels_in_fixed_image_space=labels_in_fixed_image_space, max_iterations=max_iterations, n4_bias_field_correction=n4_bias_field_correction, outprefix=outprefix, quality_check=quality_check, similarity_metric=similarity_metric, transformation_model=transformation_model)
    return ants_introduction_sh_execute(params, execution)


__all__ = [
    "ANTS_INTRODUCTION_SH_METADATA",
    "AntsIntroductionShOutputs",
    "AntsIntroductionShParameters",
    "ants_introduction_sh",
    "ants_introduction_sh_params",
]

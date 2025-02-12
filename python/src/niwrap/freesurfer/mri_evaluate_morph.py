# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EVALUATE_MORPH_METADATA = Metadata(
    id="80d2aca899795eab8a40cb4bb8b3d34e4bf9970e.boutiques",
    name="mri_evaluate_morph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriEvaluateMorphParameters = typing.TypedDict('MriEvaluateMorphParameters', {
    "__STYX_TYPE__": typing.Literal["mri_evaluate_morph"],
    "xform_name": InputPathType,
    "segmentation_files": list[InputPathType],
    "output_file": str,
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
        "mri_evaluate_morph": mri_evaluate_morph_cargs,
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
        "mri_evaluate_morph": mri_evaluate_morph_outputs,
    }.get(t)


class MriEvaluateMorphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_evaluate_morph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlap_file: OutputPathType
    """The output file containing overlap results."""


def mri_evaluate_morph_params(
    xform_name: InputPathType,
    segmentation_files: list[InputPathType],
    output_file: str,
) -> MriEvaluateMorphParameters:
    """
    Build parameters.
    
    Args:
        xform_name: Transformation file name.
        segmentation_files: Input segmentation files.
        output_file: Output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_evaluate_morph",
        "xform_name": xform_name,
        "segmentation_files": segmentation_files,
        "output_file": output_file,
    }
    return params


def mri_evaluate_morph_cargs(
    params: MriEvaluateMorphParameters,
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
    cargs.append("mri_evaluate_morph")
    cargs.append(execution.input_file(params.get("xform_name")))
    cargs.extend([execution.input_file(f) for f in params.get("segmentation_files")])
    cargs.append(params.get("output_file"))
    return cargs


def mri_evaluate_morph_outputs(
    params: MriEvaluateMorphParameters,
    execution: Execution,
) -> MriEvaluateMorphOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriEvaluateMorphOutputs(
        root=execution.output_file("."),
        output_overlap_file=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_evaluate_morph_execute(
    params: MriEvaluateMorphParameters,
    execution: Execution,
) -> MriEvaluateMorphOutputs:
    """
    This program computes the overlap of a set of segmentations for a given morph
    using an xform file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriEvaluateMorphOutputs`).
    """
    cargs = mri_evaluate_morph_cargs(params, execution)
    ret = mri_evaluate_morph_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_evaluate_morph(
    xform_name: InputPathType,
    segmentation_files: list[InputPathType],
    output_file: str,
    runner: Runner | None = None,
) -> MriEvaluateMorphOutputs:
    """
    This program computes the overlap of a set of segmentations for a given morph
    using an xform file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        xform_name: Transformation file name.
        segmentation_files: Input segmentation files.
        output_file: Output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEvaluateMorphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EVALUATE_MORPH_METADATA)
    params = mri_evaluate_morph_params(xform_name=xform_name, segmentation_files=segmentation_files, output_file=output_file)
    return mri_evaluate_morph_execute(params, execution)


__all__ = [
    "MRI_EVALUATE_MORPH_METADATA",
    "MriEvaluateMorphOutputs",
    "MriEvaluateMorphParameters",
    "mri_evaluate_morph",
    "mri_evaluate_morph_params",
]

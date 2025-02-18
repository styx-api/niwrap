# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_PROBABILITY_METADATA = Metadata(
    id="e56f56942b5ff7cb28acb95c758d3ed822e1b2d5.boutiques",
    name="label-probability",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
LabelProbabilityParameters = typing.TypedDict('LabelProbabilityParameters', {
    "__STYX_TYPE__": typing.Literal["label-probability"],
    "label_maps": InputPathType,
    "probability_metric_out": str,
    "opt_exclude_unlabeled": bool,
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
        "label-probability": label_probability_cargs,
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
        "label-probability": label_probability_outputs,
    }.get(t)


class LabelProbabilityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_probability(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_metric_out: OutputPathType
    """the relative frequencies of each label at each vertex"""


def label_probability_params(
    label_maps: InputPathType,
    probability_metric_out: str,
    opt_exclude_unlabeled: bool = False,
) -> LabelProbabilityParameters:
    """
    Build parameters.
    
    Args:
        label_maps: label file containing individual label maps from many\
            subjects.
        probability_metric_out: the relative frequencies of each label at each\
            vertex.
        opt_exclude_unlabeled: don't make a probability map of the unlabeled\
            key.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label-probability",
        "label_maps": label_maps,
        "probability_metric_out": probability_metric_out,
        "opt_exclude_unlabeled": opt_exclude_unlabeled,
    }
    return params


def label_probability_cargs(
    params: LabelProbabilityParameters,
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
    cargs.append("wb_command")
    cargs.append("-label-probability")
    cargs.append(execution.input_file(params.get("label_maps")))
    cargs.append(params.get("probability_metric_out"))
    if params.get("opt_exclude_unlabeled"):
        cargs.append("-exclude-unlabeled")
    return cargs


def label_probability_outputs(
    params: LabelProbabilityParameters,
    execution: Execution,
) -> LabelProbabilityOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelProbabilityOutputs(
        root=execution.output_file("."),
        probability_metric_out=execution.output_file(params.get("probability_metric_out")),
    )
    return ret


def label_probability_execute(
    params: LabelProbabilityParameters,
    execution: Execution,
) -> LabelProbabilityOutputs:
    """
    Find frequency of surface labels.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that vertex,
    divided by the number of input maps.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelProbabilityOutputs`).
    """
    cargs = label_probability_cargs(params, execution)
    ret = label_probability_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def label_probability(
    label_maps: InputPathType,
    probability_metric_out: str,
    opt_exclude_unlabeled: bool = False,
    runner: Runner | None = None,
) -> LabelProbabilityOutputs:
    """
    Find frequency of surface labels.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that vertex,
    divided by the number of input maps.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_maps: label file containing individual label maps from many\
            subjects.
        probability_metric_out: the relative frequencies of each label at each\
            vertex.
        opt_exclude_unlabeled: don't make a probability map of the unlabeled\
            key.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelProbabilityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_PROBABILITY_METADATA)
    params = label_probability_params(label_maps=label_maps, probability_metric_out=probability_metric_out, opt_exclude_unlabeled=opt_exclude_unlabeled)
    return label_probability_execute(params, execution)


__all__ = [
    "LABEL_PROBABILITY_METADATA",
    "LabelProbabilityOutputs",
    "LabelProbabilityParameters",
    "label_probability",
    "label_probability_params",
]

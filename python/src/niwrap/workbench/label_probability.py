# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_PROBABILITY_METADATA = Metadata(
    id="b2f5704732f9b3382402cd967489df06d20de400.boutiques",
    name="label-probability",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class LabelProbabilityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_probability(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_metric_out: OutputPathType
    """the relative frequencies of each label at each vertex"""


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
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-probability")
    cargs.append(execution.input_file(label_maps))
    cargs.append(probability_metric_out)
    if opt_exclude_unlabeled:
        cargs.append("-exclude-unlabeled")
    ret = LabelProbabilityOutputs(
        root=execution.output_file("."),
        probability_metric_out=execution.output_file(probability_metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_PROBABILITY_METADATA",
    "LabelProbabilityOutputs",
    "label_probability",
]

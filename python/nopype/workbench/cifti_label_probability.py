# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_LABEL_PROBABILITY_METADATA = Metadata(
    id="038551e4acd1c3404c8269c1ef741afeddca6d17",
    name="cifti-label-probability",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiLabelProbabilityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_probability(...)`.
    """
    probability_dscalar_out: OutputPathType
    """the relative frequencies of each label at each vertex/voxel"""


def cifti_label_probability(
    runner: Runner,
    label_maps: InputPathType,
    probability_dscalar_out: InputPathType,
    opt_exclude_unlabeled: bool = False,
) -> CiftiLabelProbabilityOutputs:
    """
    FIND FREQUENCY OF CIFTI LABELS.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that
    vertex/voxel, divided by the number of input maps.
    
    Args:
        runner: Command runner
        label_maps: cifti dlabel file containing individual label maps from many
            subjects
        probability_dscalar_out: the relative frequencies of each label at each
            vertex/voxel
        opt_exclude_unlabeled: don't make a probability map of the unlabeled key
    Returns:
        NamedTuple of outputs (described in `CiftiLabelProbabilityOutputs`).
    """
    execution = runner.start_execution(CIFTI_LABEL_PROBABILITY_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-probability")
    cargs.append(execution.input_file(label_maps))
    cargs.append(execution.input_file(probability_dscalar_out))
    if opt_exclude_unlabeled:
        cargs.append("-exclude-unlabeled")
    ret = CiftiLabelProbabilityOutputs(
        probability_dscalar_out=execution.output_file(f"{probability_dscalar_out}"),
    )
    execution.run(cargs)
    return ret

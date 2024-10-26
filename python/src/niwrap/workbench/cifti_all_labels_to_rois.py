# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_ALL_LABELS_TO_ROIS_METADATA = Metadata(
    id="138d55df6e41806c01407f888e6e03dcf7e15eb0.boutiques",
    name="cifti-all-labels-to-rois",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class CiftiAllLabelsToRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_all_labels_to_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_all_labels_to_rois(
    label_in: InputPathType,
    map_: str,
    cifti_out: str,
    runner: Runner | None = None,
) -> CiftiAllLabelsToRoisOutputs:
    """
    Make rois from all labels in a cifti label map.
    
    The output cifti file is a dscalar file with a column (map) for each label
    in the specified input map, other than the ??? label, each of which contains
    a binary ROI of all brainordinates that are set to the corresponding label.
    
    Most of the time, specifying '1' for the <map> argument will do what is
    desired.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input cifti label file.
        map_: the number or name of the label map to use.
        cifti_out: the output cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiAllLabelsToRoisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ALL_LABELS_TO_ROIS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-all-labels-to-rois")
    cargs.append(execution.input_file(label_in))
    cargs.append(map_)
    cargs.append(cifti_out)
    ret = CiftiAllLabelsToRoisOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ALL_LABELS_TO_ROIS_METADATA",
    "CiftiAllLabelsToRoisOutputs",
    "cifti_all_labels_to_rois",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_MASK_METADATA = Metadata(
    id="c800dbf5e18e0d79c62bcbe9addf92ea1b420b84.boutiques",
    name="label-mask",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class LabelMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def label_mask(
    label: InputPathType,
    mask: InputPathType,
    label_out: str,
    opt_column_column: str | None = None,
    runner: Runner | None = None,
) -> LabelMaskOutputs:
    """
    Mask a label file.
    
    By default, the output label is a copy of the input label, but with the
    'unused' label wherever the mask metric is zero or negative. if -column is
    specified, the output contains only one column, the masked version of the
    specified input column.
    
    Author: Washington University School of Medicin
    
    Args:
        label: the label file to mask.
        mask: the mask metric.
        label_out: the output label file.
        opt_column_column: select a single column: the column number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MASK_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-mask")
    cargs.append(execution.input_file(label))
    cargs.append(execution.input_file(mask))
    cargs.append(label_out)
    if opt_column_column is not None:
        cargs.extend([
            "-column",
            opt_column_column
        ])
    ret = LabelMaskOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(label_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_MASK_METADATA",
    "LabelMaskOutputs",
    "label_mask",
]

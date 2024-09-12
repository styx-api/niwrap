# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA = Metadata(
    id="32140024ca7b96c0d11ae8c7eb35cc233f5f818a.boutiques",
    name="cifti-parcel-mapping-to-label",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class CiftiParcelMappingToLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_parcel_mapping_to_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dlabel_out: OutputPathType
    """the output dense label file"""


def cifti_parcel_mapping_to_label(
    cifti_in: InputPathType,
    direction: str,
    template_cifti: InputPathType,
    dlabel_out: str,
    runner: Runner | None = None,
) -> CiftiParcelMappingToLabelOutputs:
    """
    Create dlabel from parcellated file.
    
    This command will output a dlabel file, useful for doing the same
    parcellation to another dense file.
    
    For ptseries, pscalar, plabel, pconn, and pdconn, using COLUMN for
    <direction> will work.
    
    Author: Washington University School of Medicin
    
    Args:
        cifti_in: the input parcellated file.
        direction: which dimension to take the parcel map from, ROW or COLUMN.
        template_cifti: a cifti file with the desired dense mapping along\
            column.
        dlabel_out: the output dense label file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiParcelMappingToLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-parcel-mapping-to-label")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(execution.input_file(template_cifti))
    cargs.append(dlabel_out)
    ret = CiftiParcelMappingToLabelOutputs(
        root=execution.output_file("."),
        dlabel_out=execution.output_file(dlabel_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA",
    "CiftiParcelMappingToLabelOutputs",
    "cifti_parcel_mapping_to_label",
]

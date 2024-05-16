# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.784233

import typing

from ..styxdefs import *


CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA = Metadata(
    id="a1fd778c5bc3b0ad733e5b5d3eff6d13777340db",
    name="cifti-parcel-mapping-to-label",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiParcelMappingToLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_parcel_mapping_to_label(...)`.
    """
    dlabel_out: OutputPathType
    """the output dense label file"""


def cifti_parcel_mapping_to_label(
    runner: Runner,
    cifti_in: InputPathType,
    direction: str,
    template_cifti: InputPathType,
    dlabel_out: InputPathType,
) -> CiftiParcelMappingToLabelOutputs:
    """
    CREATE DLABEL FROM PARCELLATED FILE.
    
    This command will output a dlabel file, useful for doing the same
    parcellation to another dense file.
    
    For ptseries, pscalar, plabel, pconn, and pdconn, using COLUMN for
    <direction> will work.
    
    Args:
        runner: Command runner
        cifti_in: the input parcellated file
        direction: which dimension to take the parcel map from, ROW or COLUMN
        template_cifti: a cifti file with the desired dense mapping along column
        dlabel_out: the output dense label file
    Returns:
        NamedTuple of outputs (described in `CiftiParcelMappingToLabelOutputs`).
    """
    execution = runner.start_execution(CIFTI_PARCEL_MAPPING_TO_LABEL_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-parcel-mapping-to-label")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(execution.input_file(template_cifti))
    cargs.append(execution.input_file(dlabel_out))
    ret = CiftiParcelMappingToLabelOutputs(
        dlabel_out=execution.output_file(f"{dlabel_out}"),
    )
    execution.run(cargs)
    return ret

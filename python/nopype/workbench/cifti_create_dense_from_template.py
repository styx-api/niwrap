# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.874443

import typing

from ..styxdefs import *


CIFTI_CREATE_DENSE_FROM_TEMPLATE_METADATA = Metadata(
    id="b0746e4ae7eee0f3713a2a08648cc9c26aa44f25",
    name="cifti-create-dense-from-template",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiCreateDenseFromTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_dense_from_template(...)`.
    """
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_dense_from_template(
    runner: Runner,
    template_cifti: InputPathType,
    cifti_out: InputPathType,
    opt_volume_all_volume_in: InputPathType | None = None,
    opt_label_collision_action: str | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
) -> CiftiCreateDenseFromTemplateOutputs:
    """
    CREATE CIFTI WITH MATCHING DENSE MAP.
    
    This command helps you make a new dscalar, dtseries, or dlabel cifti file
    that matches the brainordinate space used in another cifti file. The
    template file must have the desired brainordinate space in the mapping along
    the column direction (for dtseries, dscalar, dlabel, and symmetric dconn
    this is always the case). All input cifti files must have a brain models
    mapping along column and use the same volume space and/or surface vertex
    count as the template for structures that they contain. If any input files
    contain label data, then input files with non-label data are not allowed,
    and the -series option may not be used.
    
    Any structure that isn't covered by an input is filled with zeros or the
    unlabeled key.
    
    The <structure> argument of -metric, -label or -volume must be one of the
    following:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT
    
    The argument to -unit must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN
    
    Args:
        runner: Command runner
        template_cifti: file to match brainordinates of
        cifti_out: the output cifti file
        opt_volume_all_volume_in: specify an input volume file for all voxel
            data: the input volume file
        opt_label_collision_action: how to handle conflicts between label keys:
            'ERROR', 'SURFACES_FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY' to
            match v1.4.2 and earlier
        opt_cifti_cifti_in: use input data from a cifti file: cifti file
            containing input data
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseFromTemplateOutputs`).
    """
    execution = runner.start_execution(CIFTI_CREATE_DENSE_FROM_TEMPLATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-dense-from-template")
    cargs.append(execution.input_file(template_cifti))
    cargs.append(execution.input_file(cifti_out))
    if opt_volume_all_volume_in is not None:
        cargs.extend(["-volume-all", execution.input_file(opt_volume_all_volume_in)])
    if opt_label_collision_action is not None:
        cargs.extend(["-label-collision", opt_label_collision_action])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiCreateDenseFromTemplateOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret

# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_CREATE_DENSE_SCALAR_METADATA = Metadata(
    id="ada827d0094bd6d1fbca1bec68f64381a83bad07",
    name="cifti-create-dense-scalar",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiCreateDenseScalarOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_dense_scalar(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_dense_scalar(
    runner: Runner,
    cifti_out: InputPathType,
    opt_left_metric_metric: InputPathType | None = None,
    opt_right_metric_metric: InputPathType | None = None,
    opt_cerebellum_metric_metric: InputPathType | None = None,
    opt_name_file_file: str | None = None,
) -> CiftiCreateDenseScalarOutputs:
    """
    cifti-create-dense-scalar by Washington University School of Medicin.
    
    CREATE A CIFTI DENSE SCALAR FILE.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti file. Map names will be
    taken from one of the input files. At least one component must be specified.
    
    See -volume-label-import and -volume-help for format details of label volume
    files. The structure-label-volume should have some of the label names from
    this list, all other label names will be ignored:
    
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
    THALAMUS_RIGHT.
    
    Args:
        runner: Command runner
        cifti_out: the output cifti file
        opt_left_metric_metric: metric for left surface: the metric file
        opt_right_metric_metric: metric for right surface: the metric file
        opt_cerebellum_metric_metric: metric for the cerebellum: the metric file
        opt_name_file_file: use a text file to set all map names: text file
            containing map names, one per line
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseScalarOutputs`).
    """
    execution = runner.start_execution(CIFTI_CREATE_DENSE_SCALAR_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-dense-scalar")
    cargs.append(execution.input_file(cifti_out))
    if opt_left_metric_metric is not None:
        cargs.extend(["-left-metric", execution.input_file(opt_left_metric_metric)])
    if opt_right_metric_metric is not None:
        cargs.extend(["-right-metric", execution.input_file(opt_right_metric_metric)])
    if opt_cerebellum_metric_metric is not None:
        cargs.extend(["-cerebellum-metric", execution.input_file(opt_cerebellum_metric_metric)])
    if opt_name_file_file is not None:
        cargs.extend(["-name-file", opt_name_file_file])
    ret = CiftiCreateDenseScalarOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret

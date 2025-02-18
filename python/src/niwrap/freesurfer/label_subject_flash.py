# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_SUBJECT_FLASH_METADATA = Metadata(
    id="6437bdd8443156c21638b016c6209131b9efc309.boutiques",
    name="label_subject_flash",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
LabelSubjectFlashParameters = typing.TypedDict('LabelSubjectFlashParameters', {
    "__STYX_TYPE__": typing.Literal["label_subject_flash"],
    "tissue_params": InputPathType,
    "norm_volume": InputPathType,
    "transform_file": InputPathType,
    "classifier_array": InputPathType,
    "aseg_output": str,
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
        "label_subject_flash": label_subject_flash_cargs,
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
        "label_subject_flash": label_subject_flash_outputs,
    }.get(t)


class LabelSubjectFlashOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_subject_flash(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aseg_outfile: OutputPathType
    """Automatic segmentation (aseg) output file"""


def label_subject_flash_params(
    tissue_params: InputPathType,
    norm_volume: InputPathType,
    transform_file: InputPathType,
    classifier_array: InputPathType,
    aseg_output: str,
) -> LabelSubjectFlashParameters:
    """
    Build parameters.
    
    Args:
        tissue_params: Path to the tissue parameter file for FLASH sequences.
        norm_volume: Path to the normalized T1 volume.
        transform_file: Talairach linear transform file.
        classifier_array: Path to the classifier array in GCA format.
        aseg_output: Output path for the automatic segmentation (aseg) file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label_subject_flash",
        "tissue_params": tissue_params,
        "norm_volume": norm_volume,
        "transform_file": transform_file,
        "classifier_array": classifier_array,
        "aseg_output": aseg_output,
    }
    return params


def label_subject_flash_cargs(
    params: LabelSubjectFlashParameters,
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
    cargs.append("mri_ca_label")
    cargs.extend([
        "-flash",
        execution.input_file(params.get("tissue_params"))
    ])
    cargs.append(execution.input_file(params.get("norm_volume")))
    cargs.append(execution.input_file(params.get("transform_file")))
    cargs.append(execution.input_file(params.get("classifier_array")))
    cargs.append(params.get("aseg_output"))
    return cargs


def label_subject_flash_outputs(
    params: LabelSubjectFlashParameters,
    execution: Execution,
) -> LabelSubjectFlashOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelSubjectFlashOutputs(
        root=execution.output_file("."),
        aseg_outfile=execution.output_file(params.get("aseg_output")),
    )
    return ret


def label_subject_flash_execute(
    params: LabelSubjectFlashParameters,
    execution: Execution,
) -> LabelSubjectFlashOutputs:
    """
    A tool for labeling brain structures in an MRI dataset using FLASH sequences and
    the FreeSurfer software.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelSubjectFlashOutputs`).
    """
    cargs = label_subject_flash_cargs(params, execution)
    ret = label_subject_flash_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def label_subject_flash(
    tissue_params: InputPathType,
    norm_volume: InputPathType,
    transform_file: InputPathType,
    classifier_array: InputPathType,
    aseg_output: str,
    runner: Runner | None = None,
) -> LabelSubjectFlashOutputs:
    """
    A tool for labeling brain structures in an MRI dataset using FLASH sequences and
    the FreeSurfer software.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        tissue_params: Path to the tissue parameter file for FLASH sequences.
        norm_volume: Path to the normalized T1 volume.
        transform_file: Talairach linear transform file.
        classifier_array: Path to the classifier array in GCA format.
        aseg_output: Output path for the automatic segmentation (aseg) file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelSubjectFlashOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_SUBJECT_FLASH_METADATA)
    params = label_subject_flash_params(tissue_params=tissue_params, norm_volume=norm_volume, transform_file=transform_file, classifier_array=classifier_array, aseg_output=aseg_output)
    return label_subject_flash_execute(params, execution)


__all__ = [
    "LABEL_SUBJECT_FLASH_METADATA",
    "LabelSubjectFlashOutputs",
    "LabelSubjectFlashParameters",
    "label_subject_flash",
    "label_subject_flash_params",
]

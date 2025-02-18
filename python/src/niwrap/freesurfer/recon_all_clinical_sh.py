# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RECON_ALL_CLINICAL_SH_METADATA = Metadata(
    id="38aa6da8e0504acf21091c65fc76ff6026418cb2.boutiques",
    name="recon-all-clinical.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ReconAllClinicalShParameters = typing.TypedDict('ReconAllClinicalShParameters', {
    "__STYX_TYPE__": typing.Literal["recon-all-clinical.sh"],
    "input_scan": InputPathType,
    "subject_id": str,
    "threads": int,
    "subject_dir": typing.NotRequired[str | None],
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
        "recon-all-clinical.sh": recon_all_clinical_sh_cargs,
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
    }.get(t)


class ReconAllClinicalShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `recon_all_clinical_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def recon_all_clinical_sh_params(
    input_scan: InputPathType,
    subject_id: str,
    threads: int,
    subject_dir: str | None = None,
) -> ReconAllClinicalShParameters:
    """
    Build parameters.
    
    Args:
        input_scan: Input scan file to be processed.
        subject_id: Identifier for the subject being processed.
        threads: Number of threads to use for processing.
        subject_dir: Optional subjects directory. Only necessary if the\
            environment variable SUBJECTS_DIR is not set or needs to be overridden.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "recon-all-clinical.sh",
        "input_scan": input_scan,
        "subject_id": subject_id,
        "threads": threads,
    }
    if subject_dir is not None:
        params["subject_dir"] = subject_dir
    return params


def recon_all_clinical_sh_cargs(
    params: ReconAllClinicalShParameters,
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
    cargs.append("recon-all-clinical.sh")
    cargs.append(execution.input_file(params.get("input_scan")))
    cargs.append(params.get("subject_id"))
    cargs.append(str(params.get("threads")))
    if params.get("subject_dir") is not None:
        cargs.append(params.get("subject_dir"))
    return cargs


def recon_all_clinical_sh_outputs(
    params: ReconAllClinicalShParameters,
    execution: Execution,
) -> ReconAllClinicalShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReconAllClinicalShOutputs(
        root=execution.output_file("."),
    )
    return ret


def recon_all_clinical_sh_execute(
    params: ReconAllClinicalShParameters,
    execution: Execution,
) -> ReconAllClinicalShOutputs:
    """
    Recon-all-like stream for processing clinical brain MRI scans of arbitrary
    orientation, resolution, and contrast using SynthSeg and SynthSR.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReconAllClinicalShOutputs`).
    """
    cargs = recon_all_clinical_sh_cargs(params, execution)
    ret = recon_all_clinical_sh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def recon_all_clinical_sh(
    input_scan: InputPathType,
    subject_id: str,
    threads: int,
    subject_dir: str | None = None,
    runner: Runner | None = None,
) -> ReconAllClinicalShOutputs:
    """
    Recon-all-like stream for processing clinical brain MRI scans of arbitrary
    orientation, resolution, and contrast using SynthSeg and SynthSR.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_scan: Input scan file to be processed.
        subject_id: Identifier for the subject being processed.
        threads: Number of threads to use for processing.
        subject_dir: Optional subjects directory. Only necessary if the\
            environment variable SUBJECTS_DIR is not set or needs to be overridden.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconAllClinicalShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECON_ALL_CLINICAL_SH_METADATA)
    params = recon_all_clinical_sh_params(input_scan=input_scan, subject_id=subject_id, threads=threads, subject_dir=subject_dir)
    return recon_all_clinical_sh_execute(params, execution)


__all__ = [
    "RECON_ALL_CLINICAL_SH_METADATA",
    "ReconAllClinicalShOutputs",
    "ReconAllClinicalShParameters",
    "recon_all_clinical_sh",
    "recon_all_clinical_sh_params",
]

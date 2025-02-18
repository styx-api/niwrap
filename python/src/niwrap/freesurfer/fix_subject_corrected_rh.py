# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIX_SUBJECT_CORRECTED_RH_METADATA = Metadata(
    id="52da465b947b94728415b771545cea34c0073071.boutiques",
    name="fix_subject_corrected-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FixSubjectCorrectedRhParameters = typing.TypedDict('FixSubjectCorrectedRhParameters', {
    "__STYX_TYPE__": typing.Literal["fix_subject_corrected-rh"],
    "subject_dir": str,
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
        "fix_subject_corrected-rh": fix_subject_corrected_rh_cargs,
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
        "fix_subject_corrected-rh": fix_subject_corrected_rh_outputs,
    }.get(t)


class FixSubjectCorrectedRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fix_subject_corrected_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    log_file: OutputPathType
    """Log file generated during the execution"""


def fix_subject_corrected_rh_params(
    subject_dir: str,
) -> FixSubjectCorrectedRhParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Path to the FreeSurfer subject directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fix_subject_corrected-rh",
        "subject_dir": subject_dir,
    }
    return params


def fix_subject_corrected_rh_cargs(
    params: FixSubjectCorrectedRhParameters,
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
    cargs.extend([
        "-rh",
        "fix_subject_corrected" + params.get("subject_dir")
    ])
    return cargs


def fix_subject_corrected_rh_outputs(
    params: FixSubjectCorrectedRhParameters,
    execution: Execution,
) -> FixSubjectCorrectedRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixSubjectCorrectedRhOutputs(
        root=execution.output_file("."),
        log_file=execution.output_file(params.get("subject_dir") + "/scripts_output.log"),
    )
    return ret


def fix_subject_corrected_rh_execute(
    params: FixSubjectCorrectedRhParameters,
    execution: Execution,
) -> FixSubjectCorrectedRhOutputs:
    """
    A tool related to FreeSurfer subject correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixSubjectCorrectedRhOutputs`).
    """
    cargs = fix_subject_corrected_rh_cargs(params, execution)
    ret = fix_subject_corrected_rh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fix_subject_corrected_rh(
    subject_dir: str,
    runner: Runner | None = None,
) -> FixSubjectCorrectedRhOutputs:
    """
    A tool related to FreeSurfer subject correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Path to the FreeSurfer subject directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FixSubjectCorrectedRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIX_SUBJECT_CORRECTED_RH_METADATA)
    params = fix_subject_corrected_rh_params(subject_dir=subject_dir)
    return fix_subject_corrected_rh_execute(params, execution)


__all__ = [
    "FIX_SUBJECT_CORRECTED_RH_METADATA",
    "FixSubjectCorrectedRhOutputs",
    "FixSubjectCorrectedRhParameters",
    "fix_subject_corrected_rh",
    "fix_subject_corrected_rh_params",
]

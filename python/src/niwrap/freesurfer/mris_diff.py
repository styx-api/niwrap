# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_DIFF_METADATA = Metadata(
    id="30172af00f20644762a6e2ce032311fb482cfc14.boutiques",
    name="mris_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisDiffParameters = typing.TypedDict('MrisDiffParameters', {
    "__STYX_TYPE__": typing.Literal["mris_diff"],
    "surface1": InputPathType,
    "surface2": InputPathType,
    "subject1": str,
    "subject2": str,
    "subj_dir1": typing.NotRequired[str | None],
    "subj_dir2": typing.NotRequired[str | None],
    "hemisphere": str,
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
        "mris_diff": mris_diff_cargs,
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


class MrisDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_diff_params(
    surface1: InputPathType,
    surface2: InputPathType,
    subject1: str,
    subject2: str,
    hemisphere: str,
    subj_dir1: str | None = None,
    subj_dir2: str | None = None,
) -> MrisDiffParameters:
    """
    Build parameters.
    
    Args:
        surface1: First surface file.
        surface2: Second surface file.
        subject1: Subject 1 name.
        subject2: Subject 2 name.
        hemisphere: Hemisphere (rh or lh).
        subj_dir1: Directory for Subject 1 (default is SUBJECTS_DIR).
        subj_dir2: Directory for Subject 2 (default is SUBJECTS_DIR).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_diff",
        "surface1": surface1,
        "surface2": surface2,
        "subject1": subject1,
        "subject2": subject2,
        "hemisphere": hemisphere,
    }
    if subj_dir1 is not None:
        params["subj_dir1"] = subj_dir1
    if subj_dir2 is not None:
        params["subj_dir2"] = subj_dir2
    return params


def mris_diff_cargs(
    params: MrisDiffParameters,
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
    cargs.append("mris_diff")
    cargs.append(execution.input_file(params.get("surface1")))
    cargs.append(execution.input_file(params.get("surface2")))
    cargs.extend([
        "--s1",
        params.get("subject1")
    ])
    cargs.extend([
        "--s2",
        params.get("subject2")
    ])
    if params.get("subj_dir1") is not None:
        cargs.extend([
            "--sd1",
            params.get("subj_dir1")
        ])
    if params.get("subj_dir2") is not None:
        cargs.extend([
            "--sd2",
            params.get("subj_dir2")
        ])
    cargs.extend([
        "--hemi",
        params.get("hemisphere")
    ])
    return cargs


def mris_diff_outputs(
    params: MrisDiffParameters,
    execution: Execution,
) -> MrisDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisDiffOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_diff_execute(
    params: MrisDiffParameters,
    execution: Execution,
) -> MrisDiffOutputs:
    """
    A tool for comparing differences between surface files in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisDiffOutputs`).
    """
    params = execution.params(params)
    cargs = mris_diff_cargs(params, execution)
    ret = mris_diff_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_diff(
    surface1: InputPathType,
    surface2: InputPathType,
    subject1: str,
    subject2: str,
    hemisphere: str,
    subj_dir1: str | None = None,
    subj_dir2: str | None = None,
    runner: Runner | None = None,
) -> MrisDiffOutputs:
    """
    A tool for comparing differences between surface files in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface1: First surface file.
        surface2: Second surface file.
        subject1: Subject 1 name.
        subject2: Subject 2 name.
        hemisphere: Hemisphere (rh or lh).
        subj_dir1: Directory for Subject 1 (default is SUBJECTS_DIR).
        subj_dir2: Directory for Subject 2 (default is SUBJECTS_DIR).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_DIFF_METADATA)
    params = mris_diff_params(
        surface1=surface1,
        surface2=surface2,
        subject1=subject1,
        subject2=subject2,
        subj_dir1=subj_dir1,
        subj_dir2=subj_dir2,
        hemisphere=hemisphere,
    )
    return mris_diff_execute(params, execution)


__all__ = [
    "MRIS_DIFF_METADATA",
    "MrisDiffOutputs",
    "MrisDiffParameters",
    "mris_diff",
    "mris_diff_params",
]

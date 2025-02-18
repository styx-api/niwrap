# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TALSEGPROB_METADATA = Metadata(
    id="ddb70e26f179b8729ed68da2fa771aa79e55b360.boutiques",
    name="talsegprob",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
TalsegprobParameters = typing.TypedDict('TalsegprobParameters', {
    "__STYX_TYPE__": typing.Literal["talsegprob"],
    "subjects_list": typing.NotRequired[list[str] | None],
    "fsgd_file": typing.NotRequired[InputPathType | None],
    "segmentation_number": typing.NotRequired[float | None],
    "second_segmentation_number": typing.NotRequired[float | None],
    "hippo_flag": bool,
    "left_hippo_flag": bool,
    "right_hippo_flag": bool,
    "segmentation_file": typing.NotRequired[InputPathType | None],
    "probability_output": typing.NotRequired[str | None],
    "vote_output": typing.NotRequired[str | None],
    "concat_output": typing.NotRequired[str | None],
    "xform_file": typing.NotRequired[InputPathType | None],
    "subjects_dir": typing.NotRequired[str | None],
    "tmpdir": typing.NotRequired[str | None],
    "nocleanup_flag": bool,
    "version_flag": bool,
    "echo_flag": bool,
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
        "talsegprob": talsegprob_cargs,
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
        "talsegprob": talsegprob_outputs,
    }.get(t)


class TalsegprobOutputs(typing.NamedTuple):
    """
    Output object returned when calling `talsegprob(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_output_file: OutputPathType | None
    """Probability output file."""
    vote_output_file: OutputPathType | None
    """Vote output file."""
    concat_output_file: OutputPathType | None
    """Concatenated output file."""


def talsegprob_params(
    subjects_list: list[str] | None = None,
    fsgd_file: InputPathType | None = None,
    segmentation_number: float | None = None,
    second_segmentation_number: float | None = None,
    hippo_flag: bool = False,
    left_hippo_flag: bool = False,
    right_hippo_flag: bool = False,
    segmentation_file: InputPathType | None = None,
    probability_output: str | None = None,
    vote_output: str | None = None,
    concat_output: str | None = None,
    xform_file: InputPathType | None = None,
    subjects_dir: str | None = None,
    tmpdir: str | None = None,
    nocleanup_flag: bool = False,
    version_flag: bool = False,
    echo_flag: bool = False,
) -> TalsegprobParameters:
    """
    Build parameters.
    
    Args:
        subjects_list: List of subjects to include in the analysis.
        fsgd_file: FSGD file to get subject list.
        segmentation_number: Segmentation number.
        second_segmentation_number: Second segmentation number.
        hippo_flag: Use segmentation numbers 17 and 53.
        left_hippo_flag: Use segmentation number 17.
        right_hippo_flag: Use segmentation number 53.
        segmentation_file: Use subject/mri/segfile.mgz instead of aseg.
        probability_output: Probability output file name.
        vote_output: Vote output file name.
        concat_output: Concatenated output file name.
        xform_file: Transformation file to use (default is talairach.xfm).
        subjects_dir: SUBJECTS_DIR to use instead of the one in the\
            environment.
        tmpdir: Temporary directory (implies --nocleanup).
        nocleanup_flag: Do not delete temporary directory.
        version_flag: Display script version information.
        echo_flag: Enable command echo, for debug.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "talsegprob",
        "hippo_flag": hippo_flag,
        "left_hippo_flag": left_hippo_flag,
        "right_hippo_flag": right_hippo_flag,
        "nocleanup_flag": nocleanup_flag,
        "version_flag": version_flag,
        "echo_flag": echo_flag,
    }
    if subjects_list is not None:
        params["subjects_list"] = subjects_list
    if fsgd_file is not None:
        params["fsgd_file"] = fsgd_file
    if segmentation_number is not None:
        params["segmentation_number"] = segmentation_number
    if second_segmentation_number is not None:
        params["second_segmentation_number"] = second_segmentation_number
    if segmentation_file is not None:
        params["segmentation_file"] = segmentation_file
    if probability_output is not None:
        params["probability_output"] = probability_output
    if vote_output is not None:
        params["vote_output"] = vote_output
    if concat_output is not None:
        params["concat_output"] = concat_output
    if xform_file is not None:
        params["xform_file"] = xform_file
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if tmpdir is not None:
        params["tmpdir"] = tmpdir
    return params


def talsegprob_cargs(
    params: TalsegprobParameters,
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
    cargs.append("talsegprob")
    if params.get("subjects_list") is not None:
        cargs.extend([
            "--subjects",
            *params.get("subjects_list")
        ])
    if params.get("fsgd_file") is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(params.get("fsgd_file"))
        ])
    if params.get("segmentation_number") is not None:
        cargs.extend([
            "--seg",
            str(params.get("segmentation_number"))
        ])
    if params.get("second_segmentation_number") is not None:
        cargs.extend([
            "<--seg",
            str(params.get("second_segmentation_number"))
        ])
    if params.get("hippo_flag"):
        cargs.append("--hippo")
    if params.get("left_hippo_flag"):
        cargs.append("--left-hippo")
    if params.get("right_hippo_flag"):
        cargs.append("--right-hippo")
    if params.get("segmentation_file") is not None:
        cargs.extend([
            "--segmentation",
            execution.input_file(params.get("segmentation_file"))
        ])
    if params.get("probability_output") is not None:
        cargs.extend([
            "--p",
            params.get("probability_output")
        ])
    if params.get("vote_output") is not None:
        cargs.extend([
            "--vote",
            params.get("vote_output")
        ])
    if params.get("concat_output") is not None:
        cargs.extend([
            "--c",
            params.get("concat_output")
        ])
    if params.get("xform_file") is not None:
        cargs.extend([
            "--xform",
            execution.input_file(params.get("xform_file"))
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sdir",
            params.get("subjects_dir")
        ])
    if params.get("tmpdir") is not None:
        cargs.extend([
            "--tmpdir",
            params.get("tmpdir")
        ])
    if params.get("nocleanup_flag"):
        cargs.append("--nocleanup")
    if params.get("version_flag"):
        cargs.append("--version")
    if params.get("echo_flag"):
        cargs.append("--echo")
    return cargs


def talsegprob_outputs(
    params: TalsegprobParameters,
    execution: Execution,
) -> TalsegprobOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TalsegprobOutputs(
        root=execution.output_file("."),
        probability_output_file=execution.output_file(params.get("probability_output")) if (params.get("probability_output") is not None) else None,
        vote_output_file=execution.output_file(params.get("vote_output")) if (params.get("vote_output") is not None) else None,
        concat_output_file=execution.output_file(params.get("concat_output")) if (params.get("concat_output") is not None) else None,
    )
    return ret


def talsegprob_execute(
    params: TalsegprobParameters,
    execution: Execution,
) -> TalsegprobOutputs:
    """
    Tool to create a binary probability volume from aseg.mgz based on segmentation
    numbers, resliced to talirach/MNI305/fsaverage space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TalsegprobOutputs`).
    """
    cargs = talsegprob_cargs(params, execution)
    ret = talsegprob_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def talsegprob(
    subjects_list: list[str] | None = None,
    fsgd_file: InputPathType | None = None,
    segmentation_number: float | None = None,
    second_segmentation_number: float | None = None,
    hippo_flag: bool = False,
    left_hippo_flag: bool = False,
    right_hippo_flag: bool = False,
    segmentation_file: InputPathType | None = None,
    probability_output: str | None = None,
    vote_output: str | None = None,
    concat_output: str | None = None,
    xform_file: InputPathType | None = None,
    subjects_dir: str | None = None,
    tmpdir: str | None = None,
    nocleanup_flag: bool = False,
    version_flag: bool = False,
    echo_flag: bool = False,
    runner: Runner | None = None,
) -> TalsegprobOutputs:
    """
    Tool to create a binary probability volume from aseg.mgz based on segmentation
    numbers, resliced to talirach/MNI305/fsaverage space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_list: List of subjects to include in the analysis.
        fsgd_file: FSGD file to get subject list.
        segmentation_number: Segmentation number.
        second_segmentation_number: Second segmentation number.
        hippo_flag: Use segmentation numbers 17 and 53.
        left_hippo_flag: Use segmentation number 17.
        right_hippo_flag: Use segmentation number 53.
        segmentation_file: Use subject/mri/segfile.mgz instead of aseg.
        probability_output: Probability output file name.
        vote_output: Vote output file name.
        concat_output: Concatenated output file name.
        xform_file: Transformation file to use (default is talairach.xfm).
        subjects_dir: SUBJECTS_DIR to use instead of the one in the\
            environment.
        tmpdir: Temporary directory (implies --nocleanup).
        nocleanup_flag: Do not delete temporary directory.
        version_flag: Display script version information.
        echo_flag: Enable command echo, for debug.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalsegprobOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALSEGPROB_METADATA)
    params = talsegprob_params(subjects_list=subjects_list, fsgd_file=fsgd_file, segmentation_number=segmentation_number, second_segmentation_number=second_segmentation_number, hippo_flag=hippo_flag, left_hippo_flag=left_hippo_flag, right_hippo_flag=right_hippo_flag, segmentation_file=segmentation_file, probability_output=probability_output, vote_output=vote_output, concat_output=concat_output, xform_file=xform_file, subjects_dir=subjects_dir, tmpdir=tmpdir, nocleanup_flag=nocleanup_flag, version_flag=version_flag, echo_flag=echo_flag)
    return talsegprob_execute(params, execution)


__all__ = [
    "TALSEGPROB_METADATA",
    "TalsegprobOutputs",
    "TalsegprobParameters",
    "talsegprob",
    "talsegprob_params",
]

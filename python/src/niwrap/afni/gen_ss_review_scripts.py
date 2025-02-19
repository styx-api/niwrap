# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GEN_SS_REVIEW_SCRIPTS_METADATA = Metadata(
    id="0b2bced52ccd788df5199b4d3c54d3385072af7d.boutiques",
    name="gen_ss_review_scripts",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


GenSsReviewScriptsParameters = typing.TypedDict('GenSsReviewScriptsParameters', {
    "__STYX_TYPE__": typing.Literal["gen_ss_review_scripts"],
    "subject_id": typing.NotRequired[str | None],
    "rm_trs": typing.NotRequired[float | None],
    "num_stim": typing.NotRequired[float | None],
    "mb_level": typing.NotRequired[float | None],
    "slice_pattern": typing.NotRequired[str | None],
    "motion_dset": typing.NotRequired[InputPathType | None],
    "outlier_dset": typing.NotRequired[InputPathType | None],
    "enorm_dset": typing.NotRequired[InputPathType | None],
    "mot_limit": typing.NotRequired[float | None],
    "out_limit": typing.NotRequired[float | None],
    "xmat_regress": typing.NotRequired[InputPathType | None],
    "xmat_uncensored": typing.NotRequired[InputPathType | None],
    "stats_dset": typing.NotRequired[InputPathType | None],
    "final_anat": typing.NotRequired[InputPathType | None],
    "final_view": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "verbosity": typing.NotRequired[float | None],
    "uvars_json": typing.NotRequired[InputPathType | None],
    "init_uvars_json": typing.NotRequired[InputPathType | None],
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
        "gen_ss_review_scripts": gen_ss_review_scripts_cargs,
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
        "gen_ss_review_scripts": gen_ss_review_scripts_outputs,
    }.get(t)


class GenSsReviewScriptsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gen_ss_review_scripts(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    basic_review: OutputPathType
    """Basic review script output"""
    driver_review: OutputPathType
    """Driver review script output"""
    driver_commands: OutputPathType
    """Driver commands script output"""


def gen_ss_review_scripts_params(
    subject_id: str | None = None,
    rm_trs: float | None = None,
    num_stim: float | None = None,
    mb_level: float | None = None,
    slice_pattern: str | None = None,
    motion_dset: InputPathType | None = None,
    outlier_dset: InputPathType | None = None,
    enorm_dset: InputPathType | None = None,
    mot_limit: float | None = None,
    out_limit: float | None = None,
    xmat_regress: InputPathType | None = None,
    xmat_uncensored: InputPathType | None = None,
    stats_dset: InputPathType | None = None,
    final_anat: InputPathType | None = None,
    final_view: str | None = None,
    prefix: str | None = None,
    verbosity: float | None = None,
    uvars_json: InputPathType | None = None,
    init_uvars_json: InputPathType | None = None,
) -> GenSsReviewScriptsParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject ID.
        rm_trs: Number of TRs removed per run.
        num_stim: Number of main stimulus classes.
        mb_level: Multiband slice acquisition level (>= 1).
        slice_pattern: Slice timing pattern.
        motion_dset: Motion parameters dataset.
        outlier_dset: Outlier fraction time series dataset.
        enorm_dset: Euclidean norm of motion parameters dataset.
        mot_limit: Motion limit.
        out_limit: Outlier fraction limit.
        xmat_regress: X-matrix file used in regression.
        xmat_uncensored: Un-censored X-matrix file.
        stats_dset: Output from 3dDeconvolve.
        final_anat: Final anatomical dataset.
        final_view: Final view of data (e.g. 'orig' or 'tlrc').
        prefix: Set the prefix for script names.
        verbosity: Set the verbosity level.
        uvars_json: Write JSON file of user variables dict.
        init_uvars_json: Initialize user variables from the given JSON file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gen_ss_review_scripts",
    }
    if subject_id is not None:
        params["subject_id"] = subject_id
    if rm_trs is not None:
        params["rm_trs"] = rm_trs
    if num_stim is not None:
        params["num_stim"] = num_stim
    if mb_level is not None:
        params["mb_level"] = mb_level
    if slice_pattern is not None:
        params["slice_pattern"] = slice_pattern
    if motion_dset is not None:
        params["motion_dset"] = motion_dset
    if outlier_dset is not None:
        params["outlier_dset"] = outlier_dset
    if enorm_dset is not None:
        params["enorm_dset"] = enorm_dset
    if mot_limit is not None:
        params["mot_limit"] = mot_limit
    if out_limit is not None:
        params["out_limit"] = out_limit
    if xmat_regress is not None:
        params["xmat_regress"] = xmat_regress
    if xmat_uncensored is not None:
        params["xmat_uncensored"] = xmat_uncensored
    if stats_dset is not None:
        params["stats_dset"] = stats_dset
    if final_anat is not None:
        params["final_anat"] = final_anat
    if final_view is not None:
        params["final_view"] = final_view
    if prefix is not None:
        params["prefix"] = prefix
    if verbosity is not None:
        params["verbosity"] = verbosity
    if uvars_json is not None:
        params["uvars_json"] = uvars_json
    if init_uvars_json is not None:
        params["init_uvars_json"] = init_uvars_json
    return params


def gen_ss_review_scripts_cargs(
    params: GenSsReviewScriptsParameters,
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
    cargs.append("gen_ss_review_scripts.py")
    if params.get("subject_id") is not None:
        cargs.extend([
            "-subj",
            params.get("subject_id")
        ])
    if params.get("rm_trs") is not None:
        cargs.extend([
            "-rm_trs",
            str(params.get("rm_trs"))
        ])
    if params.get("num_stim") is not None:
        cargs.extend([
            "-num_stim",
            str(params.get("num_stim"))
        ])
    if params.get("mb_level") is not None:
        cargs.extend([
            "-mb_level",
            str(params.get("mb_level"))
        ])
    if params.get("slice_pattern") is not None:
        cargs.extend([
            "-slice_pattern",
            params.get("slice_pattern")
        ])
    if params.get("motion_dset") is not None:
        cargs.extend([
            "-motion_dset",
            execution.input_file(params.get("motion_dset"))
        ])
    if params.get("outlier_dset") is not None:
        cargs.extend([
            "-outlier_dset",
            execution.input_file(params.get("outlier_dset"))
        ])
    if params.get("enorm_dset") is not None:
        cargs.extend([
            "-enorm_dset",
            execution.input_file(params.get("enorm_dset"))
        ])
    if params.get("mot_limit") is not None:
        cargs.extend([
            "-mot_limit",
            str(params.get("mot_limit"))
        ])
    if params.get("out_limit") is not None:
        cargs.extend([
            "-out_limit",
            str(params.get("out_limit"))
        ])
    if params.get("xmat_regress") is not None:
        cargs.extend([
            "-xmat_regress",
            execution.input_file(params.get("xmat_regress"))
        ])
    if params.get("xmat_uncensored") is not None:
        cargs.extend([
            "-xmat_uncensored",
            execution.input_file(params.get("xmat_uncensored"))
        ])
    if params.get("stats_dset") is not None:
        cargs.extend([
            "-stats_dset",
            execution.input_file(params.get("stats_dset"))
        ])
    if params.get("final_anat") is not None:
        cargs.extend([
            "-final_anat",
            execution.input_file(params.get("final_anat"))
        ])
    if params.get("final_view") is not None:
        cargs.extend([
            "-final_view",
            params.get("final_view")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("verbosity") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbosity"))
        ])
    if params.get("uvars_json") is not None:
        cargs.extend([
            "-write_uvars_json",
            execution.input_file(params.get("uvars_json"))
        ])
    if params.get("init_uvars_json") is not None:
        cargs.extend([
            "-init_uvars_json",
            execution.input_file(params.get("init_uvars_json"))
        ])
    return cargs


def gen_ss_review_scripts_outputs(
    params: GenSsReviewScriptsParameters,
    execution: Execution,
) -> GenSsReviewScriptsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GenSsReviewScriptsOutputs(
        root=execution.output_file("."),
        basic_review=execution.output_file("./@ss_review_basic"),
        driver_review=execution.output_file("./@ss_review_driver"),
        driver_commands=execution.output_file("./@ss_review_driver_commands"),
    )
    return ret


def gen_ss_review_scripts_execute(
    params: GenSsReviewScriptsParameters,
    execution: Execution,
) -> GenSsReviewScriptsOutputs:
    """
    Generate single subject analysis review scripts.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GenSsReviewScriptsOutputs`).
    """
    params = execution.params(params)
    cargs = gen_ss_review_scripts_cargs(params, execution)
    ret = gen_ss_review_scripts_outputs(params, execution)
    execution.run(cargs)
    return ret


def gen_ss_review_scripts(
    subject_id: str | None = None,
    rm_trs: float | None = None,
    num_stim: float | None = None,
    mb_level: float | None = None,
    slice_pattern: str | None = None,
    motion_dset: InputPathType | None = None,
    outlier_dset: InputPathType | None = None,
    enorm_dset: InputPathType | None = None,
    mot_limit: float | None = None,
    out_limit: float | None = None,
    xmat_regress: InputPathType | None = None,
    xmat_uncensored: InputPathType | None = None,
    stats_dset: InputPathType | None = None,
    final_anat: InputPathType | None = None,
    final_view: str | None = None,
    prefix: str | None = None,
    verbosity: float | None = None,
    uvars_json: InputPathType | None = None,
    init_uvars_json: InputPathType | None = None,
    runner: Runner | None = None,
) -> GenSsReviewScriptsOutputs:
    """
    Generate single subject analysis review scripts.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        subject_id: Subject ID.
        rm_trs: Number of TRs removed per run.
        num_stim: Number of main stimulus classes.
        mb_level: Multiband slice acquisition level (>= 1).
        slice_pattern: Slice timing pattern.
        motion_dset: Motion parameters dataset.
        outlier_dset: Outlier fraction time series dataset.
        enorm_dset: Euclidean norm of motion parameters dataset.
        mot_limit: Motion limit.
        out_limit: Outlier fraction limit.
        xmat_regress: X-matrix file used in regression.
        xmat_uncensored: Un-censored X-matrix file.
        stats_dset: Output from 3dDeconvolve.
        final_anat: Final anatomical dataset.
        final_view: Final view of data (e.g. 'orig' or 'tlrc').
        prefix: Set the prefix for script names.
        verbosity: Set the verbosity level.
        uvars_json: Write JSON file of user variables dict.
        init_uvars_json: Initialize user variables from the given JSON file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GenSsReviewScriptsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GEN_SS_REVIEW_SCRIPTS_METADATA)
    params = gen_ss_review_scripts_params(
        subject_id=subject_id,
        rm_trs=rm_trs,
        num_stim=num_stim,
        mb_level=mb_level,
        slice_pattern=slice_pattern,
        motion_dset=motion_dset,
        outlier_dset=outlier_dset,
        enorm_dset=enorm_dset,
        mot_limit=mot_limit,
        out_limit=out_limit,
        xmat_regress=xmat_regress,
        xmat_uncensored=xmat_uncensored,
        stats_dset=stats_dset,
        final_anat=final_anat,
        final_view=final_view,
        prefix=prefix,
        verbosity=verbosity,
        uvars_json=uvars_json,
        init_uvars_json=init_uvars_json,
    )
    return gen_ss_review_scripts_execute(params, execution)


__all__ = [
    "GEN_SS_REVIEW_SCRIPTS_METADATA",
    "GenSsReviewScriptsOutputs",
    "GenSsReviewScriptsParameters",
    "gen_ss_review_scripts",
    "gen_ss_review_scripts_params",
]

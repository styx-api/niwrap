# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CONCAT_METADATA = Metadata(
    id="fb2ef824b603c3920fd8a70883332abeb5fd81d4.boutiques",
    name="mri_concat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriConcatParameters = typing.TypedDict('MriConcatParameters', {
    "__STYX_TYPE__": typing.Literal["mri_concat"],
    "input_files": list[InputPathType],
    "output_file": str,
    "file_list": typing.NotRequired[str | None],
    "paired_sum": bool,
    "paired_avg": bool,
    "paired_diff": bool,
    "paired_diff_norm": bool,
    "paired_diff_norm1": bool,
    "paired_diff_norm2": bool,
    "norm_mean": bool,
    "norm1": bool,
    "matrix": typing.NotRequired[InputPathType | None],
    "frame_weight": typing.NotRequired[InputPathType | None],
    "norm_weight": bool,
    "group_mean": typing.NotRequired[float | None],
    "combine": bool,
    "keep_datatype": bool,
    "abs": bool,
    "pos": bool,
    "neg": bool,
    "mean": bool,
    "median": bool,
    "mean_div_n": bool,
    "sum": bool,
    "var": bool,
    "std": bool,
    "max": bool,
    "max_index": bool,
    "max_index_prune": bool,
    "max_index_add": typing.NotRequired[float | None],
    "min": bool,
    "replicate_times": typing.NotRequired[float | None],
    "fnorm": bool,
    "conjunction": bool,
    "vote": bool,
    "sort": bool,
    "temporal_ar1": typing.NotRequired[float | None],
    "prune": bool,
    "pca": bool,
    "pca_mask": typing.NotRequired[InputPathType | None],
    "scm": bool,
    "zconcat": typing.NotRequired[str | None],
    "max_bonfcor": bool,
    "multiply": typing.NotRequired[float | None],
    "add": typing.NotRequired[float | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "rms": bool,
    "no_check": bool,
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
        "mri_concat": mri_concat_cargs,
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


class MriConcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_concat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_concat_params(
    input_files: list[InputPathType],
    output_file: str,
    file_list: str | None = None,
    paired_sum: bool = False,
    paired_avg: bool = False,
    paired_diff: bool = False,
    paired_diff_norm: bool = False,
    paired_diff_norm1: bool = False,
    paired_diff_norm2: bool = False,
    norm_mean: bool = False,
    norm1: bool = False,
    matrix: InputPathType | None = None,
    frame_weight: InputPathType | None = None,
    norm_weight: bool = False,
    group_mean: float | None = None,
    combine: bool = False,
    keep_datatype: bool = False,
    abs_: bool = False,
    pos: bool = False,
    neg: bool = False,
    mean: bool = False,
    median: bool = False,
    mean_div_n: bool = False,
    sum_: bool = False,
    var: bool = False,
    std: bool = False,
    max_: bool = False,
    max_index: bool = False,
    max_index_prune: bool = False,
    max_index_add: float | None = None,
    min_: bool = False,
    replicate_times: float | None = None,
    fnorm: bool = False,
    conjunction: bool = False,
    vote: bool = False,
    sort: bool = False,
    temporal_ar1: float | None = None,
    prune: bool = False,
    pca: bool = False,
    pca_mask: InputPathType | None = None,
    scm: bool = False,
    zconcat: str | None = None,
    max_bonfcor: bool = False,
    multiply: float | None = None,
    add: float | None = None,
    mask_file: InputPathType | None = None,
    rms: bool = False,
    no_check: bool = False,
) -> MriConcatParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input image files (e.g. file1.mgh file2.mgh ...).
        output_file: Output file name (e.g. output.mgh).
        file_list: List file containing a text list of files to process (up to\
            400000 files).
        paired_sum: Compute paired sum (1+2, 3+4, etc).
        paired_avg: Compute paired average (1+2, 3+4, etc).
        paired_diff: Compute paired difference (1-2, 3-4, etc).
        paired_diff_norm: Compute paired difference normalized by TP1,2\
            average.
        paired_diff_norm1: Compute paired difference normalized by TP1.
        paired_diff_norm2: Compute paired difference normalized by TP2.
        norm_mean: Normalize frames by mean of all time points.
        norm1: Normalize frames by first time point (TP1).
        matrix: Multiply by matrix from ASCII file.
        frame_weight: Weight each frame by values in ASCII file (one value per\
            frame).
        norm_weight: Normalize frames to sum to 1 after weighting.
        group_mean: Create matrix to average Ng groups, Nper=Ntot/Ng.
        combine: Average frames from non-zero voxels.
        keep_datatype: Write output in the same datatype as input (default is\
            Float format).
        abs_: Take absolute value of input.
        pos: Set input negatives to 0.
        neg: Set input positives to 0.
        mean: Compute mean of concatenated volumes.
        median: Compute median of concatenated volumes.
        mean_div_n: Compute mean divided by number of frames.
        sum_: Compute sum of concatenated volumes.
        var: Compute variance of concatenated volumes.
        std: Compute standard deviation of concatenated volumes.
        max_: Compute maximum of concatenated volumes.
        max_index: Compute index of maximum of concatenated volumes.
        max_index_prune: Set max index to 0 where all frames are 0.
        max_index_add: Add value to non-zero max indices.
        min_: Compute minimum of concatenated volumes.
        replicate_times: Replicate N times over frames.
        fnorm: Normalize time series at each voxel.
        conjunction: Compute voxel-wise conjunction of concatenated volumes.
        vote: Most frequent value at each voxel and fraction of occurrences.
        sort: Sort each voxel by ascending frame value.
        temporal_ar1: Compute temporal AR1 with degree of freedom adjustment.
        prune: Set voxel value to 0 unless all frames are non-zero.
        pca: Compute and output principal component analysis (PCA).
        pca_mask: Mask used to select voxels for PCA (mask > 0.5).
        scm: Compute spatial covariance matrix.
        zconcat: Concatenate in slice direction skipping nskip slices.
        max_bonfcor: Compute maximum and Bonferroni correct.
        multiply: Multiply volumes by value.
        add: Add value to volumes.
        mask_file: Mask file used with vote or sort.
        rms: Compute root mean square of concatenated volumes.
        no_check: Do not check inputs.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_concat",
        "input_files": input_files,
        "output_file": output_file,
        "paired_sum": paired_sum,
        "paired_avg": paired_avg,
        "paired_diff": paired_diff,
        "paired_diff_norm": paired_diff_norm,
        "paired_diff_norm1": paired_diff_norm1,
        "paired_diff_norm2": paired_diff_norm2,
        "norm_mean": norm_mean,
        "norm1": norm1,
        "norm_weight": norm_weight,
        "combine": combine,
        "keep_datatype": keep_datatype,
        "abs": abs_,
        "pos": pos,
        "neg": neg,
        "mean": mean,
        "median": median,
        "mean_div_n": mean_div_n,
        "sum": sum_,
        "var": var,
        "std": std,
        "max": max_,
        "max_index": max_index,
        "max_index_prune": max_index_prune,
        "min": min_,
        "fnorm": fnorm,
        "conjunction": conjunction,
        "vote": vote,
        "sort": sort,
        "prune": prune,
        "pca": pca,
        "scm": scm,
        "max_bonfcor": max_bonfcor,
        "rms": rms,
        "no_check": no_check,
    }
    if file_list is not None:
        params["file_list"] = file_list
    if matrix is not None:
        params["matrix"] = matrix
    if frame_weight is not None:
        params["frame_weight"] = frame_weight
    if group_mean is not None:
        params["group_mean"] = group_mean
    if max_index_add is not None:
        params["max_index_add"] = max_index_add
    if replicate_times is not None:
        params["replicate_times"] = replicate_times
    if temporal_ar1 is not None:
        params["temporal_ar1"] = temporal_ar1
    if pca_mask is not None:
        params["pca_mask"] = pca_mask
    if zconcat is not None:
        params["zconcat"] = zconcat
    if multiply is not None:
        params["multiply"] = multiply
    if add is not None:
        params["add"] = add
    if mask_file is not None:
        params["mask_file"] = mask_file
    return params


def mri_concat_cargs(
    params: MriConcatParameters,
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
    cargs.append("mri_concat")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    if params.get("file_list") is not None:
        cargs.extend([
            "--f",
            params.get("file_list")
        ])
    if params.get("paired_sum"):
        cargs.append("--paired-sum")
    if params.get("paired_avg"):
        cargs.append("--paired-avg")
    if params.get("paired_diff"):
        cargs.append("--paired-diff")
    if params.get("paired_diff_norm"):
        cargs.append("--paired-diff-norm")
    if params.get("paired_diff_norm1"):
        cargs.append("--paired-diff-norm1")
    if params.get("paired_diff_norm2"):
        cargs.append("--paired-diff-norm2")
    if params.get("norm_mean"):
        cargs.append("--norm-mean")
    if params.get("norm1"):
        cargs.append("--norm1")
    if params.get("matrix") is not None:
        cargs.extend([
            "--mtx",
            execution.input_file(params.get("matrix"))
        ])
    if params.get("frame_weight") is not None:
        cargs.extend([
            "--w",
            execution.input_file(params.get("frame_weight"))
        ])
    if params.get("norm_weight"):
        cargs.append("--wn")
    if params.get("group_mean") is not None:
        cargs.extend([
            "--gmean",
            str(params.get("group_mean"))
        ])
    if params.get("combine"):
        cargs.append("--combine")
    if params.get("keep_datatype"):
        cargs.append("--keep-datatype")
    if params.get("abs"):
        cargs.append("--abs")
    if params.get("pos"):
        cargs.append("--pos")
    if params.get("neg"):
        cargs.append("--neg")
    if params.get("mean"):
        cargs.append("--mean")
    if params.get("median"):
        cargs.append("--median")
    if params.get("mean_div_n"):
        cargs.append("--mean-div-n")
    if params.get("sum"):
        cargs.append("--sum")
    if params.get("var"):
        cargs.append("--var")
    if params.get("std"):
        cargs.append("--std")
    if params.get("max"):
        cargs.append("--max")
    if params.get("max_index"):
        cargs.append("--max-index")
    if params.get("max_index_prune"):
        cargs.append("--max-index-prune")
    if params.get("max_index_add") is not None:
        cargs.extend([
            "--max-index-add",
            str(params.get("max_index_add"))
        ])
    if params.get("min"):
        cargs.append("--min")
    if params.get("replicate_times") is not None:
        cargs.extend([
            "--rep",
            str(params.get("replicate_times"))
        ])
    if params.get("fnorm"):
        cargs.append("--fnorm")
    if params.get("conjunction"):
        cargs.append("--conjunct")
    if params.get("vote"):
        cargs.append("--vote")
    if params.get("sort"):
        cargs.append("--sort")
    if params.get("temporal_ar1") is not None:
        cargs.extend([
            "--tar1",
            str(params.get("temporal_ar1"))
        ])
    if params.get("prune"):
        cargs.append("--prune")
    if params.get("pca"):
        cargs.append("--pca")
    if params.get("pca_mask") is not None:
        cargs.extend([
            "--pca-mask",
            execution.input_file(params.get("pca_mask"))
        ])
    if params.get("scm"):
        cargs.append("--scm")
    if params.get("zconcat") is not None:
        cargs.extend([
            "--zconcat",
            params.get("zconcat")
        ])
    if params.get("max_bonfcor"):
        cargs.append("--max-bonfcor")
    if params.get("multiply") is not None:
        cargs.extend([
            "--mul",
            str(params.get("multiply"))
        ])
    if params.get("add") is not None:
        cargs.extend([
            "--add",
            str(params.get("add"))
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("rms"):
        cargs.append("--rms")
    if params.get("no_check"):
        cargs.append("--no-check")
    return cargs


def mri_concat_outputs(
    params: MriConcatParameters,
    execution: Execution,
) -> MriConcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriConcatOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_concat_execute(
    params: MriConcatParameters,
    execution: Execution,
) -> MriConcatOutputs:
    """
    Concatenates input data sets.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriConcatOutputs`).
    """
    cargs = mri_concat_cargs(params, execution)
    ret = mri_concat_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_concat(
    input_files: list[InputPathType],
    output_file: str,
    file_list: str | None = None,
    paired_sum: bool = False,
    paired_avg: bool = False,
    paired_diff: bool = False,
    paired_diff_norm: bool = False,
    paired_diff_norm1: bool = False,
    paired_diff_norm2: bool = False,
    norm_mean: bool = False,
    norm1: bool = False,
    matrix: InputPathType | None = None,
    frame_weight: InputPathType | None = None,
    norm_weight: bool = False,
    group_mean: float | None = None,
    combine: bool = False,
    keep_datatype: bool = False,
    abs_: bool = False,
    pos: bool = False,
    neg: bool = False,
    mean: bool = False,
    median: bool = False,
    mean_div_n: bool = False,
    sum_: bool = False,
    var: bool = False,
    std: bool = False,
    max_: bool = False,
    max_index: bool = False,
    max_index_prune: bool = False,
    max_index_add: float | None = None,
    min_: bool = False,
    replicate_times: float | None = None,
    fnorm: bool = False,
    conjunction: bool = False,
    vote: bool = False,
    sort: bool = False,
    temporal_ar1: float | None = None,
    prune: bool = False,
    pca: bool = False,
    pca_mask: InputPathType | None = None,
    scm: bool = False,
    zconcat: str | None = None,
    max_bonfcor: bool = False,
    multiply: float | None = None,
    add: float | None = None,
    mask_file: InputPathType | None = None,
    rms: bool = False,
    no_check: bool = False,
    runner: Runner | None = None,
) -> MriConcatOutputs:
    """
    Concatenates input data sets.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input image files (e.g. file1.mgh file2.mgh ...).
        output_file: Output file name (e.g. output.mgh).
        file_list: List file containing a text list of files to process (up to\
            400000 files).
        paired_sum: Compute paired sum (1+2, 3+4, etc).
        paired_avg: Compute paired average (1+2, 3+4, etc).
        paired_diff: Compute paired difference (1-2, 3-4, etc).
        paired_diff_norm: Compute paired difference normalized by TP1,2\
            average.
        paired_diff_norm1: Compute paired difference normalized by TP1.
        paired_diff_norm2: Compute paired difference normalized by TP2.
        norm_mean: Normalize frames by mean of all time points.
        norm1: Normalize frames by first time point (TP1).
        matrix: Multiply by matrix from ASCII file.
        frame_weight: Weight each frame by values in ASCII file (one value per\
            frame).
        norm_weight: Normalize frames to sum to 1 after weighting.
        group_mean: Create matrix to average Ng groups, Nper=Ntot/Ng.
        combine: Average frames from non-zero voxels.
        keep_datatype: Write output in the same datatype as input (default is\
            Float format).
        abs_: Take absolute value of input.
        pos: Set input negatives to 0.
        neg: Set input positives to 0.
        mean: Compute mean of concatenated volumes.
        median: Compute median of concatenated volumes.
        mean_div_n: Compute mean divided by number of frames.
        sum_: Compute sum of concatenated volumes.
        var: Compute variance of concatenated volumes.
        std: Compute standard deviation of concatenated volumes.
        max_: Compute maximum of concatenated volumes.
        max_index: Compute index of maximum of concatenated volumes.
        max_index_prune: Set max index to 0 where all frames are 0.
        max_index_add: Add value to non-zero max indices.
        min_: Compute minimum of concatenated volumes.
        replicate_times: Replicate N times over frames.
        fnorm: Normalize time series at each voxel.
        conjunction: Compute voxel-wise conjunction of concatenated volumes.
        vote: Most frequent value at each voxel and fraction of occurrences.
        sort: Sort each voxel by ascending frame value.
        temporal_ar1: Compute temporal AR1 with degree of freedom adjustment.
        prune: Set voxel value to 0 unless all frames are non-zero.
        pca: Compute and output principal component analysis (PCA).
        pca_mask: Mask used to select voxels for PCA (mask > 0.5).
        scm: Compute spatial covariance matrix.
        zconcat: Concatenate in slice direction skipping nskip slices.
        max_bonfcor: Compute maximum and Bonferroni correct.
        multiply: Multiply volumes by value.
        add: Add value to volumes.
        mask_file: Mask file used with vote or sort.
        rms: Compute root mean square of concatenated volumes.
        no_check: Do not check inputs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONCAT_METADATA)
    params = mri_concat_params(input_files=input_files, output_file=output_file, file_list=file_list, paired_sum=paired_sum, paired_avg=paired_avg, paired_diff=paired_diff, paired_diff_norm=paired_diff_norm, paired_diff_norm1=paired_diff_norm1, paired_diff_norm2=paired_diff_norm2, norm_mean=norm_mean, norm1=norm1, matrix=matrix, frame_weight=frame_weight, norm_weight=norm_weight, group_mean=group_mean, combine=combine, keep_datatype=keep_datatype, abs_=abs_, pos=pos, neg=neg, mean=mean, median=median, mean_div_n=mean_div_n, sum_=sum_, var=var, std=std, max_=max_, max_index=max_index, max_index_prune=max_index_prune, max_index_add=max_index_add, min_=min_, replicate_times=replicate_times, fnorm=fnorm, conjunction=conjunction, vote=vote, sort=sort, temporal_ar1=temporal_ar1, prune=prune, pca=pca, pca_mask=pca_mask, scm=scm, zconcat=zconcat, max_bonfcor=max_bonfcor, multiply=multiply, add=add, mask_file=mask_file, rms=rms, no_check=no_check)
    return mri_concat_execute(params, execution)


__all__ = [
    "MRI_CONCAT_METADATA",
    "MriConcatOutputs",
    "MriConcatParameters",
    "mri_concat",
    "mri_concat_params",
]

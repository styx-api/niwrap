# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__RADIAL_CORRELATE_METADATA = Metadata(
    id="1cbb44d20d4e3ca23ba7981bb4c49932fce75bf0.boutiques",
    name="@radial_correlate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VRadialCorrelateParameters = typing.TypedDict('VRadialCorrelateParameters', {
    "__STYX_TYPE__": typing.Literal["@radial_correlate"],
    "input_files": list[InputPathType],
    "results_dir": typing.NotRequired[str | None],
    "do_corr": typing.NotRequired[str | None],
    "do_clust": typing.NotRequired[str | None],
    "mask_dset": typing.NotRequired[InputPathType | None],
    "cthresh": typing.NotRequired[float | None],
    "frac_limit": typing.NotRequired[float | None],
    "sphere_rad": typing.NotRequired[float | None],
    "use_3dmerge": typing.NotRequired[str | None],
    "percentile": typing.NotRequired[float | None],
    "min_thr": typing.NotRequired[float | None],
    "nfirst": typing.NotRequired[float | None],
    "ver": bool,
    "verbose": bool,
    "help": bool,
    "hist": bool,
    "corr_mask": typing.NotRequired[str | None],
    "do_clean": typing.NotRequired[str | None],
    "polort": typing.NotRequired[float | None],
    "merge_frad": typing.NotRequired[float | None],
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
        "@radial_correlate": v__radial_correlate_cargs,
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
        "@radial_correlate": v__radial_correlate_outputs,
    }.get(t)


class VRadialCorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__radial_correlate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corr_volumes: OutputPathType | None
    """Directory containing correlation volumes"""


def v__radial_correlate_params(
    input_files: list[InputPathType],
    results_dir: str | None = None,
    do_corr: str | None = None,
    do_clust: str | None = None,
    mask_dset: InputPathType | None = None,
    cthresh: float | None = None,
    frac_limit: float | None = None,
    sphere_rad: float | None = None,
    use_3dmerge: str | None = None,
    percentile: float | None = None,
    min_thr: float | None = None,
    nfirst: float | None = None,
    ver: bool = False,
    verbose: bool = False,
    help_: bool = False,
    hist: bool = False,
    corr_mask: str | None = None,
    do_clean: str | None = None,
    polort: float | None = None,
    merge_frad: float | None = None,
) -> VRadialCorrelateParameters:
    """
    Build parameters.
    
    Args:
        input_files: A list of EPI datasets.
        results_dir: Results directory for correlations.
        do_corr: Create correlation volumes (yes/no).
        do_clust: Cluster correlation volumes (yes/no).
        mask_dset: Specify a mask dataset to replace automask.
        cthresh: Threshold on correlation values.
        frac_limit: Minimum mask fraction surviving cluster.
        sphere_rad: Generate correlations within voxel spheres.
        use_3dmerge: Use 3dmerge rather than 3dLocalstat (yes/no).
        percentile: Percentile to use as threshold.
        min_thr: Minimum percentile threshold to be considered.
        nfirst: Number of initial TRs to remove.
        ver: Show version number.
        verbose: Make verbose: set echo.
        help_: Show help.
        hist: Show modification history.
        corr_mask: Mask time series before correlation blurring (yes/no).
        do_clean: Clean up at end, leaving only correlations (yes/no).
        polort: Detrend time series with given polynomial degree.
        merge_frad: Specify a radius fraction for 3dmerge blurring.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@radial_correlate",
        "input_files": input_files,
        "ver": ver,
        "verbose": verbose,
        "help": help_,
        "hist": hist,
    }
    if results_dir is not None:
        params["results_dir"] = results_dir
    if do_corr is not None:
        params["do_corr"] = do_corr
    if do_clust is not None:
        params["do_clust"] = do_clust
    if mask_dset is not None:
        params["mask_dset"] = mask_dset
    if cthresh is not None:
        params["cthresh"] = cthresh
    if frac_limit is not None:
        params["frac_limit"] = frac_limit
    if sphere_rad is not None:
        params["sphere_rad"] = sphere_rad
    if use_3dmerge is not None:
        params["use_3dmerge"] = use_3dmerge
    if percentile is not None:
        params["percentile"] = percentile
    if min_thr is not None:
        params["min_thr"] = min_thr
    if nfirst is not None:
        params["nfirst"] = nfirst
    if corr_mask is not None:
        params["corr_mask"] = corr_mask
    if do_clean is not None:
        params["do_clean"] = do_clean
    if polort is not None:
        params["polort"] = polort
    if merge_frad is not None:
        params["merge_frad"] = merge_frad
    return params


def v__radial_correlate_cargs(
    params: VRadialCorrelateParameters,
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
    cargs.append("@radial_correlate")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("results_dir") is not None:
        cargs.extend([
            "-rdir",
            params.get("results_dir")
        ])
    if params.get("do_corr") is not None:
        cargs.extend([
            "-do_corr",
            params.get("do_corr")
        ])
    if params.get("do_clust") is not None:
        cargs.extend([
            "-do_clust",
            params.get("do_clust")
        ])
    if params.get("mask_dset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dset"))
        ])
    if params.get("cthresh") is not None:
        cargs.extend([
            "-cthresh",
            str(params.get("cthresh"))
        ])
    if params.get("frac_limit") is not None:
        cargs.extend([
            "-frac_limit",
            str(params.get("frac_limit"))
        ])
    if params.get("sphere_rad") is not None:
        cargs.extend([
            "-sphere_rad",
            str(params.get("sphere_rad"))
        ])
    if params.get("use_3dmerge") is not None:
        cargs.extend([
            "-use_3dmerge",
            params.get("use_3dmerge")
        ])
    if params.get("percentile") is not None:
        cargs.extend([
            "-percentile",
            str(params.get("percentile"))
        ])
    if params.get("min_thr") is not None:
        cargs.extend([
            "-min_thr",
            str(params.get("min_thr"))
        ])
    if params.get("nfirst") is not None:
        cargs.extend([
            "-nfirst",
            str(params.get("nfirst"))
        ])
    if params.get("ver"):
        cargs.append("-ver")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hist"):
        cargs.append("-hist")
    if params.get("corr_mask") is not None:
        cargs.extend([
            "-corr_mask",
            params.get("corr_mask")
        ])
    if params.get("do_clean") is not None:
        cargs.extend([
            "-do_clean",
            params.get("do_clean")
        ])
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("merge_frad") is not None:
        cargs.extend([
            "-merge_frad",
            str(params.get("merge_frad"))
        ])
    return cargs


def v__radial_correlate_outputs(
    params: VRadialCorrelateParameters,
    execution: Execution,
) -> VRadialCorrelateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VRadialCorrelateOutputs(
        root=execution.output_file("."),
        corr_volumes=execution.output_file(params.get("results_dir") + "/correlation_volumes") if (params.get("results_dir") is not None) else None,
    )
    return ret


def v__radial_correlate_execute(
    params: VRadialCorrelateParameters,
    execution: Execution,
) -> VRadialCorrelateOutputs:
    """
    Check datasets for correlation artifacts.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VRadialCorrelateOutputs`).
    """
    cargs = v__radial_correlate_cargs(params, execution)
    ret = v__radial_correlate_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__radial_correlate(
    input_files: list[InputPathType],
    results_dir: str | None = None,
    do_corr: str | None = None,
    do_clust: str | None = None,
    mask_dset: InputPathType | None = None,
    cthresh: float | None = None,
    frac_limit: float | None = None,
    sphere_rad: float | None = None,
    use_3dmerge: str | None = None,
    percentile: float | None = None,
    min_thr: float | None = None,
    nfirst: float | None = None,
    ver: bool = False,
    verbose: bool = False,
    help_: bool = False,
    hist: bool = False,
    corr_mask: str | None = None,
    do_clean: str | None = None,
    polort: float | None = None,
    merge_frad: float | None = None,
    runner: Runner | None = None,
) -> VRadialCorrelateOutputs:
    """
    Check datasets for correlation artifacts.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: A list of EPI datasets.
        results_dir: Results directory for correlations.
        do_corr: Create correlation volumes (yes/no).
        do_clust: Cluster correlation volumes (yes/no).
        mask_dset: Specify a mask dataset to replace automask.
        cthresh: Threshold on correlation values.
        frac_limit: Minimum mask fraction surviving cluster.
        sphere_rad: Generate correlations within voxel spheres.
        use_3dmerge: Use 3dmerge rather than 3dLocalstat (yes/no).
        percentile: Percentile to use as threshold.
        min_thr: Minimum percentile threshold to be considered.
        nfirst: Number of initial TRs to remove.
        ver: Show version number.
        verbose: Make verbose: set echo.
        help_: Show help.
        hist: Show modification history.
        corr_mask: Mask time series before correlation blurring (yes/no).
        do_clean: Clean up at end, leaving only correlations (yes/no).
        polort: Detrend time series with given polynomial degree.
        merge_frad: Specify a radius fraction for 3dmerge blurring.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRadialCorrelateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__RADIAL_CORRELATE_METADATA)
    params = v__radial_correlate_params(input_files=input_files, results_dir=results_dir, do_corr=do_corr, do_clust=do_clust, mask_dset=mask_dset, cthresh=cthresh, frac_limit=frac_limit, sphere_rad=sphere_rad, use_3dmerge=use_3dmerge, percentile=percentile, min_thr=min_thr, nfirst=nfirst, ver=ver, verbose=verbose, help_=help_, hist=hist, corr_mask=corr_mask, do_clean=do_clean, polort=polort, merge_frad=merge_frad)
    return v__radial_correlate_execute(params, execution)


__all__ = [
    "VRadialCorrelateOutputs",
    "VRadialCorrelateParameters",
    "V__RADIAL_CORRELATE_METADATA",
    "v__radial_correlate",
    "v__radial_correlate_params",
]

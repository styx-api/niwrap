# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_HIST_METADATA = Metadata(
    id="5dff8f7ac913ce4a3781c6d59d7827316323eded.boutiques",
    name="3dHist",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dHistParameters = typing.TypedDict('V3dHistParameters', {
    "__STYX_TYPE__": typing.Literal["3dHist"],
    "input": InputPathType,
    "mask_dset": typing.NotRequired[InputPathType | None],
    "mask_range": typing.NotRequired[list[float] | None],
    "cmask": typing.NotRequired[str | None],
    "hist_file": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "equalized": typing.NotRequired[str | None],
    "nbin": typing.NotRequired[float | None],
    "min": typing.NotRequired[float | None],
    "max": typing.NotRequired[float | None],
    "binwidth": typing.NotRequired[float | None],
    "ignore_out": bool,
    "range_hist": typing.NotRequired[InputPathType | None],
    "showhist": bool,
    "at_val": typing.NotRequired[float | None],
    "get_params": typing.NotRequired[str | None],
    "voxvol": typing.NotRequired[float | None],
    "val_at": typing.NotRequired[str | None],
    "quiet": bool,
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
        "3dHist": v_3d_hist_cargs,
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


class V3dHistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_hist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_hist_params(
    input_: InputPathType,
    mask_dset: InputPathType | None = None,
    mask_range: list[float] | None = None,
    cmask: str | None = None,
    hist_file: InputPathType | None = None,
    prefix: str | None = None,
    equalized: str | None = None,
    nbin: float | None = None,
    min_: float | None = None,
    max_: float | None = None,
    binwidth: float | None = None,
    ignore_out: bool = False,
    range_hist: InputPathType | None = None,
    showhist: bool = False,
    at_val: float | None = None,
    get_params: str | None = None,
    voxvol: float | None = None,
    val_at: str | None = None,
    quiet: bool = False,
) -> V3dHistParameters:
    """
    Build parameters.
    
    Args:
        input_: Dataset providing values for histogram.
        mask_dset: Provide mask dataset to select subset of input.
        mask_range: Specify the range of values to consider from MSET. Default\
            is anything non-zero.
        cmask: Provide cmask expression. Voxels where expression is 0 are\
            excluded from computations.
        hist_file: Read this previously created histogram instead of forming\
            one from DSET.
        prefix: Write histogram to niml file called PREF.niml.hist.
        equalized: Write a histogram equalized version of the input dataset.
        nbin: Use K bins.
        min_: Minimum intensity.
        max_: Maximum intensity.
        binwidth: Bin width.
        ignore_out: Do not count samples outside the user specified range.
        range_hist: Use previously created histogram to set range and binwidth\
            parameters.
        showhist: Display histogram to stdout.
        at_val: Set the value at which you want histogram values.
        get_params: Return the desired properties at a given value. You can\
            select multiple properties.
        voxvol: Specify voxel volume in mm^3. To be used with upvol.
        val_at: Return the value where histogram property PAR is equal to\
            PARVAL. PAR can be: cdf, rcdf, ncdf, nrcdf, upvol.
        quiet: Return a concise output to simplify parsing.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dHist",
        "input": input_,
        "ignore_out": ignore_out,
        "showhist": showhist,
        "quiet": quiet,
    }
    if mask_dset is not None:
        params["mask_dset"] = mask_dset
    if mask_range is not None:
        params["mask_range"] = mask_range
    if cmask is not None:
        params["cmask"] = cmask
    if hist_file is not None:
        params["hist_file"] = hist_file
    if prefix is not None:
        params["prefix"] = prefix
    if equalized is not None:
        params["equalized"] = equalized
    if nbin is not None:
        params["nbin"] = nbin
    if min_ is not None:
        params["min"] = min_
    if max_ is not None:
        params["max"] = max_
    if binwidth is not None:
        params["binwidth"] = binwidth
    if range_hist is not None:
        params["range_hist"] = range_hist
    if at_val is not None:
        params["at_val"] = at_val
    if get_params is not None:
        params["get_params"] = get_params
    if voxvol is not None:
        params["voxvol"] = voxvol
    if val_at is not None:
        params["val_at"] = val_at
    return params


def v_3d_hist_cargs(
    params: V3dHistParameters,
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
    cargs.append("3dHist")
    cargs.append(execution.input_file(params.get("input")))
    if params.get("mask_dset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dset"))
        ])
    if params.get("mask_range") is not None:
        cargs.extend([
            "-mask_range",
            *map(str, params.get("mask_range"))
        ])
    if params.get("cmask") is not None:
        cargs.extend([
            "-cmask",
            params.get("cmask")
        ])
    if params.get("hist_file") is not None:
        cargs.extend([
            "-thishist",
            execution.input_file(params.get("hist_file"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("equalized") is not None:
        cargs.extend([
            "-equalized",
            params.get("equalized")
        ])
    if params.get("nbin") is not None:
        cargs.extend([
            "-nbin",
            str(params.get("nbin"))
        ])
    if params.get("min") is not None:
        cargs.extend([
            "-min",
            str(params.get("min"))
        ])
    if params.get("max") is not None:
        cargs.extend([
            "-max",
            str(params.get("max"))
        ])
    if params.get("binwidth") is not None:
        cargs.extend([
            "-binwidth",
            str(params.get("binwidth"))
        ])
    if params.get("ignore_out"):
        cargs.append("-ignore_out")
    if params.get("range_hist") is not None:
        cargs.extend([
            "-rhist",
            execution.input_file(params.get("range_hist"))
        ])
    if params.get("showhist"):
        cargs.append("-showhist")
    if params.get("at_val") is not None:
        cargs.extend([
            "-at",
            str(params.get("at_val"))
        ])
    if params.get("get_params") is not None:
        cargs.extend([
            "-get",
            params.get("get_params")
        ])
    if params.get("voxvol") is not None:
        cargs.extend([
            "-voxvol",
            str(params.get("voxvol"))
        ])
    if params.get("val_at") is not None:
        cargs.extend([
            "-val_at",
            params.get("val_at")
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3d_hist_outputs(
    params: V3dHistParameters,
    execution: Execution,
) -> V3dHistOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dHistOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_hist_execute(
    params: V3dHistParameters,
    execution: Execution,
) -> V3dHistOutputs:
    """
    Computes histograms using functions for generating priors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dHistOutputs`).
    """
    cargs = v_3d_hist_cargs(params, execution)
    ret = v_3d_hist_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_hist(
    input_: InputPathType,
    mask_dset: InputPathType | None = None,
    mask_range: list[float] | None = None,
    cmask: str | None = None,
    hist_file: InputPathType | None = None,
    prefix: str | None = None,
    equalized: str | None = None,
    nbin: float | None = None,
    min_: float | None = None,
    max_: float | None = None,
    binwidth: float | None = None,
    ignore_out: bool = False,
    range_hist: InputPathType | None = None,
    showhist: bool = False,
    at_val: float | None = None,
    get_params: str | None = None,
    voxvol: float | None = None,
    val_at: str | None = None,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dHistOutputs:
    """
    Computes histograms using functions for generating priors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Dataset providing values for histogram.
        mask_dset: Provide mask dataset to select subset of input.
        mask_range: Specify the range of values to consider from MSET. Default\
            is anything non-zero.
        cmask: Provide cmask expression. Voxels where expression is 0 are\
            excluded from computations.
        hist_file: Read this previously created histogram instead of forming\
            one from DSET.
        prefix: Write histogram to niml file called PREF.niml.hist.
        equalized: Write a histogram equalized version of the input dataset.
        nbin: Use K bins.
        min_: Minimum intensity.
        max_: Maximum intensity.
        binwidth: Bin width.
        ignore_out: Do not count samples outside the user specified range.
        range_hist: Use previously created histogram to set range and binwidth\
            parameters.
        showhist: Display histogram to stdout.
        at_val: Set the value at which you want histogram values.
        get_params: Return the desired properties at a given value. You can\
            select multiple properties.
        voxvol: Specify voxel volume in mm^3. To be used with upvol.
        val_at: Return the value where histogram property PAR is equal to\
            PARVAL. PAR can be: cdf, rcdf, ncdf, nrcdf, upvol.
        quiet: Return a concise output to simplify parsing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dHistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_HIST_METADATA)
    params = v_3d_hist_params(input_=input_, mask_dset=mask_dset, mask_range=mask_range, cmask=cmask, hist_file=hist_file, prefix=prefix, equalized=equalized, nbin=nbin, min_=min_, max_=max_, binwidth=binwidth, ignore_out=ignore_out, range_hist=range_hist, showhist=showhist, at_val=at_val, get_params=get_params, voxvol=voxvol, val_at=val_at, quiet=quiet)
    return v_3d_hist_execute(params, execution)


__all__ = [
    "V3dHistOutputs",
    "V3dHistParameters",
    "V_3D_HIST_METADATA",
    "v_3d_hist",
    "v_3d_hist_params",
]

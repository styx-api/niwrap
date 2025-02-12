# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_QWARP_METADATA = Metadata(
    id="b31e14a7b7123e83340819abf222feefbe217a71.boutiques",
    name="3dQwarp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dQwarpParameters = typing.TypedDict('V3dQwarpParameters', {
    "__STYX_TYPE__": typing.Literal["3dQwarp"],
    "base_dataset": InputPathType,
    "source_dataset": InputPathType,
    "prefix": str,
    "no_warp": bool,
    "inverse_warp": bool,
    "no_dataset": bool,
    "a_warp": bool,
    "pcl": bool,
    "pear": bool,
    "hel": bool,
    "mi": bool,
    "nmi": bool,
    "lpc": bool,
    "lpa": bool,
    "noneg": bool,
    "nopenalty": bool,
    "minpatch": typing.NotRequired[float | None],
    "maxlev": typing.NotRequired[float | None],
    "verbose": bool,
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
        "3dQwarp": v_3d_qwarp_cargs,
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
        "3dQwarp": v_3d_qwarp_outputs,
    }.get(t)


class V3dQwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_qwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warped_dataset: OutputPathType
    """Warped dataset"""
    warp_dataset: OutputPathType
    """Warp dataset"""
    inverse_warp_dataset: OutputPathType
    """Inverse warp dataset"""


def v_3d_qwarp_params(
    base_dataset: InputPathType,
    source_dataset: InputPathType,
    prefix: str,
    no_warp: bool = False,
    inverse_warp: bool = False,
    no_dataset: bool = False,
    a_warp: bool = False,
    pcl: bool = False,
    pear: bool = False,
    hel: bool = False,
    mi: bool = False,
    nmi: bool = False,
    lpc: bool = False,
    lpa: bool = False,
    noneg: bool = False,
    nopenalty: bool = False,
    minpatch: float | None = None,
    maxlev: float | None = None,
    verbose: bool = False,
    quiet: bool = False,
) -> V3dQwarpParameters:
    """
    Build parameters.
    
    Args:
        base_dataset: Base dataset.
        source_dataset: Source dataset.
        prefix: Prefix for the output datasets.
        no_warp: Do not save the _WARP file.
        inverse_warp: Compute and save the _WARPINV file.
        no_dataset: Do not save the warped source dataset.
        a_warp: Output the nonlinear warp when -allineate is used.
        pcl: Clipped Pearson correlation (default method).
        pear: Use strict Pearson correlation for matching.
        hel: Use Hellinger metric for matching.
        mi: Use Mutual Information for matching.
        nmi: Use Normalized Mutual Information for matching.
        lpc: Use Local Pearson correlation (signed) for matching.
        lpa: Use Local Pearson correlation (absolute value) for matching.
        noneg: Replace negative values in either input volume with 0.
        nopenalty: Don't use a penalty on the cost functional.
        minpatch: Set the minimum patch size for warp searching.
        maxlev: Set the maximum refinement level.
        verbose: Print out very verbose progress messages.
        quiet: Cut out most progress messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dQwarp",
        "base_dataset": base_dataset,
        "source_dataset": source_dataset,
        "prefix": prefix,
        "no_warp": no_warp,
        "inverse_warp": inverse_warp,
        "no_dataset": no_dataset,
        "a_warp": a_warp,
        "pcl": pcl,
        "pear": pear,
        "hel": hel,
        "mi": mi,
        "nmi": nmi,
        "lpc": lpc,
        "lpa": lpa,
        "noneg": noneg,
        "nopenalty": nopenalty,
        "verbose": verbose,
        "quiet": quiet,
    }
    if minpatch is not None:
        params["minpatch"] = minpatch
    if maxlev is not None:
        params["maxlev"] = maxlev
    return params


def v_3d_qwarp_cargs(
    params: V3dQwarpParameters,
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
    cargs.append("3dQwarp")
    cargs.append(execution.input_file(params.get("base_dataset")))
    cargs.append(execution.input_file(params.get("source_dataset")))
    cargs.append(params.get("prefix"))
    if params.get("no_warp"):
        cargs.append("-nowarp")
    if params.get("inverse_warp"):
        cargs.append("-iwarp")
    if params.get("no_dataset"):
        cargs.append("-nodset")
    if params.get("a_warp"):
        cargs.append("-awarp")
    if params.get("pcl"):
        cargs.append("-pcl")
    if params.get("pear"):
        cargs.append("-pear")
    if params.get("hel"):
        cargs.append("-hel")
    if params.get("mi"):
        cargs.append("-mi")
    if params.get("nmi"):
        cargs.append("-nmi")
    if params.get("lpc"):
        cargs.append("-lpc")
    if params.get("lpa"):
        cargs.append("-lpa")
    if params.get("noneg"):
        cargs.append("-noneg")
    if params.get("nopenalty"):
        cargs.append("-nopenalty")
    if params.get("minpatch") is not None:
        cargs.extend([
            "-minpatch",
            str(params.get("minpatch"))
        ])
    if params.get("maxlev") is not None:
        cargs.extend([
            "-maxlev",
            str(params.get("maxlev"))
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3d_qwarp_outputs(
    params: V3dQwarpParameters,
    execution: Execution,
) -> V3dQwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dQwarpOutputs(
        root=execution.output_file("."),
        warped_dataset=execution.output_file("{PREFIX}+tlrc"),
        warp_dataset=execution.output_file("{PREFIX}_WARP+tlrc"),
        inverse_warp_dataset=execution.output_file("{PREFIX}_WARPINV+tlrc"),
    )
    return ret


def v_3d_qwarp_execute(
    params: V3dQwarpParameters,
    execution: Execution,
) -> V3dQwarpOutputs:
    """
    Computes a nonlinearly warped version of source_dataset to match base_dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dQwarpOutputs`).
    """
    cargs = v_3d_qwarp_cargs(params, execution)
    ret = v_3d_qwarp_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_qwarp(
    base_dataset: InputPathType,
    source_dataset: InputPathType,
    prefix: str,
    no_warp: bool = False,
    inverse_warp: bool = False,
    no_dataset: bool = False,
    a_warp: bool = False,
    pcl: bool = False,
    pear: bool = False,
    hel: bool = False,
    mi: bool = False,
    nmi: bool = False,
    lpc: bool = False,
    lpa: bool = False,
    noneg: bool = False,
    nopenalty: bool = False,
    minpatch: float | None = None,
    maxlev: float | None = None,
    verbose: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dQwarpOutputs:
    """
    Computes a nonlinearly warped version of source_dataset to match base_dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        base_dataset: Base dataset.
        source_dataset: Source dataset.
        prefix: Prefix for the output datasets.
        no_warp: Do not save the _WARP file.
        inverse_warp: Compute and save the _WARPINV file.
        no_dataset: Do not save the warped source dataset.
        a_warp: Output the nonlinear warp when -allineate is used.
        pcl: Clipped Pearson correlation (default method).
        pear: Use strict Pearson correlation for matching.
        hel: Use Hellinger metric for matching.
        mi: Use Mutual Information for matching.
        nmi: Use Normalized Mutual Information for matching.
        lpc: Use Local Pearson correlation (signed) for matching.
        lpa: Use Local Pearson correlation (absolute value) for matching.
        noneg: Replace negative values in either input volume with 0.
        nopenalty: Don't use a penalty on the cost functional.
        minpatch: Set the minimum patch size for warp searching.
        maxlev: Set the maximum refinement level.
        verbose: Print out very verbose progress messages.
        quiet: Cut out most progress messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dQwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_QWARP_METADATA)
    params = v_3d_qwarp_params(base_dataset=base_dataset, source_dataset=source_dataset, prefix=prefix, no_warp=no_warp, inverse_warp=inverse_warp, no_dataset=no_dataset, a_warp=a_warp, pcl=pcl, pear=pear, hel=hel, mi=mi, nmi=nmi, lpc=lpc, lpa=lpa, noneg=noneg, nopenalty=nopenalty, minpatch=minpatch, maxlev=maxlev, verbose=verbose, quiet=quiet)
    return v_3d_qwarp_execute(params, execution)


__all__ = [
    "V3dQwarpOutputs",
    "V3dQwarpParameters",
    "V_3D_QWARP_METADATA",
    "v_3d_qwarp",
    "v_3d_qwarp_params",
]

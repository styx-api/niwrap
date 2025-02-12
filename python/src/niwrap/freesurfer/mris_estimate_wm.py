# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ESTIMATE_WM_METADATA = Metadata(
    id="cac77a4401a904ea7c3d8eb641009c3991349f87.boutiques",
    name="mris_estimate_wm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisEstimateWmParameters = typing.TypedDict('MrisEstimateWmParameters', {
    "__STYX_TYPE__": typing.Literal["mris_estimate_wm"],
    "subjs": list[str],
    "hemi": str,
    "sdir": typing.NotRequired[str | None],
    "model": typing.NotRequired[str | None],
    "suffix": typing.NotRequired[str | None],
    "gpu": bool,
    "rsi": bool,
    "single_iter": bool,
    "vol": typing.NotRequired[str | None],
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
        "mris_estimate_wm": mris_estimate_wm_cargs,
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


class MrisEstimateWmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_estimate_wm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_estimate_wm_params(
    subjs: list[str],
    hemi: str,
    sdir: str | None = None,
    model: str | None = None,
    suffix: str | None = None,
    gpu: bool = False,
    rsi: bool = False,
    single_iter: bool = False,
    vol: str | None = None,
) -> MrisEstimateWmParameters:
    """
    Build parameters.
    
    Args:
        subjs: List of subjects to process.
        hemi: Hemisphere to reconstruct (lh or rh).
        sdir: Override SUBJECTS_DIR.
        model: Override default model.
        suffix: Suffix of output surface (default is 'topofit').
        gpu: Use the GPU.
        rsi: Remove self-intersecting faces during the deformation.
        single_iter: Prevent deformation steps from running more than once.
        vol: Subject volume to use as input.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_estimate_wm",
        "subjs": subjs,
        "hemi": hemi,
        "gpu": gpu,
        "rsi": rsi,
        "single_iter": single_iter,
    }
    if sdir is not None:
        params["sdir"] = sdir
    if model is not None:
        params["model"] = model
    if suffix is not None:
        params["suffix"] = suffix
    if vol is not None:
        params["vol"] = vol
    return params


def mris_estimate_wm_cargs(
    params: MrisEstimateWmParameters,
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
    cargs.append("mris_estimate_wm")
    cargs.extend([
        "-s",
        *params.get("subjs")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemi")
    ])
    if params.get("sdir") is not None:
        cargs.extend([
            "-d",
            params.get("sdir")
        ])
    if params.get("model") is not None:
        cargs.extend([
            "-m",
            params.get("model")
        ])
    if params.get("suffix") is not None:
        cargs.extend([
            "-x",
            params.get("suffix")
        ])
    if params.get("gpu"):
        cargs.append("-g")
    if params.get("rsi"):
        cargs.append("--rsi")
    if params.get("single_iter"):
        cargs.append("--single-iter")
    if params.get("vol") is not None:
        cargs.extend([
            "--vol",
            params.get("vol")
        ])
    return cargs


def mris_estimate_wm_outputs(
    params: MrisEstimateWmParameters,
    execution: Execution,
) -> MrisEstimateWmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisEstimateWmOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_estimate_wm_execute(
    params: MrisEstimateWmParameters,
    execution: Execution,
) -> MrisEstimateWmOutputs:
    """
    Tool to estimate white matter surfaces using MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisEstimateWmOutputs`).
    """
    cargs = mris_estimate_wm_cargs(params, execution)
    ret = mris_estimate_wm_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_estimate_wm(
    subjs: list[str],
    hemi: str,
    sdir: str | None = None,
    model: str | None = None,
    suffix: str | None = None,
    gpu: bool = False,
    rsi: bool = False,
    single_iter: bool = False,
    vol: str | None = None,
    runner: Runner | None = None,
) -> MrisEstimateWmOutputs:
    """
    Tool to estimate white matter surfaces using MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjs: List of subjects to process.
        hemi: Hemisphere to reconstruct (lh or rh).
        sdir: Override SUBJECTS_DIR.
        model: Override default model.
        suffix: Suffix of output surface (default is 'topofit').
        gpu: Use the GPU.
        rsi: Remove self-intersecting faces during the deformation.
        single_iter: Prevent deformation steps from running more than once.
        vol: Subject volume to use as input.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisEstimateWmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ESTIMATE_WM_METADATA)
    params = mris_estimate_wm_params(subjs=subjs, hemi=hemi, sdir=sdir, model=model, suffix=suffix, gpu=gpu, rsi=rsi, single_iter=single_iter, vol=vol)
    return mris_estimate_wm_execute(params, execution)


__all__ = [
    "MRIS_ESTIMATE_WM_METADATA",
    "MrisEstimateWmOutputs",
    "MrisEstimateWmParameters",
    "mris_estimate_wm",
    "mris_estimate_wm_params",
]

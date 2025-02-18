# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RBBR_METADATA = Metadata(
    id="6f8461b7fae6d16cb41c5377c9a0a117f94c76da.boutiques",
    name="rbbr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RbbrParameters = typing.TypedDict('RbbrParameters', {
    "__STYX_TYPE__": typing.Literal["rbbr"],
    "subject": typing.NotRequired[str | None],
    "moving_image": str,
    "t2_contrast": bool,
    "init_header": bool,
    "cost_threshold": typing.NotRequired[float | None],
    "gtm_synthesize": typing.NotRequired[str | None],
    "tt_reduce": bool,
    "iterations": typing.NotRequired[float | None],
    "output_reg": typing.NotRequired[str | None],
    "output_lta": typing.NotRequired[str | None],
    "left_hemi": bool,
    "right_hemi": bool,
    "gm_proj_frac": typing.NotRequired[float | None],
    "gm_proj_abs": typing.NotRequired[float | None],
    "wm_proj_abs": typing.NotRequired[float | None],
    "frame_no": typing.NotRequired[float | None],
    "output_template": typing.NotRequired[str | None],
    "no_merge": bool,
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
        "rbbr": rbbr_cargs,
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
        "rbbr": rbbr_outputs,
    }.get(t)


class RbbrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rbbr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_reg_file: OutputPathType | None
    """Output registration file"""
    output_lta_file: OutputPathType | None
    """Output LTA file"""
    output_template_file: OutputPathType | None
    """Saved template output file"""


def rbbr_params(
    moving_image: str,
    subject: str | None = None,
    t2_contrast: bool = False,
    init_header: bool = False,
    cost_threshold: float | None = None,
    gtm_synthesize: str | None = None,
    tt_reduce: bool = False,
    iterations: float | None = None,
    output_reg: str | None = None,
    output_lta: str | None = None,
    left_hemi: bool = False,
    right_hemi: bool = False,
    gm_proj_frac: float | None = None,
    gm_proj_abs: float | None = None,
    wm_proj_abs: float | None = None,
    frame_no: float | None = None,
    output_template: str | None = None,
    no_merge: bool = False,
) -> RbbrParameters:
    """
    Build parameters.
    
    Args:
        moving_image: Input moving image.
        subject: FreeSurfer subject (not needed with --init-reg).
        t2_contrast: Use T2 tissue contrast.
        init_header: Initialize using header.
        cost_threshold: Cost threshold to define outlier.
        gtm_synthesize: Use GTM to synthesize.
        tt_reduce: Reduce GTM Seg to tissue types for faster processing.
        iterations: Number of iterations.
        output_reg: Output registration file.
        output_lta: Output LTA file.
        left_hemi: Only use left hemisphere.
        right_hemi: Only use right hemisphere.
        gm_proj_frac: GM projection fraction.
        gm_proj_abs: GM projection absolute.
        wm_proj_abs: WM projection absolute.
        frame_no: Use 0-based frame number as template.
        output_template: Save template as an output.
        no_merge: Do not merge GTM Ids.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rbbr",
        "moving_image": moving_image,
        "t2_contrast": t2_contrast,
        "init_header": init_header,
        "tt_reduce": tt_reduce,
        "left_hemi": left_hemi,
        "right_hemi": right_hemi,
        "no_merge": no_merge,
    }
    if subject is not None:
        params["subject"] = subject
    if cost_threshold is not None:
        params["cost_threshold"] = cost_threshold
    if gtm_synthesize is not None:
        params["gtm_synthesize"] = gtm_synthesize
    if iterations is not None:
        params["iterations"] = iterations
    if output_reg is not None:
        params["output_reg"] = output_reg
    if output_lta is not None:
        params["output_lta"] = output_lta
    if gm_proj_frac is not None:
        params["gm_proj_frac"] = gm_proj_frac
    if gm_proj_abs is not None:
        params["gm_proj_abs"] = gm_proj_abs
    if wm_proj_abs is not None:
        params["wm_proj_abs"] = wm_proj_abs
    if frame_no is not None:
        params["frame_no"] = frame_no
    if output_template is not None:
        params["output_template"] = output_template
    return params


def rbbr_cargs(
    params: RbbrParameters,
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
    cargs.append("rbbr")
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    cargs.extend([
        "--mov",
        params.get("moving_image")
    ])
    if params.get("t2_contrast"):
        cargs.append("--t2")
    if params.get("init_header"):
        cargs.append("--init-header")
    if params.get("cost_threshold") is not None:
        cargs.extend([
            "--cthresh",
            str(params.get("cost_threshold"))
        ])
    if params.get("gtm_synthesize") is not None:
        cargs.extend([
            "--gtm",
            params.get("gtm_synthesize")
        ])
    if params.get("tt_reduce"):
        cargs.append("--tt-reduce")
    if params.get("iterations") is not None:
        cargs.extend([
            "--iters",
            str(params.get("iterations"))
        ])
    if params.get("output_reg") is not None:
        cargs.extend([
            "--reg",
            params.get("output_reg")
        ])
    if params.get("output_lta") is not None:
        cargs.extend([
            "--lta",
            params.get("output_lta")
        ])
    if params.get("left_hemi"):
        cargs.append("--lh-only")
    if params.get("right_hemi"):
        cargs.append("--rh-only")
    if params.get("gm_proj_frac") is not None:
        cargs.extend([
            "--gm-proj-frac",
            str(params.get("gm_proj_frac"))
        ])
    if params.get("gm_proj_abs") is not None:
        cargs.extend([
            "--gm-proj-abs",
            str(params.get("gm_proj_abs"))
        ])
    if params.get("wm_proj_abs") is not None:
        cargs.extend([
            "--wm-proj-abs",
            str(params.get("wm_proj_abs"))
        ])
    if params.get("frame_no") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame_no"))
        ])
    if params.get("output_template") is not None:
        cargs.extend([
            "--template",
            params.get("output_template")
        ])
    if params.get("no_merge"):
        cargs.append("--no-merge")
    return cargs


def rbbr_outputs(
    params: RbbrParameters,
    execution: Execution,
) -> RbbrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RbbrOutputs(
        root=execution.output_file("."),
        output_reg_file=execution.output_file(params.get("output_reg")) if (params.get("output_reg") is not None) else None,
        output_lta_file=execution.output_file(params.get("output_lta")) if (params.get("output_lta") is not None) else None,
        output_template_file=execution.output_file(params.get("output_template")) if (params.get("output_template") is not None) else None,
    )
    return ret


def rbbr_execute(
    params: RbbrParameters,
    execution: Execution,
) -> RbbrOutputs:
    """
    Robust version of bbregister.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RbbrOutputs`).
    """
    cargs = rbbr_cargs(params, execution)
    ret = rbbr_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def rbbr(
    moving_image: str,
    subject: str | None = None,
    t2_contrast: bool = False,
    init_header: bool = False,
    cost_threshold: float | None = None,
    gtm_synthesize: str | None = None,
    tt_reduce: bool = False,
    iterations: float | None = None,
    output_reg: str | None = None,
    output_lta: str | None = None,
    left_hemi: bool = False,
    right_hemi: bool = False,
    gm_proj_frac: float | None = None,
    gm_proj_abs: float | None = None,
    wm_proj_abs: float | None = None,
    frame_no: float | None = None,
    output_template: str | None = None,
    no_merge: bool = False,
    runner: Runner | None = None,
) -> RbbrOutputs:
    """
    Robust version of bbregister.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        moving_image: Input moving image.
        subject: FreeSurfer subject (not needed with --init-reg).
        t2_contrast: Use T2 tissue contrast.
        init_header: Initialize using header.
        cost_threshold: Cost threshold to define outlier.
        gtm_synthesize: Use GTM to synthesize.
        tt_reduce: Reduce GTM Seg to tissue types for faster processing.
        iterations: Number of iterations.
        output_reg: Output registration file.
        output_lta: Output LTA file.
        left_hemi: Only use left hemisphere.
        right_hemi: Only use right hemisphere.
        gm_proj_frac: GM projection fraction.
        gm_proj_abs: GM projection absolute.
        wm_proj_abs: WM projection absolute.
        frame_no: Use 0-based frame number as template.
        output_template: Save template as an output.
        no_merge: Do not merge GTM Ids.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RbbrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RBBR_METADATA)
    params = rbbr_params(subject=subject, moving_image=moving_image, t2_contrast=t2_contrast, init_header=init_header, cost_threshold=cost_threshold, gtm_synthesize=gtm_synthesize, tt_reduce=tt_reduce, iterations=iterations, output_reg=output_reg, output_lta=output_lta, left_hemi=left_hemi, right_hemi=right_hemi, gm_proj_frac=gm_proj_frac, gm_proj_abs=gm_proj_abs, wm_proj_abs=wm_proj_abs, frame_no=frame_no, output_template=output_template, no_merge=no_merge)
    return rbbr_execute(params, execution)


__all__ = [
    "RBBR_METADATA",
    "RbbrOutputs",
    "RbbrParameters",
    "rbbr",
    "rbbr_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RBBR_METADATA = Metadata(
    id="4b521df5d260eef774b777205fa0b7feecebbc20.boutiques",
    name="rbbr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


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
    cargs = []
    cargs.append("rbbr")
    if subject is not None:
        cargs.extend([
            "--s",
            subject
        ])
    cargs.extend([
        "--mov",
        moving_image
    ])
    if t2_contrast:
        cargs.append("--t2")
    if init_header:
        cargs.append("--init-header")
    if cost_threshold is not None:
        cargs.extend([
            "--cthresh",
            str(cost_threshold)
        ])
    if gtm_synthesize is not None:
        cargs.extend([
            "--gtm",
            gtm_synthesize
        ])
    if tt_reduce:
        cargs.append("--tt-reduce")
    if iterations is not None:
        cargs.extend([
            "--iters",
            str(iterations)
        ])
    if output_reg is not None:
        cargs.extend([
            "--reg",
            output_reg
        ])
    if output_lta is not None:
        cargs.extend([
            "--lta",
            output_lta
        ])
    if left_hemi:
        cargs.append("--lh-only")
    if right_hemi:
        cargs.append("--rh-only")
    if gm_proj_frac is not None:
        cargs.extend([
            "--gm-proj-frac",
            str(gm_proj_frac)
        ])
    if gm_proj_abs is not None:
        cargs.extend([
            "--gm-proj-abs",
            str(gm_proj_abs)
        ])
    if wm_proj_abs is not None:
        cargs.extend([
            "--wm-proj-abs",
            str(wm_proj_abs)
        ])
    if frame_no is not None:
        cargs.extend([
            "--frame",
            str(frame_no)
        ])
    if output_template is not None:
        cargs.extend([
            "--template",
            output_template
        ])
    if no_merge:
        cargs.append("--no-merge")
    ret = RbbrOutputs(
        root=execution.output_file("."),
        output_reg_file=execution.output_file(output_reg) if (output_reg is not None) else None,
        output_lta_file=execution.output_file(output_lta) if (output_lta is not None) else None,
        output_template_file=execution.output_file(output_template) if (output_template is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RBBR_METADATA",
    "RbbrOutputs",
    "rbbr",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GTMSEG_METADATA = Metadata(
    id="29e1c1370e446a18137bbf4e9561c7972ac57725.boutiques",
    name="gtmseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class GtmsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gtmseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType | None
    """Output segmentation volume"""
    output_ctab: OutputPathType
    """Generated color table for the output segmentation"""


def gtmseg(
    subject: str,
    outvol: str | None = "gtmseg.mgz",
    usf: float | None = 2,
    subsegwm: bool = False,
    keep_hypo: bool = False,
    keep_cc: bool = False,
    dmax: float | None = 5,
    ctx_annot: str | None = "aparc 1000 2000",
    wm_annot: str | None = "lobes 3200 4200",
    output_usf: float | None = None,
    head: str | None = None,
    subseg_cbwm: bool = False,
    no_pons: bool = False,
    no_vermis: bool = False,
    ctab: InputPathType | None = None,
    no_seg_stats: bool = False,
    xcerseg: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> GtmsegOutputs:
    """
    Creates an anatomical segmentation for the geometric transfer matrix (GTM) used
    in PET partial volume correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject to analyze.
        outvol: Output volume relative to subject/mri.
        usf: Upsampling factor for segmentation resolution.
        subsegwm: Subsegment white matter into lobes.
        keep_hypo: Do not relabel hypointensities as white matter when\
            subsegmenting WM.
        keep_cc: Do not relabel corpus callosum as white matter.
        dmax: Distance threshold for subsegmenting WM.
        ctx_annot: Annotation for cortical segmentation.
        wm_annot: Annotation for WM segmentation with --subsegwm.
        output_usf: Set output upsampling factor different from input USF for\
            debugging.
        head: Use alternative head segmentation file.
        subseg_cbwm: Subsegment cerebellum WM into core and gyri.
        no_pons: Do not add pons segmentation when running xcerebralseg.
        no_vermis: Do not add vermis segmentation when running xcerebralseg.
        ctab: Color table for custom segmentation.
        no_seg_stats: Do not compute segmentation statistics.
        xcerseg: Run xcerebralseg to create apas+head.mgz.
        debug: Enable debugging mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GtmsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GTMSEG_METADATA)
    cargs = []
    cargs.append("gtmseg")
    cargs.extend([
        "--s",
        subject
    ])
    if outvol is not None:
        cargs.extend([
            "--o",
            outvol
        ])
    if usf is not None:
        cargs.extend([
            "--usf",
            str(usf)
        ])
    if subsegwm:
        cargs.append("--subsegwm")
    if keep_hypo:
        cargs.append("--keep-hypo")
    if keep_cc:
        cargs.append("--keep-cc")
    if dmax is not None:
        cargs.extend([
            "--dmax",
            str(dmax)
        ])
    if ctx_annot is not None:
        cargs.extend([
            "--ctx-annot",
            ctx_annot
        ])
    if wm_annot is not None:
        cargs.extend([
            "--wm-annot",
            wm_annot
        ])
    if output_usf is not None:
        cargs.extend([
            "--output-usf",
            str(output_usf)
        ])
    if head is not None:
        cargs.extend([
            "--head",
            head
        ])
    if subseg_cbwm:
        cargs.append("--subseg-cblum-wm")
    if no_pons:
        cargs.append("--no-pons")
    if no_vermis:
        cargs.append("--no-vermis")
    if ctab is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(ctab)
        ])
    if no_seg_stats:
        cargs.append("--no-seg-stats")
    if xcerseg:
        cargs.append("--xcerseg")
    if debug:
        cargs.append("--debug")
    ret = GtmsegOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file("$SUBJECTS_DIR/" + subject + "/mri/" + outvol) if (outvol is not None) else None,
        output_ctab=execution.output_file("$SUBJECTS_DIR/" + subject + "/mri/gtmseg+myseg.ctab"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GTMSEG_METADATA",
    "GtmsegOutputs",
    "gtmseg",
]

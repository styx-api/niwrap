# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_TRAIN_METADATA = Metadata(
    id="813952c1ec5a866c05dcd797951dba894391ce06.boutiques",
    name="dmri_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriTrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_train(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_train(
    slist: InputPathType,
    trk_files: list[InputPathType],
    seg: InputPathType,
    cmask: InputPathType,
    lmask: list[float],
    bmask_training: list[InputPathType],
    outtrk: list[InputPathType],
    bmask_test: list[InputPathType],
    ncpts: list[float],
    max_streamlines: float,
    out_files: list[str],
    rois: list[InputPathType] | None = None,
    fa: list[InputPathType] | None = None,
    reg: InputPathType | None = None,
    regnl: InputPathType | None = None,
    refnl: InputPathType | None = None,
    basereg: list[InputPathType] | None = None,
    baseref: list[InputPathType] | None = None,
    xstr: bool = False,
    aprior: bool = False,
    sprior: bool = False,
    trunc: bool = False,
    outdir: str | None = None,
    cptdir: str | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DmriTrainOutputs:
    """
    DMRI training tool for processing diffusion MRI data in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        slist: Text file with list of training subject directories.
        trk_files: Name(s) of input .trk file(s), one per path.
        seg: Name of input aparc+aseg volume.
        cmask: Name of input cortex mask volume.
        lmask: Add a label ID from aparc+aseg to cortex mask, one per path.
        bmask_training: Input brain mask volume(s).
        outtrk: Name(s) of output, pre-sorted .trk file(s), one per path.
        bmask_test: Input brain mask volume(s) for test subject.
        ncpts: Number of control points for initial spline.
        max_streamlines: Maximum number of training streamlines to keep per\
            path.
        out_files: Base name(s) of output(s) for test subject, one per path.
        rois: Optional, names of input tract labeling ROIs, two per path.
        fa: Input FA volume(s) for test subject.
        reg: Affine registration from atlas to base space.
        regnl: Nonlinear registration from atlas to base space.
        refnl: Nonlinear registration source reference volume.
        basereg: Affine registration(s) from base to FA volume(s).
        baseref: Base space reference volume.
        xstr: Exclude previously chosen center streamline(s).
        aprior: Compute priors on underlying anatomy.
        sprior: Compute priors on shape.
        trunc: Use all training streamlines, truncated or not.
        outdir: Output directory.
        cptdir: Output directory for control points in test subject's space.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_TRAIN_METADATA)
    cargs = []
    cargs.append("dmri_train")
    cargs.extend([
        "--slist",
        execution.input_file(slist)
    ])
    cargs.extend([
        "--trk",
        *[execution.input_file(f) for f in trk_files]
    ])
    if rois is not None:
        cargs.extend([
            "--rois",
            *[execution.input_file(f) for f in rois]
        ])
    cargs.extend([
        "--seg",
        execution.input_file(seg)
    ])
    cargs.extend([
        "--cmask",
        execution.input_file(cmask)
    ])
    cargs.extend([
        "--lmask",
        *map(str, lmask)
    ])
    cargs.extend([
        "--bmask",
        *[execution.input_file(f) for f in bmask_training]
    ])
    cargs.extend([
        "--outtrk",
        *[execution.input_file(f) for f in outtrk]
    ])
    cargs.extend([
        "--bmask",
        *[execution.input_file(f) for f in bmask_test]
    ])
    if fa is not None:
        cargs.extend([
            "--fa",
            *[execution.input_file(f) for f in fa]
        ])
    if reg is not None:
        cargs.extend([
            "--reg",
            execution.input_file(reg)
        ])
    if regnl is not None:
        cargs.extend([
            "--regnl",
            execution.input_file(regnl)
        ])
    if refnl is not None:
        cargs.extend([
            "--refnl",
            execution.input_file(refnl)
        ])
    if basereg is not None:
        cargs.extend([
            "--basereg",
            *[execution.input_file(f) for f in basereg]
        ])
    if baseref is not None:
        cargs.extend([
            "--baseref",
            *[execution.input_file(f) for f in baseref]
        ])
    cargs.extend([
        "--ncpts",
        *map(str, ncpts)
    ])
    cargs.extend([
        "--max",
        str(max_streamlines)
    ])
    if xstr:
        cargs.append("--xstr")
    if aprior:
        cargs.append("--aprior")
    if sprior:
        cargs.append("--sprior")
    if trunc:
        cargs.append("--trunc")
    cargs.extend([
        "--out",
        *out_files
    ])
    if outdir is not None:
        cargs.extend([
            "--outdir",
            outdir
        ])
    if cptdir is not None:
        cargs.extend([
            "--cptdir",
            cptdir
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = DmriTrainOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_TRAIN_METADATA",
    "DmriTrainOutputs",
    "dmri_train",
]

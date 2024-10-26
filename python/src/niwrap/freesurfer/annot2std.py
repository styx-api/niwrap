# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANNOT2STD_METADATA = Metadata(
    id="da6908bba70906156b526b7c73f0a7bb27ad1958.boutiques",
    name="annot2std",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Annot2stdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `annot2std(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_annot_file: OutputPathType
    """Main output annotation file"""
    out_prob_map_file: OutputPathType
    """Output annotation probability map file"""
    output_surface_segmentation: OutputPathType | None
    """Output surface segmentation file"""


def annot2std(
    output_annot_path: str,
    subjects: list[str],
    fsgd_file: InputPathType | None = None,
    subject_list_file: InputPathType | None = None,
    target: str | None = None,
    right_hemisphere: bool = False,
    xhemi: bool = False,
    surfreg: str | None = None,
    srcsurfreg: str | None = None,
    trgsurfreg: str | None = None,
    a2009s: bool = False,
    segmentation: str | None = None,
    stack: str | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Annot2stdOutputs:
    """
    Creates an average annotation in a standard space based on transforming the
    annotations of the individual subjects to the standard space through the surface
    registration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_annot_path: Full output annotation path (also creates\
            outannotpath.p.mgh).
        subjects: Input subject(s), specify each subject with --s subj.
        fsgd_file: FSGD file for group descriptor.
        subject_list_file: Subject list file.
        target: Target subject (e.g., fsaverage).
        right_hemisphere: Use right hemisphere.
        xhemi: For interhemispheric analysis.
        surfreg: Surface registration type (default is sphere.reg).
        srcsurfreg: Source surface registration type (default is sphere.reg).
        trgsurfreg: Target surface registration type (default is sphere.reg).
        a2009s: Annotation name set to aparc.a2009s.
        segmentation: Save output as a surface segmentation (2 frames, second =\
            p).
        stack: Stack of individual annotations as segmentation.
        help_: Display help.
        version: Display version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Annot2stdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANNOT2STD_METADATA)
    cargs = []
    cargs.append("annot2std")
    cargs.extend([
        "--o",
        output_annot_path
    ])
    cargs.extend([
        "--s",
        *subjects
    ])
    if fsgd_file is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(fsgd_file)
        ])
    if subject_list_file is not None:
        cargs.extend([
            "--f",
            execution.input_file(subject_list_file)
        ])
    if target is not None:
        cargs.extend([
            "--t",
            target
        ])
    if right_hemisphere:
        cargs.append("--rh")
    if xhemi:
        cargs.append("--xhemi")
    if surfreg is not None:
        cargs.extend([
            "--surfreg",
            surfreg
        ])
    if srcsurfreg is not None:
        cargs.extend([
            "--srcsurfreg",
            srcsurfreg
        ])
    if trgsurfreg is not None:
        cargs.extend([
            "--trgsurfreg",
            trgsurfreg
        ])
    if a2009s:
        cargs.append("--a2009s")
    if segmentation is not None:
        cargs.extend([
            "--seg",
            segmentation
        ])
    if stack is not None:
        cargs.extend([
            "--stack",
            stack
        ])
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = Annot2stdOutputs(
        root=execution.output_file("."),
        out_annot_file=execution.output_file(output_annot_path),
        out_prob_map_file=execution.output_file(output_annot_path + ".p.mgh"),
        output_surface_segmentation=execution.output_file(segmentation) if (segmentation is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANNOT2STD_METADATA",
    "Annot2stdOutputs",
    "annot2std",
]

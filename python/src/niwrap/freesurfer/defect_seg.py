# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DEFECT_SEG_METADATA = Metadata(
    id="0e4a4cf0254a2348ea18fc134e746047a23ee4d4.boutiques",
    name="defect-seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DefectSegParameters = typing.TypedDict('DefectSegParameters', {
    "__STYX_TYPE__": typing.Literal["defect-seg"],
    "subject": str,
    "lh_only": bool,
    "rh_only": bool,
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
        "defect-seg": defect_seg_cargs,
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
        "defect-seg": defect_seg_outputs,
    }.get(t)


class DefectSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `defect_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_defects: OutputPathType
    """Surface defects volume."""
    defects_summary: OutputPathType
    """Summary of defects indicating numerical ID and number of vertices."""
    defect_labels_fix: OutputPathType
    """Fixed defect labels on the surface."""
    defect_labels_fix_bin: OutputPathType
    """Binary labels for fixed defects."""
    defects_nofix_annot: OutputPathType
    """Annotation file for defects without fixes."""
    defects_fix_annot: OutputPathType
    """Annotation file for defects with fixes."""
    defects_stats: OutputPathType
    """Statistics summary of defects indicating area and average thickness."""


def defect_seg_params(
    subject: str,
    lh_only: bool = False,
    rh_only: bool = False,
) -> DefectSegParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        lh_only: Only process the left hemisphere.
        rh_only: Only process the right hemisphere.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "defect-seg",
        "subject": subject,
        "lh_only": lh_only,
        "rh_only": rh_only,
    }
    return params


def defect_seg_cargs(
    params: DefectSegParameters,
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
    cargs.append("defect-seg")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("lh_only"):
        cargs.append("--lh-only")
    if params.get("rh_only"):
        cargs.append("--rh-only")
    return cargs


def defect_seg_outputs(
    params: DefectSegParameters,
    execution: Execution,
) -> DefectSegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DefectSegOutputs(
        root=execution.output_file("."),
        surface_defects=execution.output_file("mri/surface.defects.mgz"),
        defects_summary=execution.output_file("scripts/?h.defects.summary"),
        defect_labels_fix=execution.output_file("surf/?h.defect_labels.fix.mgz"),
        defect_labels_fix_bin=execution.output_file("surf/?h.defect_labels.fix.bin.mgz"),
        defects_nofix_annot=execution.output_file("label/?h.defects.nofix.annot"),
        defects_fix_annot=execution.output_file("label/?h.defects.fix.annot"),
        defects_stats=execution.output_file("stats/?h.defects.stats"),
    )
    return ret


def defect_seg_execute(
    params: DefectSegParameters,
    execution: Execution,
) -> DefectSegOutputs:
    """
    This program creates some files that allows the user to visualize and evaluate
    the surface defects that were automatically detected and fixed by the topology
    correction program.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DefectSegOutputs`).
    """
    cargs = defect_seg_cargs(params, execution)
    ret = defect_seg_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def defect_seg(
    subject: str,
    lh_only: bool = False,
    rh_only: bool = False,
    runner: Runner | None = None,
) -> DefectSegOutputs:
    """
    This program creates some files that allows the user to visualize and evaluate
    the surface defects that were automatically detected and fixed by the topology
    correction program.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        lh_only: Only process the left hemisphere.
        rh_only: Only process the right hemisphere.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DefectSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DEFECT_SEG_METADATA)
    params = defect_seg_params(subject=subject, lh_only=lh_only, rh_only=rh_only)
    return defect_seg_execute(params, execution)


__all__ = [
    "DEFECT_SEG_METADATA",
    "DefectSegOutputs",
    "DefectSegParameters",
    "defect_seg",
    "defect_seg_params",
]

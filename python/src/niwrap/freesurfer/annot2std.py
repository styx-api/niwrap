# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANNOT2STD_METADATA = Metadata(
    id="fcdd66f979c54df988b9364c89c1d5056e322ab6.boutiques",
    name="annot2std",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Annot2stdParameters = typing.TypedDict('Annot2stdParameters', {
    "__STYX_TYPE__": typing.Literal["annot2std"],
    "output_annot_path": str,
    "subjects": list[str],
    "fsgd_file": typing.NotRequired[InputPathType | None],
    "subject_list_file": typing.NotRequired[InputPathType | None],
    "target": typing.NotRequired[str | None],
    "right_hemisphere": bool,
    "xhemi": bool,
    "surfreg": typing.NotRequired[str | None],
    "srcsurfreg": typing.NotRequired[str | None],
    "trgsurfreg": typing.NotRequired[str | None],
    "a2009s": bool,
    "segmentation": typing.NotRequired[str | None],
    "stack": typing.NotRequired[str | None],
    "help": bool,
    "version": bool,
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
        "annot2std": annot2std_cargs,
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
        "annot2std": annot2std_outputs,
    }.get(t)


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


def annot2std_params(
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
) -> Annot2stdParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "annot2std",
        "output_annot_path": output_annot_path,
        "subjects": subjects,
        "right_hemisphere": right_hemisphere,
        "xhemi": xhemi,
        "a2009s": a2009s,
        "help": help_,
        "version": version,
    }
    if fsgd_file is not None:
        params["fsgd_file"] = fsgd_file
    if subject_list_file is not None:
        params["subject_list_file"] = subject_list_file
    if target is not None:
        params["target"] = target
    if surfreg is not None:
        params["surfreg"] = surfreg
    if srcsurfreg is not None:
        params["srcsurfreg"] = srcsurfreg
    if trgsurfreg is not None:
        params["trgsurfreg"] = trgsurfreg
    if segmentation is not None:
        params["segmentation"] = segmentation
    if stack is not None:
        params["stack"] = stack
    return params


def annot2std_cargs(
    params: Annot2stdParameters,
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
    cargs.append("annot2std")
    cargs.extend([
        "--o",
        params.get("output_annot_path")
    ])
    cargs.extend([
        "--s",
        *params.get("subjects")
    ])
    if params.get("fsgd_file") is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(params.get("fsgd_file"))
        ])
    if params.get("subject_list_file") is not None:
        cargs.extend([
            "--f",
            execution.input_file(params.get("subject_list_file"))
        ])
    if params.get("target") is not None:
        cargs.extend([
            "--t",
            params.get("target")
        ])
    if params.get("right_hemisphere"):
        cargs.append("--rh")
    if params.get("xhemi"):
        cargs.append("--xhemi")
    if params.get("surfreg") is not None:
        cargs.extend([
            "--surfreg",
            params.get("surfreg")
        ])
    if params.get("srcsurfreg") is not None:
        cargs.extend([
            "--srcsurfreg",
            params.get("srcsurfreg")
        ])
    if params.get("trgsurfreg") is not None:
        cargs.extend([
            "--trgsurfreg",
            params.get("trgsurfreg")
        ])
    if params.get("a2009s"):
        cargs.append("--a2009s")
    if params.get("segmentation") is not None:
        cargs.extend([
            "--seg",
            params.get("segmentation")
        ])
    if params.get("stack") is not None:
        cargs.extend([
            "--stack",
            params.get("stack")
        ])
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def annot2std_outputs(
    params: Annot2stdParameters,
    execution: Execution,
) -> Annot2stdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Annot2stdOutputs(
        root=execution.output_file("."),
        out_annot_file=execution.output_file(params.get("output_annot_path")),
        out_prob_map_file=execution.output_file(params.get("output_annot_path") + ".p.mgh"),
        output_surface_segmentation=execution.output_file(params.get("segmentation")) if (params.get("segmentation") is not None) else None,
    )
    return ret


def annot2std_execute(
    params: Annot2stdParameters,
    execution: Execution,
) -> Annot2stdOutputs:
    """
    Creates an average annotation in a standard space based on transforming the
    annotations of the individual subjects to the standard space through the surface
    registration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Annot2stdOutputs`).
    """
    cargs = annot2std_cargs(params, execution)
    ret = annot2std_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


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
    params = annot2std_params(output_annot_path=output_annot_path, subjects=subjects, fsgd_file=fsgd_file, subject_list_file=subject_list_file, target=target, right_hemisphere=right_hemisphere, xhemi=xhemi, surfreg=surfreg, srcsurfreg=srcsurfreg, trgsurfreg=trgsurfreg, a2009s=a2009s, segmentation=segmentation, stack=stack, help_=help_, version=version)
    return annot2std_execute(params, execution)


__all__ = [
    "ANNOT2STD_METADATA",
    "Annot2stdOutputs",
    "Annot2stdParameters",
    "annot2std",
    "annot2std_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EXVIVO_HEMI_PROC_METADATA = Metadata(
    id="9ef40c3f2cab9928f235df79043cbc38b92918d6.boutiques",
    name="exvivo-hemi-proc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


ExvivoHemiProcParameters = typing.TypedDict('ExvivoHemiProcParameters', {
    "__STYX_TYPE__": typing.Literal["exvivo-hemi-proc"],
    "flashdir": str,
    "outdir": str,
    "subject": str,
    "right_hemi": bool,
    "suptent": bool,
    "no_rotate": bool,
    "t1thresh": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
    "check_only": bool,
    "prep_only": bool,
    "mask_only": bool,
    "samseg_only": bool,
    "stop_mmppsp_after": typing.NotRequired[str | None],
    "force": bool,
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
        "exvivo-hemi-proc": exvivo_hemi_proc_cargs,
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


class ExvivoHemiProcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `exvivo_hemi_proc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def exvivo_hemi_proc_params(
    flashdir: str,
    outdir: str,
    subject: str,
    right_hemi: bool = False,
    suptent: bool = False,
    no_rotate: bool = False,
    t1thresh: float | None = None,
    threads: float | None = None,
    check_only: bool = False,
    prep_only: bool = False,
    mask_only: bool = False,
    samseg_only: bool = False,
    stop_mmppsp_after: str | None = None,
    force: bool = False,
) -> ExvivoHemiProcParameters:
    """
    Build parameters.
    
    Args:
        flashdir: Path to the FLASH data directory.
        outdir: Output directory where results will be saved.
        subject: Full path to the subject.
        right_hemi: Process right hemisphere.
        suptent: Indicate no tentorium (cblum and bstem) in the sample.
        no_rotate: Indicate rotation is not needed.
        t1thresh: T1 threshold, default is 415.
        threads: Number of threads to use.
        check_only: Only perform check, without further processing.
        prep_only: Only run up to manual rotation.
        mask_only: Only run up to creation of masks.
        samseg_only: Only run up to samseg.
        stop_mmppsp_after: Stop processing after a specific step\
            {tess,fix,preaparc,sphere,spherereg,white,pial}.
        force: Force the execution, overriding checks.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "exvivo-hemi-proc",
        "flashdir": flashdir,
        "outdir": outdir,
        "subject": subject,
        "right_hemi": right_hemi,
        "suptent": suptent,
        "no_rotate": no_rotate,
        "check_only": check_only,
        "prep_only": prep_only,
        "mask_only": mask_only,
        "samseg_only": samseg_only,
        "force": force,
    }
    if t1thresh is not None:
        params["t1thresh"] = t1thresh
    if threads is not None:
        params["threads"] = threads
    if stop_mmppsp_after is not None:
        params["stop_mmppsp_after"] = stop_mmppsp_after
    return params


def exvivo_hemi_proc_cargs(
    params: ExvivoHemiProcParameters,
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
    cargs.append("exvivo-hemi-proc")
    cargs.extend([
        "--i",
        params.get("flashdir")
    ])
    cargs.extend([
        "--o",
        params.get("outdir")
    ])
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("right_hemi"):
        cargs.append("--rh")
    if params.get("suptent"):
        cargs.append("--suptent")
    if params.get("no_rotate"):
        cargs.append("--no-rotate")
    if params.get("t1thresh") is not None:
        cargs.extend([
            "--t1thresh",
            str(params.get("t1thresh"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("check_only"):
        cargs.append("--check-only")
    if params.get("prep_only"):
        cargs.append("--prep-only")
    if params.get("mask_only"):
        cargs.append("--mask-only")
    if params.get("samseg_only"):
        cargs.append("--samseg-only")
    if params.get("stop_mmppsp_after") is not None:
        cargs.extend([
            "--stop-mmppsp-after",
            params.get("stop_mmppsp_after")
        ])
    if params.get("force"):
        cargs.append("--force")
    return cargs


def exvivo_hemi_proc_outputs(
    params: ExvivoHemiProcParameters,
    execution: Execution,
) -> ExvivoHemiProcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ExvivoHemiProcOutputs(
        root=execution.output_file("."),
    )
    return ret


def exvivo_hemi_proc_execute(
    params: ExvivoHemiProcParameters,
    execution: Execution,
) -> ExvivoHemiProcOutputs:
    """
    Processes whole hemisphere data for Jeans entorhinal subfield labeling project.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ExvivoHemiProcOutputs`).
    """
    params = execution.params(params)
    cargs = exvivo_hemi_proc_cargs(params, execution)
    ret = exvivo_hemi_proc_outputs(params, execution)
    execution.run(cargs)
    return ret


def exvivo_hemi_proc(
    flashdir: str,
    outdir: str,
    subject: str,
    right_hemi: bool = False,
    suptent: bool = False,
    no_rotate: bool = False,
    t1thresh: float | None = None,
    threads: float | None = None,
    check_only: bool = False,
    prep_only: bool = False,
    mask_only: bool = False,
    samseg_only: bool = False,
    stop_mmppsp_after: str | None = None,
    force: bool = False,
    runner: Runner | None = None,
) -> ExvivoHemiProcOutputs:
    """
    Processes whole hemisphere data for Jeans entorhinal subfield labeling project.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        flashdir: Path to the FLASH data directory.
        outdir: Output directory where results will be saved.
        subject: Full path to the subject.
        right_hemi: Process right hemisphere.
        suptent: Indicate no tentorium (cblum and bstem) in the sample.
        no_rotate: Indicate rotation is not needed.
        t1thresh: T1 threshold, default is 415.
        threads: Number of threads to use.
        check_only: Only perform check, without further processing.
        prep_only: Only run up to manual rotation.
        mask_only: Only run up to creation of masks.
        samseg_only: Only run up to samseg.
        stop_mmppsp_after: Stop processing after a specific step\
            {tess,fix,preaparc,sphere,spherereg,white,pial}.
        force: Force the execution, overriding checks.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExvivoHemiProcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXVIVO_HEMI_PROC_METADATA)
    params = exvivo_hemi_proc_params(
        flashdir=flashdir,
        outdir=outdir,
        subject=subject,
        right_hemi=right_hemi,
        suptent=suptent,
        no_rotate=no_rotate,
        t1thresh=t1thresh,
        threads=threads,
        check_only=check_only,
        prep_only=prep_only,
        mask_only=mask_only,
        samseg_only=samseg_only,
        stop_mmppsp_after=stop_mmppsp_after,
        force=force,
    )
    return exvivo_hemi_proc_execute(params, execution)


__all__ = [
    "EXVIVO_HEMI_PROC_METADATA",
    "ExvivoHemiProcOutputs",
    "ExvivoHemiProcParameters",
    "exvivo_hemi_proc",
    "exvivo_hemi_proc_params",
]

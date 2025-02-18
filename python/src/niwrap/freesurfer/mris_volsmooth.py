# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_VOLSMOOTH_METADATA = Metadata(
    id="e771a27b746ea9fefc370e231755f9773a9c0720.boutiques",
    name="mris_volsmooth",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisVolsmoothParameters = typing.TypedDict('MrisVolsmoothParameters', {
    "__STYX_TYPE__": typing.Literal["mris_volsmooth"],
    "input_volume": InputPathType,
    "output_volume": str,
    "registration": InputPathType,
    "projfrac": typing.NotRequired[float | None],
    "projfrac_avg": typing.NotRequired[str | None],
    "fill_ribbon": bool,
    "surf_out": typing.NotRequired[str | None],
    "fwhm": typing.NotRequired[float | None],
    "niters": typing.NotRequired[float | None],
    "vol_fwhm": typing.NotRequired[float | None],
    "log": typing.NotRequired[str | None],
    "nocleanup": bool,
    "debug": bool,
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
        "mris_volsmooth": mris_volsmooth_cargs,
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
        "mris_volsmooth": mris_volsmooth_outputs,
    }.get(t)


class MrisVolsmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_volsmooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outvol_file: OutputPathType
    """Output volume file after surface-based smoothing."""
    lh_surface_output: OutputPathType | None
    """Left hemisphere smoothed surface output."""
    rh_surface_output: OutputPathType | None
    """Right hemisphere smoothed surface output."""


def mris_volsmooth_params(
    input_volume: InputPathType,
    output_volume: str,
    registration: InputPathType,
    projfrac: float | None = None,
    projfrac_avg: str | None = None,
    fill_ribbon: bool = False,
    surf_out: str | None = None,
    fwhm: float | None = None,
    niters: float | None = None,
    vol_fwhm: float | None = None,
    log: str | None = None,
    nocleanup: bool = False,
    debug: bool = False,
) -> MrisVolsmoothParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Source volume with values that will be smoothed on the\
            surface.
        output_volume: Output volume.
        registration: TKRegister-style registration matrix that maps between\
            the input/output volumes and the FreeSurfer surface anatomical.
        projfrac: Fraction of thickness to project along surface normal.
        projfrac_avg: Average sampling along normal, specified by min, max, and\
            delta.
        fill_ribbon: Fill ribbon.
        surf_out: Save smoothed surfaces as basename.?h.mgh.
        fwhm: Surface smoothing by full-width/half-max in mm.
        niters: Specify surface smoothing by number of nearest neighbor\
            smoothing iterations.
        vol_fwhm: Volume smoothing outside of the surface. Surface voxels and\
            non-surface voxels are smoothed separately.
        log: Explicitly set log file.
        nocleanup: Do not delete temporary files.
        debug: Turn on debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_volsmooth",
        "input_volume": input_volume,
        "output_volume": output_volume,
        "registration": registration,
        "fill_ribbon": fill_ribbon,
        "nocleanup": nocleanup,
        "debug": debug,
    }
    if projfrac is not None:
        params["projfrac"] = projfrac
    if projfrac_avg is not None:
        params["projfrac_avg"] = projfrac_avg
    if surf_out is not None:
        params["surf_out"] = surf_out
    if fwhm is not None:
        params["fwhm"] = fwhm
    if niters is not None:
        params["niters"] = niters
    if vol_fwhm is not None:
        params["vol_fwhm"] = vol_fwhm
    if log is not None:
        params["log"] = log
    return params


def mris_volsmooth_cargs(
    params: MrisVolsmoothParameters,
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
    cargs.append("mris_volsmooth")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "-o",
        params.get("output_volume")
    ])
    cargs.extend([
        "-reg",
        execution.input_file(params.get("registration"))
    ])
    if params.get("projfrac") is not None:
        cargs.extend([
            "--projfrac",
            str(params.get("projfrac"))
        ])
    if params.get("projfrac_avg") is not None:
        cargs.extend([
            "--projfrac-avg",
            params.get("projfrac_avg")
        ])
    if params.get("fill_ribbon"):
        cargs.append("--fill-ribbon")
    if params.get("surf_out") is not None:
        cargs.extend([
            "--surf-out",
            params.get("surf_out")
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("niters") is not None:
        cargs.extend([
            "--niters",
            str(params.get("niters"))
        ])
    if params.get("vol_fwhm") is not None:
        cargs.extend([
            "--vol-fwhm",
            str(params.get("vol_fwhm"))
        ])
    if params.get("log") is not None:
        cargs.extend([
            "--log",
            params.get("log")
        ])
    if params.get("nocleanup"):
        cargs.append("--nocleanup")
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def mris_volsmooth_outputs(
    params: MrisVolsmoothParameters,
    execution: Execution,
) -> MrisVolsmoothOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisVolsmoothOutputs(
        root=execution.output_file("."),
        outvol_file=execution.output_file(params.get("output_volume") + ".mgh"),
        lh_surface_output=execution.output_file(params.get("surf_out") + ".lh.mgh") if (params.get("surf_out") is not None) else None,
        rh_surface_output=execution.output_file(params.get("surf_out") + ".rh.mgh") if (params.get("surf_out") is not None) else None,
    )
    return ret


def mris_volsmooth_execute(
    params: MrisVolsmoothParameters,
    execution: Execution,
) -> MrisVolsmoothOutputs:
    """
    Performs surface-based smoothing inside a volume by sampling a volume to a
    surface, smoothing on the surface, then replacing the surface voxels in the
    volume with values that were smoothed.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisVolsmoothOutputs`).
    """
    cargs = mris_volsmooth_cargs(params, execution)
    ret = mris_volsmooth_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_volsmooth(
    input_volume: InputPathType,
    output_volume: str,
    registration: InputPathType,
    projfrac: float | None = None,
    projfrac_avg: str | None = None,
    fill_ribbon: bool = False,
    surf_out: str | None = None,
    fwhm: float | None = None,
    niters: float | None = None,
    vol_fwhm: float | None = None,
    log: str | None = None,
    nocleanup: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> MrisVolsmoothOutputs:
    """
    Performs surface-based smoothing inside a volume by sampling a volume to a
    surface, smoothing on the surface, then replacing the surface voxels in the
    volume with values that were smoothed.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Source volume with values that will be smoothed on the\
            surface.
        output_volume: Output volume.
        registration: TKRegister-style registration matrix that maps between\
            the input/output volumes and the FreeSurfer surface anatomical.
        projfrac: Fraction of thickness to project along surface normal.
        projfrac_avg: Average sampling along normal, specified by min, max, and\
            delta.
        fill_ribbon: Fill ribbon.
        surf_out: Save smoothed surfaces as basename.?h.mgh.
        fwhm: Surface smoothing by full-width/half-max in mm.
        niters: Specify surface smoothing by number of nearest neighbor\
            smoothing iterations.
        vol_fwhm: Volume smoothing outside of the surface. Surface voxels and\
            non-surface voxels are smoothed separately.
        log: Explicitly set log file.
        nocleanup: Do not delete temporary files.
        debug: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisVolsmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_VOLSMOOTH_METADATA)
    params = mris_volsmooth_params(input_volume=input_volume, output_volume=output_volume, registration=registration, projfrac=projfrac, projfrac_avg=projfrac_avg, fill_ribbon=fill_ribbon, surf_out=surf_out, fwhm=fwhm, niters=niters, vol_fwhm=vol_fwhm, log=log, nocleanup=nocleanup, debug=debug)
    return mris_volsmooth_execute(params, execution)


__all__ = [
    "MRIS_VOLSMOOTH_METADATA",
    "MrisVolsmoothOutputs",
    "MrisVolsmoothParameters",
    "mris_volsmooth",
    "mris_volsmooth_params",
]

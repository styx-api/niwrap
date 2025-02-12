# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_NITERS2FWHM_METADATA = Metadata(
    id="46d8d10a4cb889cf8adeaf5acc47511663af44b8.boutiques",
    name="mris_niters2fwhm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisNiters2fwhmParameters = typing.TypedDict('MrisNiters2fwhmParameters', {
    "__STYX_TYPE__": typing.Literal["mris_niters2fwhm"],
    "subject": str,
    "hemi": str,
    "surf": str,
    "dof": float,
    "niters": float,
    "debug": bool,
    "checkopts": bool,
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
        "mris_niters2fwhm": mris_niters2fwhm_cargs,
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


class MrisNiters2fwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_niters2fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_niters2fwhm_params(
    subject: str,
    hemi: str,
    surf: str,
    dof: float,
    niters: float,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
) -> MrisNiters2fwhmParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        surf: Surface type (e.g., white, pial).
        dof: Degrees of Freedom.
        niters: Maximum number of iterations.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_niters2fwhm",
        "subject": subject,
        "hemi": hemi,
        "surf": surf,
        "dof": dof,
        "niters": niters,
        "debug": debug,
        "checkopts": checkopts,
        "help": help_,
        "version": version,
    }
    return params


def mris_niters2fwhm_cargs(
    params: MrisNiters2fwhmParameters,
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
    cargs.append("mris_niters2fwhm")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    cargs.extend([
        "--h",
        params.get("hemi")
    ])
    cargs.extend([
        "--surf",
        params.get("surf")
    ])
    cargs.extend([
        "--dof",
        str(params.get("dof"))
    ])
    cargs.extend([
        "--niters",
        str(params.get("niters"))
    ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mris_niters2fwhm_outputs(
    params: MrisNiters2fwhmParameters,
    execution: Execution,
) -> MrisNiters2fwhmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisNiters2fwhmOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_niters2fwhm_execute(
    params: MrisNiters2fwhmParameters,
    execution: Execution,
) -> MrisNiters2fwhmOutputs:
    """
    Convert number of iterations to full width at half maximum (FWHM) for surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisNiters2fwhmOutputs`).
    """
    cargs = mris_niters2fwhm_cargs(params, execution)
    ret = mris_niters2fwhm_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_niters2fwhm(
    subject: str,
    hemi: str,
    surf: str,
    dof: float,
    niters: float,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrisNiters2fwhmOutputs:
    """
    Convert number of iterations to full width at half maximum (FWHM) for surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        surf: Surface type (e.g., white, pial).
        dof: Degrees of Freedom.
        niters: Maximum number of iterations.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisNiters2fwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_NITERS2FWHM_METADATA)
    params = mris_niters2fwhm_params(subject=subject, hemi=hemi, surf=surf, dof=dof, niters=niters, debug=debug, checkopts=checkopts, help_=help_, version=version)
    return mris_niters2fwhm_execute(params, execution)


__all__ = [
    "MRIS_NITERS2FWHM_METADATA",
    "MrisNiters2fwhmOutputs",
    "MrisNiters2fwhmParameters",
    "mris_niters2fwhm",
    "mris_niters2fwhm_params",
]

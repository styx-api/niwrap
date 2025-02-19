# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SH2RESPONSE_METADATA = Metadata(
    id="73af982ff7a9439d2a7181a0cb546efa4f302105.boutiques",
    name="sh2response",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Sh2responseConfigParameters = typing.TypedDict('Sh2responseConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Sh2responseParameters = typing.TypedDict('Sh2responseParameters', {
    "__STYX_TYPE__": typing.Literal["sh2response"],
    "lmax": typing.NotRequired[int | None],
    "dump": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Sh2responseConfigParameters] | None],
    "help": bool,
    "version": bool,
    "SH": InputPathType,
    "mask": InputPathType,
    "directions": InputPathType,
    "response": str,
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
        "sh2response": sh2response_cargs,
        "config": sh2response_config_cargs,
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
        "sh2response": sh2response_outputs,
    }.get(t)


def sh2response_config_params(
    key: str,
    value: str,
) -> Sh2responseConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def sh2response_config_cargs(
    params: Sh2responseConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class Sh2responseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sh2response(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    response: OutputPathType
    """the output axially-symmetric spherical harmonic coefficients"""
    dump: OutputPathType | None
    """dump the m=0 SH coefficients from all voxels in the mask to the output
    file, rather than their mean """


def sh2response_params(
    sh: InputPathType,
    mask: InputPathType,
    directions: InputPathType,
    response: str,
    lmax: int | None = None,
    dump: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Sh2responseConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Sh2responseParameters:
    """
    Build parameters.
    
    Args:
        sh: the spherical harmonic decomposition of the diffusion-weighted\
            images.
        mask: the mask containing the voxels from which to estimate the\
            response function.
        directions: a 4D image containing the direction vectors along which to\
            estimate the response function.
        response: the output axially-symmetric spherical harmonic coefficients.
        lmax: specify the maximum harmonic degree of the response function to\
            estimate.
        dump: dump the m=0 SH coefficients from all voxels in the mask to the\
            output file, rather than their mean.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sh2response",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "SH": sh,
        "mask": mask,
        "directions": directions,
        "response": response,
    }
    if lmax is not None:
        params["lmax"] = lmax
    if dump is not None:
        params["dump"] = dump
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def sh2response_cargs(
    params: Sh2responseParameters,
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
    cargs.append("sh2response")
    if params.get("lmax") is not None:
        cargs.extend([
            "-lmax",
            str(params.get("lmax"))
        ])
    if params.get("dump") is not None:
        cargs.extend([
            "-dump",
            params.get("dump")
        ])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("SH")))
    cargs.append(execution.input_file(params.get("mask")))
    cargs.append(execution.input_file(params.get("directions")))
    cargs.append(params.get("response"))
    return cargs


def sh2response_outputs(
    params: Sh2responseParameters,
    execution: Execution,
) -> Sh2responseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Sh2responseOutputs(
        root=execution.output_file("."),
        response=execution.output_file(params.get("response")),
        dump=execution.output_file(params.get("dump")) if (params.get("dump") is not None) else None,
    )
    return ret


def sh2response_execute(
    params: Sh2responseParameters,
    execution: Execution,
) -> Sh2responseOutputs:
    """
    Generate an appropriate response function from the image data for spherical
    deconvolution.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Sh2responseOutputs`).
    """
    params = execution.params(params)
    cargs = sh2response_cargs(params, execution)
    ret = sh2response_outputs(params, execution)
    execution.run(cargs)
    return ret


def sh2response(
    sh: InputPathType,
    mask: InputPathType,
    directions: InputPathType,
    response: str,
    lmax: int | None = None,
    dump: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Sh2responseConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Sh2responseOutputs:
    """
    Generate an appropriate response function from the image data for spherical
    deconvolution.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        sh: the spherical harmonic decomposition of the diffusion-weighted\
            images.
        mask: the mask containing the voxels from which to estimate the\
            response function.
        directions: a 4D image containing the direction vectors along which to\
            estimate the response function.
        response: the output axially-symmetric spherical harmonic coefficients.
        lmax: specify the maximum harmonic degree of the response function to\
            estimate.
        dump: dump the m=0 SH coefficients from all voxels in the mask to the\
            output file, rather than their mean.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Sh2responseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SH2RESPONSE_METADATA)
    params = sh2response_params(
        lmax=lmax,
        dump=dump,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        sh=sh,
        mask=mask,
        directions=directions,
        response=response,
    )
    return sh2response_execute(params, execution)


__all__ = [
    "SH2RESPONSE_METADATA",
    "Sh2responseConfigParameters",
    "Sh2responseOutputs",
    "Sh2responseParameters",
    "sh2response",
    "sh2response_config_params",
    "sh2response_params",
]

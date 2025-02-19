# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIXEL2SH_METADATA = Metadata(
    id="ad311f3879760b3a8467869800c42a82cc4da4d8.boutiques",
    name="fixel2sh",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Fixel2shConfigParameters = typing.TypedDict('Fixel2shConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Fixel2shParameters = typing.TypedDict('Fixel2shParameters', {
    "__STYX_TYPE__": typing.Literal["fixel2sh"],
    "lmax": typing.NotRequired[int | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Fixel2shConfigParameters] | None],
    "help": bool,
    "version": bool,
    "fixel_in": InputPathType,
    "sh_out": str,
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
        "fixel2sh": fixel2sh_cargs,
        "config": fixel2sh_config_cargs,
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
        "fixel2sh": fixel2sh_outputs,
    }.get(t)


def fixel2sh_config_params(
    key: str,
    value: str,
) -> Fixel2shConfigParameters:
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


def fixel2sh_config_cargs(
    params: Fixel2shConfigParameters,
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


class Fixel2shOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixel2sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sh_out: OutputPathType
    """the output sh image."""


def fixel2sh_params(
    fixel_in: InputPathType,
    sh_out: str,
    lmax: int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fixel2shConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Fixel2shParameters:
    """
    Build parameters.
    
    Args:
        fixel_in: the input fixel data file.
        sh_out: the output sh image.
        lmax: set the maximum harmonic order for the output series (Default: 8).
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
        "__STYXTYPE__": "fixel2sh",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "fixel_in": fixel_in,
        "sh_out": sh_out,
    }
    if lmax is not None:
        params["lmax"] = lmax
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fixel2sh_cargs(
    params: Fixel2shParameters,
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
    cargs.append("fixel2sh")
    if params.get("lmax") is not None:
        cargs.extend([
            "-lmax",
            str(params.get("lmax"))
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
    cargs.append(execution.input_file(params.get("fixel_in")))
    cargs.append(params.get("sh_out"))
    return cargs


def fixel2sh_outputs(
    params: Fixel2shParameters,
    execution: Execution,
) -> Fixel2shOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fixel2shOutputs(
        root=execution.output_file("."),
        sh_out=execution.output_file(params.get("sh_out")),
    )
    return ret


def fixel2sh_execute(
    params: Fixel2shParameters,
    execution: Execution,
) -> Fixel2shOutputs:
    """
    Convert a fixel-based sparse-data image into an spherical harmonic image.
    
    This command generates spherical harmonic data from fixels that can be
    visualised using the ODF tool in MRview. The output ODF lobes are scaled
    according to the values in the input fixel image.
    
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
        NamedTuple of outputs (described in `Fixel2shOutputs`).
    """
    params = execution.params(params)
    cargs = fixel2sh_cargs(params, execution)
    ret = fixel2sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def fixel2sh(
    fixel_in: InputPathType,
    sh_out: str,
    lmax: int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fixel2shConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Fixel2shOutputs:
    """
    Convert a fixel-based sparse-data image into an spherical harmonic image.
    
    This command generates spherical harmonic data from fixels that can be
    visualised using the ODF tool in MRview. The output ODF lobes are scaled
    according to the values in the input fixel image.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        fixel_in: the input fixel data file.
        sh_out: the output sh image.
        lmax: set the maximum harmonic order for the output series (Default: 8).
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
        NamedTuple of outputs (described in `Fixel2shOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXEL2SH_METADATA)
    params = fixel2sh_params(
        lmax=lmax,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        fixel_in=fixel_in,
        sh_out=sh_out,
    )
    return fixel2sh_execute(params, execution)


__all__ = [
    "FIXEL2SH_METADATA",
    "Fixel2shConfigParameters",
    "Fixel2shOutputs",
    "Fixel2shParameters",
    "fixel2sh",
    "fixel2sh_config_params",
    "fixel2sh_params",
]

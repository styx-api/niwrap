# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PEAKS2FIXEL_METADATA = Metadata(
    id="d7a45807f5df2a3ff0f6456f9bc36be6cdae2250.boutiques",
    name="peaks2fixel",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Peaks2fixelConfigParameters = typing.TypedDict('Peaks2fixelConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Peaks2fixelParameters = typing.TypedDict('Peaks2fixelParameters', {
    "__STYX_TYPE__": typing.Literal["peaks2fixel"],
    "dataname": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Peaks2fixelConfigParameters] | None],
    "help": bool,
    "version": bool,
    "directions": InputPathType,
    "fixels": str,
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
        "peaks2fixel": peaks2fixel_cargs,
        "config": peaks2fixel_config_cargs,
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
        "peaks2fixel": peaks2fixel_outputs,
    }.get(t)


def peaks2fixel_config_params(
    key: str,
    value: str,
) -> Peaks2fixelConfigParameters:
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


def peaks2fixel_config_cargs(
    params: Peaks2fixelConfigParameters,
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


class Peaks2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `peaks2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fixels: OutputPathType
    """the output fixel directory."""


def peaks2fixel_params(
    directions: InputPathType,
    fixels: str,
    dataname: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Peaks2fixelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Peaks2fixelParameters:
    """
    Build parameters.
    
    Args:
        directions: the input directions image; each volume corresponds to the\
            x, y & z component of each direction vector in turn.
        fixels: the output fixel directory.
        dataname: the name of the output fixel data file encoding peak\
            amplitudes.
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
        "__STYXTYPE__": "peaks2fixel",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "directions": directions,
        "fixels": fixels,
    }
    if dataname is not None:
        params["dataname"] = dataname
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def peaks2fixel_cargs(
    params: Peaks2fixelParameters,
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
    cargs.append("peaks2fixel")
    if params.get("dataname") is not None:
        cargs.extend([
            "-dataname",
            params.get("dataname")
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
    cargs.append(execution.input_file(params.get("directions")))
    cargs.append(params.get("fixels"))
    return cargs


def peaks2fixel_outputs(
    params: Peaks2fixelParameters,
    execution: Execution,
) -> Peaks2fixelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Peaks2fixelOutputs(
        root=execution.output_file("."),
        fixels=execution.output_file(params.get("fixels")),
    )
    return ret


def peaks2fixel_execute(
    params: Peaks2fixelParameters,
    execution: Execution,
) -> Peaks2fixelOutputs:
    """
    Convert peak directions image to a fixel directory.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Peaks2fixelOutputs`).
    """
    params = execution.params(params)
    cargs = peaks2fixel_cargs(params, execution)
    ret = peaks2fixel_outputs(params, execution)
    execution.run(cargs)
    return ret


def peaks2fixel(
    directions: InputPathType,
    fixels: str,
    dataname: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Peaks2fixelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Peaks2fixelOutputs:
    """
    Convert peak directions image to a fixel directory.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        directions: the input directions image; each volume corresponds to the\
            x, y & z component of each direction vector in turn.
        fixels: the output fixel directory.
        dataname: the name of the output fixel data file encoding peak\
            amplitudes.
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
        NamedTuple of outputs (described in `Peaks2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PEAKS2FIXEL_METADATA)
    params = peaks2fixel_params(
        dataname=dataname,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        directions=directions,
        fixels=fixels,
    )
    return peaks2fixel_execute(params, execution)


__all__ = [
    "PEAKS2FIXEL_METADATA",
    "Peaks2fixelConfigParameters",
    "Peaks2fixelOutputs",
    "Peaks2fixelParameters",
    "peaks2fixel",
    "peaks2fixel_config_params",
    "peaks2fixel_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TCK2FIXEL_METADATA = Metadata(
    id="0ebab309539e07f49a62d79a33984c3cbda69b88.boutiques",
    name="tck2fixel",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Tck2fixelConfigParameters = typing.TypedDict('Tck2fixelConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Tck2fixelParameters = typing.TypedDict('Tck2fixelParameters', {
    "__STYX_TYPE__": typing.Literal["tck2fixel"],
    "angle": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Tck2fixelConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks": InputPathType,
    "fixel_folder_in": InputPathType,
    "fixel_folder_out": str,
    "fixel_data_out": str,
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
        "tck2fixel": tck2fixel_cargs,
        "config": tck2fixel_config_cargs,
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


def tck2fixel_config_params(
    key: str,
    value: str,
) -> Tck2fixelConfigParameters:
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


def tck2fixel_config_cargs(
    params: Tck2fixelConfigParameters,
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


class Tck2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tck2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tck2fixel_params(
    tracks: InputPathType,
    fixel_folder_in: InputPathType,
    fixel_folder_out: str,
    fixel_data_out: str,
    angle: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tck2fixelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Tck2fixelParameters:
    """
    Build parameters.
    
    Args:
        tracks: the input tracks.
        fixel_folder_in: the input fixel folder. Used to define the fixels and\
            their directions.
        fixel_folder_out: the fixel folder to which the output will be written.\
            This can be the same as the input folder if desired.
        fixel_data_out: the name of the fixel data image.
        angle: the max angle threshold for assigning streamline tangents to\
            fixels (Default: 45 degrees).
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
        "__STYXTYPE__": "tck2fixel",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks": tracks,
        "fixel_folder_in": fixel_folder_in,
        "fixel_folder_out": fixel_folder_out,
        "fixel_data_out": fixel_data_out,
    }
    if angle is not None:
        params["angle"] = angle
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tck2fixel_cargs(
    params: Tck2fixelParameters,
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
    cargs.append("tck2fixel")
    if params.get("angle") is not None:
        cargs.extend([
            "-angle",
            str(params.get("angle"))
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
    cargs.append(execution.input_file(params.get("tracks")))
    cargs.append(execution.input_file(params.get("fixel_folder_in")))
    cargs.append(params.get("fixel_folder_out"))
    cargs.append(params.get("fixel_data_out"))
    return cargs


def tck2fixel_outputs(
    params: Tck2fixelParameters,
    execution: Execution,
) -> Tck2fixelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tck2fixelOutputs(
        root=execution.output_file("."),
    )
    return ret


def tck2fixel_execute(
    params: Tck2fixelParameters,
    execution: Execution,
) -> Tck2fixelOutputs:
    """
    Compute a fixel TDI map from a tractogram.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tck2fixelOutputs`).
    """
    params = execution.params(params)
    cargs = tck2fixel_cargs(params, execution)
    ret = tck2fixel_outputs(params, execution)
    execution.run(cargs)
    return ret


def tck2fixel(
    tracks: InputPathType,
    fixel_folder_in: InputPathType,
    fixel_folder_out: str,
    fixel_data_out: str,
    angle: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tck2fixelConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Tck2fixelOutputs:
    """
    Compute a fixel TDI map from a tractogram.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks: the input tracks.
        fixel_folder_in: the input fixel folder. Used to define the fixels and\
            their directions.
        fixel_folder_out: the fixel folder to which the output will be written.\
            This can be the same as the input folder if desired.
        fixel_data_out: the name of the fixel data image.
        angle: the max angle threshold for assigning streamline tangents to\
            fixels (Default: 45 degrees).
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
        NamedTuple of outputs (described in `Tck2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCK2FIXEL_METADATA)
    params = tck2fixel_params(
        angle=angle,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        tracks=tracks,
        fixel_folder_in=fixel_folder_in,
        fixel_folder_out=fixel_folder_out,
        fixel_data_out=fixel_data_out,
    )
    return tck2fixel_execute(params, execution)


__all__ = [
    "TCK2FIXEL_METADATA",
    "Tck2fixelConfigParameters",
    "Tck2fixelOutputs",
    "Tck2fixelParameters",
    "tck2fixel",
    "tck2fixel_config_params",
    "tck2fixel_params",
]

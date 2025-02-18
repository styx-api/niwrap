# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIXELCONNECTIVITY_METADATA = Metadata(
    id="811fe5b2580b330dbeded0c16e56819fd86331a7.boutiques",
    name="fixelconnectivity",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
FixelconnectivityConfigParameters = typing.TypedDict('FixelconnectivityConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
FixelconnectivityParameters = typing.TypedDict('FixelconnectivityParameters', {
    "__STYX_TYPE__": typing.Literal["fixelconnectivity"],
    "threshold": typing.NotRequired[float | None],
    "angle": typing.NotRequired[float | None],
    "mask": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[FixelconnectivityConfigParameters] | None],
    "help": bool,
    "version": bool,
    "fixel_directory": InputPathType,
    "tracks": InputPathType,
    "matrix": str,
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
        "fixelconnectivity": fixelconnectivity_cargs,
        "config": fixelconnectivity_config_cargs,
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
        "fixelconnectivity": fixelconnectivity_outputs,
    }.get(t)


def fixelconnectivity_config_params(
    key: str,
    value: str,
) -> FixelconnectivityConfigParameters:
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


def fixelconnectivity_config_cargs(
    params: FixelconnectivityConfigParameters,
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


class FixelconnectivityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelconnectivity(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    matrix: OutputPathType
    """the output fixel-fixel connectivity matrix directory path"""


def fixelconnectivity_params(
    fixel_directory: InputPathType,
    tracks: InputPathType,
    matrix: str,
    threshold: float | None = None,
    angle: float | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelconnectivityConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> FixelconnectivityParameters:
    """
    Build parameters.
    
    Args:
        fixel_directory: the directory containing the fixels between which\
            connectivity will be quantified.
        tracks: the tracks used to determine fixel-fixel connectivity.
        matrix: the output fixel-fixel connectivity matrix directory path.
        threshold: a threshold to define the required fraction of shared\
            connections to be included in the neighbourhood (default: 0.01).
        angle: the max angle threshold for assigning streamline tangents to\
            fixels (Default: 45 degrees).
        mask: provide a fixel data file containing a mask of those fixels to be\
            computed; fixels outside the mask will be empty in the output matrix.
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
        "__STYXTYPE__": "fixelconnectivity",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "fixel_directory": fixel_directory,
        "tracks": tracks,
        "matrix": matrix,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if angle is not None:
        params["angle"] = angle
    if mask is not None:
        params["mask"] = mask
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fixelconnectivity_cargs(
    params: FixelconnectivityParameters,
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
    cargs.append("fixelconnectivity")
    if params.get("threshold") is not None:
        cargs.extend([
            "-threshold",
            str(params.get("threshold"))
        ])
    if params.get("angle") is not None:
        cargs.extend([
            "-angle",
            str(params.get("angle"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
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
    cargs.append(execution.input_file(params.get("fixel_directory")))
    cargs.append(execution.input_file(params.get("tracks")))
    cargs.append(params.get("matrix"))
    return cargs


def fixelconnectivity_outputs(
    params: FixelconnectivityParameters,
    execution: Execution,
) -> FixelconnectivityOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixelconnectivityOutputs(
        root=execution.output_file("."),
        matrix=execution.output_file(params.get("matrix")),
    )
    return ret


def fixelconnectivity_execute(
    params: FixelconnectivityParameters,
    execution: Execution,
) -> FixelconnectivityOutputs:
    """
    Generate a fixel-fixel connectivity matrix.
    
    This command will generate a directory containing three images, which
    encodes the fixel-fixel connectivity matrix. Documentation regarding this
    format and how to use it will come in the future.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixelconnectivityOutputs`).
    """
    cargs = fixelconnectivity_cargs(params, execution)
    ret = fixelconnectivity_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fixelconnectivity(
    fixel_directory: InputPathType,
    tracks: InputPathType,
    matrix: str,
    threshold: float | None = None,
    angle: float | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelconnectivityConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelconnectivityOutputs:
    """
    Generate a fixel-fixel connectivity matrix.
    
    This command will generate a directory containing three images, which
    encodes the fixel-fixel connectivity matrix. Documentation regarding this
    format and how to use it will come in the future.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        fixel_directory: the directory containing the fixels between which\
            connectivity will be quantified.
        tracks: the tracks used to determine fixel-fixel connectivity.
        matrix: the output fixel-fixel connectivity matrix directory path.
        threshold: a threshold to define the required fraction of shared\
            connections to be included in the neighbourhood (default: 0.01).
        angle: the max angle threshold for assigning streamline tangents to\
            fixels (Default: 45 degrees).
        mask: provide a fixel data file containing a mask of those fixels to be\
            computed; fixels outside the mask will be empty in the output matrix.
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
        NamedTuple of outputs (described in `FixelconnectivityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCONNECTIVITY_METADATA)
    params = fixelconnectivity_params(threshold=threshold, angle=angle, mask=mask, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, fixel_directory=fixel_directory, tracks=tracks, matrix=matrix)
    return fixelconnectivity_execute(params, execution)


__all__ = [
    "FIXELCONNECTIVITY_METADATA",
    "FixelconnectivityConfigParameters",
    "FixelconnectivityOutputs",
    "FixelconnectivityParameters",
    "fixelconnectivity",
    "fixelconnectivity_config_params",
    "fixelconnectivity_params",
]

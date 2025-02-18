# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WARPCORRECT_METADATA = Metadata(
    id="ac61099f3060923f7f158e31279303a1a92afb02.boutiques",
    name="warpcorrect",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
WarpcorrectConfigParameters = typing.TypedDict('WarpcorrectConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
WarpcorrectParameters = typing.TypedDict('WarpcorrectParameters', {
    "__STYX_TYPE__": typing.Literal["warpcorrect"],
    "marker": typing.NotRequired[list[float] | None],
    "tolerance": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[WarpcorrectConfigParameters] | None],
    "help": bool,
    "version": bool,
    "in": InputPathType,
    "out": str,
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
        "warpcorrect": warpcorrect_cargs,
        "config": warpcorrect_config_cargs,
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
        "warpcorrect": warpcorrect_outputs,
    }.get(t)


def warpcorrect_config_params(
    key: str,
    value: str,
) -> WarpcorrectConfigParameters:
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


def warpcorrect_config_cargs(
    params: WarpcorrectConfigParameters,
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


class WarpcorrectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warpcorrect(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output warp image."""


def warpcorrect_params(
    in_: InputPathType,
    out: str,
    marker: list[float] | None = None,
    tolerance: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpcorrectConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> WarpcorrectParameters:
    """
    Build parameters.
    
    Args:
        in_: the input warp image.
        out: the output warp image.
        marker: single value or a comma separated list of values that define\
            out of bounds voxels in the input warp image. Default: (0,0,0).
        tolerance: numerical precision used for L2 matrix norm comparison.\
            Default: 9.99999975e-06.
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
        "__STYXTYPE__": "warpcorrect",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "in": in_,
        "out": out,
    }
    if marker is not None:
        params["marker"] = marker
    if tolerance is not None:
        params["tolerance"] = tolerance
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def warpcorrect_cargs(
    params: WarpcorrectParameters,
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
    cargs.append("warpcorrect")
    if params.get("marker") is not None:
        cargs.extend([
            "-marker",
            *map(str, params.get("marker"))
        ])
    if params.get("tolerance") is not None:
        cargs.extend([
            "-tolerance",
            str(params.get("tolerance"))
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
    cargs.append(execution.input_file(params.get("in")))
    cargs.append(params.get("out"))
    return cargs


def warpcorrect_outputs(
    params: WarpcorrectParameters,
    execution: Execution,
) -> WarpcorrectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WarpcorrectOutputs(
        root=execution.output_file("."),
        out=execution.output_file(params.get("out")),
    )
    return ret


def warpcorrect_execute(
    params: WarpcorrectParameters,
    execution: Execution,
) -> WarpcorrectOutputs:
    """
    Replaces voxels in a deformation field that point to a specific out of bounds
    location with nan,nan,nan.
    
    This can be used in conjunction with the warpinit command to compute a
    MRtrix compatible deformation field from non-linear transformations
    generated by any other registration package.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WarpcorrectOutputs`).
    """
    cargs = warpcorrect_cargs(params, execution)
    ret = warpcorrect_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def warpcorrect(
    in_: InputPathType,
    out: str,
    marker: list[float] | None = None,
    tolerance: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpcorrectConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> WarpcorrectOutputs:
    """
    Replaces voxels in a deformation field that point to a specific out of bounds
    location with nan,nan,nan.
    
    This can be used in conjunction with the warpinit command to compute a
    MRtrix compatible deformation field from non-linear transformations
    generated by any other registration package.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_: the input warp image.
        out: the output warp image.
        marker: single value or a comma separated list of values that define\
            out of bounds voxels in the input warp image. Default: (0,0,0).
        tolerance: numerical precision used for L2 matrix norm comparison.\
            Default: 9.99999975e-06.
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
        NamedTuple of outputs (described in `WarpcorrectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARPCORRECT_METADATA)
    params = warpcorrect_params(marker=marker, tolerance=tolerance, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, in_=in_, out=out)
    return warpcorrect_execute(params, execution)


__all__ = [
    "WARPCORRECT_METADATA",
    "WarpcorrectConfigParameters",
    "WarpcorrectOutputs",
    "WarpcorrectParameters",
    "warpcorrect",
    "warpcorrect_config_params",
    "warpcorrect_params",
]

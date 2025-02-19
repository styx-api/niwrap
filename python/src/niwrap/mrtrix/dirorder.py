# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DIRORDER_METADATA = Metadata(
    id="822332bcb7593b804c24d6da3c7da0a1eb44ba1a.boutiques",
    name="dirorder",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


DirorderConfigParameters = typing.TypedDict('DirorderConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


DirorderParameters = typing.TypedDict('DirorderParameters', {
    "__STYX_TYPE__": typing.Literal["dirorder"],
    "cartesian": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[DirorderConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": str,
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
        "dirorder": dirorder_cargs,
        "config": dirorder_config_cargs,
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
        "dirorder": dirorder_outputs,
    }.get(t)


def dirorder_config_params(
    key: str,
    value: str,
) -> DirorderConfigParameters:
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


def dirorder_config_cargs(
    params: DirorderConfigParameters,
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


class DirorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirorder(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output directions file"""


def dirorder_params(
    input_: InputPathType,
    output: str,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirorderConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> DirorderParameters:
    """
    Build parameters.
    
    Args:
        input_: the input directions file.
        output: the output directions file.
        cartesian: Output the directions in Cartesian coordinates [x y z]\
            instead of [az el].
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
        "__STYXTYPE__": "dirorder",
        "cartesian": cartesian,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dirorder_cargs(
    params: DirorderParameters,
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
    cargs.append("dirorder")
    if params.get("cartesian"):
        cargs.append("-cartesian")
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
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("output"))
    return cargs


def dirorder_outputs(
    params: DirorderParameters,
    execution: Execution,
) -> DirorderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DirorderOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def dirorder_execute(
    params: DirorderParameters,
    execution: Execution,
) -> DirorderOutputs:
    """
    Reorder a set of directions to ensure near-uniformity upon truncation.
    
    The intent of this command is to reorder a set of gradient directions such
    that if a scan is terminated prematurely, at any point, the acquired
    directions will still be close to optimally distributed on the half-sphere.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DirorderOutputs`).
    """
    params = execution.params(params)
    cargs = dirorder_cargs(params, execution)
    ret = dirorder_outputs(params, execution)
    execution.run(cargs)
    return ret


def dirorder(
    input_: InputPathType,
    output: str,
    cartesian: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirorderConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DirorderOutputs:
    """
    Reorder a set of directions to ensure near-uniformity upon truncation.
    
    The intent of this command is to reorder a set of gradient directions such
    that if a scan is terminated prematurely, at any point, the acquired
    directions will still be close to optimally distributed on the half-sphere.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input directions file.
        output: the output directions file.
        cartesian: Output the directions in Cartesian coordinates [x y z]\
            instead of [az el].
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
        NamedTuple of outputs (described in `DirorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRORDER_METADATA)
    params = dirorder_params(
        cartesian=cartesian,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        input_=input_,
        output=output,
    )
    return dirorder_execute(params, execution)


__all__ = [
    "DIRORDER_METADATA",
    "DirorderConfigParameters",
    "DirorderOutputs",
    "DirorderParameters",
    "dirorder",
    "dirorder_config_params",
    "dirorder_params",
]

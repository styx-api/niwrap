# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRDUMP_METADATA = Metadata(
    id="e5986855c45bf7b67212dd583f998650804933d1.boutiques",
    name="mrdump",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MrdumpConfigParameters = typing.TypedDict('MrdumpConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MrdumpParameters = typing.TypedDict('MrdumpParameters', {
    "__STYX_TYPE__": typing.Literal["mrdump"],
    "mask": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrdumpConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": typing.NotRequired[str | None],
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
        "mrdump": mrdump_cargs,
        "config": mrdump_config_cargs,
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
        "mrdump": mrdump_outputs,
    }.get(t)


def mrdump_config_params(
    key: str,
    value: str,
) -> MrdumpConfigParameters:
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


def mrdump_config_cargs(
    params: MrdumpConfigParameters,
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


class MrdumpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrdump(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """the (optional) output text file."""


def mrdump_params(
    input_: InputPathType,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrdumpConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    output: str | None = None,
) -> MrdumpParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image.
        mask: only write the image values within voxels specified by a mask\
            image.
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
        output: the (optional) output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mrdump",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
    }
    if mask is not None:
        params["mask"] = mask
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    if output is not None:
        params["output"] = output
    return params


def mrdump_cargs(
    params: MrdumpParameters,
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
    cargs.append("mrdump")
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
    cargs.append(execution.input_file(params.get("input")))
    if params.get("output") is not None:
        cargs.append(params.get("output"))
    return cargs


def mrdump_outputs(
    params: MrdumpParameters,
    execution: Execution,
) -> MrdumpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrdumpOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")) if (params.get("output") is not None) else None,
    )
    return ret


def mrdump_execute(
    params: MrdumpParameters,
    execution: Execution,
) -> MrdumpOutputs:
    """
    Print out the values within an image.
    
    If no destination file is specified, the voxel locations will be printed to
    stdout.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrdumpOutputs`).
    """
    cargs = mrdump_cargs(params, execution)
    ret = mrdump_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrdump(
    input_: InputPathType,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrdumpConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    output: str | None = None,
    runner: Runner | None = None,
) -> MrdumpOutputs:
    """
    Print out the values within an image.
    
    If no destination file is specified, the voxel locations will be printed to
    stdout.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image.
        mask: only write the image values within voxels specified by a mask\
            image.
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
        output: the (optional) output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrdumpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRDUMP_METADATA)
    params = mrdump_params(mask=mask, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, output=output)
    return mrdump_execute(params, execution)


__all__ = [
    "MRDUMP_METADATA",
    "MrdumpConfigParameters",
    "MrdumpOutputs",
    "MrdumpParameters",
    "mrdump",
    "mrdump_config_params",
    "mrdump_params",
]

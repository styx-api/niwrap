# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MESHCONVERT_METADATA = Metadata(
    id="762c9b5d3b33c0ecdebcfabfcf5bf55092f9fed9.boutiques",
    name="meshconvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


MeshconvertTransformParameters = typing.TypedDict('MeshconvertTransformParameters', {
    "__STYX_TYPE__": typing.Literal["transform"],
    "mode": str,
    "image": InputPathType,
})


MeshconvertConfigParameters = typing.TypedDict('MeshconvertConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


MeshconvertParameters = typing.TypedDict('MeshconvertParameters', {
    "__STYX_TYPE__": typing.Literal["meshconvert"],
    "binary": bool,
    "transform": typing.NotRequired[MeshconvertTransformParameters | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MeshconvertConfigParameters] | None],
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
        "meshconvert": meshconvert_cargs,
        "transform": meshconvert_transform_cargs,
        "config": meshconvert_config_cargs,
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
        "meshconvert": meshconvert_outputs,
    }.get(t)


def meshconvert_transform_params(
    mode: str,
    image: InputPathType,
) -> MeshconvertTransformParameters:
    """
    Build parameters.
    
    Args:
        mode: transform vertices from one coordinate space to another, based on\
            a template image; options are: first2real, real2first, voxel2real,\
            real2voxel, fs2real.
        image: transform vertices from one coordinate space to another, based\
            on a template image; options are: first2real, real2first, voxel2real,\
            real2voxel, fs2real.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "transform",
        "mode": mode,
        "image": image,
    }
    return params


def meshconvert_transform_cargs(
    params: MeshconvertTransformParameters,
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
    cargs.append("-transform")
    cargs.append(params.get("mode"))
    cargs.append(execution.input_file(params.get("image")))
    return cargs


def meshconvert_config_params(
    key: str,
    value: str,
) -> MeshconvertConfigParameters:
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


def meshconvert_config_cargs(
    params: MeshconvertConfigParameters,
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


class MeshconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meshconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output mesh file"""


def meshconvert_params(
    input_: InputPathType,
    output: str,
    binary: bool = False,
    transform: MeshconvertTransformParameters | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MeshconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MeshconvertParameters:
    """
    Build parameters.
    
    Args:
        input_: the input mesh file.
        output: the output mesh file.
        binary: write the output mesh file in binary format (if supported).
        transform: transform vertices from one coordinate space to another,\
            based on a template image; options are: first2real, real2first,\
            voxel2real, real2voxel, fs2real.
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
        "__STYXTYPE__": "meshconvert",
        "binary": binary,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if transform is not None:
        params["transform"] = transform
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def meshconvert_cargs(
    params: MeshconvertParameters,
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
    cargs.append("meshconvert")
    if params.get("binary"):
        cargs.append("-binary")
    if params.get("transform") is not None:
        cargs.extend(dyn_cargs(params.get("transform")["__STYXTYPE__"])(params.get("transform"), execution))
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


def meshconvert_outputs(
    params: MeshconvertParameters,
    execution: Execution,
) -> MeshconvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MeshconvertOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def meshconvert_execute(
    params: MeshconvertParameters,
    execution: Execution,
) -> MeshconvertOutputs:
    """
    Convert meshes between different formats, and apply transformations.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MeshconvertOutputs`).
    """
    params = execution.params(params)
    cargs = meshconvert_cargs(params, execution)
    ret = meshconvert_outputs(params, execution)
    execution.run(cargs)
    return ret


def meshconvert(
    input_: InputPathType,
    output: str,
    binary: bool = False,
    transform: MeshconvertTransformParameters | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MeshconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MeshconvertOutputs:
    """
    Convert meshes between different formats, and apply transformations.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input mesh file.
        output: the output mesh file.
        binary: write the output mesh file in binary format (if supported).
        transform: transform vertices from one coordinate space to another,\
            based on a template image; options are: first2real, real2first,\
            voxel2real, real2voxel, fs2real.
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
        NamedTuple of outputs (described in `MeshconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MESHCONVERT_METADATA)
    params = meshconvert_params(
        binary=binary,
        transform=transform,
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
    return meshconvert_execute(params, execution)


__all__ = [
    "MESHCONVERT_METADATA",
    "MeshconvertConfigParameters",
    "MeshconvertOutputs",
    "MeshconvertParameters",
    "MeshconvertTransformParameters",
    "meshconvert",
    "meshconvert_config_params",
    "meshconvert_params",
    "meshconvert_transform_params",
]

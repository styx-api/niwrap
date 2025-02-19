# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRCAT_METADATA = Metadata(
    id="b3de92bc09aeac701d99649eaea82387c297125a.boutiques",
    name="mrcat",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


MrcatConfigParameters = typing.TypedDict('MrcatConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


MrcatParameters = typing.TypedDict('MrcatParameters', {
    "__STYX_TYPE__": typing.Literal["mrcat"],
    "axis": typing.NotRequired[int | None],
    "datatype": typing.NotRequired[str | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrcatConfigParameters] | None],
    "help": bool,
    "version": bool,
    "image1": InputPathType,
    "image2": list[InputPathType],
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
        "mrcat": mrcat_cargs,
        "config": mrcat_config_cargs,
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
        "mrcat": mrcat_outputs,
    }.get(t)


def mrcat_config_params(
    key: str,
    value: str,
) -> MrcatConfigParameters:
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


def mrcat_config_cargs(
    params: MrcatConfigParameters,
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


class MrcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""


def mrcat_params(
    image1: InputPathType,
    image2: list[InputPathType],
    output: str,
    axis: int | None = None,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcatConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrcatParameters:
    """
    Build parameters.
    
    Args:
        image1: the first input image.
        image2: additional input image(s).
        output: the output image.
        axis: specify axis along which concatenation should be performed. By\
            default, the program will use the last non-singleton, non-spatial axis\
            of any of the input images - in other words axis 3 or whichever axis\
            (greater than 3) of the input images has size greater than one.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
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
        "__STYXTYPE__": "mrcat",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "image1": image1,
        "image2": image2,
        "output": output,
    }
    if axis is not None:
        params["axis"] = axis
    if datatype is not None:
        params["datatype"] = datatype
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrcat_cargs(
    params: MrcatParameters,
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
    cargs.append("mrcat")
    if params.get("axis") is not None:
        cargs.extend([
            "-axis",
            str(params.get("axis"))
        ])
    if params.get("datatype") is not None:
        cargs.extend([
            "-datatype",
            params.get("datatype")
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
    cargs.append(execution.input_file(params.get("image1")))
    cargs.extend([execution.input_file(f) for f in params.get("image2")])
    cargs.append(params.get("output"))
    return cargs


def mrcat_outputs(
    params: MrcatParameters,
    execution: Execution,
) -> MrcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrcatOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mrcat_execute(
    params: MrcatParameters,
    execution: Execution,
) -> MrcatOutputs:
    """
    Concatenate several images into one.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrcatOutputs`).
    """
    params = execution.params(params)
    cargs = mrcat_cargs(params, execution)
    ret = mrcat_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrcat(
    image1: InputPathType,
    image2: list[InputPathType],
    output: str,
    axis: int | None = None,
    datatype: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcatConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrcatOutputs:
    """
    Concatenate several images into one.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        image1: the first input image.
        image2: additional input image(s).
        output: the output image.
        axis: specify axis along which concatenation should be performed. By\
            default, the program will use the last non-singleton, non-spatial axis\
            of any of the input images - in other words axis 3 or whichever axis\
            (greater than 3) of the input images has size greater than one.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
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
        NamedTuple of outputs (described in `MrcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCAT_METADATA)
    params = mrcat_params(
        axis=axis,
        datatype=datatype,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        image1=image1,
        image2=image2,
        output=output,
    )
    return mrcat_execute(params, execution)


__all__ = [
    "MRCAT_METADATA",
    "MrcatConfigParameters",
    "MrcatOutputs",
    "MrcatParameters",
    "mrcat",
    "mrcat_config_params",
    "mrcat_params",
]

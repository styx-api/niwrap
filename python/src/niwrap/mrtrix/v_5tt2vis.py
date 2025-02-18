# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_5TT2VIS_METADATA = Metadata(
    id="702b49a5b25df0d2069fb4f29ba6316bbc4674e9.boutiques",
    name="5tt2vis",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
V5tt2visConfigParameters = typing.TypedDict('V5tt2visConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
V5tt2visParameters = typing.TypedDict('V5tt2visParameters', {
    "__STYX_TYPE__": typing.Literal["5tt2vis"],
    "bg": typing.NotRequired[float | None],
    "cgm": typing.NotRequired[float | None],
    "sgm": typing.NotRequired[float | None],
    "wm": typing.NotRequired[float | None],
    "csf": typing.NotRequired[float | None],
    "path": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[V5tt2visConfigParameters] | None],
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
        "5tt2vis": v_5tt2vis_cargs,
        "config": v_5tt2vis_config_cargs,
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
        "5tt2vis": v_5tt2vis_outputs,
    }.get(t)


def v_5tt2vis_config_params(
    key: str,
    value: str,
) -> V5tt2visConfigParameters:
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


def v_5tt2vis_config_cargs(
    params: V5tt2visConfigParameters,
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


class V5tt2visOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_5tt2vis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output 3D image for visualisation"""


def v_5tt2vis_params(
    input_: InputPathType,
    output: str,
    bg: float | None = None,
    cgm: float | None = None,
    sgm: float | None = None,
    wm: float | None = None,
    csf: float | None = None,
    path: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[V5tt2visConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> V5tt2visParameters:
    """
    Build parameters.
    
    Args:
        input_: the input 4D tissue-segmented image.
        output: the output 3D image for visualisation.
        bg: image intensity of background (default: 0).
        cgm: image intensity of cortical grey matter (default: 0.5).
        sgm: image intensity of sub-cortical grey matter (default: 0.75).
        wm: image intensity of white matter (default: 1).
        csf: image intensity of CSF (default: 0.15).
        path: image intensity of pathological tissue (default: 2).
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
        "__STYXTYPE__": "5tt2vis",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if bg is not None:
        params["bg"] = bg
    if cgm is not None:
        params["cgm"] = cgm
    if sgm is not None:
        params["sgm"] = sgm
    if wm is not None:
        params["wm"] = wm
    if csf is not None:
        params["csf"] = csf
    if path is not None:
        params["path"] = path
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def v_5tt2vis_cargs(
    params: V5tt2visParameters,
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
    cargs.append("5tt2vis")
    if params.get("bg") is not None:
        cargs.extend([
            "-bg",
            str(params.get("bg"))
        ])
    if params.get("cgm") is not None:
        cargs.extend([
            "-cgm",
            str(params.get("cgm"))
        ])
    if params.get("sgm") is not None:
        cargs.extend([
            "-sgm",
            str(params.get("sgm"))
        ])
    if params.get("wm") is not None:
        cargs.extend([
            "-wm",
            str(params.get("wm"))
        ])
    if params.get("csf") is not None:
        cargs.extend([
            "-csf",
            str(params.get("csf"))
        ])
    if params.get("path") is not None:
        cargs.extend([
            "-path",
            str(params.get("path"))
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
    cargs.append(params.get("output"))
    return cargs


def v_5tt2vis_outputs(
    params: V5tt2visParameters,
    execution: Execution,
) -> V5tt2visOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V5tt2visOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def v_5tt2vis_execute(
    params: V5tt2visParameters,
    execution: Execution,
) -> V5tt2visOutputs:
    """
    Generate an image for visualisation purposes from an ACT 5TT segmented
    anatomical image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V5tt2visOutputs`).
    """
    cargs = v_5tt2vis_cargs(params, execution)
    ret = v_5tt2vis_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_5tt2vis(
    input_: InputPathType,
    output: str,
    bg: float | None = None,
    cgm: float | None = None,
    sgm: float | None = None,
    wm: float | None = None,
    csf: float | None = None,
    path: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[V5tt2visConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> V5tt2visOutputs:
    """
    Generate an image for visualisation purposes from an ACT 5TT segmented
    anatomical image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input 4D tissue-segmented image.
        output: the output 3D image for visualisation.
        bg: image intensity of background (default: 0).
        cgm: image intensity of cortical grey matter (default: 0.5).
        sgm: image intensity of sub-cortical grey matter (default: 0.75).
        wm: image intensity of white matter (default: 1).
        csf: image intensity of CSF (default: 0.15).
        path: image intensity of pathological tissue (default: 2).
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
        NamedTuple of outputs (described in `V5tt2visOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_5TT2VIS_METADATA)
    params = v_5tt2vis_params(bg=bg, cgm=cgm, sgm=sgm, wm=wm, csf=csf, path=path, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, output=output)
    return v_5tt2vis_execute(params, execution)


__all__ = [
    "V5tt2visConfigParameters",
    "V5tt2visOutputs",
    "V5tt2visParameters",
    "V_5TT2VIS_METADATA",
    "v_5tt2vis",
    "v_5tt2vis_config_params",
    "v_5tt2vis_params",
]

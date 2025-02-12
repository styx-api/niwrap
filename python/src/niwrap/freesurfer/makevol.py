# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAKEVOL_METADATA = Metadata(
    id="b095c7a5e6e89f542d67def46cd9241f840756fe.boutiques",
    name="makevol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MakevolParameters = typing.TypedDict('MakevolParameters', {
    "__STYX_TYPE__": typing.Literal["makevol"],
    "filename": typing.NotRequired[str | None],
    "width": typing.NotRequired[int | None],
    "height": typing.NotRequired[int | None],
    "depth": typing.NotRequired[int | None],
    "sizex": typing.NotRequired[float | None],
    "sizey": typing.NotRequired[float | None],
    "sizez": typing.NotRequired[float | None],
    "set_method": typing.NotRequired[str | None],
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
        "makevol": makevol_cargs,
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
        "makevol": makevol_outputs,
    }.get(t)


class MakevolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `makevol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """The created volume file."""


def makevol_params(
    filename: str | None = "new_volume.mgz",
    width: int | None = 256,
    height: int | None = 256,
    depth: int | None = 256,
    sizex: float | None = 1.0,
    sizey: float | None = 1.0,
    sizez: float | None = 1.0,
    set_method: str | None = "xyz",
) -> MakevolParameters:
    """
    Build parameters.
    
    Args:
        filename: Write volume to the given file name, implying type.
        width: Use integer WIDTH as the x dimension.
        height: Use integer HEIGHT as the y dimension.
        depth: Use integer DEPTH as the z dimension.
        sizex: Use float SIZEX as the x resolution.
        sizey: Use float SIZEY as the y resolution.
        sizez: Use float SIZEZ as the z resolution.
        set_method: Use METHOD to fill the values. Methods: xyz, random,\
            constant.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "makevol",
    }
    if filename is not None:
        params["filename"] = filename
    if width is not None:
        params["width"] = width
    if height is not None:
        params["height"] = height
    if depth is not None:
        params["depth"] = depth
    if sizex is not None:
        params["sizex"] = sizex
    if sizey is not None:
        params["sizey"] = sizey
    if sizez is not None:
        params["sizez"] = sizez
    if set_method is not None:
        params["set_method"] = set_method
    return params


def makevol_cargs(
    params: MakevolParameters,
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
    cargs.append("makevol")
    if params.get("filename") is not None:
        cargs.extend([
            "-f",
            params.get("filename")
        ])
    if params.get("width") is not None:
        cargs.extend([
            "-x",
            str(params.get("width"))
        ])
    if params.get("height") is not None:
        cargs.extend([
            "-y",
            str(params.get("height"))
        ])
    if params.get("depth") is not None:
        cargs.extend([
            "-z",
            str(params.get("depth"))
        ])
    if params.get("sizex") is not None:
        cargs.extend([
            "--sizex",
            str(params.get("sizex"))
        ])
    if params.get("sizey") is not None:
        cargs.extend([
            "--sizey",
            str(params.get("sizey"))
        ])
    if params.get("sizez") is not None:
        cargs.extend([
            "--sizez",
            str(params.get("sizez"))
        ])
    if params.get("set_method") is not None:
        cargs.extend([
            "--set-method",
            params.get("set_method")
        ])
    return cargs


def makevol_outputs(
    params: MakevolParameters,
    execution: Execution,
) -> MakevolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MakevolOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("filename")) if (params.get("filename") is not None) else None,
    )
    return ret


def makevol_execute(
    params: MakevolParameters,
    execution: Execution,
) -> MakevolOutputs:
    """
    A tool to create a volume with given parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MakevolOutputs`).
    """
    cargs = makevol_cargs(params, execution)
    ret = makevol_outputs(params, execution)
    execution.run(cargs)
    return ret


def makevol(
    filename: str | None = "new_volume.mgz",
    width: int | None = 256,
    height: int | None = 256,
    depth: int | None = 256,
    sizex: float | None = 1.0,
    sizey: float | None = 1.0,
    sizez: float | None = 1.0,
    set_method: str | None = "xyz",
    runner: Runner | None = None,
) -> MakevolOutputs:
    """
    A tool to create a volume with given parameters.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        filename: Write volume to the given file name, implying type.
        width: Use integer WIDTH as the x dimension.
        height: Use integer HEIGHT as the y dimension.
        depth: Use integer DEPTH as the z dimension.
        sizex: Use float SIZEX as the x resolution.
        sizey: Use float SIZEY as the y resolution.
        sizez: Use float SIZEZ as the z resolution.
        set_method: Use METHOD to fill the values. Methods: xyz, random,\
            constant.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakevolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKEVOL_METADATA)
    params = makevol_params(filename=filename, width=width, height=height, depth=depth, sizex=sizex, sizey=sizey, sizez=sizez, set_method=set_method)
    return makevol_execute(params, execution)


__all__ = [
    "MAKEVOL_METADATA",
    "MakevolOutputs",
    "MakevolParameters",
    "makevol",
    "makevol_params",
]

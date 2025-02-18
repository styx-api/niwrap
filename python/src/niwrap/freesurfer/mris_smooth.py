# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SMOOTH_METADATA = Metadata(
    id="75bc8e87c534738bfed1dc6d67307d0c1e29317a.boutiques",
    name="mris_smooth",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSmoothParameters = typing.TypedDict('MrisSmoothParameters', {
    "__STYX_TYPE__": typing.Literal["mris_smooth"],
    "input_surface": InputPathType,
    "output_surface": str,
    "average_iters": typing.NotRequired[float | None],
    "smoothing_iters": typing.NotRequired[float | None],
    "no_write": bool,
    "curvature_name": typing.NotRequired[str | None],
    "area_name": typing.NotRequired[str | None],
    "gaussian_params": typing.NotRequired[list[float] | None],
    "normalize_area": bool,
    "momentum": typing.NotRequired[float | None],
    "snapshot_interval": typing.NotRequired[float | None],
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
        "mris_smooth": mris_smooth_cargs,
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
        "mris_smooth": mris_smooth_outputs,
    }.get(t)


class MrisSmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_smooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """Output smoothed surface file."""
    curvature_file: OutputPathType
    """Output curvature file (if written)."""
    area_file: OutputPathType
    """Output area file (if written)."""


def mris_smooth_params(
    input_surface: InputPathType,
    output_surface: str,
    average_iters: float | None = 10,
    smoothing_iters: float | None = 10,
    no_write: bool = False,
    curvature_name: str | None = "curv",
    area_name: str | None = "area",
    gaussian_params: list[float] | None = None,
    normalize_area: bool = False,
    momentum: float | None = None,
    snapshot_interval: float | None = None,
) -> MrisSmoothParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file for smoothing.
        output_surface: Output surface file after smoothing.
        average_iters: Specify number of curvature averaging iterations\
            (default is 10).
        smoothing_iters: Specify number of smoothing iterations (default is\
            10).
        no_write: Disable writing of curvature and area estimates.
        curvature_name: Write curvature to a specified file name (default\
            'curv').
        area_name: Write area to a specified file name (default 'area').
        gaussian_params: Use Gaussian curvature smoothing with specified norm\
            and steps.
        normalize_area: Normalize area after smoothing.
        momentum: Set momentum value.
        snapshot_interval: Write snapshot every specified number of iterations.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_smooth",
        "input_surface": input_surface,
        "output_surface": output_surface,
        "no_write": no_write,
        "normalize_area": normalize_area,
    }
    if average_iters is not None:
        params["average_iters"] = average_iters
    if smoothing_iters is not None:
        params["smoothing_iters"] = smoothing_iters
    if curvature_name is not None:
        params["curvature_name"] = curvature_name
    if area_name is not None:
        params["area_name"] = area_name
    if gaussian_params is not None:
        params["gaussian_params"] = gaussian_params
    if momentum is not None:
        params["momentum"] = momentum
    if snapshot_interval is not None:
        params["snapshot_interval"] = snapshot_interval
    return params


def mris_smooth_cargs(
    params: MrisSmoothParameters,
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
    cargs.append("mris_smooth")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(params.get("output_surface"))
    if params.get("average_iters") is not None:
        cargs.extend([
            "-a",
            str(params.get("average_iters"))
        ])
    if params.get("smoothing_iters") is not None:
        cargs.extend([
            "-n",
            str(params.get("smoothing_iters"))
        ])
    if params.get("no_write"):
        cargs.append("-nw")
    if params.get("curvature_name") is not None:
        cargs.extend([
            "-c",
            params.get("curvature_name")
        ])
    if params.get("area_name") is not None:
        cargs.extend([
            "-b",
            params.get("area_name")
        ])
    if params.get("gaussian_params") is not None:
        cargs.extend([
            "-g",
            *map(str, params.get("gaussian_params"))
        ])
    if params.get("normalize_area"):
        cargs.append("-area")
    if params.get("momentum") is not None:
        cargs.extend([
            "-m",
            str(params.get("momentum"))
        ])
    if params.get("snapshot_interval") is not None:
        cargs.extend([
            "-w",
            str(params.get("snapshot_interval"))
        ])
    return cargs


def mris_smooth_outputs(
    params: MrisSmoothParameters,
    execution: Execution,
) -> MrisSmoothOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSmoothOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(params.get("output_surface")),
        curvature_file=execution.output_file("${OUTPUT_SURFACE}_curvature"),
        area_file=execution.output_file("${OUTPUT_SURFACE}_area"),
    )
    return ret


def mris_smooth_execute(
    params: MrisSmoothParameters,
    execution: Execution,
) -> MrisSmoothOutputs:
    """
    This program smooths the tessellation of a cortical surface and writes out the
    mean curvature and area files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSmoothOutputs`).
    """
    cargs = mris_smooth_cargs(params, execution)
    ret = mris_smooth_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_smooth(
    input_surface: InputPathType,
    output_surface: str,
    average_iters: float | None = 10,
    smoothing_iters: float | None = 10,
    no_write: bool = False,
    curvature_name: str | None = "curv",
    area_name: str | None = "area",
    gaussian_params: list[float] | None = None,
    normalize_area: bool = False,
    momentum: float | None = None,
    snapshot_interval: float | None = None,
    runner: Runner | None = None,
) -> MrisSmoothOutputs:
    """
    This program smooths the tessellation of a cortical surface and writes out the
    mean curvature and area files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file for smoothing.
        output_surface: Output surface file after smoothing.
        average_iters: Specify number of curvature averaging iterations\
            (default is 10).
        smoothing_iters: Specify number of smoothing iterations (default is\
            10).
        no_write: Disable writing of curvature and area estimates.
        curvature_name: Write curvature to a specified file name (default\
            'curv').
        area_name: Write area to a specified file name (default 'area').
        gaussian_params: Use Gaussian curvature smoothing with specified norm\
            and steps.
        normalize_area: Normalize area after smoothing.
        momentum: Set momentum value.
        snapshot_interval: Write snapshot every specified number of iterations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SMOOTH_METADATA)
    params = mris_smooth_params(input_surface=input_surface, output_surface=output_surface, average_iters=average_iters, smoothing_iters=smoothing_iters, no_write=no_write, curvature_name=curvature_name, area_name=area_name, gaussian_params=gaussian_params, normalize_area=normalize_area, momentum=momentum, snapshot_interval=snapshot_interval)
    return mris_smooth_execute(params, execution)


__all__ = [
    "MRIS_SMOOTH_METADATA",
    "MrisSmoothOutputs",
    "MrisSmoothParameters",
    "mris_smooth",
    "mris_smooth_params",
]

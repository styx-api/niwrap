# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BORDER_TO_ROIS_METADATA = Metadata(
    id="53ffc190f09f435ce8a8a69ab0341699da3030a0.boutiques",
    name="border-to-rois",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


BorderToRoisParameters = typing.TypedDict('BorderToRoisParameters', {
    "__STYX_TYPE__": typing.Literal["border-to-rois"],
    "surface": InputPathType,
    "border_file": InputPathType,
    "metric_out": str,
    "opt_border_name": typing.NotRequired[str | None],
    "opt_inverse": bool,
    "opt_include_border": bool,
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
        "border-to-rois": border_to_rois_cargs,
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
        "border-to-rois": border_to_rois_outputs,
    }.get(t)


class BorderToRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_to_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def border_to_rois_params(
    surface: InputPathType,
    border_file: InputPathType,
    metric_out: str,
    opt_border_name: str | None = None,
    opt_inverse: bool = False,
    opt_include_border: bool = False,
) -> BorderToRoisParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface the borders are drawn on.
        border_file: the border file.
        metric_out: the output metric file.
        opt_border_name: create ROI for only one border: the name of the border.
        opt_inverse: use inverse selection (outside border).
        opt_include_border: include vertices the border is closest to.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "border-to-rois",
        "surface": surface,
        "border_file": border_file,
        "metric_out": metric_out,
        "opt_inverse": opt_inverse,
        "opt_include_border": opt_include_border,
    }
    if opt_border_name is not None:
        params["opt_border_name"] = opt_border_name
    return params


def border_to_rois_cargs(
    params: BorderToRoisParameters,
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
    cargs.append("wb_command")
    cargs.append("-border-to-rois")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("border_file")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_border_name") is not None:
        cargs.extend([
            "-border",
            params.get("opt_border_name")
        ])
    if params.get("opt_inverse"):
        cargs.append("-inverse")
    if params.get("opt_include_border"):
        cargs.append("-include-border")
    return cargs


def border_to_rois_outputs(
    params: BorderToRoisParameters,
    execution: Execution,
) -> BorderToRoisOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BorderToRoisOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def border_to_rois_execute(
    params: BorderToRoisParameters,
    execution: Execution,
) -> BorderToRoisOutputs:
    """
    Make metric rois from borders.
    
    By default, draws ROIs inside all borders in the border file, as separate
    metric columns.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BorderToRoisOutputs`).
    """
    params = execution.params(params)
    cargs = border_to_rois_cargs(params, execution)
    ret = border_to_rois_outputs(params, execution)
    execution.run(cargs)
    return ret


def border_to_rois(
    surface: InputPathType,
    border_file: InputPathType,
    metric_out: str,
    opt_border_name: str | None = None,
    opt_inverse: bool = False,
    opt_include_border: bool = False,
    runner: Runner | None = None,
) -> BorderToRoisOutputs:
    """
    Make metric rois from borders.
    
    By default, draws ROIs inside all borders in the border file, as separate
    metric columns.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface the borders are drawn on.
        border_file: the border file.
        metric_out: the output metric file.
        opt_border_name: create ROI for only one border: the name of the border.
        opt_inverse: use inverse selection (outside border).
        opt_include_border: include vertices the border is closest to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderToRoisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_TO_ROIS_METADATA)
    params = border_to_rois_params(
        surface=surface,
        border_file=border_file,
        metric_out=metric_out,
        opt_border_name=opt_border_name,
        opt_inverse=opt_inverse,
        opt_include_border=opt_include_border,
    )
    return border_to_rois_execute(params, execution)


__all__ = [
    "BORDER_TO_ROIS_METADATA",
    "BorderToRoisOutputs",
    "BorderToRoisParameters",
    "border_to_rois",
    "border_to_rois_params",
]

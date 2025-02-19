# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_DILATE_METADATA = Metadata(
    id="f636c722a86c2948ae67646d52f753fe26a10b28.boutiques",
    name="label-dilate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


LabelDilateParameters = typing.TypedDict('LabelDilateParameters', {
    "__STYX_TYPE__": typing.Literal["label-dilate"],
    "label": InputPathType,
    "surface": InputPathType,
    "dilate_dist": float,
    "label_out": str,
    "opt_bad_vertex_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
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
        "label-dilate": label_dilate_cargs,
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
        "label-dilate": label_dilate_outputs,
    }.get(t)


class LabelDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def label_dilate_params(
    label: InputPathType,
    surface: InputPathType,
    dilate_dist: float,
    label_out: str,
    opt_bad_vertex_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> LabelDilateParameters:
    """
    Build parameters.
    
    Args:
        label: the input label.
        surface: the surface to dilate on.
        dilate_dist: distance in mm to dilate the labels.
        label_out: the output label file.
        opt_bad_vertex_roi_roi_metric: specify an roi of vertices to overwrite,\
            rather than vertices with the unlabeled key: metric file, positive\
            values denote vertices to have their values replaced.
        opt_column_column: select a single column to dilate: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label-dilate",
        "label": label,
        "surface": surface,
        "dilate_dist": dilate_dist,
        "label_out": label_out,
    }
    if opt_bad_vertex_roi_roi_metric is not None:
        params["opt_bad_vertex_roi_roi_metric"] = opt_bad_vertex_roi_roi_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def label_dilate_cargs(
    params: LabelDilateParameters,
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
    cargs.append("-label-dilate")
    cargs.append(execution.input_file(params.get("label")))
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(str(params.get("dilate_dist")))
    cargs.append(params.get("label_out"))
    if params.get("opt_bad_vertex_roi_roi_metric") is not None:
        cargs.extend([
            "-bad-vertex-roi",
            execution.input_file(params.get("opt_bad_vertex_roi_roi_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    return cargs


def label_dilate_outputs(
    params: LabelDilateParameters,
    execution: Execution,
) -> LabelDilateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelDilateOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
    )
    return ret


def label_dilate_execute(
    params: LabelDilateParameters,
    execution: Execution,
) -> LabelDilateOutputs:
    """
    Dilate a label file.
    
    Fills in label information for all vertices designated as bad, up to the
    specified distance away from other labels. If -bad-vertex-roi is specified,
    all vertices, including those with the unlabeled key, are good, except for
    vertices with a positive value in the ROI. If it is not specified, only
    vertices with the unlabeled key are bad.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelDilateOutputs`).
    """
    params = execution.params(params)
    cargs = label_dilate_cargs(params, execution)
    ret = label_dilate_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_dilate(
    label: InputPathType,
    surface: InputPathType,
    dilate_dist: float,
    label_out: str,
    opt_bad_vertex_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> LabelDilateOutputs:
    """
    Dilate a label file.
    
    Fills in label information for all vertices designated as bad, up to the
    specified distance away from other labels. If -bad-vertex-roi is specified,
    all vertices, including those with the unlabeled key, are good, except for
    vertices with a positive value in the ROI. If it is not specified, only
    vertices with the unlabeled key are bad.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label: the input label.
        surface: the surface to dilate on.
        dilate_dist: distance in mm to dilate the labels.
        label_out: the output label file.
        opt_bad_vertex_roi_roi_metric: specify an roi of vertices to overwrite,\
            rather than vertices with the unlabeled key: metric file, positive\
            values denote vertices to have their values replaced.
        opt_column_column: select a single column to dilate: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_DILATE_METADATA)
    params = label_dilate_params(
        label=label,
        surface=surface,
        dilate_dist=dilate_dist,
        label_out=label_out,
        opt_bad_vertex_roi_roi_metric=opt_bad_vertex_roi_roi_metric,
        opt_column_column=opt_column_column,
        opt_corrected_areas_area_metric=opt_corrected_areas_area_metric,
    )
    return label_dilate_execute(params, execution)


__all__ = [
    "LABEL_DILATE_METADATA",
    "LabelDilateOutputs",
    "LabelDilateParameters",
    "label_dilate",
    "label_dilate_params",
]

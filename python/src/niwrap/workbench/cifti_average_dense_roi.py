# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_AVERAGE_DENSE_ROI_METADATA = Metadata(
    id="7c085aa8c9afe5e56e95447c34a9a19302b7d9c9.boutiques",
    name="cifti-average-dense-roi",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiAverageDenseRoiCiftiRoiParameters = typing.TypedDict('CiftiAverageDenseRoiCiftiRoiParameters', {
    "__STYX_TYPE__": typing.Literal["cifti_roi"],
    "roi_cifti": InputPathType,
    "opt_in_memory": bool,
})
CiftiAverageDenseRoiCiftiParameters = typing.TypedDict('CiftiAverageDenseRoiCiftiParameters', {
    "__STYX_TYPE__": typing.Literal["cifti"],
    "cifti_in": InputPathType,
})
CiftiAverageDenseRoiParameters = typing.TypedDict('CiftiAverageDenseRoiParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-average-dense-roi"],
    "cifti_out": str,
    "cifti_roi": typing.NotRequired[CiftiAverageDenseRoiCiftiRoiParameters | None],
    "opt_left_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_right_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_vol_roi_roi_vol": typing.NotRequired[InputPathType | None],
    "opt_left_area_surf_left_surf": typing.NotRequired[InputPathType | None],
    "opt_right_area_surf_right_surf": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_area_surf_cerebellum_surf": typing.NotRequired[InputPathType | None],
    "cifti": typing.NotRequired[list[CiftiAverageDenseRoiCiftiParameters] | None],
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
        "cifti-average-dense-roi": cifti_average_dense_roi_cargs,
        "cifti_roi": cifti_average_dense_roi_cifti_roi_cargs,
        "cifti": cifti_average_dense_roi_cifti_cargs,
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
        "cifti-average-dense-roi": cifti_average_dense_roi_outputs,
    }.get(t)


def cifti_average_dense_roi_cifti_roi_params(
    roi_cifti: InputPathType,
    opt_in_memory: bool = False,
) -> CiftiAverageDenseRoiCiftiRoiParameters:
    """
    Build parameters.
    
    Args:
        roi_cifti: the roi cifti file.
        opt_in_memory: cache the roi in memory so that it isn't re-read for\
            each input cifti.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti_roi",
        "roi_cifti": roi_cifti,
        "opt_in_memory": opt_in_memory,
    }
    return params


def cifti_average_dense_roi_cifti_roi_cargs(
    params: CiftiAverageDenseRoiCiftiRoiParameters,
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
    cargs.append("-cifti-roi")
    cargs.append(execution.input_file(params.get("roi_cifti")))
    if params.get("opt_in_memory"):
        cargs.append("-in-memory")
    return cargs


def cifti_average_dense_roi_cifti_params(
    cifti_in: InputPathType,
) -> CiftiAverageDenseRoiCiftiParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: a cifti file to average across.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti",
        "cifti_in": cifti_in,
    }
    return params


def cifti_average_dense_roi_cifti_cargs(
    params: CiftiAverageDenseRoiCiftiParameters,
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
    cargs.append("-cifti")
    cargs.append(execution.input_file(params.get("cifti_in")))
    return cargs


class CiftiAverageDenseRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average_dense_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti dscalar file"""


def cifti_average_dense_roi_params(
    cifti_out: str,
    cifti_roi: CiftiAverageDenseRoiCiftiRoiParameters | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    cifti: list[CiftiAverageDenseRoiCiftiParameters] | None = None,
) -> CiftiAverageDenseRoiParameters:
    """
    Build parameters.
    
    Args:
        cifti_out: output cifti dscalar file.
        cifti_roi: cifti file containing combined weights.
        opt_left_roi_roi_metric: weights to use for left hempsphere: the left\
            roi as a metric file.
        opt_right_roi_roi_metric: weights to use for right hempsphere: the\
            right roi as a metric file.
        opt_cerebellum_roi_roi_metric: weights to use for cerebellum surface:\
            the cerebellum roi as a metric file.
        opt_vol_roi_roi_vol: voxel weights to use: the roi volume file.
        opt_left_area_surf_left_surf: specify the left surface for vertex area\
            correction: the left surface file.
        opt_right_area_surf_right_surf: specify the right surface for vertex\
            area correction: the right surface file.
        opt_cerebellum_area_surf_cerebellum_surf: specify the cerebellum\
            surface for vertex area correction: the cerebellum surface file.
        cifti: specify an input cifti file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-average-dense-roi",
        "cifti_out": cifti_out,
    }
    if cifti_roi is not None:
        params["cifti_roi"] = cifti_roi
    if opt_left_roi_roi_metric is not None:
        params["opt_left_roi_roi_metric"] = opt_left_roi_roi_metric
    if opt_right_roi_roi_metric is not None:
        params["opt_right_roi_roi_metric"] = opt_right_roi_roi_metric
    if opt_cerebellum_roi_roi_metric is not None:
        params["opt_cerebellum_roi_roi_metric"] = opt_cerebellum_roi_roi_metric
    if opt_vol_roi_roi_vol is not None:
        params["opt_vol_roi_roi_vol"] = opt_vol_roi_roi_vol
    if opt_left_area_surf_left_surf is not None:
        params["opt_left_area_surf_left_surf"] = opt_left_area_surf_left_surf
    if opt_right_area_surf_right_surf is not None:
        params["opt_right_area_surf_right_surf"] = opt_right_area_surf_right_surf
    if opt_cerebellum_area_surf_cerebellum_surf is not None:
        params["opt_cerebellum_area_surf_cerebellum_surf"] = opt_cerebellum_area_surf_cerebellum_surf
    if cifti is not None:
        params["cifti"] = cifti
    return params


def cifti_average_dense_roi_cargs(
    params: CiftiAverageDenseRoiParameters,
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
    cargs.append("-cifti-average-dense-roi")
    cargs.append(params.get("cifti_out"))
    if params.get("cifti_roi") is not None:
        cargs.extend(dyn_cargs(params.get("cifti_roi")["__STYXTYPE__"])(params.get("cifti_roi"), execution))
    if params.get("opt_left_roi_roi_metric") is not None:
        cargs.extend([
            "-left-roi",
            execution.input_file(params.get("opt_left_roi_roi_metric"))
        ])
    if params.get("opt_right_roi_roi_metric") is not None:
        cargs.extend([
            "-right-roi",
            execution.input_file(params.get("opt_right_roi_roi_metric"))
        ])
    if params.get("opt_cerebellum_roi_roi_metric") is not None:
        cargs.extend([
            "-cerebellum-roi",
            execution.input_file(params.get("opt_cerebellum_roi_roi_metric"))
        ])
    if params.get("opt_vol_roi_roi_vol") is not None:
        cargs.extend([
            "-vol-roi",
            execution.input_file(params.get("opt_vol_roi_roi_vol"))
        ])
    if params.get("opt_left_area_surf_left_surf") is not None:
        cargs.extend([
            "-left-area-surf",
            execution.input_file(params.get("opt_left_area_surf_left_surf"))
        ])
    if params.get("opt_right_area_surf_right_surf") is not None:
        cargs.extend([
            "-right-area-surf",
            execution.input_file(params.get("opt_right_area_surf_right_surf"))
        ])
    if params.get("opt_cerebellum_area_surf_cerebellum_surf") is not None:
        cargs.extend([
            "-cerebellum-area-surf",
            execution.input_file(params.get("opt_cerebellum_area_surf_cerebellum_surf"))
        ])
    if params.get("cifti") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("cifti")] for a in c])
    return cargs


def cifti_average_dense_roi_outputs(
    params: CiftiAverageDenseRoiParameters,
    execution: Execution,
) -> CiftiAverageDenseRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiAverageDenseRoiOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_average_dense_roi_execute(
    params: CiftiAverageDenseRoiParameters,
    execution: Execution,
) -> CiftiAverageDenseRoiOutputs:
    """
    Average cifti rows across subjects by roi.
    
    Averages rows for each map of the ROI(s), across all files. ROI maps are
    treated as weighting functions, including negative values. For efficiency,
    ensure that everything that is not intended to be used is zero in the ROI
    map. If -cifti-roi is specified, -left-roi, -right-roi, -cerebellum-roi, and
    -vol-roi must not be specified. If multiple non-cifti ROI files are
    specified, they must have the same number of columns.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiAverageDenseRoiOutputs`).
    """
    cargs = cifti_average_dense_roi_cargs(params, execution)
    ret = cifti_average_dense_roi_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def cifti_average_dense_roi(
    cifti_out: str,
    cifti_roi: CiftiAverageDenseRoiCiftiRoiParameters | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    cifti: list[CiftiAverageDenseRoiCiftiParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiAverageDenseRoiOutputs:
    """
    Average cifti rows across subjects by roi.
    
    Averages rows for each map of the ROI(s), across all files. ROI maps are
    treated as weighting functions, including negative values. For efficiency,
    ensure that everything that is not intended to be used is zero in the ROI
    map. If -cifti-roi is specified, -left-roi, -right-roi, -cerebellum-roi, and
    -vol-roi must not be specified. If multiple non-cifti ROI files are
    specified, they must have the same number of columns.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_out: output cifti dscalar file.
        cifti_roi: cifti file containing combined weights.
        opt_left_roi_roi_metric: weights to use for left hempsphere: the left\
            roi as a metric file.
        opt_right_roi_roi_metric: weights to use for right hempsphere: the\
            right roi as a metric file.
        opt_cerebellum_roi_roi_metric: weights to use for cerebellum surface:\
            the cerebellum roi as a metric file.
        opt_vol_roi_roi_vol: voxel weights to use: the roi volume file.
        opt_left_area_surf_left_surf: specify the left surface for vertex area\
            correction: the left surface file.
        opt_right_area_surf_right_surf: specify the right surface for vertex\
            area correction: the right surface file.
        opt_cerebellum_area_surf_cerebellum_surf: specify the cerebellum\
            surface for vertex area correction: the cerebellum surface file.
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiAverageDenseRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_AVERAGE_DENSE_ROI_METADATA)
    params = cifti_average_dense_roi_params(cifti_out=cifti_out, cifti_roi=cifti_roi, opt_left_roi_roi_metric=opt_left_roi_roi_metric, opt_right_roi_roi_metric=opt_right_roi_roi_metric, opt_cerebellum_roi_roi_metric=opt_cerebellum_roi_roi_metric, opt_vol_roi_roi_vol=opt_vol_roi_roi_vol, opt_left_area_surf_left_surf=opt_left_area_surf_left_surf, opt_right_area_surf_right_surf=opt_right_area_surf_right_surf, opt_cerebellum_area_surf_cerebellum_surf=opt_cerebellum_area_surf_cerebellum_surf, cifti=cifti)
    return cifti_average_dense_roi_execute(params, execution)


__all__ = [
    "CIFTI_AVERAGE_DENSE_ROI_METADATA",
    "CiftiAverageDenseRoiCiftiParameters",
    "CiftiAverageDenseRoiCiftiRoiParameters",
    "CiftiAverageDenseRoiOutputs",
    "CiftiAverageDenseRoiParameters",
    "cifti_average_dense_roi",
    "cifti_average_dense_roi_cifti_params",
    "cifti_average_dense_roi_cifti_roi_params",
    "cifti_average_dense_roi_params",
]

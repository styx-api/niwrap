# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_INV_FMRI_METADATA = Metadata(
    id="0e98d6cd57d0addd162bfa97a9fce6949e7b4f85.boutiques",
    name="3dInvFMRI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dInvFmriParameters = typing.TypedDict('V3dInvFmriParameters', {
    "__STYX_TYPE__": typing.Literal["3dInvFMRI"],
    "input_file": InputPathType,
    "activation_map": InputPathType,
    "map_weight": typing.NotRequired[InputPathType | None],
    "mask": typing.NotRequired[InputPathType | None],
    "baseline_file": typing.NotRequired[list[InputPathType] | None],
    "polynom_order": typing.NotRequired[float | None],
    "output_file": typing.NotRequired[str | None],
    "method": typing.NotRequired[str | None],
    "alpha": typing.NotRequired[float | None],
    "smooth_fir": bool,
    "smooth_median": bool,
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
        "3dInvFMRI": v_3d_inv_fmri_cargs,
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
        "3dInvFMRI": v_3d_inv_fmri_outputs,
    }.get(t)


class V3dInvFmriOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_inv_fmri(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """The output 1D file."""


def v_3d_inv_fmri_params(
    input_file: InputPathType,
    activation_map: InputPathType,
    map_weight: InputPathType | None = None,
    mask: InputPathType | None = None,
    baseline_file: list[InputPathType] | None = None,
    polynom_order: float | None = None,
    output_file: str | None = None,
    method: str | None = None,
    alpha: float | None = None,
    smooth_fir: bool = False,
    smooth_median: bool = False,
) -> V3dInvFmriParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input 3D+time dataset.
        activation_map: Defines activation map; should be a bucket dataset\
            where each sub-brick defines the beta weight map for an unknown\
            stimulus time series.
        map_weight: Defines a weighting factor for the map. Dataset can have\
            either 1 sub-brick or the same number as in the -map dataset.
        mask: Defines a mask dataset to restrict input voxels from -data and\
            -map.
        baseline_file: Baseline time series file. Each column of the file\
            defines a baseline time series.
        polynom_order: Adds polynomials of specified order to the baseline\
            collection.
        output_file: Name of the 1D output file.
        method: Determines the method to use: C for least squares fit to data\
            matrix (default) or K for least squares fit to activation matrix.
        alpha: Set the alpha factor to penalize large values of the output\
            vectors.
        smooth_fir: Smooth the results with a 5 point lowpass FIR filter.
        smooth_median: Smooth the results with a 5 point median filter.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dInvFMRI",
        "input_file": input_file,
        "activation_map": activation_map,
        "smooth_fir": smooth_fir,
        "smooth_median": smooth_median,
    }
    if map_weight is not None:
        params["map_weight"] = map_weight
    if mask is not None:
        params["mask"] = mask
    if baseline_file is not None:
        params["baseline_file"] = baseline_file
    if polynom_order is not None:
        params["polynom_order"] = polynom_order
    if output_file is not None:
        params["output_file"] = output_file
    if method is not None:
        params["method"] = method
    if alpha is not None:
        params["alpha"] = alpha
    return params


def v_3d_inv_fmri_cargs(
    params: V3dInvFmriParameters,
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
    cargs.append("3dInvFMRI")
    cargs.extend([
        "-data",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-map",
        execution.input_file(params.get("activation_map"))
    ])
    if params.get("map_weight") is not None:
        cargs.extend([
            "-mapwt",
            execution.input_file(params.get("map_weight"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("baseline_file") is not None:
        cargs.extend([
            "-base",
            *[execution.input_file(f) for f in params.get("baseline_file")]
        ])
    if params.get("polynom_order") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polynom_order"))
        ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-out",
            params.get("output_file")
        ])
    if params.get("method") is not None:
        cargs.extend([
            "-method",
            params.get("method")
        ])
    if params.get("alpha") is not None:
        cargs.extend([
            "-alpha",
            str(params.get("alpha"))
        ])
    if params.get("smooth_fir"):
        cargs.append("-fir5")
    if params.get("smooth_median"):
        cargs.append("-median5")
    return cargs


def v_3d_inv_fmri_outputs(
    params: V3dInvFmriParameters,
    execution: Execution,
) -> V3dInvFmriOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dInvFmriOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def v_3d_inv_fmri_execute(
    params: V3dInvFmriParameters,
    execution: Execution,
) -> V3dInvFmriOutputs:
    """
    Program to compute stimulus time series, given a 3D+time dataset and an
    activation map (the inverse of the usual FMRI analysis problem).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dInvFmriOutputs`).
    """
    cargs = v_3d_inv_fmri_cargs(params, execution)
    ret = v_3d_inv_fmri_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_inv_fmri(
    input_file: InputPathType,
    activation_map: InputPathType,
    map_weight: InputPathType | None = None,
    mask: InputPathType | None = None,
    baseline_file: list[InputPathType] | None = None,
    polynom_order: float | None = None,
    output_file: str | None = None,
    method: str | None = None,
    alpha: float | None = None,
    smooth_fir: bool = False,
    smooth_median: bool = False,
    runner: Runner | None = None,
) -> V3dInvFmriOutputs:
    """
    Program to compute stimulus time series, given a 3D+time dataset and an
    activation map (the inverse of the usual FMRI analysis problem).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input 3D+time dataset.
        activation_map: Defines activation map; should be a bucket dataset\
            where each sub-brick defines the beta weight map for an unknown\
            stimulus time series.
        map_weight: Defines a weighting factor for the map. Dataset can have\
            either 1 sub-brick or the same number as in the -map dataset.
        mask: Defines a mask dataset to restrict input voxels from -data and\
            -map.
        baseline_file: Baseline time series file. Each column of the file\
            defines a baseline time series.
        polynom_order: Adds polynomials of specified order to the baseline\
            collection.
        output_file: Name of the 1D output file.
        method: Determines the method to use: C for least squares fit to data\
            matrix (default) or K for least squares fit to activation matrix.
        alpha: Set the alpha factor to penalize large values of the output\
            vectors.
        smooth_fir: Smooth the results with a 5 point lowpass FIR filter.
        smooth_median: Smooth the results with a 5 point median filter.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dInvFmriOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_INV_FMRI_METADATA)
    params = v_3d_inv_fmri_params(input_file=input_file, activation_map=activation_map, map_weight=map_weight, mask=mask, baseline_file=baseline_file, polynom_order=polynom_order, output_file=output_file, method=method, alpha=alpha, smooth_fir=smooth_fir, smooth_median=smooth_median)
    return v_3d_inv_fmri_execute(params, execution)


__all__ = [
    "V3dInvFmriOutputs",
    "V3dInvFmriParameters",
    "V_3D_INV_FMRI_METADATA",
    "v_3d_inv_fmri",
    "v_3d_inv_fmri_params",
]

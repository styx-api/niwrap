# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EDDY_COMBINE_METADATA = Metadata(
    id="986d7981faa09f892fa1fdefbe0561363b5309f4.boutiques",
    name="eddy_combine",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


EddyCombineParameters = typing.TypedDict('EddyCombineParameters', {
    "__STYX_TYPE__": typing.Literal["eddy_combine"],
    "pos_data": InputPathType,
    "pos_bvals": InputPathType,
    "pos_bvecs": InputPathType,
    "pos_series_vol": float,
    "neg_data": InputPathType,
    "neg_bvals": InputPathType,
    "neg_bvecs": InputPathType,
    "neg_series_vol": float,
    "output_path": str,
    "only_matched_flag": int,
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
        "eddy_combine": eddy_combine_cargs,
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
        "eddy_combine": eddy_combine_outputs,
    }.get(t)


class EddyCombineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy_combine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    combined_data: OutputPathType
    """Combined positive and negative phase-encoded data"""
    combined_bvals: OutputPathType
    """Combined b-values file"""
    combined_bvecs: OutputPathType
    """Combined b-vectors file"""


def eddy_combine_params(
    pos_data: InputPathType,
    pos_bvals: InputPathType,
    pos_bvecs: InputPathType,
    pos_series_vol: float,
    neg_data: InputPathType,
    neg_bvals: InputPathType,
    neg_bvecs: InputPathType,
    neg_series_vol: float,
    output_path: str,
    only_matched_flag: int,
) -> EddyCombineParameters:
    """
    Build parameters.
    
    Args:
        pos_data: Path to the positive phase-encoded data file (e.g.\
            PosData.nii.gz).
        pos_bvals: Path to the positive phase-encoded b-values file (e.g.\
            Posbvals).
        pos_bvecs: Path to the positive phase-encoded b-vectors file (e.g.\
            Posbvecs).
        pos_series_vol: Positive series volume count.
        neg_data: Path to the negative phase-encoded data file (e.g.\
            NegData.nii.gz).
        neg_bvals: Path to the negative phase-encoded b-values file (e.g.\
            Negbvals).
        neg_bvecs: Path to the negative phase-encoded b-vectors file (e.g.\
            Negbvecs).
        neg_series_vol: Negative series volume count.
        output_path: Output directory path.
        only_matched_flag: Flag to include only matched volumes (set to 1 to\
            include only matched volumes, otherwise 0).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "eddy_combine",
        "pos_data": pos_data,
        "pos_bvals": pos_bvals,
        "pos_bvecs": pos_bvecs,
        "pos_series_vol": pos_series_vol,
        "neg_data": neg_data,
        "neg_bvals": neg_bvals,
        "neg_bvecs": neg_bvecs,
        "neg_series_vol": neg_series_vol,
        "output_path": output_path,
        "only_matched_flag": only_matched_flag,
    }
    return params


def eddy_combine_cargs(
    params: EddyCombineParameters,
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
    cargs.append("eddy_combine")
    cargs.append(execution.input_file(params.get("pos_data")))
    cargs.append(execution.input_file(params.get("pos_bvals")))
    cargs.append(execution.input_file(params.get("pos_bvecs")))
    cargs.append(str(params.get("pos_series_vol")))
    cargs.append(execution.input_file(params.get("neg_data")))
    cargs.append(execution.input_file(params.get("neg_bvals")))
    cargs.append(execution.input_file(params.get("neg_bvecs")))
    cargs.append(str(params.get("neg_series_vol")))
    cargs.append(params.get("output_path"))
    cargs.append(str(params.get("only_matched_flag")))
    return cargs


def eddy_combine_outputs(
    params: EddyCombineParameters,
    execution: Execution,
) -> EddyCombineOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = EddyCombineOutputs(
        root=execution.output_file("."),
        combined_data=execution.output_file(params.get("output_path") + "/combined_data.nii.gz"),
        combined_bvals=execution.output_file(params.get("output_path") + "/combined_bvals"),
        combined_bvecs=execution.output_file(params.get("output_path") + "/combined_bvecs"),
    )
    return ret


def eddy_combine_execute(
    params: EddyCombineParameters,
    execution: Execution,
) -> EddyCombineOutputs:
    """
    Combines diffusion data sets with opposite phase encoding directions for use
    with FSL's EDDY.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `EddyCombineOutputs`).
    """
    params = execution.params(params)
    cargs = eddy_combine_cargs(params, execution)
    ret = eddy_combine_outputs(params, execution)
    execution.run(cargs)
    return ret


def eddy_combine(
    pos_data: InputPathType,
    pos_bvals: InputPathType,
    pos_bvecs: InputPathType,
    pos_series_vol: float,
    neg_data: InputPathType,
    neg_bvals: InputPathType,
    neg_bvecs: InputPathType,
    neg_series_vol: float,
    output_path: str,
    only_matched_flag: int,
    runner: Runner | None = None,
) -> EddyCombineOutputs:
    """
    Combines diffusion data sets with opposite phase encoding directions for use
    with FSL's EDDY.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        pos_data: Path to the positive phase-encoded data file (e.g.\
            PosData.nii.gz).
        pos_bvals: Path to the positive phase-encoded b-values file (e.g.\
            Posbvals).
        pos_bvecs: Path to the positive phase-encoded b-vectors file (e.g.\
            Posbvecs).
        pos_series_vol: Positive series volume count.
        neg_data: Path to the negative phase-encoded data file (e.g.\
            NegData.nii.gz).
        neg_bvals: Path to the negative phase-encoded b-values file (e.g.\
            Negbvals).
        neg_bvecs: Path to the negative phase-encoded b-vectors file (e.g.\
            Negbvecs).
        neg_series_vol: Negative series volume count.
        output_path: Output directory path.
        only_matched_flag: Flag to include only matched volumes (set to 1 to\
            include only matched volumes, otherwise 0).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyCombineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_COMBINE_METADATA)
    params = eddy_combine_params(
        pos_data=pos_data,
        pos_bvals=pos_bvals,
        pos_bvecs=pos_bvecs,
        pos_series_vol=pos_series_vol,
        neg_data=neg_data,
        neg_bvals=neg_bvals,
        neg_bvecs=neg_bvecs,
        neg_series_vol=neg_series_vol,
        output_path=output_path,
        only_matched_flag=only_matched_flag,
    )
    return eddy_combine_execute(params, execution)


__all__ = [
    "EDDY_COMBINE_METADATA",
    "EddyCombineOutputs",
    "EddyCombineParameters",
    "eddy_combine",
    "eddy_combine_params",
]

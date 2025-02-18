# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMATCALC_METADATA = Metadata(
    id="9c4d323b9663dd4eadd79fdc472de04da567e563.boutiques",
    name="3dmatcalc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dmatcalcParameters = typing.TypedDict('V3dmatcalcParameters', {
    "__STYX_TYPE__": typing.Literal["3dmatcalc"],
    "input_dataset": InputPathType,
    "input_matrix": InputPathType,
    "output_dataset": str,
    "mask": typing.NotRequired[InputPathType | None],
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
        "3dmatcalc": v_3dmatcalc_cargs,
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
        "3dmatcalc": v_3dmatcalc_outputs,
    }.get(t)


class V3dmatcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmatcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_header: OutputPathType
    """Output dataset header file."""
    output_brick: OutputPathType
    """Output dataset brick file."""


def v_3dmatcalc_params(
    input_dataset: InputPathType,
    input_matrix: InputPathType,
    output_dataset: str,
    mask: InputPathType | None = None,
) -> V3dmatcalcParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset to be processed.
        input_matrix: The matrix to be applied, specified as a .1D file or as\
            an expression in the syntax of 1dmatcalc.
        output_dataset: Prefix for the output dataset.
        mask: Apply the matrix only to voxels in the mask; other voxels will be\
            set to all zeroes.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmatcalc",
        "input_dataset": input_dataset,
        "input_matrix": input_matrix,
        "output_dataset": output_dataset,
    }
    if mask is not None:
        params["mask"] = mask
    return params


def v_3dmatcalc_cargs(
    params: V3dmatcalcParameters,
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
    cargs.append("3dmatcalc")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dataset"))
    ])
    cargs.extend([
        "-matrix",
        execution.input_file(params.get("input_matrix"))
    ])
    cargs.extend([
        "-prefix",
        params.get("output_dataset")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    return cargs


def v_3dmatcalc_outputs(
    params: V3dmatcalcParameters,
    execution: Execution,
) -> V3dmatcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmatcalcOutputs(
        root=execution.output_file("."),
        output_header=execution.output_file(params.get("output_dataset") + "+tlrc.HEAD"),
        output_brick=execution.output_file(params.get("output_dataset") + "+tlrc.BRIK"),
    )
    return ret


def v_3dmatcalc_execute(
    params: V3dmatcalcParameters,
    execution: Execution,
) -> V3dmatcalcOutputs:
    """
    Apply a matrix to a dataset, voxel-by-voxel, to produce a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmatcalcOutputs`).
    """
    cargs = v_3dmatcalc_cargs(params, execution)
    ret = v_3dmatcalc_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3dmatcalc(
    input_dataset: InputPathType,
    input_matrix: InputPathType,
    output_dataset: str,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dmatcalcOutputs:
    """
    Apply a matrix to a dataset, voxel-by-voxel, to produce a new dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset to be processed.
        input_matrix: The matrix to be applied, specified as a .1D file or as\
            an expression in the syntax of 1dmatcalc.
        output_dataset: Prefix for the output dataset.
        mask: Apply the matrix only to voxels in the mask; other voxels will be\
            set to all zeroes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmatcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMATCALC_METADATA)
    params = v_3dmatcalc_params(input_dataset=input_dataset, input_matrix=input_matrix, output_dataset=output_dataset, mask=mask)
    return v_3dmatcalc_execute(params, execution)


__all__ = [
    "V3dmatcalcOutputs",
    "V3dmatcalcParameters",
    "V_3DMATCALC_METADATA",
    "v_3dmatcalc",
    "v_3dmatcalc_params",
]

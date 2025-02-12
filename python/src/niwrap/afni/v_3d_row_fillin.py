# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ROW_FILLIN_METADATA = Metadata(
    id="efdbcc5556b9f847fe0eba3e015856a0addd50be.boutiques",
    name="3dRowFillin",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dRowFillinParameters = typing.TypedDict('V3dRowFillinParameters', {
    "__STYX_TYPE__": typing.Literal["3dRowFillin"],
    "maxgap": typing.NotRequired[float | None],
    "dir": typing.NotRequired[str | None],
    "binary": bool,
    "prefix": typing.NotRequired[str | None],
    "input_dataset": InputPathType,
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
        "3dRowFillin": v_3d_row_fillin_cargs,
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
        "3dRowFillin": v_3d_row_fillin_outputs,
    }.get(t)


class V3dRowFillinOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_row_fillin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """Output dataset in BRIK format"""
    output_head: OutputPathType | None
    """Output dataset in HEAD format"""


def v_3d_row_fillin_params(
    input_dataset: InputPathType,
    maxgap: float | None = None,
    dir_: str | None = None,
    binary: bool = False,
    prefix: str | None = None,
) -> V3dRowFillinParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input 3D dataset (e.g., dataset+orig).
        maxgap: Set the maximum length of a blank region that will be filled in.
        dir_: Set the direction of fill, e.g., A-P, P-A, I-S, S-I, L-R, R-L, x,\
            y, z, XYZ.OR, XYZ.AND.
        binary: Turn input dataset to binary (0 and 1) before filling in.\
            Output will also be binary.
        prefix: Set the prefix for the output dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dRowFillin",
        "binary": binary,
        "input_dataset": input_dataset,
    }
    if maxgap is not None:
        params["maxgap"] = maxgap
    if dir_ is not None:
        params["dir"] = dir_
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_row_fillin_cargs(
    params: V3dRowFillinParameters,
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
    cargs.append("3dRowFillin")
    if params.get("maxgap") is not None:
        cargs.extend([
            "-maxgap",
            str(params.get("maxgap"))
        ])
    if params.get("dir") is not None:
        cargs.extend([
            "-dir",
            params.get("dir")
        ])
    if params.get("binary"):
        cargs.append("-binary")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    cargs.append(execution.input_file(params.get("input_dataset")))
    return cargs


def v_3d_row_fillin_outputs(
    params: V3dRowFillinParameters,
    execution: Execution,
) -> V3dRowFillinOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRowFillinOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
        output_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_row_fillin_execute(
    params: V3dRowFillinParameters,
    execution: Execution,
) -> V3dRowFillinOutputs:
    """
    Fills in blank regions in 1D rows extracted from a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRowFillinOutputs`).
    """
    cargs = v_3d_row_fillin_cargs(params, execution)
    ret = v_3d_row_fillin_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_row_fillin(
    input_dataset: InputPathType,
    maxgap: float | None = None,
    dir_: str | None = None,
    binary: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dRowFillinOutputs:
    """
    Fills in blank regions in 1D rows extracted from a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input 3D dataset (e.g., dataset+orig).
        maxgap: Set the maximum length of a blank region that will be filled in.
        dir_: Set the direction of fill, e.g., A-P, P-A, I-S, S-I, L-R, R-L, x,\
            y, z, XYZ.OR, XYZ.AND.
        binary: Turn input dataset to binary (0 and 1) before filling in.\
            Output will also be binary.
        prefix: Set the prefix for the output dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRowFillinOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ROW_FILLIN_METADATA)
    params = v_3d_row_fillin_params(maxgap=maxgap, dir_=dir_, binary=binary, prefix=prefix, input_dataset=input_dataset)
    return v_3d_row_fillin_execute(params, execution)


__all__ = [
    "V3dRowFillinOutputs",
    "V3dRowFillinParameters",
    "V_3D_ROW_FILLIN_METADATA",
    "v_3d_row_fillin",
    "v_3d_row_fillin_params",
]

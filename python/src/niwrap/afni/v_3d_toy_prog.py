# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TOY_PROG_METADATA = Metadata(
    id="1311a81e171aae35dd519b54379bb3bfad692a46.boutiques",
    name="3dToyProg",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dToyProgParameters = typing.TypedDict('V3dToyProgParameters', {
    "__STYX_TYPE__": typing.Literal["3dToyProg"],
    "input_dataset": InputPathType,
    "output_prefix": typing.NotRequired[str | None],
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "output_datum": typing.NotRequired[typing.Literal["float", "short"] | None],
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
        "3dToyProg": v_3d_toy_prog_cargs,
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
    }.get(t)


class V3dToyProgOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_toy_prog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_toy_prog_params(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    mask_dataset: InputPathType | None = None,
    output_datum: typing.Literal["float", "short"] | None = None,
) -> V3dToyProgParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Reference dataset.
        output_prefix: Prefix of the output datasets.
        mask_dataset: Restrict analysis to non-zero voxels in the mask dataset.
        output_datum: Output datum type for one of the datasets. Choose from\
            'float' or 'short'. Default is 'float'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dToyProg",
        "input_dataset": input_dataset,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if output_datum is not None:
        params["output_datum"] = output_datum
    return params


def v_3d_toy_prog_cargs(
    params: V3dToyProgParameters,
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
    cargs.append("3dToyProg")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dataset"))
    ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    if params.get("output_datum") is not None:
        cargs.extend([
            "-datum",
            params.get("output_datum")
        ])
    return cargs


def v_3d_toy_prog_outputs(
    params: V3dToyProgParameters,
    execution: Execution,
) -> V3dToyProgOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dToyProgOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_toy_prog_execute(
    params: V3dToyProgParameters,
    execution: Execution,
) -> V3dToyProgOutputs:
    """
    A program to illustrate dataset creation and manipulation in C using AFNI's API.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dToyProgOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_toy_prog_cargs(params, execution)
    ret = v_3d_toy_prog_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_toy_prog(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    mask_dataset: InputPathType | None = None,
    output_datum: typing.Literal["float", "short"] | None = None,
    runner: Runner | None = None,
) -> V3dToyProgOutputs:
    """
    A program to illustrate dataset creation and manipulation in C using AFNI's API.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Reference dataset.
        output_prefix: Prefix of the output datasets.
        mask_dataset: Restrict analysis to non-zero voxels in the mask dataset.
        output_datum: Output datum type for one of the datasets. Choose from\
            'float' or 'short'. Default is 'float'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dToyProgOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TOY_PROG_METADATA)
    params = v_3d_toy_prog_params(
        input_dataset=input_dataset,
        output_prefix=output_prefix,
        mask_dataset=mask_dataset,
        output_datum=output_datum,
    )
    return v_3d_toy_prog_execute(params, execution)


__all__ = [
    "V3dToyProgOutputs",
    "V3dToyProgParameters",
    "V_3D_TOY_PROG_METADATA",
    "v_3d_toy_prog",
    "v_3d_toy_prog_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COPY_PARAMS_METADATA = Metadata(
    id="04ff7772827c0d2910e0be4cad90ac6d7da938f2.boutiques",
    name="mri_copy_params",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriCopyParamsParameters = typing.TypedDict('MriCopyParamsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_copy_params"],
    "in_vol": InputPathType,
    "template_vol": InputPathType,
    "out_vol": str,
    "size_flag": bool,
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
        "mri_copy_params": mri_copy_params_cargs,
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
        "mri_copy_params": mri_copy_params_outputs,
    }.get(t)


class MriCopyParamsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_copy_params(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Output volume file with parameters copied."""


def mri_copy_params_params(
    in_vol: InputPathType,
    template_vol: InputPathType,
    out_vol: str,
    size_flag: bool = False,
) -> MriCopyParamsParameters:
    """
    Build parameters.
    
    Args:
        in_vol: Input volume file whose parameters will be replaced.
        template_vol: Template volume file whose parameters will be copied.
        out_vol: Output volume file with replaced parameters.
        size_flag: Force copying of voxel sizes when resolutions vary.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_copy_params",
        "in_vol": in_vol,
        "template_vol": template_vol,
        "out_vol": out_vol,
        "size_flag": size_flag,
    }
    return params


def mri_copy_params_cargs(
    params: MriCopyParamsParameters,
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
    cargs.append("mri_copy_params")
    cargs.append(execution.input_file(params.get("in_vol")))
    cargs.append(execution.input_file(params.get("template_vol")))
    cargs.append(params.get("out_vol"))
    if params.get("size_flag"):
        cargs.append("--size")
    return cargs


def mri_copy_params_outputs(
    params: MriCopyParamsParameters,
    execution: Execution,
) -> MriCopyParamsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCopyParamsOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("out_vol")),
    )
    return ret


def mri_copy_params_execute(
    params: MriCopyParamsParameters,
    execution: Execution,
) -> MriCopyParamsOutputs:
    """
    A tool to replace the volume parameters of an input volume with those of a
    template volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCopyParamsOutputs`).
    """
    cargs = mri_copy_params_cargs(params, execution)
    ret = mri_copy_params_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_copy_params(
    in_vol: InputPathType,
    template_vol: InputPathType,
    out_vol: str,
    size_flag: bool = False,
    runner: Runner | None = None,
) -> MriCopyParamsOutputs:
    """
    A tool to replace the volume parameters of an input volume with those of a
    template volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        in_vol: Input volume file whose parameters will be replaced.
        template_vol: Template volume file whose parameters will be copied.
        out_vol: Output volume file with replaced parameters.
        size_flag: Force copying of voxel sizes when resolutions vary.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCopyParamsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COPY_PARAMS_METADATA)
    params = mri_copy_params_params(in_vol=in_vol, template_vol=template_vol, out_vol=out_vol, size_flag=size_flag)
    return mri_copy_params_execute(params, execution)


__all__ = [
    "MRI_COPY_PARAMS_METADATA",
    "MriCopyParamsOutputs",
    "MriCopyParamsParameters",
    "mri_copy_params",
    "mri_copy_params_params",
]

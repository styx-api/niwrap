# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DFRACTIONIZE_METADATA = Metadata(
    id="700df8ed70958c3087524da2a286d3508d1bd05d.boutiques",
    name="3dfractionize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dfractionizeParameters = typing.TypedDict('V3dfractionizeParameters', {
    "__STYX_TYPE__": typing.Literal["3dfractionize"],
    "template": InputPathType,
    "input": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "clip": typing.NotRequired[float | None],
    "warp": typing.NotRequired[InputPathType | None],
    "preserve": bool,
    "vote": bool,
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
        "3dfractionize": v_3dfractionize_cargs,
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
        "3dfractionize": v_3dfractionize_outputs,
    }.get(t)


class V3dfractionizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dfractionize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """Output dataset with the specified prefix."""


def v_3dfractionize_params(
    template: InputPathType,
    input_: InputPathType,
    prefix: str | None = None,
    clip: float | None = None,
    warp: InputPathType | None = None,
    preserve: bool = False,
    vote: bool = False,
) -> V3dfractionizeParameters:
    """
    Build parameters.
    
    Args:
        template: Use dataset as a template for the output. The output dataset\
            will be on the same grid as this dataset.
        input_: Use dataset for the input. Only the sub-brick #0 of the input\
            is used.
        prefix: Prefix for the output dataset.
        clip: Clip off voxels that are less than the specified occupancy\
            fraction.
        warp: Dataset that provides a transformation (warp) from +orig\
            coordinates to the coordinates of the input dataset.
        preserve: Preserve the nonzero values of input voxels in the output\
            dataset rather than creating a fractional mask.
        vote: Vote for which input value to preserve when using the preserve\
            flag.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dfractionize",
        "template": template,
        "input": input_,
        "preserve": preserve,
        "vote": vote,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if clip is not None:
        params["clip"] = clip
    if warp is not None:
        params["warp"] = warp
    return params


def v_3dfractionize_cargs(
    params: V3dfractionizeParameters,
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
    cargs.append("3dfractionize")
    cargs.extend([
        "-template",
        execution.input_file(params.get("template"))
    ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("input"))
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("clip") is not None:
        cargs.extend([
            "-clip",
            str(params.get("clip"))
        ])
    if params.get("warp") is not None:
        cargs.extend([
            "-warp",
            execution.input_file(params.get("warp"))
        ])
    if params.get("preserve"):
        cargs.append("-preserve")
    if params.get("vote"):
        cargs.append("-vote")
    return cargs


def v_3dfractionize_outputs(
    params: V3dfractionizeParameters,
    execution: Execution,
) -> V3dfractionizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dfractionizeOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3dfractionize_execute(
    params: V3dfractionizeParameters,
    execution: Execution,
) -> V3dfractionizeOutputs:
    """
    For each voxel in the output dataset, computes the fraction of it that is
    occupied by nonzero voxels from the input.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dfractionizeOutputs`).
    """
    cargs = v_3dfractionize_cargs(params, execution)
    ret = v_3dfractionize_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dfractionize(
    template: InputPathType,
    input_: InputPathType,
    prefix: str | None = None,
    clip: float | None = None,
    warp: InputPathType | None = None,
    preserve: bool = False,
    vote: bool = False,
    runner: Runner | None = None,
) -> V3dfractionizeOutputs:
    """
    For each voxel in the output dataset, computes the fraction of it that is
    occupied by nonzero voxels from the input.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        template: Use dataset as a template for the output. The output dataset\
            will be on the same grid as this dataset.
        input_: Use dataset for the input. Only the sub-brick #0 of the input\
            is used.
        prefix: Prefix for the output dataset.
        clip: Clip off voxels that are less than the specified occupancy\
            fraction.
        warp: Dataset that provides a transformation (warp) from +orig\
            coordinates to the coordinates of the input dataset.
        preserve: Preserve the nonzero values of input voxels in the output\
            dataset rather than creating a fractional mask.
        vote: Vote for which input value to preserve when using the preserve\
            flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dfractionizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DFRACTIONIZE_METADATA)
    params = v_3dfractionize_params(template=template, input_=input_, prefix=prefix, clip=clip, warp=warp, preserve=preserve, vote=vote)
    return v_3dfractionize_execute(params, execution)


__all__ = [
    "V3dfractionizeOutputs",
    "V3dfractionizeParameters",
    "V_3DFRACTIONIZE_METADATA",
    "v_3dfractionize",
    "v_3dfractionize_params",
]

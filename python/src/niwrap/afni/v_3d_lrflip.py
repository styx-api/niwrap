# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_LRFLIP_METADATA = Metadata(
    id="b3e8fe43a4546f9996744e159107df5ff817046b.boutiques",
    name="3dLRflip",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dLrflipParameters = typing.TypedDict('V3dLrflipParameters', {
    "__STYX_TYPE__": typing.Literal["3dLRflip"],
    "flip_z": bool,
    "output_prefix": typing.NotRequired[str | None],
    "datasets": list[InputPathType],
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
        "3dLRflip": v_3d_lrflip_cargs,
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
        "3dLRflip": v_3d_lrflip_outputs,
    }.get(t)


class V3dLrflipOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lrflip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    flipped_output: OutputPathType | None
    """Output dataset after flipping"""


def v_3d_lrflip_params(
    datasets: list[InputPathType],
    flip_z: bool = False,
    output_prefix: str | None = None,
) -> V3dLrflipParameters:
    """
    Build parameters.
    
    Args:
        datasets: Datasets to flip.
        flip_z: Flip about the 3rd direction.
        output_prefix: Prefix to use for output. If multiple datasets are\
            input, the program will choose a prefix for each output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLRflip",
        "flip_z": flip_z,
        "datasets": datasets,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def v_3d_lrflip_cargs(
    params: V3dLrflipParameters,
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
    cargs.append("3dLRflip")
    if params.get("flip_z"):
        cargs.append("-Z")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    return cargs


def v_3d_lrflip_outputs(
    params: V3dLrflipParameters,
    execution: Execution,
) -> V3dLrflipOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLrflipOutputs(
        root=execution.output_file("."),
        flipped_output=execution.output_file(params.get("output_prefix") + "*") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_lrflip_execute(
    params: V3dLrflipParameters,
    execution: Execution,
) -> V3dLrflipOutputs:
    """
    Flips the rows of a dataset along one of the three axes to correct dataset
    direction labeling errors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLrflipOutputs`).
    """
    cargs = v_3d_lrflip_cargs(params, execution)
    ret = v_3d_lrflip_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_lrflip(
    datasets: list[InputPathType],
    flip_z: bool = False,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dLrflipOutputs:
    """
    Flips the rows of a dataset along one of the three axes to correct dataset
    direction labeling errors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Datasets to flip.
        flip_z: Flip about the 3rd direction.
        output_prefix: Prefix to use for output. If multiple datasets are\
            input, the program will choose a prefix for each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLrflipOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LRFLIP_METADATA)
    params = v_3d_lrflip_params(flip_z=flip_z, output_prefix=output_prefix, datasets=datasets)
    return v_3d_lrflip_execute(params, execution)


__all__ = [
    "V3dLrflipOutputs",
    "V3dLrflipParameters",
    "V_3D_LRFLIP_METADATA",
    "v_3d_lrflip",
    "v_3d_lrflip_params",
]

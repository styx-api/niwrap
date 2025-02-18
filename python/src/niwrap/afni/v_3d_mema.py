# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MEMA_METADATA = Metadata(
    id="3e49aad2d71d54e4f942b7cc6311a0fe4225ef3f.boutiques",
    name="3dMEMA",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dMemaParameters = typing.TypedDict('V3dMemaParameters', {
    "__STYX_TYPE__": typing.Literal["3dMEMA"],
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
        "3dMEMA": v_3d_mema_cargs,
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
        "3dMEMA": v_3d_mema_outputs,
    }.get(t)


class V3dMemaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file from the analysis"""


def v_3d_mema_params(
) -> V3dMemaParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMEMA",
    }
    return params


def v_3d_mema_cargs(
    params: V3dMemaParameters,
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
    cargs.append("3dMEMA")
    cargs.append("[OPTIONS]")
    return cargs


def v_3d_mema_outputs(
    params: V3dMemaParameters,
    execution: Execution,
) -> V3dMemaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMemaOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[PREFIX].nii.gz"),
    )
    return ret


def v_3d_mema_execute(
    params: V3dMemaParameters,
    execution: Execution,
) -> V3dMemaOutputs:
    """
    3dMEMA is a program for performing Mixed Effects Meta Analysis at group level
    that models both within- and across-subjects variability.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMemaOutputs`).
    """
    cargs = v_3d_mema_cargs(params, execution)
    ret = v_3d_mema_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_mema(
    runner: Runner | None = None,
) -> V3dMemaOutputs:
    """
    3dMEMA is a program for performing Mixed Effects Meta Analysis at group level
    that models both within- and across-subjects variability.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMemaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MEMA_METADATA)
    params = v_3d_mema_params()
    return v_3d_mema_execute(params, execution)


__all__ = [
    "V3dMemaOutputs",
    "V3dMemaParameters",
    "V_3D_MEMA_METADATA",
    "v_3d_mema",
    "v_3d_mema_params",
]

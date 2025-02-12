# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_DESPIKE_METADATA = Metadata(
    id="724be608ea12115bb59f6e6981f0905bfd860c95.boutiques",
    name="3dDespike",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dDespikeParameters = typing.TypedDict('V3dDespikeParameters', {
    "__STYX_TYPE__": typing.Literal["3dDespike"],
    "prefix": typing.NotRequired[str | None],
    "in_file": InputPathType,
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
        "3dDespike": v_3d_despike_cargs,
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
        "3dDespike": v_3d_despike_outputs,
    }.get(t)


class V3dDespikeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_despike(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output file."""


def v_3d_despike_params(
    in_file: InputPathType,
    prefix: str | None = None,
) -> V3dDespikeParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input file to 3ddespike.
        prefix: Prefix for output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dDespike",
        "in_file": in_file,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_despike_cargs(
    params: V3dDespikeParameters,
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
    cargs.append("3dDespike")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    cargs.append(execution.input_file(params.get("in_file")))
    return cargs


def v_3d_despike_outputs(
    params: V3dDespikeParameters,
    execution: Execution,
) -> V3dDespikeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dDespikeOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_despike_execute(
    params: V3dDespikeParameters,
    execution: Execution,
) -> V3dDespikeOutputs:
    """
    Removes 'spikes' from the 3D+time input dataset and writes a new dataset with
    the spike values replaced by something more pleasing to the eye.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dDespikeOutputs`).
    """
    cargs = v_3d_despike_cargs(params, execution)
    ret = v_3d_despike_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_despike(
    in_file: InputPathType,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dDespikeOutputs:
    """
    Removes 'spikes' from the 3D+time input dataset and writes a new dataset with
    the spike values replaced by something more pleasing to the eye.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3ddespike.
        prefix: Prefix for output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDespikeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DESPIKE_METADATA)
    params = v_3d_despike_params(prefix=prefix, in_file=in_file)
    return v_3d_despike_execute(params, execution)


__all__ = [
    "V3dDespikeOutputs",
    "V3dDespikeParameters",
    "V_3D_DESPIKE_METADATA",
    "v_3d_despike",
    "v_3d_despike_params",
]

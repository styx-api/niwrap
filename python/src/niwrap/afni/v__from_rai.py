# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FROM_RAI_METADATA = Metadata(
    id="34d0b2acd8f2be090b2dfad6b13f248d55bc3857.boutiques",
    name="@FromRAI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VFromRaiParameters = typing.TypedDict('VFromRaiParameters', {
    "__STYX_TYPE__": typing.Literal["@FromRAI"],
    "rai_coordinates": list[float],
    "orientation": str,
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
        "@FromRAI": v__from_rai_cargs,
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


class VFromRaiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__from_rai(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__from_rai_params(
    rai_coordinates: list[float],
    orientation: str,
) -> VFromRaiParameters:
    """
    Build parameters.
    
    Args:
        rai_coordinates: RAI coordinates X, Y, and Z.
        orientation: Orientation format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@FromRAI",
        "rai_coordinates": rai_coordinates,
        "orientation": orientation,
    }
    return params


def v__from_rai_cargs(
    params: VFromRaiParameters,
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
    cargs.append("@FromRAI")
    cargs.extend([
        "-xyz",
        *map(str, params.get("rai_coordinates"))
    ])
    cargs.extend([
        "-or",
        params.get("orientation")
    ])
    return cargs


def v__from_rai_outputs(
    params: VFromRaiParameters,
    execution: Execution,
) -> VFromRaiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFromRaiOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__from_rai_execute(
    params: VFromRaiParameters,
    execution: Execution,
) -> VFromRaiOutputs:
    """
    Changes the RAI coordinates to the specified orientation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFromRaiOutputs`).
    """
    cargs = v__from_rai_cargs(params, execution)
    ret = v__from_rai_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__from_rai(
    rai_coordinates: list[float],
    orientation: str,
    runner: Runner | None = None,
) -> VFromRaiOutputs:
    """
    Changes the RAI coordinates to the specified orientation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        rai_coordinates: RAI coordinates X, Y, and Z.
        orientation: Orientation format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFromRaiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FROM_RAI_METADATA)
    params = v__from_rai_params(rai_coordinates=rai_coordinates, orientation=orientation)
    return v__from_rai_execute(params, execution)


__all__ = [
    "VFromRaiOutputs",
    "VFromRaiParameters",
    "V__FROM_RAI_METADATA",
    "v__from_rai",
    "v__from_rai_params",
]

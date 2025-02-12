# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_CREATE_METADATA = Metadata(
    id="ae422f4e56594a807daeeede3f3f8be904fa1b31.boutiques",
    name="volume-create",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeCreatePlumbParameters = typing.TypedDict('VolumeCreatePlumbParameters', {
    "__STYX_TYPE__": typing.Literal["plumb"],
    "axis_order": str,
    "x_spacing": float,
    "y_spacing": float,
    "z_spacing": float,
    "x_offset": float,
    "y_offset": float,
    "z_offset": float,
})
VolumeCreateSformParameters = typing.TypedDict('VolumeCreateSformParameters', {
    "__STYX_TYPE__": typing.Literal["sform"],
    "xi_spacing": float,
    "xj_spacing": float,
    "xk_spacing": float,
    "x_offset": float,
    "yi_spacing": float,
    "yj_spacing": float,
    "yk_spacing": float,
    "y_offset": float,
    "zi_spacing": float,
    "zj_spacing": float,
    "zk_spacing": float,
    "z_offset": float,
})
VolumeCreateParameters = typing.TypedDict('VolumeCreateParameters', {
    "__STYX_TYPE__": typing.Literal["volume-create"],
    "i_dim": int,
    "j_dim": int,
    "k_dim": int,
    "volume_out": str,
    "plumb": typing.NotRequired[VolumeCreatePlumbParameters | None],
    "sform": typing.NotRequired[VolumeCreateSformParameters | None],
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
        "volume-create": volume_create_cargs,
        "plumb": volume_create_plumb_cargs,
        "sform": volume_create_sform_cargs,
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
        "volume-create": volume_create_outputs,
    }.get(t)


def volume_create_plumb_params(
    axis_order: str,
    x_spacing: float,
    y_spacing: float,
    z_spacing: float,
    x_offset: float,
    y_offset: float,
    z_offset: float,
) -> VolumeCreatePlumbParameters:
    """
    Build parameters.
    
    Args:
        axis_order: a string like 'XYZ' that specifies which index is along\
            which spatial dimension.
        x_spacing: change in x-coordinate from incrementing the relevant index.
        y_spacing: change in y-coordinate from incrementing the relevant index.
        z_spacing: change in z-coordinate from incrementing the relevant index.
        x_offset: the x-coordinate of the center of the first voxel.
        y_offset: the y-coordinate of the center of the first voxel.
        z_offset: the z-coordinate of the center of the first voxel.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "plumb",
        "axis_order": axis_order,
        "x_spacing": x_spacing,
        "y_spacing": y_spacing,
        "z_spacing": z_spacing,
        "x_offset": x_offset,
        "y_offset": y_offset,
        "z_offset": z_offset,
    }
    return params


def volume_create_plumb_cargs(
    params: VolumeCreatePlumbParameters,
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
    cargs.append("-plumb")
    cargs.append(params.get("axis_order"))
    cargs.append(str(params.get("x_spacing")))
    cargs.append(str(params.get("y_spacing")))
    cargs.append(str(params.get("z_spacing")))
    cargs.append(str(params.get("x_offset")))
    cargs.append(str(params.get("y_offset")))
    cargs.append(str(params.get("z_offset")))
    return cargs


def volume_create_sform_params(
    xi_spacing: float,
    xj_spacing: float,
    xk_spacing: float,
    x_offset: float,
    yi_spacing: float,
    yj_spacing: float,
    yk_spacing: float,
    y_offset: float,
    zi_spacing: float,
    zj_spacing: float,
    zk_spacing: float,
    z_offset: float,
) -> VolumeCreateSformParameters:
    """
    Build parameters.
    
    Args:
        xi_spacing: increase in x coordinate from incrementing the i index.
        xj_spacing: increase in x coordinate from incrementing the j index.
        xk_spacing: increase in x coordinate from incrementing the k index.
        x_offset: x coordinate of first voxel.
        yi_spacing: increase in y coordinate from incrementing the i index.
        yj_spacing: increase in y coordinate from incrementing the j index.
        yk_spacing: increase in y coordinate from incrementing the k index.
        y_offset: y coordinate of first voxel.
        zi_spacing: increase in z coordinate from incrementing the i index.
        zj_spacing: increase in z coordinate from incrementing the j index.
        zk_spacing: increase in z coordinate from incrementing the k index.
        z_offset: z coordinate of first voxel.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sform",
        "xi_spacing": xi_spacing,
        "xj_spacing": xj_spacing,
        "xk_spacing": xk_spacing,
        "x_offset": x_offset,
        "yi_spacing": yi_spacing,
        "yj_spacing": yj_spacing,
        "yk_spacing": yk_spacing,
        "y_offset": y_offset,
        "zi_spacing": zi_spacing,
        "zj_spacing": zj_spacing,
        "zk_spacing": zk_spacing,
        "z_offset": z_offset,
    }
    return params


def volume_create_sform_cargs(
    params: VolumeCreateSformParameters,
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
    cargs.append("-sform")
    cargs.append(str(params.get("xi_spacing")))
    cargs.append(str(params.get("xj_spacing")))
    cargs.append(str(params.get("xk_spacing")))
    cargs.append(str(params.get("x_offset")))
    cargs.append(str(params.get("yi_spacing")))
    cargs.append(str(params.get("yj_spacing")))
    cargs.append(str(params.get("yk_spacing")))
    cargs.append(str(params.get("y_offset")))
    cargs.append(str(params.get("zi_spacing")))
    cargs.append(str(params.get("zj_spacing")))
    cargs.append(str(params.get("zk_spacing")))
    cargs.append(str(params.get("z_offset")))
    return cargs


class VolumeCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_create(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_create_params(
    i_dim: int,
    j_dim: int,
    k_dim: int,
    volume_out: str,
    plumb: VolumeCreatePlumbParameters | None = None,
    sform: VolumeCreateSformParameters | None = None,
) -> VolumeCreateParameters:
    """
    Build parameters.
    
    Args:
        i_dim: length of first dimension.
        j_dim: length of second dimension.
        k_dim: length of third dimension.
        volume_out: the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-create",
        "i_dim": i_dim,
        "j_dim": j_dim,
        "k_dim": k_dim,
        "volume_out": volume_out,
    }
    if plumb is not None:
        params["plumb"] = plumb
    if sform is not None:
        params["sform"] = sform
    return params


def volume_create_cargs(
    params: VolumeCreateParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-create")
    cargs.append(str(params.get("i_dim")))
    cargs.append(str(params.get("j_dim")))
    cargs.append(str(params.get("k_dim")))
    cargs.append(params.get("volume_out"))
    if params.get("plumb") is not None:
        cargs.extend(dyn_cargs(params.get("plumb")["__STYXTYPE__"])(params.get("plumb"), execution))
    if params.get("sform") is not None:
        cargs.extend(dyn_cargs(params.get("sform")["__STYXTYPE__"])(params.get("sform"), execution))
    return cargs


def volume_create_outputs(
    params: VolumeCreateParameters,
    execution: Execution,
) -> VolumeCreateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeCreateOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_create_execute(
    params: VolumeCreateParameters,
    execution: Execution,
) -> VolumeCreateOutputs:
    """
    Create a blank volume file.
    
    Creates a volume file full of zeros. Exactly one of -plumb or -sform must be
    specified.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeCreateOutputs`).
    """
    cargs = volume_create_cargs(params, execution)
    ret = volume_create_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_create(
    i_dim: int,
    j_dim: int,
    k_dim: int,
    volume_out: str,
    plumb: VolumeCreatePlumbParameters | None = None,
    sform: VolumeCreateSformParameters | None = None,
    runner: Runner | None = None,
) -> VolumeCreateOutputs:
    """
    Create a blank volume file.
    
    Creates a volume file full of zeros. Exactly one of -plumb or -sform must be
    specified.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        i_dim: length of first dimension.
        j_dim: length of second dimension.
        k_dim: length of third dimension.
        volume_out: the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeCreateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_CREATE_METADATA)
    params = volume_create_params(i_dim=i_dim, j_dim=j_dim, k_dim=k_dim, volume_out=volume_out, plumb=plumb, sform=sform)
    return volume_create_execute(params, execution)


__all__ = [
    "VOLUME_CREATE_METADATA",
    "VolumeCreateOutputs",
    "VolumeCreateParameters",
    "VolumeCreatePlumbParameters",
    "VolumeCreateSformParameters",
    "volume_create",
    "volume_create_params",
    "volume_create_plumb_params",
    "volume_create_sform_params",
]

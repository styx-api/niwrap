# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FIX_FSSPHERE_METADATA = Metadata(
    id="b742177d5b0ebe3a73650e2f92bfe87238f0bcca.boutiques",
    name="@fix_FSsphere",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VFixFssphereParameters = typing.TypedDict('VFixFssphereParameters', {
    "__STYX_TYPE__": typing.Literal["@fix_FSsphere"],
    "spec_file": InputPathType,
    "sphere_file": InputPathType,
    "num_iterations": typing.NotRequired[int | None],
    "extent_lim": typing.NotRequired[float | None],
    "project_first": bool,
    "keep_temp": bool,
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
        "@fix_FSsphere": v__fix_fssphere_cargs,
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
        "@fix_FSsphere": v__fix_fssphere_outputs,
    }.get(t)


class VFixFssphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fix_fssphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_surface: OutputPathType
    """Corrected surface"""


def v__fix_fssphere_params(
    spec_file: InputPathType,
    sphere_file: InputPathType,
    num_iterations: int | None = None,
    extent_lim: float | None = None,
    project_first: bool = False,
    keep_temp: bool = False,
) -> VFixFssphereParameters:
    """
    Build parameters.
    
    Args:
        spec_file: Spec file.
        sphere_file: SPHERE.asc is the sphere to be used.
        num_iterations: Number of local smoothing operations. Default is 3000.
        extent_lim: Extent, in mm, by which troubled sections are fattened.\
            Default is 6.
        project_first: Project to a sphere, before smoothing. Default is 0.
        keep_temp: Keep temporary files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@fix_FSsphere",
        "spec_file": spec_file,
        "sphere_file": sphere_file,
        "project_first": project_first,
        "keep_temp": keep_temp,
    }
    if num_iterations is not None:
        params["num_iterations"] = num_iterations
    if extent_lim is not None:
        params["extent_lim"] = extent_lim
    return params


def v__fix_fssphere_cargs(
    params: VFixFssphereParameters,
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
    cargs.append("@fix_FSsphere")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("spec_file"))
    ])
    cargs.extend([
        "-sphere",
        execution.input_file(params.get("sphere_file"))
    ])
    if params.get("num_iterations") is not None:
        cargs.extend([
            "-niter",
            str(params.get("num_iterations"))
        ])
    if params.get("extent_lim") is not None:
        cargs.extend([
            "-lim",
            str(params.get("extent_lim"))
        ])
    if params.get("project_first"):
        cargs.append("-project_first")
    if params.get("keep_temp"):
        cargs.append("-keep_temp")
    return cargs


def v__fix_fssphere_outputs(
    params: VFixFssphereParameters,
    execution: Execution,
) -> VFixFssphereOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFixFssphereOutputs(
        root=execution.output_file("."),
        corrected_surface=execution.output_file("[SPHERE]_fxd.asc"),
    )
    return ret


def v__fix_fssphere_execute(
    params: VFixFssphereParameters,
    execution: Execution,
) -> VFixFssphereOutputs:
    """
    Tool for fixing errors in FreeSurfer spherical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFixFssphereOutputs`).
    """
    cargs = v__fix_fssphere_cargs(params, execution)
    ret = v__fix_fssphere_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__fix_fssphere(
    spec_file: InputPathType,
    sphere_file: InputPathType,
    num_iterations: int | None = None,
    extent_lim: float | None = None,
    project_first: bool = False,
    keep_temp: bool = False,
    runner: Runner | None = None,
) -> VFixFssphereOutputs:
    """
    Tool for fixing errors in FreeSurfer spherical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_file: Spec file.
        sphere_file: SPHERE.asc is the sphere to be used.
        num_iterations: Number of local smoothing operations. Default is 3000.
        extent_lim: Extent, in mm, by which troubled sections are fattened.\
            Default is 6.
        project_first: Project to a sphere, before smoothing. Default is 0.
        keep_temp: Keep temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFixFssphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FIX_FSSPHERE_METADATA)
    params = v__fix_fssphere_params(spec_file=spec_file, sphere_file=sphere_file, num_iterations=num_iterations, extent_lim=extent_lim, project_first=project_first, keep_temp=keep_temp)
    return v__fix_fssphere_execute(params, execution)


__all__ = [
    "VFixFssphereOutputs",
    "VFixFssphereParameters",
    "V__FIX_FSSPHERE_METADATA",
    "v__fix_fssphere",
    "v__fix_fssphere_params",
]

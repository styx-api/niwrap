# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_EXVIVO_SURFACES_METADATA = Metadata(
    id="6158a382349b4ec3826fd3779a0f0dfa5790c075.boutiques",
    name="mris_exvivo_surfaces",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisExvivoSurfacesParameters = typing.TypedDict('MrisExvivoSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_exvivo_surfaces"],
    "subject_name": str,
    "hemisphere": str,
    "omit_self_intersection": bool,
    "create_curvature_area": bool,
    "average_curvature": typing.NotRequired[float | None],
    "white_only": bool,
    "formalin": typing.NotRequired[int | None],
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
        "mris_exvivo_surfaces": mris_exvivo_surfaces_cargs,
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
        "mris_exvivo_surfaces": mris_exvivo_surfaces_outputs,
    }.get(t)


class MrisExvivoSurfacesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_exvivo_surfaces(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    white_surface: OutputPathType
    """Generated white matter surface file"""
    gray_surface: OutputPathType
    """Generated gray matter surface file"""
    curvature_file: OutputPathType
    """Curvature file for cortical thickness"""
    layer_iv_surface: OutputPathType
    """Surface file approximating layer IV of the cortical sheet"""


def mris_exvivo_surfaces_params(
    subject_name: str,
    hemisphere: str,
    omit_self_intersection: bool = False,
    create_curvature_area: bool = False,
    average_curvature: float | None = 10,
    white_only: bool = False,
    formalin: int | None = None,
) -> MrisExvivoSurfacesParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Hemisphere (e.g., lh or rh).
        omit_self_intersection: Omit self-intersection check and only generate\
            gray/white surface.
        create_curvature_area: Create curvature and area files from white\
            matter surface.
        average_curvature: Average curvature values a specified number of\
            times.
        white_only: Only generate the white matter surface.
        formalin: Assume hemisphere is in formalin, with provided value\
            indicating presence (0,1).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_exvivo_surfaces",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "omit_self_intersection": omit_self_intersection,
        "create_curvature_area": create_curvature_area,
        "white_only": white_only,
    }
    if average_curvature is not None:
        params["average_curvature"] = average_curvature
    if formalin is not None:
        params["formalin"] = formalin
    return params


def mris_exvivo_surfaces_cargs(
    params: MrisExvivoSurfacesParameters,
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
    cargs.append("mris_exvivo_surfaces")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    if params.get("omit_self_intersection"):
        cargs.append("-q")
    if params.get("create_curvature_area"):
        cargs.append("-c")
    if params.get("average_curvature") is not None:
        cargs.extend([
            "-a",
            str(params.get("average_curvature"))
        ])
    if params.get("white_only"):
        cargs.append("-whiteonly")
    if params.get("formalin") is not None:
        cargs.extend([
            "-formalin",
            str(params.get("formalin"))
        ])
    return cargs


def mris_exvivo_surfaces_outputs(
    params: MrisExvivoSurfacesParameters,
    execution: Execution,
) -> MrisExvivoSurfacesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisExvivoSurfacesOutputs(
        root=execution.output_file("."),
        white_surface=execution.output_file("<subject_name>_<hemisphere>_white"),
        gray_surface=execution.output_file("<subject_name>_<hemisphere>_gray"),
        curvature_file=execution.output_file("<subject_name>_<hemisphere>_curvature"),
        layer_iv_surface=execution.output_file("<subject_name>_<hemisphere>_layerIV"),
    )
    return ret


def mris_exvivo_surfaces_execute(
    params: MrisExvivoSurfacesParameters,
    execution: Execution,
) -> MrisExvivoSurfacesOutputs:
    """
    FreeSurfer tool to position tessellation of the cortical surface at the white
    and gray matter surfaces, and generate relevant surface files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisExvivoSurfacesOutputs`).
    """
    cargs = mris_exvivo_surfaces_cargs(params, execution)
    ret = mris_exvivo_surfaces_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_exvivo_surfaces(
    subject_name: str,
    hemisphere: str,
    omit_self_intersection: bool = False,
    create_curvature_area: bool = False,
    average_curvature: float | None = 10,
    white_only: bool = False,
    formalin: int | None = None,
    runner: Runner | None = None,
) -> MrisExvivoSurfacesOutputs:
    """
    FreeSurfer tool to position tessellation of the cortical surface at the white
    and gray matter surfaces, and generate relevant surface files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Hemisphere (e.g., lh or rh).
        omit_self_intersection: Omit self-intersection check and only generate\
            gray/white surface.
        create_curvature_area: Create curvature and area files from white\
            matter surface.
        average_curvature: Average curvature values a specified number of\
            times.
        white_only: Only generate the white matter surface.
        formalin: Assume hemisphere is in formalin, with provided value\
            indicating presence (0,1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisExvivoSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_EXVIVO_SURFACES_METADATA)
    params = mris_exvivo_surfaces_params(subject_name=subject_name, hemisphere=hemisphere, omit_self_intersection=omit_self_intersection, create_curvature_area=create_curvature_area, average_curvature=average_curvature, white_only=white_only, formalin=formalin)
    return mris_exvivo_surfaces_execute(params, execution)


__all__ = [
    "MRIS_EXVIVO_SURFACES_METADATA",
    "MrisExvivoSurfacesOutputs",
    "MrisExvivoSurfacesParameters",
    "mris_exvivo_surfaces",
    "mris_exvivo_surfaces_params",
]

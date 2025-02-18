# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONVERT_SURFACE_METADATA = Metadata(
    id="2b7452b8bf057bc43ac7efc4c5a01abd5236749c.boutiques",
    name="ConvertSurface",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ConvertSurfaceParameters = typing.TypedDict('ConvertSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["ConvertSurface"],
    "input_surface": str,
    "output_surface": str,
    "surface_volume": typing.NotRequired[str | None],
    "transform_tlrc": bool,
    "mni_lpi": bool,
    "ixmat_1D": typing.NotRequired[str | None],
    "native": bool,
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
        "ConvertSurface": convert_surface_cargs,
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
        "ConvertSurface": convert_surface_outputs,
    }.get(t)


class ConvertSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """The converted output surface file."""


def convert_surface_params(
    input_surface: str,
    output_surface: str,
    surface_volume: str | None = None,
    transform_tlrc: bool = False,
    mni_lpi: bool = False,
    ixmat_1_d: str | None = None,
    native: bool = False,
) -> ConvertSurfaceParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Specifies the input surface.
        output_surface: Specifies the output surface.
        surface_volume: Specifies a surface volume.
        transform_tlrc: Apply Talairach transform.
        mni_lpi: Turn AFNI tlrc coordinates (RAI) into MNI coord space in LPI.
        ixmat_1_d: Apply inverse transformation specified in 1D file.
        native: Write the output surface in the coordinate system native to its\
            format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ConvertSurface",
        "input_surface": input_surface,
        "output_surface": output_surface,
        "transform_tlrc": transform_tlrc,
        "mni_lpi": mni_lpi,
        "native": native,
    }
    if surface_volume is not None:
        params["surface_volume"] = surface_volume
    if ixmat_1_d is not None:
        params["ixmat_1D"] = ixmat_1_d
    return params


def convert_surface_cargs(
    params: ConvertSurfaceParameters,
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
    cargs.append("ConvertSurface")
    cargs.extend([
        "-i",
        params.get("input_surface")
    ])
    cargs.extend([
        "-o",
        params.get("output_surface")
    ])
    if params.get("surface_volume") is not None:
        cargs.extend([
            "-sv",
            params.get("surface_volume")
        ])
    if params.get("transform_tlrc"):
        cargs.append("-tlrc")
    if params.get("mni_lpi"):
        cargs.append("-MNI_lpi")
    if params.get("ixmat_1D") is not None:
        cargs.extend([
            "-ixmat_1D",
            params.get("ixmat_1D")
        ])
    if params.get("native"):
        cargs.append("-native")
    return cargs


def convert_surface_outputs(
    params: ConvertSurfaceParameters,
    execution: Execution,
) -> ConvertSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertSurfaceOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(params.get("output_surface")),
    )
    return ret


def convert_surface_execute(
    params: ConvertSurfaceParameters,
    execution: Execution,
) -> ConvertSurfaceOutputs:
    """
    Reads in a surface and writes it out in another format. Only fields pertinent to
    SUMA are preserved.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertSurfaceOutputs`).
    """
    cargs = convert_surface_cargs(params, execution)
    ret = convert_surface_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def convert_surface(
    input_surface: str,
    output_surface: str,
    surface_volume: str | None = None,
    transform_tlrc: bool = False,
    mni_lpi: bool = False,
    ixmat_1_d: str | None = None,
    native: bool = False,
    runner: Runner | None = None,
) -> ConvertSurfaceOutputs:
    """
    Reads in a surface and writes it out in another format. Only fields pertinent to
    SUMA are preserved.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_surface: Specifies the input surface.
        output_surface: Specifies the output surface.
        surface_volume: Specifies a surface volume.
        transform_tlrc: Apply Talairach transform.
        mni_lpi: Turn AFNI tlrc coordinates (RAI) into MNI coord space in LPI.
        ixmat_1_d: Apply inverse transformation specified in 1D file.
        native: Write the output surface in the coordinate system native to its\
            format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_SURFACE_METADATA)
    params = convert_surface_params(input_surface=input_surface, output_surface=output_surface, surface_volume=surface_volume, transform_tlrc=transform_tlrc, mni_lpi=mni_lpi, ixmat_1_d=ixmat_1_d, native=native)
    return convert_surface_execute(params, execution)


__all__ = [
    "CONVERT_SURFACE_METADATA",
    "ConvertSurfaceOutputs",
    "ConvertSurfaceParameters",
    "convert_surface",
    "convert_surface_params",
]

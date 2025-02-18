# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMG2IMGCOORD_METADATA = Metadata(
    id="c0184a18acdc535cdea447e6dcf5b37d6e69053d.boutiques",
    name="img2imgcoord",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Img2imgcoordParameters = typing.TypedDict('Img2imgcoordParameters', {
    "__STYX_TYPE__": typing.Literal["img2imgcoord"],
    "coordinates_file": str,
    "source_image": InputPathType,
    "dest_image": InputPathType,
    "affine_transform": InputPathType,
    "warp_field": typing.NotRequired[InputPathType | None],
    "pre_warp_affine": typing.NotRequired[InputPathType | None],
    "coords_in_voxels": bool,
    "coords_in_mm": bool,
    "verbose": bool,
    "help": bool,
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
        "img2imgcoord": img2imgcoord_cargs,
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


class Img2imgcoordOutputs(typing.NamedTuple):
    """
    Output object returned when calling `img2imgcoord(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def img2imgcoord_params(
    coordinates_file: str,
    source_image: InputPathType,
    dest_image: InputPathType,
    affine_transform: InputPathType,
    warp_field: InputPathType | None = None,
    pre_warp_affine: InputPathType | None = None,
    coords_in_voxels: bool = False,
    coords_in_mm: bool = False,
    verbose: bool = False,
    help_: bool = False,
) -> Img2imgcoordParameters:
    """
    Build parameters.
    
    Args:
        coordinates_file: Filename containing coordinates.
        source_image: Filename of source image.
        dest_image: Filename of destination image.
        affine_transform: Filename of affine transform (e.g. source2dest.mat).
        warp_field: Filename of warpfield (e.g. intermediate2dest_warp.nii.gz).
        pre_warp_affine: Filename of pre-warp affine transform\
            (default=identity).
        coords_in_voxels: All coordinates in voxels (default).
        coords_in_mm: All coordinates in mm.
        verbose: Verbose mode.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "img2imgcoord",
        "coordinates_file": coordinates_file,
        "source_image": source_image,
        "dest_image": dest_image,
        "affine_transform": affine_transform,
        "coords_in_voxels": coords_in_voxels,
        "coords_in_mm": coords_in_mm,
        "verbose": verbose,
        "help": help_,
    }
    if warp_field is not None:
        params["warp_field"] = warp_field
    if pre_warp_affine is not None:
        params["pre_warp_affine"] = pre_warp_affine
    return params


def img2imgcoord_cargs(
    params: Img2imgcoordParameters,
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
    cargs.append("img2imgcoord")
    cargs.append(params.get("coordinates_file"))
    cargs.extend([
        "-src",
        execution.input_file(params.get("source_image"))
    ])
    cargs.extend([
        "-dest",
        execution.input_file(params.get("dest_image"))
    ])
    cargs.extend([
        "-xfm",
        execution.input_file(params.get("affine_transform"))
    ])
    if params.get("warp_field") is not None:
        cargs.extend([
            "-warp",
            execution.input_file(params.get("warp_field"))
        ])
    if params.get("pre_warp_affine") is not None:
        cargs.extend([
            "-premat",
            execution.input_file(params.get("pre_warp_affine"))
        ])
    if params.get("coords_in_voxels"):
        cargs.append("-vox")
    if params.get("coords_in_mm"):
        cargs.append("-mm")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def img2imgcoord_outputs(
    params: Img2imgcoordParameters,
    execution: Execution,
) -> Img2imgcoordOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Img2imgcoordOutputs(
        root=execution.output_file("."),
    )
    return ret


def img2imgcoord_execute(
    params: Img2imgcoordParameters,
    execution: Execution,
) -> Img2imgcoordOutputs:
    """
    Tool for transforming coordinates between images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Img2imgcoordOutputs`).
    """
    cargs = img2imgcoord_cargs(params, execution)
    ret = img2imgcoord_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def img2imgcoord(
    coordinates_file: str,
    source_image: InputPathType,
    dest_image: InputPathType,
    affine_transform: InputPathType,
    warp_field: InputPathType | None = None,
    pre_warp_affine: InputPathType | None = None,
    coords_in_voxels: bool = False,
    coords_in_mm: bool = False,
    verbose: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> Img2imgcoordOutputs:
    """
    Tool for transforming coordinates between images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        coordinates_file: Filename containing coordinates.
        source_image: Filename of source image.
        dest_image: Filename of destination image.
        affine_transform: Filename of affine transform (e.g. source2dest.mat).
        warp_field: Filename of warpfield (e.g. intermediate2dest_warp.nii.gz).
        pre_warp_affine: Filename of pre-warp affine transform\
            (default=identity).
        coords_in_voxels: All coordinates in voxels (default).
        coords_in_mm: All coordinates in mm.
        verbose: Verbose mode.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Img2imgcoordOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMG2IMGCOORD_METADATA)
    params = img2imgcoord_params(coordinates_file=coordinates_file, source_image=source_image, dest_image=dest_image, affine_transform=affine_transform, warp_field=warp_field, pre_warp_affine=pre_warp_affine, coords_in_voxels=coords_in_voxels, coords_in_mm=coords_in_mm, verbose=verbose, help_=help_)
    return img2imgcoord_execute(params, execution)


__all__ = [
    "IMG2IMGCOORD_METADATA",
    "Img2imgcoordOutputs",
    "Img2imgcoordParameters",
    "img2imgcoord",
    "img2imgcoord_params",
]

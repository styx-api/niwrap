# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PASTE_IMAGE_INTO_IMAGE_METADATA = Metadata(
    id="84fede77ce1571671d2df31a0ca7da2716107704.boutiques",
    name="PasteImageIntoImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
PasteImageIntoImageParameters = typing.TypedDict('PasteImageIntoImageParameters', {
    "__STYX_TYPE__": typing.Literal["PasteImageIntoImage"],
    "image_dimension": int,
    "input_canvas_image": InputPathType,
    "input_image": InputPathType,
    "output_image": str,
    "start_index": str,
    "background_label": typing.NotRequired[int | None],
    "paint_over_non_background_voxels": typing.NotRequired[typing.Literal[0, 1, 2] | None],
    "conflict_label": typing.NotRequired[int | None],
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
        "PasteImageIntoImage": paste_image_into_image_cargs,
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
        "PasteImageIntoImage": paste_image_into_image_outputs,
    }.get(t)


class PasteImageIntoImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `paste_image_into_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """The final output image with the input image pasted onto the canvas."""


def paste_image_into_image_params(
    image_dimension: int,
    input_canvas_image: InputPathType,
    input_image: InputPathType,
    output_image: str,
    start_index: str,
    background_label: int | None = 0,
    paint_over_non_background_voxels: typing.Literal[0, 1, 2] | None = 0,
    conflict_label: int | None = -1,
) -> PasteImageIntoImageParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Specify the dimension of the images.
        input_canvas_image: The canvas image on which the input image will be\
            pasted.
        input_image: The image to be pasted onto the canvas.
        output_image: The resulting image after pasting.
        start_index: The starting index where the input image will be pasted on\
            the canvas.
        background_label: The label value considered as background.
        paint_over_non_background_voxels: Defines behavior when the input image\
            voxel is non-background and the corresponding canvas voxel is\
            background: 0 - leave as is, 1 - replace with input voxel value, 2 -\
            replace with conflict label.
        conflict_label: The label value used for conflicting non-background\
            voxels if 'paintOverNonBackgroundVoxels' is set to 2.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "PasteImageIntoImage",
        "image_dimension": image_dimension,
        "input_canvas_image": input_canvas_image,
        "input_image": input_image,
        "output_image": output_image,
        "start_index": start_index,
    }
    if background_label is not None:
        params["background_label"] = background_label
    if paint_over_non_background_voxels is not None:
        params["paint_over_non_background_voxels"] = paint_over_non_background_voxels
    if conflict_label is not None:
        params["conflict_label"] = conflict_label
    return params


def paste_image_into_image_cargs(
    params: PasteImageIntoImageParameters,
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
    cargs.append("PasteImageIntoImage")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_canvas_image")))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    cargs.append(params.get("start_index"))
    if params.get("background_label") is not None:
        cargs.append(str(params.get("background_label")))
    if params.get("paint_over_non_background_voxels") is not None:
        cargs.append(str(params.get("paint_over_non_background_voxels")))
    if params.get("conflict_label") is not None:
        cargs.append(str(params.get("conflict_label")))
    return cargs


def paste_image_into_image_outputs(
    params: PasteImageIntoImageParameters,
    execution: Execution,
) -> PasteImageIntoImageOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PasteImageIntoImageOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")),
    )
    return ret


def paste_image_into_image_execute(
    params: PasteImageIntoImageParameters,
    execution: Execution,
) -> PasteImageIntoImageOutputs:
    """
    Paste the input image into the input canvas image. Depending on parameters, it
    can replace or merge existing voxel values.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PasteImageIntoImageOutputs`).
    """
    cargs = paste_image_into_image_cargs(params, execution)
    ret = paste_image_into_image_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def paste_image_into_image(
    image_dimension: int,
    input_canvas_image: InputPathType,
    input_image: InputPathType,
    output_image: str,
    start_index: str,
    background_label: int | None = 0,
    paint_over_non_background_voxels: typing.Literal[0, 1, 2] | None = 0,
    conflict_label: int | None = -1,
    runner: Runner | None = None,
) -> PasteImageIntoImageOutputs:
    """
    Paste the input image into the input canvas image. Depending on parameters, it
    can replace or merge existing voxel values.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Specify the dimension of the images.
        input_canvas_image: The canvas image on which the input image will be\
            pasted.
        input_image: The image to be pasted onto the canvas.
        output_image: The resulting image after pasting.
        start_index: The starting index where the input image will be pasted on\
            the canvas.
        background_label: The label value considered as background.
        paint_over_non_background_voxels: Defines behavior when the input image\
            voxel is non-background and the corresponding canvas voxel is\
            background: 0 - leave as is, 1 - replace with input voxel value, 2 -\
            replace with conflict label.
        conflict_label: The label value used for conflicting non-background\
            voxels if 'paintOverNonBackgroundVoxels' is set to 2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PasteImageIntoImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PASTE_IMAGE_INTO_IMAGE_METADATA)
    params = paste_image_into_image_params(image_dimension=image_dimension, input_canvas_image=input_canvas_image, input_image=input_image, output_image=output_image, start_index=start_index, background_label=background_label, paint_over_non_background_voxels=paint_over_non_background_voxels, conflict_label=conflict_label)
    return paste_image_into_image_execute(params, execution)


__all__ = [
    "PASTE_IMAGE_INTO_IMAGE_METADATA",
    "PasteImageIntoImageOutputs",
    "PasteImageIntoImageParameters",
    "paste_image_into_image",
    "paste_image_into_image_params",
]

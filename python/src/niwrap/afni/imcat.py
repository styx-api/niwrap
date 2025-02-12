# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMCAT_METADATA = Metadata(
    id="aaf3852ed2e5487ca6e742c661a53a14976a9a76.boutiques",
    name="imcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ImcatParameters = typing.TypedDict('ImcatParameters', {
    "__STYX_TYPE__": typing.Literal["imcat"],
    "input_files": list[InputPathType],
    "scale_image": typing.NotRequired[InputPathType | None],
    "scale_pixels": typing.NotRequired[InputPathType | None],
    "scale_intensity": bool,
    "gscale": typing.NotRequired[float | None],
    "rgb_out": bool,
    "res_in": typing.NotRequired[list[float] | None],
    "respad_in": typing.NotRequired[list[float] | None],
    "pad_val": typing.NotRequired[float | None],
    "crop": typing.NotRequired[list[float] | None],
    "autocrop_ctol": typing.NotRequired[float | None],
    "autocrop_atol": typing.NotRequired[float | None],
    "autocrop": bool,
    "zero_wrap": bool,
    "white_wrap": bool,
    "gray_wrap": typing.NotRequired[float | None],
    "image_wrap": bool,
    "rand_wrap": bool,
    "prefix": typing.NotRequired[str | None],
    "matrix": typing.NotRequired[list[float] | None],
    "nx": typing.NotRequired[float | None],
    "ny": typing.NotRequired[float | None],
    "matrix_from_scale": bool,
    "gap": typing.NotRequired[float | None],
    "gap_col": typing.NotRequired[list[float] | None],
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
        "imcat": imcat_cargs,
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
        "imcat": imcat_outputs,
    }.get(t)


class ImcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType | None
    """Output image file"""


def imcat_params(
    input_files: list[InputPathType],
    scale_image: InputPathType | None = None,
    scale_pixels: InputPathType | None = None,
    scale_intensity: bool = False,
    gscale: float | None = None,
    rgb_out: bool = False,
    res_in: list[float] | None = None,
    respad_in: list[float] | None = None,
    pad_val: float | None = None,
    crop: list[float] | None = None,
    autocrop_ctol: float | None = None,
    autocrop_atol: float | None = None,
    autocrop: bool = False,
    zero_wrap: bool = False,
    white_wrap: bool = False,
    gray_wrap: float | None = None,
    image_wrap: bool = False,
    rand_wrap: bool = False,
    prefix: str | None = None,
    matrix: list[float] | None = None,
    nx: float | None = None,
    ny: float | None = None,
    matrix_from_scale: bool = False,
    gap: float | None = None,
    gap_col: list[float] | None = None,
) -> ImcatParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input image files.
        scale_image: Multiply each image IM(i,j) in output image matrix IM by\
            the color or intensity of the pixel (i,j) in SCALE_IMG.
        scale_pixels: Multiply each pixel (i,j) in output image by the color or\
            intensity of the pixel (i,j) in SCALE_IMG. SCALE_IMG is automatically\
            resized to the resolution of the output image.
        scale_intensity: Instead of multiplying by the color of pixel (i,j),\
            use its intensity (average color).
        gscale: Apply FAC in addition to scaling of -scale_* options.
        rgb_out: Force output to be in RGB, even if input is bytes. This option\
            is turned on automatically in certain cases.
        res_in: Set resolution of all input images to RX by RY pixels. Default\
            is to make all input have the same resolution as the first image.
        respad_in: Like -res_in, but resample to the max while respecting the\
            aspect ratio, and then pad to achieve desired pixel count.
        pad_val: Set the padding value, should it be needed by -respad_in to\
            VAL. VAL is typecast to byte, default is 0, max is 255.
        crop: Crop images by L (Left), R (Right), T (Top), B (Bottom) pixels.\
            Cutting is performed after any resolution change, if any, is to be\
            done.
        autocrop_ctol: A line is eliminated if none of its R G B values differ\
            by more than CTOL% from those of the corner pixel.
        autocrop_atol: A line is eliminated if none of its R G B values differ\
            by more than ATOL% from those of line average.
        autocrop: This option is the same as using both of -autocrop_atol 20\
            and -autocrop_ctol 20.
        zero_wrap: If number of images is not enough to fill matrix solid black\
            images are used.
        white_wrap: If number of images is not enough to fill matrix solid\
            white images are used.
        gray_wrap: If number of images is not enough to fill matrix, solid gray\
            images are used. GRAY must be between 0 and 1.0.
        image_wrap: If number of images is not enough to fill matrix, images on\
            command line are reused (default).
        rand_wrap: When reusing images to fill matrix, randomize the order in\
            refill section only.
        prefix: Prefix the output files with string 'ppp'.
        matrix: Specify number of images in each row and column of IM at the\
            same time.
        nx: Number of images in each row.
        ny: Number of images in each column.
        matrix_from_scale: Set NX and NY to be the same as the SCALE_IMG's\
            dimensions. (needs -scale_image).
        gap: Put a line G pixels wide between images.
        gap_col: Set color of line to R G B values. Values range between 0 and\
            255.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imcat",
        "input_files": input_files,
        "scale_intensity": scale_intensity,
        "rgb_out": rgb_out,
        "autocrop": autocrop,
        "zero_wrap": zero_wrap,
        "white_wrap": white_wrap,
        "image_wrap": image_wrap,
        "rand_wrap": rand_wrap,
        "matrix_from_scale": matrix_from_scale,
    }
    if scale_image is not None:
        params["scale_image"] = scale_image
    if scale_pixels is not None:
        params["scale_pixels"] = scale_pixels
    if gscale is not None:
        params["gscale"] = gscale
    if res_in is not None:
        params["res_in"] = res_in
    if respad_in is not None:
        params["respad_in"] = respad_in
    if pad_val is not None:
        params["pad_val"] = pad_val
    if crop is not None:
        params["crop"] = crop
    if autocrop_ctol is not None:
        params["autocrop_ctol"] = autocrop_ctol
    if autocrop_atol is not None:
        params["autocrop_atol"] = autocrop_atol
    if gray_wrap is not None:
        params["gray_wrap"] = gray_wrap
    if prefix is not None:
        params["prefix"] = prefix
    if matrix is not None:
        params["matrix"] = matrix
    if nx is not None:
        params["nx"] = nx
    if ny is not None:
        params["ny"] = ny
    if gap is not None:
        params["gap"] = gap
    if gap_col is not None:
        params["gap_col"] = gap_col
    return params


def imcat_cargs(
    params: ImcatParameters,
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
    cargs.append("imcat")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("scale_image") is not None:
        cargs.extend([
            "-scale_image",
            execution.input_file(params.get("scale_image"))
        ])
    if params.get("scale_pixels") is not None:
        cargs.extend([
            "-scale_pixels",
            execution.input_file(params.get("scale_pixels"))
        ])
    if params.get("scale_intensity"):
        cargs.append("-scale_intensity")
    if params.get("gscale") is not None:
        cargs.extend([
            "-gscale",
            str(params.get("gscale"))
        ])
    if params.get("rgb_out"):
        cargs.append("-rgb_out")
    if params.get("res_in") is not None:
        cargs.extend([
            "-res_in",
            *map(str, params.get("res_in"))
        ])
    if params.get("respad_in") is not None:
        cargs.extend([
            "-respad_in",
            *map(str, params.get("respad_in"))
        ])
    if params.get("pad_val") is not None:
        cargs.extend([
            "-pad_val",
            str(params.get("pad_val"))
        ])
    if params.get("crop") is not None:
        cargs.extend([
            "-crop",
            *map(str, params.get("crop"))
        ])
    if params.get("autocrop_ctol") is not None:
        cargs.extend([
            "-autocrop_ctol",
            str(params.get("autocrop_ctol"))
        ])
    if params.get("autocrop_atol") is not None:
        cargs.extend([
            "-autocrop_atol",
            str(params.get("autocrop_atol"))
        ])
    if params.get("autocrop"):
        cargs.append("-autocrop")
    if params.get("zero_wrap"):
        cargs.append("-zero_wrap")
    if params.get("white_wrap"):
        cargs.append("-white_wrap")
    if params.get("gray_wrap") is not None:
        cargs.extend([
            "-gray_wrap",
            str(params.get("gray_wrap"))
        ])
    if params.get("image_wrap"):
        cargs.append("-image_wrap")
    if params.get("rand_wrap"):
        cargs.append("-rand_wrap")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("matrix") is not None:
        cargs.extend([
            "-matrix",
            *map(str, params.get("matrix"))
        ])
    if params.get("nx") is not None:
        cargs.extend([
            "-nx",
            str(params.get("nx"))
        ])
    if params.get("ny") is not None:
        cargs.extend([
            "-ny",
            str(params.get("ny"))
        ])
    if params.get("matrix_from_scale"):
        cargs.append("-matrix_from_scale")
    if params.get("gap") is not None:
        cargs.extend([
            "-gap",
            str(params.get("gap"))
        ])
    if params.get("gap_col") is not None:
        cargs.extend([
            "-gap_col",
            *map(str, params.get("gap_col"))
        ])
    return cargs


def imcat_outputs(
    params: ImcatParameters,
    execution: Execution,
) -> ImcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImcatOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("prefix") + "output_image.[EXT]") if (params.get("prefix") is not None) else None,
    )
    return ret


def imcat_execute(
    params: ImcatParameters,
    execution: Execution,
) -> ImcatOutputs:
    """
    Assembles a set of images into an image matrix (IM) montage of NX by NY images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImcatOutputs`).
    """
    cargs = imcat_cargs(params, execution)
    ret = imcat_outputs(params, execution)
    execution.run(cargs)
    return ret


def imcat(
    input_files: list[InputPathType],
    scale_image: InputPathType | None = None,
    scale_pixels: InputPathType | None = None,
    scale_intensity: bool = False,
    gscale: float | None = None,
    rgb_out: bool = False,
    res_in: list[float] | None = None,
    respad_in: list[float] | None = None,
    pad_val: float | None = None,
    crop: list[float] | None = None,
    autocrop_ctol: float | None = None,
    autocrop_atol: float | None = None,
    autocrop: bool = False,
    zero_wrap: bool = False,
    white_wrap: bool = False,
    gray_wrap: float | None = None,
    image_wrap: bool = False,
    rand_wrap: bool = False,
    prefix: str | None = None,
    matrix: list[float] | None = None,
    nx: float | None = None,
    ny: float | None = None,
    matrix_from_scale: bool = False,
    gap: float | None = None,
    gap_col: list[float] | None = None,
    runner: Runner | None = None,
) -> ImcatOutputs:
    """
    Assembles a set of images into an image matrix (IM) montage of NX by NY images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input image files.
        scale_image: Multiply each image IM(i,j) in output image matrix IM by\
            the color or intensity of the pixel (i,j) in SCALE_IMG.
        scale_pixels: Multiply each pixel (i,j) in output image by the color or\
            intensity of the pixel (i,j) in SCALE_IMG. SCALE_IMG is automatically\
            resized to the resolution of the output image.
        scale_intensity: Instead of multiplying by the color of pixel (i,j),\
            use its intensity (average color).
        gscale: Apply FAC in addition to scaling of -scale_* options.
        rgb_out: Force output to be in RGB, even if input is bytes. This option\
            is turned on automatically in certain cases.
        res_in: Set resolution of all input images to RX by RY pixels. Default\
            is to make all input have the same resolution as the first image.
        respad_in: Like -res_in, but resample to the max while respecting the\
            aspect ratio, and then pad to achieve desired pixel count.
        pad_val: Set the padding value, should it be needed by -respad_in to\
            VAL. VAL is typecast to byte, default is 0, max is 255.
        crop: Crop images by L (Left), R (Right), T (Top), B (Bottom) pixels.\
            Cutting is performed after any resolution change, if any, is to be\
            done.
        autocrop_ctol: A line is eliminated if none of its R G B values differ\
            by more than CTOL% from those of the corner pixel.
        autocrop_atol: A line is eliminated if none of its R G B values differ\
            by more than ATOL% from those of line average.
        autocrop: This option is the same as using both of -autocrop_atol 20\
            and -autocrop_ctol 20.
        zero_wrap: If number of images is not enough to fill matrix solid black\
            images are used.
        white_wrap: If number of images is not enough to fill matrix solid\
            white images are used.
        gray_wrap: If number of images is not enough to fill matrix, solid gray\
            images are used. GRAY must be between 0 and 1.0.
        image_wrap: If number of images is not enough to fill matrix, images on\
            command line are reused (default).
        rand_wrap: When reusing images to fill matrix, randomize the order in\
            refill section only.
        prefix: Prefix the output files with string 'ppp'.
        matrix: Specify number of images in each row and column of IM at the\
            same time.
        nx: Number of images in each row.
        ny: Number of images in each column.
        matrix_from_scale: Set NX and NY to be the same as the SCALE_IMG's\
            dimensions. (needs -scale_image).
        gap: Put a line G pixels wide between images.
        gap_col: Set color of line to R G B values. Values range between 0 and\
            255.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMCAT_METADATA)
    params = imcat_params(input_files=input_files, scale_image=scale_image, scale_pixels=scale_pixels, scale_intensity=scale_intensity, gscale=gscale, rgb_out=rgb_out, res_in=res_in, respad_in=respad_in, pad_val=pad_val, crop=crop, autocrop_ctol=autocrop_ctol, autocrop_atol=autocrop_atol, autocrop=autocrop, zero_wrap=zero_wrap, white_wrap=white_wrap, gray_wrap=gray_wrap, image_wrap=image_wrap, rand_wrap=rand_wrap, prefix=prefix, matrix=matrix, nx=nx, ny=ny, matrix_from_scale=matrix_from_scale, gap=gap, gap_col=gap_col)
    return imcat_execute(params, execution)


__all__ = [
    "IMCAT_METADATA",
    "ImcatOutputs",
    "ImcatParameters",
    "imcat",
    "imcat_params",
]

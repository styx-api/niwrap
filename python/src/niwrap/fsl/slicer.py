# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLICER_METADATA = Metadata(
    id="7c28c8912deeb7ca0f43a49f175823fe5d4e25b2.boutiques",
    name="slicer",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SlicerParameters = typing.TypedDict('SlicerParameters', {
    "__STYX_TYPE__": typing.Literal["slicer"],
    "in_file": InputPathType,
    "overlay_file": typing.NotRequired[InputPathType | None],
    "label_slices": bool,
    "colour_map": typing.NotRequired[InputPathType | None],
    "scaling": typing.NotRequired[float | None],
    "intensity_range": typing.NotRequired[list[float] | None],
    "threshold_edges": typing.NotRequired[float | None],
    "dither_edges": bool,
    "nearest_neighbour": bool,
    "show_orientation": bool,
    "red_dot_marker": bool,
    "output_single_image": typing.NotRequired[str | None],
    "output_sagittal_slice": bool,
    "output_sagittal_slice_fname": typing.NotRequired[str | None],
    "output_axial_slice": bool,
    "output_axial_slice_fname": typing.NotRequired[str | None],
    "output_coronal_slice": bool,
    "output_coronal_slice_fname": typing.NotRequired[str | None],
    "output_all_axial_slices": bool,
    "output_all_axial_slices_fname": typing.NotRequired[str | None],
    "output_sample_axial_slices": bool,
    "output_sample_axial_slices_width": typing.NotRequired[str | None],
    "output_sample_axial_slices_fname": typing.NotRequired[str | None],
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
        "slicer": slicer_cargs,
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
        "slicer": slicer_outputs,
    }.get(t)


class SlicerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sagittal_slice_outfile: OutputPathType | None
    """Output sagittal slice."""
    axial_slice_outfile: OutputPathType | None
    """Output axial slice."""
    coronal_slice_outfile: OutputPathType | None
    """Output coronal slice."""
    single_image_outfile: OutputPathType | None
    """Output mid-sagittal, -coronal, and -axial slices into one image."""
    all_axial_slices_outfile: OutputPathType | None
    """File name of every <sample'th> axial slice output image."""


def slicer_params(
    in_file: InputPathType,
    overlay_file: InputPathType | None = None,
    label_slices: bool = False,
    colour_map: InputPathType | None = None,
    scaling: float | None = None,
    intensity_range: list[float] | None = None,
    threshold_edges: float | None = None,
    dither_edges: bool = False,
    nearest_neighbour: bool = False,
    show_orientation: bool = False,
    red_dot_marker: bool = False,
    output_single_image: str | None = None,
    output_sagittal_slice: bool = False,
    output_sagittal_slice_fname: str | None = None,
    output_axial_slice: bool = False,
    output_axial_slice_fname: str | None = None,
    output_coronal_slice: bool = False,
    output_coronal_slice_fname: str | None = None,
    output_all_axial_slices: bool = False,
    output_all_axial_slices_fname: str | None = None,
    output_sample_axial_slices: bool = False,
    output_sample_axial_slices_width: str | None = None,
    output_sample_axial_slices_fname: str | None = None,
) -> SlicerParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input volume.
        overlay_file: Overlay volume.
        label_slices: Label slices with slice number.
        colour_map: Use different colour map from that specified in the header.
        scaling: Image scale.
        intensity_range: Specify intensity min and max for display range.
        threshold_edges: Use specified threshold for edges (if >0 use this\
            proportion of max-min, if <0, use the absolute value).
        dither_edges: Produce semi-transparent (dithered) edges.
        nearest_neighbour: Use nearest neighbor interpolation for output.
        show_orientation: Do not put left-right labels in output.
        red_dot_marker: Add a red dot marker to topright of image.
        output_single_image: Output mid-sagittal, -coronal, and -axial slices\
            into one image.
        output_sagittal_slice: Output sagittal slice (if slice >0, it is a\
            fraction of image dimension, if <0, it is absolute slice number).
        output_sagittal_slice_fname: Output file name sagittal slice.
        output_axial_slice: Output axial slice (if slice >0, it is a fraction\
            of image dimension, if <0, it is absolute slice number).
        output_axial_slice_fname: Output file name axial slice.
        output_coronal_slice: Output coronal slice (if slice >0, it is a\
            fraction of image dimension, if <0, it is absolute slice number).
        output_coronal_slice_fname: Output file name coronal slice.
        output_all_axial_slices: Maximum width of image of all axial slices.
        output_all_axial_slices_fname: File name of all axial slice output\
            image.
        output_sample_axial_slices: Ouput every <sample>'th axial slice.
        output_sample_axial_slices_width: Width of every <sample'th> axial\
            slice output image.
        output_sample_axial_slices_fname: File name of every <sample'th> axial\
            slice output image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slicer",
        "in_file": in_file,
        "label_slices": label_slices,
        "dither_edges": dither_edges,
        "nearest_neighbour": nearest_neighbour,
        "show_orientation": show_orientation,
        "red_dot_marker": red_dot_marker,
        "output_sagittal_slice": output_sagittal_slice,
        "output_axial_slice": output_axial_slice,
        "output_coronal_slice": output_coronal_slice,
        "output_all_axial_slices": output_all_axial_slices,
        "output_sample_axial_slices": output_sample_axial_slices,
    }
    if overlay_file is not None:
        params["overlay_file"] = overlay_file
    if colour_map is not None:
        params["colour_map"] = colour_map
    if scaling is not None:
        params["scaling"] = scaling
    if intensity_range is not None:
        params["intensity_range"] = intensity_range
    if threshold_edges is not None:
        params["threshold_edges"] = threshold_edges
    if output_single_image is not None:
        params["output_single_image"] = output_single_image
    if output_sagittal_slice_fname is not None:
        params["output_sagittal_slice_fname"] = output_sagittal_slice_fname
    if output_axial_slice_fname is not None:
        params["output_axial_slice_fname"] = output_axial_slice_fname
    if output_coronal_slice_fname is not None:
        params["output_coronal_slice_fname"] = output_coronal_slice_fname
    if output_all_axial_slices_fname is not None:
        params["output_all_axial_slices_fname"] = output_all_axial_slices_fname
    if output_sample_axial_slices_width is not None:
        params["output_sample_axial_slices_width"] = output_sample_axial_slices_width
    if output_sample_axial_slices_fname is not None:
        params["output_sample_axial_slices_fname"] = output_sample_axial_slices_fname
    return params


def slicer_cargs(
    params: SlicerParameters,
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
    cargs.append("slicer")
    cargs.append(execution.input_file(params.get("in_file")))
    if params.get("overlay_file") is not None:
        cargs.append(execution.input_file(params.get("overlay_file")))
    if params.get("label_slices"):
        cargs.append("-L")
    if params.get("colour_map") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("colour_map"))
        ])
    if params.get("scaling") is not None:
        cargs.extend([
            "-s",
            str(params.get("scaling"))
        ])
    if params.get("intensity_range") is not None:
        cargs.extend([
            "-i",
            *map(str, params.get("intensity_range"))
        ])
    if params.get("threshold_edges") is not None:
        cargs.extend([
            "-e",
            str(params.get("threshold_edges"))
        ])
    if params.get("dither_edges"):
        cargs.append("-t")
    if params.get("nearest_neighbour"):
        cargs.append("-n")
    if params.get("show_orientation"):
        cargs.append("-u")
    if params.get("red_dot_marker"):
        cargs.append("-c")
    cargs.append("...slices...")
    if params.get("output_single_image") is not None:
        cargs.extend([
            "-a",
            params.get("output_single_image")
        ])
    if params.get("output_sagittal_slice"):
        cargs.append("-x")
    if params.get("output_sagittal_slice_fname") is not None:
        cargs.append(params.get("output_sagittal_slice_fname"))
    if params.get("output_axial_slice"):
        cargs.append("-y")
    if params.get("output_axial_slice_fname") is not None:
        cargs.append(params.get("output_axial_slice_fname"))
    if params.get("output_coronal_slice"):
        cargs.append("-z")
    if params.get("output_coronal_slice_fname") is not None:
        cargs.append(params.get("output_coronal_slice_fname"))
    if params.get("output_all_axial_slices"):
        cargs.append("-A")
    if params.get("output_all_axial_slices_fname") is not None:
        cargs.append(params.get("output_all_axial_slices_fname"))
    if params.get("output_sample_axial_slices"):
        cargs.append("-S")
    if params.get("output_sample_axial_slices_width") is not None:
        cargs.append(params.get("output_sample_axial_slices_width"))
    if params.get("output_sample_axial_slices_fname") is not None:
        cargs.append(params.get("output_sample_axial_slices_fname"))
    return cargs


def slicer_outputs(
    params: SlicerParameters,
    execution: Execution,
) -> SlicerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlicerOutputs(
        root=execution.output_file("."),
        sagittal_slice_outfile=execution.output_file(params.get("output_sagittal_slice_fname")) if (params.get("output_sagittal_slice_fname") is not None) else None,
        axial_slice_outfile=execution.output_file(params.get("output_axial_slice_fname")) if (params.get("output_axial_slice_fname") is not None) else None,
        coronal_slice_outfile=execution.output_file(params.get("output_coronal_slice_fname")) if (params.get("output_coronal_slice_fname") is not None) else None,
        single_image_outfile=execution.output_file(params.get("output_single_image")) if (params.get("output_single_image") is not None) else None,
        all_axial_slices_outfile=execution.output_file(params.get("output_sample_axial_slices_fname")) if (params.get("output_sample_axial_slices_fname") is not None) else None,
    )
    return ret


def slicer_execute(
    params: SlicerParameters,
    execution: Execution,
) -> SlicerOutputs:
    """
    the main program which takes in one or two input images and produces as many
    separate output pictures of slices as are requested. The basic output options
    (-x, -y and -z) produce single slice pictures. The more advanced options (-a, -A
    and -S) produce montages of various slices. slicer outputs PPM format pictures.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlicerOutputs`).
    """
    cargs = slicer_cargs(params, execution)
    ret = slicer_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def slicer(
    in_file: InputPathType,
    overlay_file: InputPathType | None = None,
    label_slices: bool = False,
    colour_map: InputPathType | None = None,
    scaling: float | None = None,
    intensity_range: list[float] | None = None,
    threshold_edges: float | None = None,
    dither_edges: bool = False,
    nearest_neighbour: bool = False,
    show_orientation: bool = False,
    red_dot_marker: bool = False,
    output_single_image: str | None = None,
    output_sagittal_slice: bool = False,
    output_sagittal_slice_fname: str | None = None,
    output_axial_slice: bool = False,
    output_axial_slice_fname: str | None = None,
    output_coronal_slice: bool = False,
    output_coronal_slice_fname: str | None = None,
    output_all_axial_slices: bool = False,
    output_all_axial_slices_fname: str | None = None,
    output_sample_axial_slices: bool = False,
    output_sample_axial_slices_width: str | None = None,
    output_sample_axial_slices_fname: str | None = None,
    runner: Runner | None = None,
) -> SlicerOutputs:
    """
    the main program which takes in one or two input images and produces as many
    separate output pictures of slices as are requested. The basic output options
    (-x, -y and -z) produce single slice pictures. The more advanced options (-a, -A
    and -S) produce montages of various slices. slicer outputs PPM format pictures.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input volume.
        overlay_file: Overlay volume.
        label_slices: Label slices with slice number.
        colour_map: Use different colour map from that specified in the header.
        scaling: Image scale.
        intensity_range: Specify intensity min and max for display range.
        threshold_edges: Use specified threshold for edges (if >0 use this\
            proportion of max-min, if <0, use the absolute value).
        dither_edges: Produce semi-transparent (dithered) edges.
        nearest_neighbour: Use nearest neighbor interpolation for output.
        show_orientation: Do not put left-right labels in output.
        red_dot_marker: Add a red dot marker to topright of image.
        output_single_image: Output mid-sagittal, -coronal, and -axial slices\
            into one image.
        output_sagittal_slice: Output sagittal slice (if slice >0, it is a\
            fraction of image dimension, if <0, it is absolute slice number).
        output_sagittal_slice_fname: Output file name sagittal slice.
        output_axial_slice: Output axial slice (if slice >0, it is a fraction\
            of image dimension, if <0, it is absolute slice number).
        output_axial_slice_fname: Output file name axial slice.
        output_coronal_slice: Output coronal slice (if slice >0, it is a\
            fraction of image dimension, if <0, it is absolute slice number).
        output_coronal_slice_fname: Output file name coronal slice.
        output_all_axial_slices: Maximum width of image of all axial slices.
        output_all_axial_slices_fname: File name of all axial slice output\
            image.
        output_sample_axial_slices: Ouput every <sample>'th axial slice.
        output_sample_axial_slices_width: Width of every <sample'th> axial\
            slice output image.
        output_sample_axial_slices_fname: File name of every <sample'th> axial\
            slice output image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICER_METADATA)
    params = slicer_params(in_file=in_file, overlay_file=overlay_file, label_slices=label_slices, colour_map=colour_map, scaling=scaling, intensity_range=intensity_range, threshold_edges=threshold_edges, dither_edges=dither_edges, nearest_neighbour=nearest_neighbour, show_orientation=show_orientation, red_dot_marker=red_dot_marker, output_single_image=output_single_image, output_sagittal_slice=output_sagittal_slice, output_sagittal_slice_fname=output_sagittal_slice_fname, output_axial_slice=output_axial_slice, output_axial_slice_fname=output_axial_slice_fname, output_coronal_slice=output_coronal_slice, output_coronal_slice_fname=output_coronal_slice_fname, output_all_axial_slices=output_all_axial_slices, output_all_axial_slices_fname=output_all_axial_slices_fname, output_sample_axial_slices=output_sample_axial_slices, output_sample_axial_slices_width=output_sample_axial_slices_width, output_sample_axial_slices_fname=output_sample_axial_slices_fname)
    return slicer_execute(params, execution)


__all__ = [
    "SLICER_METADATA",
    "SlicerOutputs",
    "SlicerParameters",
    "slicer",
    "slicer_params",
]

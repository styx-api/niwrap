# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_MAT2D_PLOT_PY_METADATA = Metadata(
    id="4a1c04bfb1114a4c4dfde20fda4aea87cabad529.boutiques",
    name="fat_mat2d_plot.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


FatMat2dPlotPyParameters = typing.TypedDict('FatMat2dPlotPyParameters', {
    "__STYX_TYPE__": typing.Literal["fat_mat2d_plot.py"],
    "input_file": InputPathType,
    "matrices": typing.NotRequired[list[str] | None],
    "prefix": typing.NotRequired[str | None],
    "file_type": typing.NotRequired[str | None],
    "dpi": typing.NotRequired[float | None],
    "min_colorbar": typing.NotRequired[float | None],
    "max_colorbar": typing.NotRequired[float | None],
    "fs_xticks": typing.NotRequired[float | None],
    "fs_yticks": typing.NotRequired[float | None],
    "fs_title": typing.NotRequired[float | None],
    "fs_cbar": typing.NotRequired[float | None],
    "cbar_n_intervals": typing.NotRequired[float | None],
    "cbar": typing.NotRequired[str | None],
    "cbar_width_perc": typing.NotRequired[float | None],
    "no_colorbar": bool,
    "figsize_x": typing.NotRequired[float | None],
    "figsize_y": typing.NotRequired[float | None],
    "hold_image": bool,
    "tight_layout": bool,
    "xticks_off": bool,
    "yticks_off": bool,
    "version": bool,
    "date": bool,
    "help": bool,
    "help_view": bool,
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
        "fat_mat2d_plot.py": fat_mat2d_plot_py_cargs,
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
        "fat_mat2d_plot.py": fat_mat2d_plot_py_outputs,
    }.get(t)


class FatMat2dPlotPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat2d_plot_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Individual image files of matrices; these can contain colorbars, as
    well."""


def fat_mat2d_plot_py_params(
    input_file: InputPathType,
    matrices: list[str] | None = None,
    prefix: str | None = None,
    file_type: str | None = None,
    dpi: float | None = None,
    min_colorbar: float | None = None,
    max_colorbar: float | None = None,
    fs_xticks: float | None = None,
    fs_yticks: float | None = None,
    fs_title: float | None = None,
    fs_cbar: float | None = None,
    cbar_n_intervals: float | None = None,
    cbar: str | None = None,
    cbar_width_perc: float | None = None,
    no_colorbar: bool = False,
    figsize_x: float | None = None,
    figsize_y: float | None = None,
    hold_image: bool = False,
    tight_layout: bool = False,
    xticks_off: bool = False,
    yticks_off: bool = False,
    version: bool = False,
    date: bool = False,
    help_: bool = False,
    help_view: bool = False,
) -> FatMat2dPlotPyParameters:
    """
    Build parameters.
    
    Args:
        input_file: Name of *.netcc or *.grid file with matrices to be plotted.
        matrices: List of matrices to be plotted, identified by their parameter\
            name. If no list is provided, then all matrices in the input file will\
            be plotted.
        prefix: Output basename for image(s). Note that this can include path\
            information, but the name of each matrix and the file extension will be\
            appended to it.
        file_type: Filetype, given as extension (e.g., png, jpg). Available\
            filetypes depend slightly on your OS and setup.
        dpi: Spatial resolution (dots per inch) of output images.
        min_colorbar: Minimum value of the colorbar.
        max_colorbar: Maximum value of the colorbar.
        fs_xticks: Font size of ticks along the x-axis.
        fs_yticks: Font size of ticks along the y-axis.
        fs_title: Font size of the title.
        fs_cbar: Font size of the colorbar.
        cbar_n_intervals: Number of intervals on colorbars for enumeration\
            purposes. This controls how many numbers appear along the colorbar\
            (which would be NI +1).
        cbar: Name of the colorbar to use. The available colormaps can be found\
            online.
        cbar_width_perc: Width of the colorbar as a percentage of the image.
        no_colorbar: Disable the colorbar in the image.
        figsize_x: Width of the created image in inches.
        figsize_y: Height of the created image in inches.
        hold_image: In addition to saving an image file, open the image and\
            keep displaying it until a key is pressed in the terminal.
        tight_layout: Use matplotlib's tight layout functionality in arranging\
            the plot.
        xticks_off: Don't display labels along the x-axis.
        yticks_off: Don't display labels along the y-axis.
        version: Display the version number of the program.
        date: Display the release/editing date of the current version.
        help_: Display help in the terminal.
        help_view: Display help in a separate text editor.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_mat2d_plot.py",
        "input_file": input_file,
        "no_colorbar": no_colorbar,
        "hold_image": hold_image,
        "tight_layout": tight_layout,
        "xticks_off": xticks_off,
        "yticks_off": yticks_off,
        "version": version,
        "date": date,
        "help": help_,
        "help_view": help_view,
    }
    if matrices is not None:
        params["matrices"] = matrices
    if prefix is not None:
        params["prefix"] = prefix
    if file_type is not None:
        params["file_type"] = file_type
    if dpi is not None:
        params["dpi"] = dpi
    if min_colorbar is not None:
        params["min_colorbar"] = min_colorbar
    if max_colorbar is not None:
        params["max_colorbar"] = max_colorbar
    if fs_xticks is not None:
        params["fs_xticks"] = fs_xticks
    if fs_yticks is not None:
        params["fs_yticks"] = fs_yticks
    if fs_title is not None:
        params["fs_title"] = fs_title
    if fs_cbar is not None:
        params["fs_cbar"] = fs_cbar
    if cbar_n_intervals is not None:
        params["cbar_n_intervals"] = cbar_n_intervals
    if cbar is not None:
        params["cbar"] = cbar
    if cbar_width_perc is not None:
        params["cbar_width_perc"] = cbar_width_perc
    if figsize_x is not None:
        params["figsize_x"] = figsize_x
    if figsize_y is not None:
        params["figsize_y"] = figsize_y
    return params


def fat_mat2d_plot_py_cargs(
    params: FatMat2dPlotPyParameters,
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
    cargs.append("fat_mat2d_plot.py")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("matrices") is not None:
        cargs.extend(params.get("matrices"))
    if params.get("prefix") is not None:
        cargs.append(params.get("prefix"))
    if params.get("file_type") is not None:
        cargs.append(params.get("file_type"))
    if params.get("dpi") is not None:
        cargs.append(str(params.get("dpi")))
    if params.get("min_colorbar") is not None:
        cargs.append(str(params.get("min_colorbar")))
    if params.get("max_colorbar") is not None:
        cargs.append(str(params.get("max_colorbar")))
    if params.get("fs_xticks") is not None:
        cargs.append(str(params.get("fs_xticks")))
    if params.get("fs_yticks") is not None:
        cargs.append(str(params.get("fs_yticks")))
    if params.get("fs_title") is not None:
        cargs.append(str(params.get("fs_title")))
    if params.get("fs_cbar") is not None:
        cargs.append(str(params.get("fs_cbar")))
    if params.get("cbar_n_intervals") is not None:
        cargs.append(str(params.get("cbar_n_intervals")))
    if params.get("cbar") is not None:
        cargs.append(params.get("cbar"))
    if params.get("cbar_width_perc") is not None:
        cargs.append(str(params.get("cbar_width_perc")))
    if params.get("no_colorbar"):
        cargs.append("-cbar_off")
    if params.get("figsize_x") is not None:
        cargs.append(str(params.get("figsize_x")))
    if params.get("figsize_y") is not None:
        cargs.append(str(params.get("figsize_y")))
    if params.get("hold_image"):
        cargs.append("-hold_image")
    if params.get("tight_layout"):
        cargs.append("-tight_layout")
    if params.get("xticks_off"):
        cargs.append("-xticks_off")
    if params.get("yticks_off"):
        cargs.append("-yticks_off")
    if params.get("version"):
        cargs.append("-ver")
    if params.get("date"):
        cargs.append("-date")
    if params.get("help"):
        cargs.append("-help")
    if params.get("help_view"):
        cargs.append("-hview")
    return cargs


def fat_mat2d_plot_py_outputs(
    params: FatMat2dPlotPyParameters,
    execution: Execution,
) -> FatMat2dPlotPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatMat2dPlotPyOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("prefix") + "_[MATRIX_NAME]." + params.get("file_type")) if (params.get("prefix") is not None and params.get("file_type") is not None) else None,
    )
    return ret


def fat_mat2d_plot_py_execute(
    params: FatMat2dPlotPyParameters,
    execution: Execution,
) -> FatMat2dPlotPyOutputs:
    """
    Plots simple matrices output from 3dNetCorr (*.netcc) and 3dTrackID (*.grid).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatMat2dPlotPyOutputs`).
    """
    params = execution.params(params)
    cargs = fat_mat2d_plot_py_cargs(params, execution)
    ret = fat_mat2d_plot_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_mat2d_plot_py(
    input_file: InputPathType,
    matrices: list[str] | None = None,
    prefix: str | None = None,
    file_type: str | None = None,
    dpi: float | None = None,
    min_colorbar: float | None = None,
    max_colorbar: float | None = None,
    fs_xticks: float | None = None,
    fs_yticks: float | None = None,
    fs_title: float | None = None,
    fs_cbar: float | None = None,
    cbar_n_intervals: float | None = None,
    cbar: str | None = None,
    cbar_width_perc: float | None = None,
    no_colorbar: bool = False,
    figsize_x: float | None = None,
    figsize_y: float | None = None,
    hold_image: bool = False,
    tight_layout: bool = False,
    xticks_off: bool = False,
    yticks_off: bool = False,
    version: bool = False,
    date: bool = False,
    help_: bool = False,
    help_view: bool = False,
    runner: Runner | None = None,
) -> FatMat2dPlotPyOutputs:
    """
    Plots simple matrices output from 3dNetCorr (*.netcc) and 3dTrackID (*.grid).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Name of *.netcc or *.grid file with matrices to be plotted.
        matrices: List of matrices to be plotted, identified by their parameter\
            name. If no list is provided, then all matrices in the input file will\
            be plotted.
        prefix: Output basename for image(s). Note that this can include path\
            information, but the name of each matrix and the file extension will be\
            appended to it.
        file_type: Filetype, given as extension (e.g., png, jpg). Available\
            filetypes depend slightly on your OS and setup.
        dpi: Spatial resolution (dots per inch) of output images.
        min_colorbar: Minimum value of the colorbar.
        max_colorbar: Maximum value of the colorbar.
        fs_xticks: Font size of ticks along the x-axis.
        fs_yticks: Font size of ticks along the y-axis.
        fs_title: Font size of the title.
        fs_cbar: Font size of the colorbar.
        cbar_n_intervals: Number of intervals on colorbars for enumeration\
            purposes. This controls how many numbers appear along the colorbar\
            (which would be NI +1).
        cbar: Name of the colorbar to use. The available colormaps can be found\
            online.
        cbar_width_perc: Width of the colorbar as a percentage of the image.
        no_colorbar: Disable the colorbar in the image.
        figsize_x: Width of the created image in inches.
        figsize_y: Height of the created image in inches.
        hold_image: In addition to saving an image file, open the image and\
            keep displaying it until a key is pressed in the terminal.
        tight_layout: Use matplotlib's tight layout functionality in arranging\
            the plot.
        xticks_off: Don't display labels along the x-axis.
        yticks_off: Don't display labels along the y-axis.
        version: Display the version number of the program.
        date: Display the release/editing date of the current version.
        help_: Display help in the terminal.
        help_view: Display help in a separate text editor.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMat2dPlotPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MAT2D_PLOT_PY_METADATA)
    params = fat_mat2d_plot_py_params(
        input_file=input_file,
        matrices=matrices,
        prefix=prefix,
        file_type=file_type,
        dpi=dpi,
        min_colorbar=min_colorbar,
        max_colorbar=max_colorbar,
        fs_xticks=fs_xticks,
        fs_yticks=fs_yticks,
        fs_title=fs_title,
        fs_cbar=fs_cbar,
        cbar_n_intervals=cbar_n_intervals,
        cbar=cbar,
        cbar_width_perc=cbar_width_perc,
        no_colorbar=no_colorbar,
        figsize_x=figsize_x,
        figsize_y=figsize_y,
        hold_image=hold_image,
        tight_layout=tight_layout,
        xticks_off=xticks_off,
        yticks_off=yticks_off,
        version=version,
        date=date,
        help_=help_,
        help_view=help_view,
    )
    return fat_mat2d_plot_py_execute(params, execution)


__all__ = [
    "FAT_MAT2D_PLOT_PY_METADATA",
    "FatMat2dPlotPyOutputs",
    "FatMat2dPlotPyParameters",
    "fat_mat2d_plot_py",
    "fat_mat2d_plot_py_params",
]

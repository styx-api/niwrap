# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FAT_MAT2D_PLOT_PY_METADATA = Metadata(
    id="75f1fbd87e1c894061007584dd4f693329caeb08",
    name="fat_mat2d_plot.py",
    container_image_type="docker",
    container_image_index="docker.io",
    container_image_tag="python:3.x",
)


class FatMat2dPlotPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat2d_plot_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Individual image files of matrices; these can contain colorbars, as well."""


def fat_mat2d_plot_py(
    input_file: InputPathType,
    matrices: list[str] | None = None,
    prefix: str | None = None,
    file_type: str | None = None,
    dpi: float | int | None = None,
    min_colorbar: float | int | None = None,
    max_colorbar: float | int | None = None,
    fs_xticks: float | int | None = None,
    fs_yticks: float | int | None = None,
    fs_title: float | int | None = None,
    fs_cbar: float | int | None = None,
    cbar_n_intervals: float | int | None = None,
    cbar: str | None = None,
    cbar_width_perc: float | int | None = None,
    no_colorbar: bool = False,
    figsize_x: float | int | None = None,
    figsize_y: float | int | None = None,
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
    fat_mat2d_plot.py by PA Taylor.
    
    Plots simple matrices output from 3dNetCorr (*.netcc) and 3dTrackID
    (*.grid).
    
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
    cargs = []
    cargs.append("fat_mat2d_plot.py")
    cargs.append(execution.input_file(input_file))
    if matrices is not None:
        cargs.extend(matrices)
    if prefix is not None:
        cargs.append(prefix)
    if file_type is not None:
        cargs.append(file_type)
    if dpi is not None:
        cargs.append(str(dpi))
    if min_colorbar is not None:
        cargs.append(str(min_colorbar))
    if max_colorbar is not None:
        cargs.append(str(max_colorbar))
    if fs_xticks is not None:
        cargs.append(str(fs_xticks))
    if fs_yticks is not None:
        cargs.append(str(fs_yticks))
    if fs_title is not None:
        cargs.append(str(fs_title))
    if fs_cbar is not None:
        cargs.append(str(fs_cbar))
    if cbar_n_intervals is not None:
        cargs.append(str(cbar_n_intervals))
    if cbar is not None:
        cargs.append(cbar)
    if cbar_width_perc is not None:
        cargs.append(str(cbar_width_perc))
    if no_colorbar:
        cargs.append("-cbar_off")
    if figsize_x is not None:
        cargs.append(str(figsize_x))
    if figsize_y is not None:
        cargs.append(str(figsize_y))
    if hold_image:
        cargs.append("-hold_image")
    if tight_layout:
        cargs.append("-tight_layout")
    if xticks_off:
        cargs.append("-xticks_off")
    if yticks_off:
        cargs.append("-yticks_off")
    if version:
        cargs.append("-ver")
    if date:
        cargs.append("-date")
    if help_:
        cargs.append("-help")
    if help_view:
        cargs.append("-hview")
    ret = FatMat2dPlotPyOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(f"{prefix}_[MATRIX_NAME].{file_type}") if prefix is not None and file_type is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_MAT2D_PLOT_PY_METADATA",
    "FatMat2dPlotPyOutputs",
    "fat_mat2d_plot_py",
]

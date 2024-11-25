# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_BOXPLOT_METADATA = Metadata(
    id="3362ac87c4f9816583c5cb508d38ea7b2722174f.boutiques",
    name="fsl_boxplot",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslBoxplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_boxplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_png: OutputPathType
    """The output boxplot image in PNG format"""


def fsl_boxplot(
    input_files: list[InputPathType],
    output_image: str,
    title: str | None = None,
    legend_file: InputPathType | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    plot_height: float | None = 450,
    plot_width: float | None = None,
    runner: Runner | None = None,
) -> FslBoxplotOutputs:
    """
    Tool for creating boxplot images from ASCII text matrices.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_files: Comma-separated list of input file names (ASCII text\
            matrices, one column per boxplot).
        output_image: Output filename for the PNG file.
        title: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        x_label: X-axis label.
        y_label: Y-axis label.
        plot_height: Plot height in pixels (default 450).
        plot_width: Plot width in pixels (default 80*#boxplots).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslBoxplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_BOXPLOT_METADATA)
    cargs = []
    cargs.append("fsl_boxplot")
    cargs.extend([
        "--in",
        *[execution.input_file(f) for f in input_files]
    ])
    cargs.extend([
        "--out",
        output_image
    ])
    if title is not None:
        cargs.extend([
            "--title",
            title
        ])
    if legend_file is not None:
        cargs.extend([
            "--legend",
            execution.input_file(legend_file)
        ])
    if x_label is not None:
        cargs.extend([
            "--xlabel",
            x_label
        ])
    if y_label is not None:
        cargs.extend([
            "--ylabel",
            y_label
        ])
    if plot_height is not None:
        cargs.extend([
            "--height",
            str(plot_height)
        ])
    if plot_width is not None:
        cargs.extend([
            "--width",
            str(plot_width)
        ])
    ret = FslBoxplotOutputs(
        root=execution.output_file("."),
        output_png=execution.output_file(output_image + ".png"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_BOXPLOT_METADATA",
    "FslBoxplotOutputs",
    "fsl_boxplot",
]

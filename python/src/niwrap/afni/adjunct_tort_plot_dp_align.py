# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_TORT_PLOT_DP_ALIGN_METADATA = Metadata(
    id="618d7b822054094255c11f8d40e4e17ed180621a.boutiques",
    name="adjunct_tort_plot_dp_align",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctTortPlotDpAlignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_tort_plot_dp_align(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    align_params: OutputPathType
    """Text file containing 6 columns of data for the rigid-body alignment
    parameters estimated by DIFFPREP."""
    enorm_file: OutputPathType
    """Text file with 1 column of data, the Euclidean norm of the differences of
    the rigid body alignment parameters."""
    plot_jpg: OutputPathType
    """A plot of enorm and the alignment parameters in JPG format."""
    plot_svg: OutputPathType
    """A plot of enorm and the alignment parameters in SVG format."""


def adjunct_tort_plot_dp_align(
    input_file: InputPathType,
    output_prefix: str,
    enorm_max: float | None = None,
    enorm_hline: float | None = None,
    no_svg: bool = False,
    runner: Runner | None = None,
) -> AdjunctTortPlotDpAlignOutputs:
    """
    Tool to display the rigid-body alignment parameters from TORTOISE's DIFFPREP,
    useful for analyzing subject motion in DWI data.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_tort_plot_dp_align.html
    
    Args:
        input_file: Name of DIFFPREP-produced file to parse, probably ending in\
            '_transformations.txt'.
        output_prefix: Base of output files; can contain path information.\
            Should *not* include any extension.
        enorm_max: Specify max value of y-axis of enorm plot in SVG image.\
            Useful for having a constant value across a study.
        enorm_hline: Specify value of a horizontal, dotted, bright cyan line\
            for the enorm plot in SVG image. Can help with visualization.
        no_svg: Opt to turn off even checking to plot an SVG version of the\
            figure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctTortPlotDpAlignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_TORT_PLOT_DP_ALIGN_METADATA)
    cargs = []
    cargs.append("adjunct_tort_plot_dp_align")
    cargs.append("-input")
    cargs.append(execution.input_file(input_file))
    cargs.append("-prefix")
    cargs.append(output_prefix)
    cargs.append("-enorm_max")
    if enorm_max is not None:
        cargs.append(str(enorm_max))
    cargs.append("-enorm_hline")
    if enorm_hline is not None:
        cargs.append(str(enorm_hline))
    if no_svg:
        cargs.append("-no_svg")
    ret = AdjunctTortPlotDpAlignOutputs(
        root=execution.output_file("."),
        align_params=execution.output_file(output_prefix + "_align.1D"),
        enorm_file=execution.output_file(output_prefix + "_enorm.1D"),
        plot_jpg=execution.output_file(output_prefix + ".jpg"),
        plot_svg=execution.output_file(output_prefix + ".svg"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_TORT_PLOT_DP_ALIGN_METADATA",
    "AdjunctTortPlotDpAlignOutputs",
    "adjunct_tort_plot_dp_align",
]

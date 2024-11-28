# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_HISTOGRAM_METADATA = Metadata(
    id="574d62ed2a96707a8b0178fbacd753480a64e3fa.boutiques",
    name="fsl_histogram",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslHistogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_histogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    png_file: OutputPathType
    """Generated PNG file"""


def fsl_histogram(
    input_file_duplicate: InputPathType,
    output_file_duplicate: str,
    mask_file_duplicate: InputPathType | None = None,
    gmmfit_file_duplicate: InputPathType | None = None,
    plot_title_duplicate: str | None = None,
    legend_file_duplicate: InputPathType | None = None,
    xlabel_duplicate: str | None = None,
    ylabel_duplicate: str | None = None,
    plot_height_duplicate: float | None = None,
    plot_width_duplicate: float | None = None,
    num_bins_duplicate: float | None = None,
    zoom_factor_duplicate: float | None = None,
    use_gmm_flag: bool = False,
    runner: Runner | None = None,
) -> FslHistogramOutputs:
    """
    Histogram plotting tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file_duplicate: Input file name.
        output_file_duplicate: Output filename for the PNG file.
        mask_file_duplicate: Mask file name.
        gmmfit_file_duplicate: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        plot_title_duplicate: Plot title.
        legend_file_duplicate: File name of ASCII text file, one row per legend\
            entry.
        xlabel_duplicate: X-axis label.
        ylabel_duplicate: Y-axis label.
        plot_height_duplicate: Plot height in pixels (default 400).
        plot_width_duplicate: Plot width in pixels (default 600).
        num_bins_duplicate: Number of histogram bins.
        zoom_factor_duplicate: Zoom factor for y-range (e.g. 2.0).
        use_gmm_flag: Use Gaussian mixture model instead of Gaussian/Gamma\
            mixture model.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslHistogramOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_HISTOGRAM_METADATA)
    cargs = []
    cargs.append("fsl_histogram")
    cargs.extend([
        "--in",
        execution.input_file(input_file_duplicate)
    ])
    cargs.extend([
        "--out",
        output_file_duplicate
    ])
    if mask_file_duplicate is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_file_duplicate)
        ])
    if gmmfit_file_duplicate is not None:
        cargs.extend([
            "--gmmfit",
            execution.input_file(gmmfit_file_duplicate)
        ])
    if plot_title_duplicate is not None:
        cargs.extend([
            "--title",
            plot_title_duplicate
        ])
    if legend_file_duplicate is not None:
        cargs.extend([
            "--legend",
            execution.input_file(legend_file_duplicate)
        ])
    if xlabel_duplicate is not None:
        cargs.extend([
            "--xlabel",
            xlabel_duplicate
        ])
    if ylabel_duplicate is not None:
        cargs.extend([
            "--ylabel",
            ylabel_duplicate
        ])
    if plot_height_duplicate is not None:
        cargs.extend([
            "--height",
            str(plot_height_duplicate)
        ])
    if plot_width_duplicate is not None:
        cargs.extend([
            "--width",
            str(plot_width_duplicate)
        ])
    if num_bins_duplicate is not None:
        cargs.extend([
            "--bins",
            str(num_bins_duplicate)
        ])
    if zoom_factor_duplicate is not None:
        cargs.extend([
            "--detail",
            str(zoom_factor_duplicate)
        ])
    if use_gmm_flag:
        cargs.append("--gmm")
    ret = FslHistogramOutputs(
        root=execution.output_file("."),
        png_file=execution.output_file("[OUTPUT_FILE]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_HISTOGRAM_METADATA",
    "FslHistogramOutputs",
    "fsl_histogram",
]

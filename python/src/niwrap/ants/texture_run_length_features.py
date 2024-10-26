# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TEXTURE_RUN_LENGTH_FEATURES_METADATA = Metadata(
    id="99c3089b305255bec7d6249a4c2fc94894071c52.boutiques",
    name="TextureRunLengthFeatures",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class TextureRunLengthFeaturesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `texture_run_length_features(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    short_run_emphasis: OutputPathType
    """Output feature: Short Run Emphasis."""
    long_run_emphasis: OutputPathType
    """Output feature: Long Run Emphasis."""
    grey_level_nonuniformity: OutputPathType
    """Output feature: Grey Level Nonuniformity."""
    run_length_nonuniformity: OutputPathType
    """Output feature: Run Length Nonuniformity."""
    low_grey_level_run_emphasis: OutputPathType
    """Output feature: Low Grey Level Run Emphasis."""
    high_grey_level_run_emphasis: OutputPathType
    """Output feature: High Grey Level Run Emphasis."""
    short_run_low_grey_level_emphasis: OutputPathType
    """Output feature: Short Run Low Grey Level Emphasis."""
    short_run_high_grey_level_emphasis: OutputPathType
    """Output feature: Short Run High Grey Level Emphasis."""
    long_run_low_grey_level_emphasis: OutputPathType
    """Output feature: Long Run Low Grey Level Emphasis."""
    long_run_high_grey_level_emphasis: OutputPathType
    """Output feature: Long Run High Grey Level Emphasis."""


def texture_run_length_features(
    image_dimension: int,
    input_image: InputPathType,
    number_of_bins_per_axis: int | None = 256,
    mask_image: InputPathType | None = None,
    mask_label: int | None = 1,
    runner: Runner | None = None,
) -> TextureRunLengthFeaturesOutputs:
    """
    A tool to calculate texture run length features on an input image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input image.
        input_image: The path to the input image file.
        number_of_bins_per_axis: The number of bins per axis for the histogram.
        mask_image: The path to the mask image file.
        mask_label: The label value in the mask image to be used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TextureRunLengthFeaturesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEXTURE_RUN_LENGTH_FEATURES_METADATA)
    cargs = []
    cargs.append("TextureRunLengthFeatures")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(input_image))
    if number_of_bins_per_axis is not None:
        cargs.append(str(number_of_bins_per_axis))
    if mask_image is not None:
        cargs.append(execution.input_file(mask_image))
    if mask_label is not None:
        cargs.append(str(mask_label))
    ret = TextureRunLengthFeaturesOutputs(
        root=execution.output_file("."),
        short_run_emphasis=execution.output_file("short_run_emphasis.csv"),
        long_run_emphasis=execution.output_file("long_run_emphasis.csv"),
        grey_level_nonuniformity=execution.output_file("grey_level_nonuniformity.csv"),
        run_length_nonuniformity=execution.output_file("run_length_nonuniformity.csv"),
        low_grey_level_run_emphasis=execution.output_file("low_grey_level_run_emphasis.csv"),
        high_grey_level_run_emphasis=execution.output_file("high_grey_level_run_emphasis.csv"),
        short_run_low_grey_level_emphasis=execution.output_file("short_run_low_grey_level_emphasis.csv"),
        short_run_high_grey_level_emphasis=execution.output_file("short_run_high_grey_level_emphasis.csv"),
        long_run_low_grey_level_emphasis=execution.output_file("long_run_low_grey_level_emphasis.csv"),
        long_run_high_grey_level_emphasis=execution.output_file("long_run_high_grey_level_emphasis.csv"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TEXTURE_RUN_LENGTH_FEATURES_METADATA",
    "TextureRunLengthFeaturesOutputs",
    "texture_run_length_features",
]

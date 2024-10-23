# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLSMOOTHFILL_METADATA = Metadata(
    id="decfe9aa72638e1ec65326903fe3b064f1752e01.boutiques",
    name="fslsmoothfill",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslsmoothfillOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslsmoothfill(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslsmoothfill(
    input_image: InputPathType,
    mask_image: InputPathType,
    output_image: str,
    number_of_iterations: int | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> FslsmoothfillOutputs:
    """
    Smoothfill is a tool designed to fill in holes in images by smoothly
    interpolating the pixel values.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Filename of the input image.
        mask_image: Filename of the mask image.
        output_image: Filename for the output smoothed result image.
        number_of_iterations: Number of iterations.
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslsmoothfillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSMOOTHFILL_METADATA)
    cargs = []
    cargs.append("fslsmoothfill")
    cargs.append("-i")
    cargs.extend([
        "--in",
        execution.input_file(input_image)
    ])
    cargs.append("-m")
    cargs.extend([
        "--mask",
        execution.input_file(mask_image)
    ])
    cargs.append("-o")
    cargs.extend([
        "--out",
        output_image
    ])
    if number_of_iterations is not None:
        cargs.extend([
            "--niter",
            str(number_of_iterations)
        ])
    if debug_flag:
        cargs.append("--debug")
    if verbose_flag:
        cargs.append("--verbose")
    ret = FslsmoothfillOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSMOOTHFILL_METADATA",
    "FslsmoothfillOutputs",
    "fslsmoothfill",
]

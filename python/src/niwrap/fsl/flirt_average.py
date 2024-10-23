# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FLIRT_AVERAGE_METADATA = Metadata(
    id="166bd09d08810b31c509ebe88b18b34b5889195a.boutiques",
    name="flirt_average",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FlirtAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flirt_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Averaged output image"""


def flirt_average(
    ninputs: int,
    input1: InputPathType,
    input2: InputPathType,
    output_file: str,
    reference_image: InputPathType | None = None,
    flirt_options: str | None = None,
    runner: Runner | None = None,
) -> FlirtAverageOutputs:
    """
    Averages multiple input images after linear registration (FLIRT).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        ninputs: Number of input images.
        input1: First input image (e.g. rawT1_1.nii.gz).
        input2: Second input image (e.g. rawT1_2.nii.gz).
        output_file: Output image (e.g. averageT1.nii.gz).
        reference_image: Reference image to use instead of first input.
        flirt_options: Options to be passed to FLIRT.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FlirtAverageOutputs`).
    """
    if not (2 <= ninputs): 
        raise ValueError(f"'ninputs' must be greater than 2 <= x but was {ninputs}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(FLIRT_AVERAGE_METADATA)
    cargs = []
    cargs.append("flirt_average")
    cargs.append(str(ninputs))
    cargs.append(execution.input_file(input1))
    cargs.append(execution.input_file(input2))
    cargs.append("...")
    cargs.append(output_file)
    if reference_image is not None:
        cargs.extend([
            "-FAref",
            execution.input_file(reference_image)
        ])
    if flirt_options is not None:
        cargs.append(flirt_options)
    ret = FlirtAverageOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(output_file + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FLIRT_AVERAGE_METADATA",
    "FlirtAverageOutputs",
    "flirt_average",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_ENTROPY_METADATA = Metadata(
    id="8fdcf1695c52124c1611443a80362f485922be1c.boutiques",
    name="mris_entropy",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisEntropyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_entropy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file containing the computed entropy"""


def mris_entropy(
    subject: str,
    hemi: str,
    wfile: InputPathType,
    curvfile: InputPathType,
    average_iterations: float | None = 0,
    normalize: bool = False,
    runner: Runner | None = None,
) -> MrisEntropyOutputs:
    """
    Computes the entropy of a surface activation pattern for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject ID.
        hemi: Hemisphere (e.g., lh or rh).
        wfile: Weight file for surface.
        curvfile: Curvature file for input.
        average_iterations: Specify number of curvature averaging iterations\
            (default=0).
        normalize: Normalize curvature before writing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisEntropyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ENTROPY_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mris_entropy")
    cargs.append(subject)
    cargs.append(hemi)
    cargs.append(execution.input_file(wfile))
    cargs.append(execution.input_file(curvfile))
    if average_iterations is not None:
        cargs.extend([
            "-a",
            str(average_iterations)
        ])
    if normalize:
        cargs.append("-n")
    ret = MrisEntropyOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(subject + "_" + hemi + "_output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_ENTROPY_METADATA",
    "MrisEntropyOutputs",
    "mris_entropy",
]

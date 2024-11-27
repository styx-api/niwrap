# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LRFLIP_METADATA = Metadata(
    id="f5fb5c24267d6a937ff2b7766ab5fb355973e781.boutiques",
    name="3dLRflip",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dLrflipOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lrflip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    flipped_output: OutputPathType
    """Output dataset after flipping"""


def v_3d_lrflip(
    datasets: list[InputPathType],
    flip_z: bool = False,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dLrflipOutputs:
    """
    Flips the rows of a dataset along one of the three axes to correct dataset
    direction labeling errors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Datasets to flip.
        flip_z: Flip about the 3rd direction.
        output_prefix: Prefix to use for output. If multiple datasets are\
            input, the program will choose a prefix for each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLrflipOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LRFLIP_METADATA)
    cargs = []
    cargs.append("3dLRflip")
    if flip_z:
        cargs.append("-Z")
    if output_prefix is not None:
        cargs.extend([
            "-prefix",
            output_prefix
        ])
    cargs.extend([execution.input_file(f) for f in datasets])
    ret = V3dLrflipOutputs(
        root=execution.output_file("."),
        flipped_output=execution.output_file("[PREFIX]*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLrflipOutputs",
    "V_3D_LRFLIP_METADATA",
    "v_3d_lrflip",
]

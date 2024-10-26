# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__2DWARPER_METADATA = Metadata(
    id="84ef515295a9aa7008fa07f5cd21d7b371f8a9f0.boutiques",
    name="@2dwarper",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V2dwarperOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__2dwarper(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Warped output image from the dataset"""


def v__2dwarper(
    input_dataset: InputPathType,
    runner: Runner | None = None,
) -> V2dwarperOutputs:
    """
    2D image warping tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g., image to be warped).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2dwarperOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__2DWARPER_METADATA)
    cargs = []
    cargs.append("@2dwarper")
    cargs.append(execution.input_file(input_dataset))
    ret = V2dwarperOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("warped_output"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V2dwarperOutputs",
    "V__2DWARPER_METADATA",
    "v__2dwarper",
]

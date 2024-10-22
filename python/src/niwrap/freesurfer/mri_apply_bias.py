# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_APPLY_BIAS_METADATA = Metadata(
    id="cd7f8c875df415ca7119b515264262a272033173.boutiques",
    name="mri_apply_bias",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriApplyBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_apply_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Output volume after applying bias"""


def mri_apply_bias(
    input_volume: InputPathType,
    bias_volume: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriApplyBiasOutputs:
    """
    A tool for applying a bias volume to an input volume to produce an output
    volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: The input volume file.
        bias_volume: The bias volume file.
        output_volume: The output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriApplyBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_APPLY_BIAS_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_apply_bias")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(bias_volume))
    cargs.append(output_volume)
    ret = MriApplyBiasOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_APPLY_BIAS_METADATA",
    "MriApplyBiasOutputs",
    "mri_apply_bias",
]

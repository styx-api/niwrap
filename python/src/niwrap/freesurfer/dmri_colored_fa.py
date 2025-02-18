# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_COLORED_FA_METADATA = Metadata(
    id="9942a5ec79bb71bf37d6af7b5ec7bc808a0b17b5.boutiques",
    name="dmri_coloredFA",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriColoredFaParameters = typing.TypedDict('DmriColoredFaParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_coloredFA"],
    "input_volume": InputPathType,
    "output_volume": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "dmri_coloredFA": dmri_colored_fa_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "dmri_coloredFA": dmri_colored_fa_outputs,
    }.get(t)


class DmriColoredFaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_colored_fa(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_colored_fa: OutputPathType
    """The output colored FA image."""


def dmri_colored_fa_params(
    input_volume: InputPathType,
    output_volume: str = "colored_FA",
) -> DmriColoredFaParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input diffusion MRI volume.
        output_volume: Output colored FA image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_coloredFA",
        "input_volume": input_volume,
        "output_volume": output_volume,
    }
    return params


def dmri_colored_fa_cargs(
    params: DmriColoredFaParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("dmri_coloredFA")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(params.get("output_volume"))
    return cargs


def dmri_colored_fa_outputs(
    params: DmriColoredFaParameters,
    execution: Execution,
) -> DmriColoredFaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriColoredFaOutputs(
        root=execution.output_file("."),
        output_colored_fa=execution.output_file(params.get("output_volume") + ".nii.gz"),
    )
    return ret


def dmri_colored_fa_execute(
    params: DmriColoredFaParameters,
    execution: Execution,
) -> DmriColoredFaOutputs:
    """
    Tool for generating colored FA maps from diffusion MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriColoredFaOutputs`).
    """
    cargs = dmri_colored_fa_cargs(params, execution)
    ret = dmri_colored_fa_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def dmri_colored_fa(
    input_volume: InputPathType,
    output_volume: str = "colored_FA",
    runner: Runner | None = None,
) -> DmriColoredFaOutputs:
    """
    Tool for generating colored FA maps from diffusion MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input diffusion MRI volume.
        output_volume: Output colored FA image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriColoredFaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_COLORED_FA_METADATA)
    params = dmri_colored_fa_params(input_volume=input_volume, output_volume=output_volume)
    return dmri_colored_fa_execute(params, execution)


__all__ = [
    "DMRI_COLORED_FA_METADATA",
    "DmriColoredFaOutputs",
    "DmriColoredFaParameters",
    "dmri_colored_fa",
    "dmri_colored_fa_params",
]

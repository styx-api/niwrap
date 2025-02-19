# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_STRIP_NONWHITE_METADATA = Metadata(
    id="85cd600947bfda4ae61eea101b99ad79680f009b.boutiques",
    name="mri_strip_nonwhite",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriStripNonwhiteParameters = typing.TypedDict('MriStripNonwhiteParameters', {
    "__STYX_TYPE__": typing.Literal["mri_strip_nonwhite"],
    "input_volume": InputPathType,
    "transform": InputPathType,
    "template_volume": InputPathType,
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
        "mri_strip_nonwhite": mri_strip_nonwhite_cargs,
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
        "mri_strip_nonwhite": mri_strip_nonwhite_outputs,
    }.get(t)


class MriStripNonwhiteOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_strip_nonwhite(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Processed output volume file"""


def mri_strip_nonwhite_params(
    input_volume: InputPathType,
    transform: InputPathType,
    template_volume: InputPathType,
    output_volume: str,
) -> MriStripNonwhiteParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input MRI volume file.
        transform: Transformation file to be applied to the input volume.
        template_volume: Template volume file used in conjunction with the\
            transform.
        output_volume: Name of the output volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_strip_nonwhite",
        "input_volume": input_volume,
        "transform": transform,
        "template_volume": template_volume,
        "output_volume": output_volume,
    }
    return params


def mri_strip_nonwhite_cargs(
    params: MriStripNonwhiteParameters,
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
    cargs.append("mri_strip_nonwhite")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("transform")))
    cargs.append(execution.input_file(params.get("template_volume")))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_strip_nonwhite_outputs(
    params: MriStripNonwhiteParameters,
    execution: Execution,
) -> MriStripNonwhiteOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriStripNonwhiteOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_strip_nonwhite_execute(
    params: MriStripNonwhiteParameters,
    execution: Execution,
) -> MriStripNonwhiteOutputs:
    """
    Tool for processing MRI images, transforming volumetric data using provided
    transformation and template files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriStripNonwhiteOutputs`).
    """
    params = execution.params(params)
    cargs = mri_strip_nonwhite_cargs(params, execution)
    ret = mri_strip_nonwhite_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_strip_nonwhite(
    input_volume: InputPathType,
    transform: InputPathType,
    template_volume: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriStripNonwhiteOutputs:
    """
    Tool for processing MRI images, transforming volumetric data using provided
    transformation and template files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input MRI volume file.
        transform: Transformation file to be applied to the input volume.
        template_volume: Template volume file used in conjunction with the\
            transform.
        output_volume: Name of the output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriStripNonwhiteOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_STRIP_NONWHITE_METADATA)
    params = mri_strip_nonwhite_params(
        input_volume=input_volume,
        transform=transform,
        template_volume=template_volume,
        output_volume=output_volume,
    )
    return mri_strip_nonwhite_execute(params, execution)


__all__ = [
    "MRI_STRIP_NONWHITE_METADATA",
    "MriStripNonwhiteOutputs",
    "MriStripNonwhiteParameters",
    "mri_strip_nonwhite",
    "mri_strip_nonwhite_params",
]

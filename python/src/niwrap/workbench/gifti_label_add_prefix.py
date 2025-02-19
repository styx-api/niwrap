# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GIFTI_LABEL_ADD_PREFIX_METADATA = Metadata(
    id="3d379a6c755dab747292a0a91f754e423ff73eca.boutiques",
    name="gifti-label-add-prefix",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


GiftiLabelAddPrefixParameters = typing.TypedDict('GiftiLabelAddPrefixParameters', {
    "__STYX_TYPE__": typing.Literal["gifti-label-add-prefix"],
    "label_in": InputPathType,
    "prefix": str,
    "label_out": str,
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
        "gifti-label-add-prefix": gifti_label_add_prefix_cargs,
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
        "gifti-label-add-prefix": gifti_label_add_prefix_outputs,
    }.get(t)


class GiftiLabelAddPrefixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_label_add_prefix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def gifti_label_add_prefix_params(
    label_in: InputPathType,
    prefix: str,
    label_out: str,
) -> GiftiLabelAddPrefixParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input label file.
        prefix: the prefix string to add.
        label_out: the output label file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gifti-label-add-prefix",
        "label_in": label_in,
        "prefix": prefix,
        "label_out": label_out,
    }
    return params


def gifti_label_add_prefix_cargs(
    params: GiftiLabelAddPrefixParameters,
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
    cargs.append("wb_command")
    cargs.append("-gifti-label-add-prefix")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("prefix"))
    cargs.append(params.get("label_out"))
    return cargs


def gifti_label_add_prefix_outputs(
    params: GiftiLabelAddPrefixParameters,
    execution: Execution,
) -> GiftiLabelAddPrefixOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GiftiLabelAddPrefixOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
    )
    return ret


def gifti_label_add_prefix_execute(
    params: GiftiLabelAddPrefixParameters,
    execution: Execution,
) -> GiftiLabelAddPrefixOutputs:
    """
    Add prefix to all label names in a gifti label file.
    
    For each label other than '???', prepend <prefix> to the label name.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GiftiLabelAddPrefixOutputs`).
    """
    params = execution.params(params)
    cargs = gifti_label_add_prefix_cargs(params, execution)
    ret = gifti_label_add_prefix_outputs(params, execution)
    execution.run(cargs)
    return ret


def gifti_label_add_prefix(
    label_in: InputPathType,
    prefix: str,
    label_out: str,
    runner: Runner | None = None,
) -> GiftiLabelAddPrefixOutputs:
    """
    Add prefix to all label names in a gifti label file.
    
    For each label other than '???', prepend <prefix> to the label name.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input label file.
        prefix: the prefix string to add.
        label_out: the output label file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GiftiLabelAddPrefixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GIFTI_LABEL_ADD_PREFIX_METADATA)
    params = gifti_label_add_prefix_params(
        label_in=label_in,
        prefix=prefix,
        label_out=label_out,
    )
    return gifti_label_add_prefix_execute(params, execution)


__all__ = [
    "GIFTI_LABEL_ADD_PREFIX_METADATA",
    "GiftiLabelAddPrefixOutputs",
    "GiftiLabelAddPrefixParameters",
    "gifti_label_add_prefix",
    "gifti_label_add_prefix_params",
]

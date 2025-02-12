# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_MODIFY_KEYS_METADATA = Metadata(
    id="ce46240e03c08d651d4c811741f57d7c7aeebe60.boutiques",
    name="label-modify-keys",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
LabelModifyKeysParameters = typing.TypedDict('LabelModifyKeysParameters', {
    "__STYX_TYPE__": typing.Literal["label-modify-keys"],
    "label_in": InputPathType,
    "remap_file": str,
    "label_out": str,
    "opt_column_column": typing.NotRequired[str | None],
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
        "label-modify-keys": label_modify_keys_cargs,
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
        "label-modify-keys": label_modify_keys_outputs,
    }.get(t)


class LabelModifyKeysOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_modify_keys(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """output label file"""


def label_modify_keys_params(
    label_in: InputPathType,
    remap_file: str,
    label_out: str,
    opt_column_column: str | None = None,
) -> LabelModifyKeysParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input label file.
        remap_file: text file with old and new key values.
        label_out: output label file.
        opt_column_column: select a single column to use: the column number or\
            name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label-modify-keys",
        "label_in": label_in,
        "remap_file": remap_file,
        "label_out": label_out,
    }
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    return params


def label_modify_keys_cargs(
    params: LabelModifyKeysParameters,
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
    cargs.append("-label-modify-keys")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("remap_file"))
    cargs.append(params.get("label_out"))
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    return cargs


def label_modify_keys_outputs(
    params: LabelModifyKeysParameters,
    execution: Execution,
) -> LabelModifyKeysOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelModifyKeysOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
    )
    return ret


def label_modify_keys_execute(
    params: LabelModifyKeysParameters,
    execution: Execution,
) -> LabelModifyKeysOutputs:
    """
    Change key values in a label file.
    
    <remap-file> should have lines of the form 'oldkey newkey', like so:
    
    3 5
    5 8
    8 2
    
    This would change the current label with key '3' to use the key '5' instead,
    5 would use 8, and 8 would use 2. Any collision in key values results in the
    label that was not specified in the remap file getting remapped to an
    otherwise unused key. Remapping more than one key to the same new key, or
    the same key to more than one new key, results in an error. This will not
    change the appearance of the file when displayed, as it will change the key
    values in the data at the same time.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelModifyKeysOutputs`).
    """
    cargs = label_modify_keys_cargs(params, execution)
    ret = label_modify_keys_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_modify_keys(
    label_in: InputPathType,
    remap_file: str,
    label_out: str,
    opt_column_column: str | None = None,
    runner: Runner | None = None,
) -> LabelModifyKeysOutputs:
    """
    Change key values in a label file.
    
    <remap-file> should have lines of the form 'oldkey newkey', like so:
    
    3 5
    5 8
    8 2
    
    This would change the current label with key '3' to use the key '5' instead,
    5 would use 8, and 8 would use 2. Any collision in key values results in the
    label that was not specified in the remap file getting remapped to an
    otherwise unused key. Remapping more than one key to the same new key, or
    the same key to more than one new key, results in an error. This will not
    change the appearance of the file when displayed, as it will change the key
    values in the data at the same time.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input label file.
        remap_file: text file with old and new key values.
        label_out: output label file.
        opt_column_column: select a single column to use: the column number or\
            name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelModifyKeysOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MODIFY_KEYS_METADATA)
    params = label_modify_keys_params(label_in=label_in, remap_file=remap_file, label_out=label_out, opt_column_column=opt_column_column)
    return label_modify_keys_execute(params, execution)


__all__ = [
    "LABEL_MODIFY_KEYS_METADATA",
    "LabelModifyKeysOutputs",
    "LabelModifyKeysParameters",
    "label_modify_keys",
    "label_modify_keys_params",
]

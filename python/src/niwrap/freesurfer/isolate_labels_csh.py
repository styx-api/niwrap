# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ISOLATE_LABELS_CSH_METADATA = Metadata(
    id="38dc57e5ac2ab0f7a3569ce5a6d3b6708f167dad.boutiques",
    name="isolate_labels.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
IsolateLabelsCshParameters = typing.TypedDict('IsolateLabelsCshParameters', {
    "__STYX_TYPE__": typing.Literal["isolate_labels.csh"],
    "label_volume": InputPathType,
    "output_prefix": str,
    "lowercase_label_option": typing.NotRequired[str | None],
    "version": bool,
    "keepval": bool,
    "help": bool,
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
        "isolate_labels.csh": isolate_labels_csh_cargs,
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
    }.get(t)


class IsolateLabelsCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `isolate_labels_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def isolate_labels_csh_params(
    label_volume: InputPathType,
    output_prefix: str,
    lowercase_label_option: str | None = None,
    version: bool = False,
    keepval: bool = False,
    help_: bool = False,
) -> IsolateLabelsCshParameters:
    """
    Build parameters.
    
    Args:
        label_volume: Label volume to be analyzed.
        output_prefix: Prefix of binary label file(s).
        lowercase_label_option: The particular label to be analyzed; default is\
            all labels.
        version: Print version and exit.
        keepval: Keeps original label values.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "isolate_labels.csh",
        "label_volume": label_volume,
        "output_prefix": output_prefix,
        "version": version,
        "keepval": keepval,
        "help": help_,
    }
    if lowercase_label_option is not None:
        params["lowercase_label_option"] = lowercase_label_option
    return params


def isolate_labels_csh_cargs(
    params: IsolateLabelsCshParameters,
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
    cargs.append("isolate_labels")
    cargs.extend([
        "--vol",
        execution.input_file(params.get("label_volume"))
    ])
    cargs.extend([
        "--outprefix",
        params.get("output_prefix")
    ])
    if params.get("lowercase_label_option") is not None:
        cargs.extend([
            "--l",
            params.get("lowercase_label_option")
        ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("keepval"):
        cargs.append("--keepval")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def isolate_labels_csh_outputs(
    params: IsolateLabelsCshParameters,
    execution: Execution,
) -> IsolateLabelsCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IsolateLabelsCshOutputs(
        root=execution.output_file("."),
    )
    return ret


def isolate_labels_csh_execute(
    params: IsolateLabelsCshParameters,
    execution: Execution,
) -> IsolateLabelsCshOutputs:
    """
    Tool to separate out a particular or all labels into individual binary files for
    subsequent shape analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IsolateLabelsCshOutputs`).
    """
    cargs = isolate_labels_csh_cargs(params, execution)
    ret = isolate_labels_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def isolate_labels_csh(
    label_volume: InputPathType,
    output_prefix: str,
    lowercase_label_option: str | None = None,
    version: bool = False,
    keepval: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> IsolateLabelsCshOutputs:
    """
    Tool to separate out a particular or all labels into individual binary files for
    subsequent shape analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_volume: Label volume to be analyzed.
        output_prefix: Prefix of binary label file(s).
        lowercase_label_option: The particular label to be analyzed; default is\
            all labels.
        version: Print version and exit.
        keepval: Keeps original label values.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsolateLabelsCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISOLATE_LABELS_CSH_METADATA)
    params = isolate_labels_csh_params(label_volume=label_volume, output_prefix=output_prefix, lowercase_label_option=lowercase_label_option, version=version, keepval=keepval, help_=help_)
    return isolate_labels_csh_execute(params, execution)


__all__ = [
    "ISOLATE_LABELS_CSH_METADATA",
    "IsolateLabelsCshOutputs",
    "IsolateLabelsCshParameters",
    "isolate_labels_csh",
    "isolate_labels_csh_params",
]

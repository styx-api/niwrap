# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_RF_LONG_LABEL_METADATA = Metadata(
    id="06cc04cbd7f8fd46c1d7544632fa8c08486bcc37.boutiques",
    name="mri_rf_long_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriRfLongLabelParameters = typing.TypedDict('MriRfLongLabelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_rf_long_label"],
    "help_flag": typing.NotRequired[str | None],
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
        "mri_rf_long_label": mri_rf_long_label_cargs,
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


class MriRfLongLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rf_long_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_rf_long_label_params(
    help_flag: str | None = None,
) -> MriRfLongLabelParameters:
    """
    Build parameters.
    
    Args:
        help_flag: Displays a message that the tool has been removed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_rf_long_label",
    }
    if help_flag is not None:
        params["help_flag"] = help_flag
    return params


def mri_rf_long_label_cargs(
    params: MriRfLongLabelParameters,
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
    cargs.append("mri_rf_long_label")
    if params.get("help_flag") is not None:
        cargs.append(params.get("help_flag"))
    return cargs


def mri_rf_long_label_outputs(
    params: MriRfLongLabelParameters,
    execution: Execution,
) -> MriRfLongLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRfLongLabelOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_rf_long_label_execute(
    params: MriRfLongLabelParameters,
    execution: Execution,
) -> MriRfLongLabelOutputs:
    """
    The mri_rf_long_label tool has been removed from this version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRfLongLabelOutputs`).
    """
    cargs = mri_rf_long_label_cargs(params, execution)
    ret = mri_rf_long_label_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_rf_long_label(
    help_flag: str | None = None,
    runner: Runner | None = None,
) -> MriRfLongLabelOutputs:
    """
    The mri_rf_long_label tool has been removed from this version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        help_flag: Displays a message that the tool has been removed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRfLongLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RF_LONG_LABEL_METADATA)
    params = mri_rf_long_label_params(help_flag=help_flag)
    return mri_rf_long_label_execute(params, execution)


__all__ = [
    "MRI_RF_LONG_LABEL_METADATA",
    "MriRfLongLabelOutputs",
    "MriRfLongLabelParameters",
    "mri_rf_long_label",
    "mri_rf_long_label_params",
]

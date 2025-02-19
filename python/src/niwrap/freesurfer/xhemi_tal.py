# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

XHEMI_TAL_METADATA = Metadata(
    id="75297464bbd5b47449915f4f1464c80da7860766.boutiques",
    name="xhemi-tal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


XhemiTalParameters = typing.TypedDict('XhemiTalParameters', {
    "__STYX_TYPE__": typing.Literal["xhemi-tal"],
    "subject": str,
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
        "xhemi-tal": xhemi_tal_cargs,
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


class XhemiTalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xhemi_tal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def xhemi_tal_params(
    subject: str,
) -> XhemiTalParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject for which to compute the talairach.xfm.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "xhemi-tal",
        "subject": subject,
    }
    return params


def xhemi_tal_cargs(
    params: XhemiTalParameters,
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
    cargs.append("xhemi-tal")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    return cargs


def xhemi_tal_outputs(
    params: XhemiTalParameters,
    execution: Execution,
) -> XhemiTalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = XhemiTalOutputs(
        root=execution.output_file("."),
    )
    return ret


def xhemi_tal_execute(
    params: XhemiTalParameters,
    execution: Execution,
) -> XhemiTalOutputs:
    """
    Computes the talairach.xfm for xhemi based on the original (unflipped)
    talairach.xfm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `XhemiTalOutputs`).
    """
    params = execution.params(params)
    cargs = xhemi_tal_cargs(params, execution)
    ret = xhemi_tal_outputs(params, execution)
    execution.run(cargs)
    return ret


def xhemi_tal(
    subject: str,
    runner: Runner | None = None,
) -> XhemiTalOutputs:
    """
    Computes the talairach.xfm for xhemi based on the original (unflipped)
    talairach.xfm.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject for which to compute the talairach.xfm.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XhemiTalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XHEMI_TAL_METADATA)
    params = xhemi_tal_params(
        subject=subject,
    )
    return xhemi_tal_execute(params, execution)


__all__ = [
    "XHEMI_TAL_METADATA",
    "XhemiTalOutputs",
    "XhemiTalParameters",
    "xhemi_tal",
    "xhemi_tal_params",
]

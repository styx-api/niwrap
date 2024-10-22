# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

XHEMI_TAL_METADATA = Metadata(
    id="bc30c34e1ebc79ae0d807f2cf3a4be8d10e1fa6a.boutiques",
    name="xhemi-tal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class XhemiTalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xhemi_tal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


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
    cargs = []
    cargs.append("xhemi-tal")
    cargs.append("--s")
    cargs.extend([
        "--s",
        subject
    ])
    ret = XhemiTalOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XHEMI_TAL_METADATA",
    "XhemiTalOutputs",
    "xhemi_tal",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__TO_RAI_METADATA = Metadata(
    id="1a5cc8a5a702a9f62a7296e2f91329b3a241311d.boutiques",
    name="@ToRAI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VToRaiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__to_rai(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__to_rai(
    runner: Runner | None = None,
) -> VToRaiOutputs:
    """
    Tool to change the ORIENT coordinates to RAI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VToRaiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__TO_RAI_METADATA)
    cargs = []
    cargs.append("@ToRAI")
    cargs.append("<-xyz")
    cargs.append("X")
    cargs.append("Y")
    cargs.append("Z>")
    cargs.append("<-or")
    cargs.append("ORIENT>")
    ret = VToRaiOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VToRaiOutputs",
    "V__TO_RAI_METADATA",
    "v__to_rai",
]

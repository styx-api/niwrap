# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_ORIENT2_RAIMAP_METADATA = Metadata(
    id="ade1258888a2ab4d7104b72e6f2921d74eaf281c.boutiques",
    name="@AfniOrient2RAImap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VAfniOrient2RaimapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_orient2_raimap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__afni_orient2_raimap(
    orientation_code: str,
    runner: Runner | None = None,
) -> VAfniOrient2RaimapOutputs:
    """
    Returns the index map for the RAI directions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        orientation_code: Orientation code (e.g., RAI, LSP).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniOrient2RaimapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_ORIENT2_RAIMAP_METADATA)
    cargs = []
    cargs.append("@AfniOrient2RAImap")
    cargs.append(orientation_code)
    ret = VAfniOrient2RaimapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAfniOrient2RaimapOutputs",
    "V__AFNI_ORIENT2_RAIMAP_METADATA",
    "v__afni_orient2_raimap",
]

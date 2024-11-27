# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SUMA_MAKE_SPEC_FS_METADATA = Metadata(
    id="35abec1cbcc0a7c9a8b395b5a4855788850c3f95.boutiques",
    name="@SUMA_Make_Spec_FS",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VSumaMakeSpecFsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_make_spec_fs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    suma_output: OutputPathType
    """All created files are stored in a new SUMA directory"""


def v__suma_make_spec_fs(
    subject_id: str,
    runner: Runner | None = None,
) -> VSumaMakeSpecFsOutputs:
    """
    Prepare for surface viewing in SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        subject_id: Required subject ID for file naming.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecFsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_MAKE_SPEC_FS_METADATA)
    cargs = []
    cargs.append("@SUMA_Make_Spec_FS")
    cargs.append("[OPTIONS]")
    cargs.extend([
        "-sid",
        subject_id
    ])
    ret = VSumaMakeSpecFsOutputs(
        root=execution.output_file("."),
        suma_output=execution.output_file("SUMA/*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSumaMakeSpecFsOutputs",
    "V__SUMA_MAKE_SPEC_FS_METADATA",
    "v__suma_make_spec_fs",
]

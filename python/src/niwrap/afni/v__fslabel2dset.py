# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__FSLABEL2DSET_METADATA = Metadata(
    id="0a20d4c58cd9ad690928488e00aca48f5beff08a.boutiques",
    name="@FSlabel2dset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VFslabel2dsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fslabel2dset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__fslabel2dset(
    fs_label_file: InputPathType,
    val: float | None = None,
    help_: bool = False,
    echo: bool = False,
    keep_tmp: bool = False,
    runner: Runner | None = None,
) -> VFslabel2dsetOutputs:
    """
    A script to convert a FreeSurfer ASCII label file into a SUMA dataset and a SUMA
    ROI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fs_label_file: Specify the ASCII label file from FreeSurfer.
        val: Assign integer VAL to the nodes in FS_LABEL_FILE (Default is 1).
        help_: Display help message.
        echo: Turn echo for debugging.
        keep_tmp: Don't cleanup temp files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFslabel2dsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FSLABEL2DSET_METADATA)
    cargs = []
    cargs.append("@FSlabel2dset")
    cargs.extend([
        "-fs",
        execution.input_file(fs_label_file)
    ])
    if val is not None:
        cargs.extend([
            "-val",
            str(val)
        ])
    if help_:
        cargs.append("-help")
    if echo:
        cargs.append("-echo")
    if keep_tmp:
        cargs.append("-keep_tmp")
    ret = VFslabel2dsetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VFslabel2dsetOutputs",
    "V__FSLABEL2DSET_METADATA",
    "v__fslabel2dset",
]

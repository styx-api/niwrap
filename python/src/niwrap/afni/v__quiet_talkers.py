# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__QUIET_TALKERS_METADATA = Metadata(
    id="b3ed968e44cf181f4b5122510d5d661ee6ef707c.boutiques",
    name="@Quiet_Talkers",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VQuietTalkersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__quiet_talkers(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__quiet_talkers(
    sudo: bool = False,
    prog: list[str] | None = None,
    npb_val: list[float] | None = None,
    npb_range: list[float] | None = None,
    pif_key: str | None = None,
    no_npb: bool = False,
    list_: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> VQuietTalkersOutputs:
    """
    A script to find and kill AFNI processes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        sudo: Invoke higher powers to kill processes that you do not own.
        prog: Instead of the default program list, only kill the specified\
            program. You can use multiple -prog options.
        npb_val: Kill those programs using NIML port block NV.
        npb_range: Kill those using NIML port blocks between NV0 and NV1.
        pif_key: Kill those programs that have a string matching KEY_STRING in\
            their commandline.
        no_npb: Kill any program in the list regardless of -npb options or -pif.
        list_: Just list process numbers, don't run kill command.
        quiet: Do it quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VQuietTalkersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__QUIET_TALKERS_METADATA)
    cargs = []
    cargs.append("@Quiet_Talkers")
    if sudo:
        cargs.append("-sudo")
    if prog is not None:
        cargs.extend([
            "-prog",
            *prog
        ])
    if npb_val is not None:
        cargs.extend([
            "-npb_val",
            *map(str, npb_val)
        ])
    if npb_range is not None:
        cargs.extend([
            "-npb_range",
            *map(str, npb_range)
        ])
    if pif_key is not None:
        cargs.extend([
            "-pif",
            pif_key
        ])
    if no_npb:
        cargs.append("-no_npb")
    if list_:
        cargs.append("-list")
    if quiet:
        cargs.append("-quiet")
    ret = VQuietTalkersOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VQuietTalkersOutputs",
    "V__QUIET_TALKERS_METADATA",
    "v__quiet_talkers",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_PROBE_IMA_METADATA = Metadata(
    id="18584d90b4496e803d7fee551923ca13a88acf1a.boutiques",
    name="mri_probe_ima",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriProbeImaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_probe_ima(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_probe_ima(
    ima_file: InputPathType,
    key_string: str | None = None,
    offset_type_len: str | None = None,
    attribute_name: str | None = None,
    fileinfo: bool = False,
    dictionary: bool = False,
    ob_stem: str | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriProbeImaOutputs:
    """
    Query Siemens IMA files to extract header information.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        ima_file: Path to the IMA file to be probed.
        key_string: String from dictionary to query the IMA file.
        offset_type_len: Offset, type, and string length for querying. Type can\
            be short, int, long, float, double, or string.
        attribute_name: Name of the file information attribute to query.
        fileinfo: Dump the interpreted file information.
        dictionary: Dump the dictionary without the need of an IMA file.
        ob_stem: Dump binary pixel data into bshort with stem prefix.
        help_: Show help message and exit.
        version: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriProbeImaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PROBE_IMA_METADATA)
    cargs = []
    cargs.append("mri_probe_ima")
    cargs.append("--i")
    cargs.extend([
        "--i",
        execution.input_file(ima_file)
    ])
    if key_string is not None:
        cargs.extend([
            "--key",
            key_string
        ])
    if offset_type_len is not None:
        cargs.extend([
            "--o",
            offset_type_len
        ])
    if attribute_name is not None:
        cargs.extend([
            "--attr",
            attribute_name
        ])
    if fileinfo:
        cargs.append("--fileinfo")
    if dictionary:
        cargs.append("--dictionary")
    if ob_stem is not None:
        cargs.extend([
            "--ob",
            ob_stem
        ])
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = MriProbeImaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_PROBE_IMA_METADATA",
    "MriProbeImaOutputs",
    "mri_probe_ima",
]

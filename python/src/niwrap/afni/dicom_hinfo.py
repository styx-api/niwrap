# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DICOM_HINFO_METADATA = Metadata(
    id="5ea1bb33f7ee89c2be57f4fd42ad48d1af53ccde.boutiques",
    name="dicom_hinfo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class DicomHinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dicom_hinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dicom_hinfo(
    tag: list[str],
    sepstr: str | None = None,
    full_entry: bool = False,
    no_name: bool = False,
    namelast: bool = False,
    runner: Runner | None = None,
) -> DicomHinfoOutputs:
    """
    Prints selected information from one or more DICOM files to stdout.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/dicom_hinfo.html
    
    Args:
        tag: Specify one or more DICOM tags to print, in the format aaaa,bbbb\
            where aaaa and bbbb are hexadecimal digits.
        sepstr: Use the specified string to separate fields instead of space.
        full_entry: Output the full entry if it is more than one word or\
            contains white space.
        no_name: Omit the filename from the output.
        namelast: Place the filename last in the output instead of first.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DicomHinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DICOM_HINFO_METADATA)
    cargs = []
    cargs.append("dicom_hinfo")
    cargs.extend([
        "-tag",
        *tag
    ])
    if sepstr is not None:
        cargs.extend([
            "-sepstr",
            sepstr
        ])
    if full_entry:
        cargs.append("-full_entry")
    if no_name:
        cargs.append("-no_name")
    if namelast:
        cargs.append("-namelast")
    cargs.append("[FILES...]")
    ret = DicomHinfoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DICOM_HINFO_METADATA",
    "DicomHinfoOutputs",
    "dicom_hinfo",
]

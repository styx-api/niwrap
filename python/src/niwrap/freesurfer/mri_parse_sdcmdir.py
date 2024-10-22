# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_PARSE_SDCMDIR_METADATA = Metadata(
    id="f3d470b7a78fa0f268a69d903a640c95fe56c7b9.boutiques",
    name="mri_parse_sdcmdir",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriParseSdcmdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_parse_sdcmdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_parse_sdcmdir(
    sdicomdir: str,
    outfile: str | None = None,
    sortbyrun: bool = False,
    summarize: bool = False,
    dwi: bool = False,
    runner: Runner | None = None,
) -> MriParseSdcmdirOutputs:
    """
    This program parses the Siemens DICOM files in a given directory and prints out
    information about each file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        sdicomdir: Path to Siemens DICOM directory.
        outfile: Name of a file to which the results will be printed. If\
            unspecified, the results will be printed to stdout.
        sortbyrun: Assign run numbers.
        summarize: Only print out info for run leaders.
        dwi: Try to read DWI params. Generally no need to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriParseSdcmdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PARSE_SDCMDIR_METADATA)
    cargs = []
    cargs.append("mri_parse_sdcmdir")
    cargs.extend([
        "--d",
        sdicomdir
    ])
    if outfile is not None:
        cargs.extend([
            "--o",
            outfile
        ])
    if sortbyrun:
        cargs.append("--sortbyrun")
    if summarize:
        cargs.append("--summarize")
    if dwi:
        cargs.append("--dwi")
    ret = MriParseSdcmdirOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_PARSE_SDCMDIR_METADATA",
    "MriParseSdcmdirOutputs",
    "mri_parse_sdcmdir",
]

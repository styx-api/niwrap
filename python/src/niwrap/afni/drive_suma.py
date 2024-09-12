# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DRIVE_SUMA_METADATA = Metadata(
    id="8732e38f8accb3657c2bb8658171028fb32be588.boutiques",
    name="DriveSuma",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class DriveSumaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `drive_suma(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def drive_suma(
    command: str,
    runner: Runner | None = None,
) -> DriveSumaOutputs:
    """
    A program to drive suma from the command line.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/DriveSuma.html
    
    Args:
        command: Command to be sent to SUMA.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DriveSumaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DRIVE_SUMA_METADATA)
    cargs = []
    cargs.append("DriveSuma")
    cargs.append("[INPUT_FILE]")
    cargs.append("-com")
    cargs.append(command)
    cargs.append("[ADDITIONAL_OPTIONS]")
    ret = DriveSumaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DRIVE_SUMA_METADATA",
    "DriveSumaOutputs",
    "drive_suma",
]

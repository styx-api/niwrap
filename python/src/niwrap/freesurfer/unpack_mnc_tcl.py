# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

UNPACK_MNC_TCL_METADATA = Metadata(
    id="9464bf0c600c04854f668e4f01ddfe8905579dac.boutiques",
    name="unpack_mnc.tcl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class UnpackMncTclOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpack_mnc_tcl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unpacked_file: OutputPathType
    """Unpacked output MINC file"""


def unpack_mnc_tcl(
    runner: Runner | None = None,
) -> UnpackMncTclOutputs:
    """
    A tool for unpacking MINC format images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpackMncTclOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACK_MNC_TCL_METADATA)
    cargs = []
    cargs.append("unpack_mnc.tcl")
    cargs.append("[OPTIONS]")
    ret = UnpackMncTclOutputs(
        root=execution.output_file("."),
        unpacked_file=execution.output_file("[OUTPUT_DIR]/unpacked_data.mnc"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UNPACK_MNC_TCL_METADATA",
    "UnpackMncTclOutputs",
    "unpack_mnc_tcl",
]

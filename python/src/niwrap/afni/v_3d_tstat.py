# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TSTAT_METADATA = Metadata(
    id="a37fc104f95cef6830f8819a559beddc088d9c89.boutiques",
    name="3dTstat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_tstat(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    options: str | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    runner: Runner | None = None,
) -> V3dTstatOutputs:
    """
    Compute voxel-wise statistics using AFNI 3dTstat command.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTstat.html
    
    Args:
        in_file: Input file to 3dtstat.
        mask: Mask file.
        options: Selected statistical output.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TSTAT_METADATA)
    cargs = []
    cargs.append("3dTstat")
    cargs.append(execution.input_file(in_file))
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if options is not None:
        cargs.append(options)
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dTstatOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(in_file).name + "_tstat"),
        out_file_=execution.output_file("out_file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTstatOutputs",
    "V_3D_TSTAT_METADATA",
    "v_3d_tstat",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DVOLREG_METADATA = Metadata(
    id="5cc2663dc96c9972a79c75185488f6362ed7420f.boutiques",
    name="3dvolreg",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dvolregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dvolreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    md1d_file: OutputPathType
    """Max displacement output file."""
    oned_file: OutputPathType
    """1d movement parameters output file."""
    oned_matrix_save: OutputPathType
    """Save the matrix transformation."""
    out_file: OutputPathType
    """Output image file name."""
    md1d_file_: OutputPathType
    """Max displacement info file."""
    oned_file_: OutputPathType
    """Movement parameters info file."""
    oned_matrix_save_: OutputPathType
    """Matrix transformation from base to input."""
    out_file_: OutputPathType
    """Registered file."""


def v_3dvolreg(
    in_file: InputPathType,
    basefile: InputPathType | None = None,
    zpad: int | None = None,
    copyorigin: bool = False,
    in_weight_volume_2: InputPathType | None = None,
    interp: typing.Literal["Fourier", "cubic", "heptic", "quintic", "linear"] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    timeshift: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dvolregOutputs:
    """
    Register input volumes to a base volume using AFNI 3dvolreg command.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dvolreg.html
    
    Args:
        in_file: Input file to 3dvolreg.
        basefile: Base file for registration.
        zpad: Zeropad around the edges by 'n' voxels during rotations.
        copyorigin: Copy base file origin coords to output.
        in_weight_volume_2: (file or string, an integer) or file or string.\
            Weights for each voxel specified by a file with an optional volume\
            number (defaults to 0).
        interp: 'fourier' or 'cubic' or 'heptic' or 'quintic' or 'linear'.\
            Spatial interpolation methods [default = heptic].
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        timeshift: Time shift to mean slice time offset.
        verbose: More detailed description of the process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dvolregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DVOLREG_METADATA)
    cargs = []
    cargs.append("3dvolreg")
    if basefile is not None:
        cargs.extend([
            "-base",
            execution.input_file(basefile)
        ])
    if zpad is not None:
        cargs.extend([
            "-zpad",
            str(zpad)
        ])
    cargs.append("[MD1D_FILE]")
    cargs.append(execution.input_file(in_file))
    if copyorigin:
        cargs.append("-twodup")
    if in_weight_volume_2 is not None:
        cargs.extend([
            "-weight '",
            execution.input_file(in_weight_volume_2)
        ])
    if interp is not None:
        cargs.extend([
            "-",
            interp
        ])
    cargs.append("[ONED_FILE]")
    cargs.append("[ONED_MATRIX_SAVE]")
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if timeshift:
        cargs.append("-tshift 0")
    if verbose:
        cargs.append("-verbose")
    ret = V3dvolregOutputs(
        root=execution.output_file("."),
        md1d_file=execution.output_file(pathlib.Path(in_file).name + "_md.1D"),
        oned_file=execution.output_file(pathlib.Path(in_file).name + ".1D"),
        oned_matrix_save=execution.output_file(pathlib.Path(in_file).name + ".aff12.1D"),
        out_file=execution.output_file(pathlib.Path(in_file).name + "_volreg"),
        md1d_file_=execution.output_file("md1d_file"),
        oned_file_=execution.output_file("oned_file"),
        oned_matrix_save_=execution.output_file("oned_matrix_save"),
        out_file_=execution.output_file("out_file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dvolregOutputs",
    "V_3DVOLREG_METADATA",
    "v_3dvolreg",
]

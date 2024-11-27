# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_LONG_NORMALIZE_METADATA = Metadata(
    id="50792d90ec13a1b27d5ecb59aea01240f09a6b39.boutiques",
    name="mri_long_normalize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriLongNormalizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_long_normalize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output MRI volume file."""


def mri_long_normalize(
    input_vol: InputPathType,
    base_tp_file: InputPathType,
    output_vol: str,
    normalization_iters: int | None = None,
    disable_1d: bool = False,
    smooth_bias: float | None = None,
    aseg: InputPathType | None = None,
    debug_gvx: list[float] | None = None,
    debug_gx: list[float] | None = None,
    reading: list[str] | None = None,
    print_usage: bool = False,
    runner: Runner | None = None,
) -> MriLongNormalizeOutputs:
    """
    Tool to normalize the white-matter of MRI volumes, optionally based on control
    points.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input MRI volume file.
        base_tp_file: Base time point file.
        output_vol: Output MRI volume file.
        normalization_iters: Use n 3D normalization iterations (default is 2).
        disable_1d: Disable 1D normalization.
        smooth_bias: Smooth the bias field.
        aseg: Aseg file specification.
        debug_gvx: For debugging: specify Gvx, Gvy, Gvz.
        debug_gx: For debugging: specify Gx, Gy, Gz.
        reading: For reading: specify control points and bias field.
        print_usage: Print usage information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriLongNormalizeOutputs`).
    """
    if reading is not None and (len(reading) != 2): 
        raise ValueError(f"Length of 'reading' must be 2 but was {len(reading)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_LONG_NORMALIZE_METADATA)
    cargs = []
    cargs.append("mri_long_normalize")
    cargs.append(execution.input_file(input_vol))
    cargs.append(execution.input_file(base_tp_file))
    cargs.append(output_vol)
    if normalization_iters is not None:
        cargs.extend([
            "-n",
            str(normalization_iters)
        ])
    if disable_1d:
        cargs.append("-no1d")
    if smooth_bias is not None:
        cargs.extend([
            "-sigma",
            str(smooth_bias)
        ])
    if aseg is not None:
        cargs.extend([
            "-a",
            execution.input_file(aseg)
        ])
    if debug_gvx is not None:
        cargs.extend([
            "-v",
            *map(str, debug_gvx)
        ])
    if debug_gx is not None:
        cargs.extend([
            "-d",
            *map(str, debug_gx)
        ])
    if reading is not None:
        cargs.extend([
            "-r",
            *reading
        ])
    if print_usage:
        cargs.append("-u")
    ret = MriLongNormalizeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_vol),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_LONG_NORMALIZE_METADATA",
    "MriLongNormalizeOutputs",
    "mri_long_normalize",
]

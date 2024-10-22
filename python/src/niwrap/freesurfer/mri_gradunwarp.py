# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_GRADUNWARP_METADATA = Metadata(
    id="31e06eb21eb3eb1926aa92ac10dc09ee2ef8736d.boutiques",
    name="mri_gradunwarp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriGradunwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gradunwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unwarped_output: OutputPathType | None
    """Unwarped output volume or surface"""
    output_transform_table: OutputPathType | None
    """Saved unwarp transform table in m3z format"""


def mri_gradunwarp(
    input_file: InputPathType,
    gradient_coeff: InputPathType | None = None,
    load_transtbl: InputPathType | None = None,
    output_file: str | None = None,
    out_transtbl: str | None = None,
    save_transtbl_only: bool = False,
    interpolation_type: str | None = "trilinear",
    nthreads: float | None = None,
    checkopts: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriGradunwarpOutputs:
    """
    Tool to correct gradient non-linearity distortions in MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input warped volume or surface.
        gradient_coeff: Gradient coefficient input file (not to be used with\
            --load_transtbl).
        load_transtbl: Load unwarp transform table in m3z format (not to be\
            used with --gradcoeff).
        output_file: Output unwarped volume or surface.
        out_transtbl: Save unwarp transform table in m3z format.
        save_transtbl_only: Just save unwarp transform table in m3z format,\
            requires --gradcoeff.
        interpolation_type: Interpolation method: nearest | trilinear | cubic\
            (default is trilinear).
        nthreads: Number of threads to run.
        checkopts: Don't run anything, just check options and exit.
        version: Print out version and exit.
        help_: Print out information on how to use this program.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGradunwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GRADUNWARP_METADATA)
    cargs = []
    cargs.append("mri_gradunwarp")
    if gradient_coeff is not None:
        cargs.extend([
            "--gradcoeff",
            execution.input_file(gradient_coeff)
        ])
    if load_transtbl is not None:
        cargs.extend([
            "--load_transtbl",
            execution.input_file(load_transtbl)
        ])
    cargs.extend([
        "--i",
        execution.input_file(input_file)
    ])
    if output_file is not None:
        cargs.extend([
            "--o",
            output_file
        ])
    if out_transtbl is not None:
        cargs.extend([
            "--out_transtbl",
            out_transtbl
        ])
    if save_transtbl_only:
        cargs.append("--save_transtbl_only")
    if interpolation_type is not None:
        cargs.extend([
            "--interp",
            interpolation_type
        ])
    if nthreads is not None:
        cargs.extend([
            "--nthreads",
            str(nthreads)
        ])
    if checkopts:
        cargs.append("--checkopts")
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = MriGradunwarpOutputs(
        root=execution.output_file("."),
        unwarped_output=execution.output_file(output_file) if (output_file is not None) else None,
        output_transform_table=execution.output_file(out_transtbl) if (out_transtbl is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_GRADUNWARP_METADATA",
    "MriGradunwarpOutputs",
    "mri_gradunwarp",
]

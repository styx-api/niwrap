# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DANISOSMOOTH_METADATA = Metadata(
    id="f9ebe5fa3b013bdcb909e178c9093254c20aada2.boutiques",
    name="3danisosmooth",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3danisosmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3danisosmooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset after anisotropic smoothing"""
    gradient_data: OutputPathType
    """Gradient dataset saved at each iteration"""
    eigens_data: OutputPathType
    """Eigens dataset saved at each iteration"""
    phi_data: OutputPathType
    """Phi dataset saved at each iteration"""
    dtensor_data: OutputPathType
    """Dtensor dataset saved at each iteration"""
    ematrix_data: OutputPathType
    """Ematrix dataset saved at the first sub-brick iteration"""
    flux_data: OutputPathType
    """Flux dataset saved at the first sub-brick iteration"""
    gmatrix_data: OutputPathType
    """Gmatrix dataset saved at the first sub-brick iteration"""
    diff_measures_data: OutputPathType
    """Dataset containing FA, MD, Cl, Cp, and Cs values saved at each
    iteration"""


def v_3danisosmooth(
    input_dataset: InputPathType,
    runner: Runner | None = None,
) -> V3danisosmoothOutputs:
    """
    Smooths a dataset using an anisotropic smoothing technique.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3danisosmooth.html
    
    Args:
        input_dataset: Input dataset to be smoothed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3danisosmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DANISOSMOOTH_METADATA)
    cargs = []
    cargs.append("3danisosmooth")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_dataset))
    ret = V3danisosmoothOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("[PREFIX]+smooth"),
        gradient_data=execution.output_file("Gradient.ITER"),
        eigens_data=execution.output_file("Eigens.ITER"),
        phi_data=execution.output_file("phi.ITER"),
        dtensor_data=execution.output_file("Dtensor.ITER"),
        ematrix_data=execution.output_file("Ematrix.ITER"),
        flux_data=execution.output_file("Flux.ITER"),
        gmatrix_data=execution.output_file("Gmatrix.ITER"),
        diff_measures_data=execution.output_file("Diff_measures.ITER"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3danisosmoothOutputs",
    "V_3DANISOSMOOTH_METADATA",
    "v_3danisosmooth",
]

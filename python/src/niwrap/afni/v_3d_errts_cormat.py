# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ERRTS_CORMAT_METADATA = Metadata(
    id="041ce1cbe7030e9af02420caf899590e04d99081.boutiques",
    name="3dErrtsCormat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dErrtsCormatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_errts_cormat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """1D file of the Toeplitz entries."""


def v_3d_errts_cormat(
    dset: InputPathType,
    runner: Runner | None = None,
) -> V3dErrtsCormatOutputs:
    """
    Computes the correlation matrix corresponding to the residual (or error) time
    series in 'dset'.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dErrtsCormat.html
    
    Args:
        dset: Dataset to read, usually the '-errts' output from 3dDeconvolve.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dErrtsCormatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ERRTS_CORMAT_METADATA)
    cargs = []
    cargs.append("3dErrtsCormat")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dset))
    ret = V3dErrtsCormatOutputs(
        root=execution.output_file("."),
        output=execution.output_file("stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dErrtsCormatOutputs",
    "V_3D_ERRTS_CORMAT_METADATA",
    "v_3d_errts_cormat",
]

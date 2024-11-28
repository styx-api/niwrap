# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_DWITO_DT_METADATA = Metadata(
    id="edef0edb2012159a76d51a09912a5bd6c5660ab2.boutiques",
    name="3dDWItoDT",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dDwitoDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dwito_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset"""


def v_3d_dwito_dt(
    gradient_file: InputPathType,
    dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dDwitoDtOutputs:
    """
    Computes 6 principal direction tensors from multiple gradient vectors and
    corresponding DTI image volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        gradient_file: A 1D file of the gradient vectors with lines of ASCII\
            floats (Gxi, Gyi, Gzi) or a 1D file of b-matrix elements.
        dataset: A 3D bucket dataset with Np+1 sub-briks where the first\
            sub-brik is the volume acquired with no diffusion weighting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDwitoDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DWITO_DT_METADATA)
    cargs = []
    cargs.append("3dDWItoDT")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(gradient_file))
    cargs.append(execution.input_file(dataset))
    ret = V3dDwitoDtOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("<PREFIX>.*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDwitoDtOutputs",
    "V_3D_DWITO_DT_METADATA",
    "v_3d_dwito_dt",
]

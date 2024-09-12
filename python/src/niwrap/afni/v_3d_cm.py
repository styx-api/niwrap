# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_CM_METADATA = Metadata(
    id="7736e53f66b944167dbd4d619f8ddc3f036d05f9.boutiques",
    name="3dCM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dCmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_cm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    center_of_mass: OutputPathType
    """Center of mass of the dataset."""


def v_3d_cm(
    dset: InputPathType,
    runner: Runner | None = None,
) -> V3dCmOutputs:
    """
    Tool for computing the center of mass of a dataset.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dCM.html
    
    Args:
        dset: Input dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dCmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CM_METADATA)
    cargs = []
    cargs.append("3dCM")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dset))
    ret = V3dCmOutputs(
        root=execution.output_file("."),
        center_of_mass=execution.output_file("<stdout>"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dCmOutputs",
    "V_3D_CM_METADATA",
    "v_3d_cm",
]

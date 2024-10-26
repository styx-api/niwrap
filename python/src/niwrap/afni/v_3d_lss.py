# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LSS_METADATA = Metadata(
    id="d9d964f3581d7546843bb8930c57337b07b0140b.boutiques",
    name="3dLSS",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dLssOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lss(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset containing the LSS estimates of the beta weights for the
    '-stim_times_IM' stimuli."""
    save1_d_output: OutputPathType
    """Estimator vectors saved in a 1D formatted file."""


def v_3d_lss(
    runner: Runner | None = None,
) -> V3dLssOutputs:
    """
    Least-Squares-Sum (LSS) estimation tool from a -stim_times_IM matrix for
    multivoxel pattern classification analyses.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLssOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LSS_METADATA)
    cargs = []
    cargs.append("3dLSS")
    cargs.append("[OPTIONS]")
    ret = V3dLssOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("LSSout+orig.HEAD"),
        save1_d_output=execution.output_file("[QQQ]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLssOutputs",
    "V_3D_LSS_METADATA",
    "v_3d_lss",
]

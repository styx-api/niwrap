# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SMOOTH_ESTIMATE_METADATA = Metadata(
    id="db35730728549b322353980c7c4f80e9b60ca48e.boutiques",
    name="SmoothEstimate",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SmoothEstimateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smooth_estimate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    res_volume: OutputPathType | None
    """Residual fit image"""
    zstat_volume: OutputPathType | None
    """Zstat image"""


def smooth_estimate(
    mask_file: InputPathType,
    dof: int | None = None,
    residual_fit_file: InputPathType | None = None,
    zstat_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> SmoothEstimateOutputs:
    """
    Estimates the smoothness of an image.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    Args:
        mask_file: Brain mask volume.
        dof: Number of degrees of freedom.
        residual_fit_file: Residual-fit image file.
        zstat_file: Zstat image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SmoothEstimateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SMOOTH_ESTIMATE_METADATA)
    cargs = []
    cargs.append("smoothest")
    if dof is not None:
        cargs.append("--dof=" + str(dof))
    cargs.append("--mask=" + execution.input_file(mask_file))
    if residual_fit_file is not None:
        cargs.append("--res=" + execution.input_file(residual_fit_file))
    if zstat_file is not None:
        cargs.append("--zstat=" + execution.input_file(zstat_file))
    ret = SmoothEstimateOutputs(
        root=execution.output_file("."),
        res_volume=execution.output_file(pathlib.Path(residual_fit_file).name) if (residual_fit_file is not None) else None,
        zstat_volume=execution.output_file(pathlib.Path(zstat_file).name) if (zstat_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SMOOTH_ESTIMATE_METADATA",
    "SmoothEstimateOutputs",
    "smooth_estimate",
]

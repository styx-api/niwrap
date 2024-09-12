# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_INFLATION_METADATA = Metadata(
    id="e150331abc2dc987286543f4111c1444aa76fe0d.boutiques",
    name="surface-inflation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceInflationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_inflation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """output surface file"""


def surface_inflation(
    anatomical_surface_in: InputPathType,
    surface_in: InputPathType,
    number_of_smoothing_cycles: int,
    smoothing_strength: float,
    smoothing_iterations: int,
    inflation_factor: float,
    surface_out: str,
    runner: Runner | None = None,
) -> SurfaceInflationOutputs:
    """
    Surface inflation.
    
    Inflate a surface by performing cycles that consist of smoothing followed by
    inflation (to correct shrinkage caused by smoothing).
    
    Author: Washington University School of Medicin
    
    Args:
        anatomical_surface_in: the anatomical surface.
        surface_in: the surface file to inflate.
        number_of_smoothing_cycles: number of smoothing cycles.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        inflation_factor: inflation factor.
        surface_out: output surface file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceInflationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_INFLATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-inflation")
    cargs.append(execution.input_file(anatomical_surface_in))
    cargs.append(execution.input_file(surface_in))
    cargs.append(str(number_of_smoothing_cycles))
    cargs.append(str(smoothing_strength))
    cargs.append(str(smoothing_iterations))
    cargs.append(str(inflation_factor))
    cargs.append(surface_out)
    ret = SurfaceInflationOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(surface_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_INFLATION_METADATA",
    "SurfaceInflationOutputs",
    "surface_inflation",
]

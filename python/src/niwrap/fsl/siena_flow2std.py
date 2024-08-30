# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SIENA_FLOW2STD_METADATA = Metadata(
    id="5c1a16e6112cdc424ccf2cc9d634a11727d98160",
    name="siena_flow2std",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class SienaFlow2stdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `siena_flow2std(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def siena_flow2std(
    fileroot1: str,
    fileroot2: str,
    sigma: float | int | None = 5,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> SienaFlow2stdOutputs:
    """
    siena_flow2std by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Convert edge flow to standard space.
    
    Args:
        fileroot1: Input file root 1.
        fileroot2: Input file root 2.
        sigma: Spatial smoothing of standard-space edge-flow image, sigma\
            (HWHM) in mm (default=5).
        debug_flag: Debug (don't delete intermediate files).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaFlow2stdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_FLOW2STD_METADATA)
    cargs = []
    cargs.append("siena_flow2std")
    cargs.append(fileroot1)
    cargs.append(fileroot2)
    if sigma is not None:
        cargs.extend(["-s", str(sigma)])
    if debug_flag:
        cargs.append("-d")
    ret = SienaFlow2stdOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIENA_FLOW2STD_METADATA",
    "SienaFlow2stdOutputs",
    "siena_flow2std",
]

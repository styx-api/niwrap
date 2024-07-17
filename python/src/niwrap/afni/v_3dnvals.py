# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DNVALS_METADATA = Metadata(
    id="faec4e4aff03ee276c5bc420f0ab234faca97907",
    name="3dnvals",
)


class V3dnvalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dnvals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dnvals(
    datasets: list[InputPathType],
    all_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> V3dnvalsOutputs:
    """
    3dnvals by AFNI.
    
    Tool to print the number of sub-bricks in a 3D dataset.
    
    More information: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Input 3D dataset(s).
        all_flag: Print out all 4 dimensions: Nx, Ny, Nz, Nvals.
        verbose_flag: Print the header name of the dataset first.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dnvalsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DNVALS_METADATA)
    cargs = []
    cargs.append("3dnvals")
    if all_flag:
        cargs.append("-all")
    if verbose_flag:
        cargs.append("-verbose")
    cargs.extend([execution.input_file(f) for f in datasets])
    ret = V3dnvalsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dnvalsOutputs",
    "V_3DNVALS_METADATA",
    "v_3dnvals",
]

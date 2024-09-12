# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FDRVAL_METADATA = Metadata(
    id="d7b752bd6acda76625f2e0880f59f3c2a7a453be.boutiques",
    name="fdrval",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FdrvalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fdrval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """Computed q-values or p-values for the given thresholds"""


def fdrval(
    dset: InputPathType,
    sub: float,
    val_list: list[float],
    runner: Runner | None = None,
) -> FdrvalOutputs:
    """
    Computes q-values from FDR curve data stored in dataset headers.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/fdrval.html
    
    Args:
        dset: Input dataset.
        sub: Sub-brick number.
        val_list: List of threshold values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FdrvalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FDRVAL_METADATA)
    cargs = []
    cargs.append("fdrval")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dset))
    cargs.append(str(sub))
    cargs.extend(map(str, val_list))
    ret = FdrvalOutputs(
        root=execution.output_file("."),
        output=execution.output_file("stdout.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FDRVAL_METADATA",
    "FdrvalOutputs",
    "fdrval",
]

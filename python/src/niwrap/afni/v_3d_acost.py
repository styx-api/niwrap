# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ACOST_METADATA = Metadata(
    id="0ff6573e114cd6d142c6db98eac6125eecf4d8dc.boutiques",
    name="3dAcost",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dAcostOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_acost(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType
    """Output aligned dataset (HEAD file)"""
    output_brik: OutputPathType
    """Output aligned dataset (BRIK file)"""


def v_3d_acost(
    infile: InputPathType,
    basefile: InputPathType,
    outfile: str,
    all_cost: bool = False,
    runner: Runner | None = None,
) -> V3dAcostOutputs:
    """
    Allineate dataset to a base dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input dataset for allineation.
        basefile: Base dataset for allineation.
        outfile: Prefix for the output dataset.
        all_cost: Prints all alignment cost metrics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAcostOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ACOST_METADATA)
    cargs = []
    cargs.append("3dAcost")
    cargs.append(execution.input_file(infile))
    cargs.extend([
        "-base",
        execution.input_file(basefile)
    ])
    cargs.extend([
        "-prefix",
        outfile
    ])
    if all_cost:
        cargs.append("-allcostX")
    ret = V3dAcostOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(outfile + "+orig.HEAD"),
        output_brik=execution.output_file(outfile + "+orig.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAcostOutputs",
    "V_3D_ACOST_METADATA",
    "v_3d_acost",
]

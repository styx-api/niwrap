# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SUMA_ACKNOWLEDGE_METADATA = Metadata(
    id="d037b40d3b42a963ac007ed6a05e2db450974d09.boutiques",
    name="@suma_acknowledge",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VSumaAcknowledgeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_acknowledge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output graph dataset"""


def v__suma_acknowledge(
    input_file: InputPathType,
    surface_file: InputPathType,
    output_prefix: str,
    center_flag: bool = False,
    subsurface_file: str | None = None,
    scale_factor: float | None = None,
    reduce_factor: float | None = None,
    runner: Runner | None = None,
) -> VSumaAcknowledgeOutputs:
    """
    Demo script to create a graph dataset to show names of individuals and groups,
    potentially useful for acknowledgements in a talk.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Required input text file with format for each line: first\
            last groupname.
        surface_file: Required surface to place nodes.
        output_prefix: Output prefix for graph dataset.
        center_flag: Put center coord at x,y,z=0,0,0. Otherwise, uses average\
            xyz in surface.
        subsurface_file: Surface for surrounding members of group (use ld2,\
            ld4, ld5, ld6, .... default is ld5).
        scale_factor: Scale xyz for group nodes (default is 1.0).
        reduce_factor: Scale xyz offsets for member nodes (xyz/r), default is\
            10.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaAcknowledgeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_ACKNOWLEDGE_METADATA)
    cargs = []
    cargs.append("@suma_acknowledge")
    cargs.append("-input")
    cargs.append(execution.input_file(input_file))
    cargs.append("-surf")
    cargs.append(execution.input_file(surface_file))
    cargs.append("-prefix")
    cargs.append(output_prefix)
    if center_flag:
        cargs.append("-center")
    if subsurface_file is not None:
        cargs.extend([
            "-subsurf",
            subsurface_file
        ])
    if scale_factor is not None:
        cargs.extend([
            "-scalefactor",
            str(scale_factor)
        ])
    if reduce_factor is not None:
        cargs.extend([
            "-reducefactor",
            str(reduce_factor)
        ])
    ret = VSumaAcknowledgeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_prefix + "_graph_dataset"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSumaAcknowledgeOutputs",
    "V__SUMA_ACKNOWLEDGE_METADATA",
    "v__suma_acknowledge",
]

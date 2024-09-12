# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_BRAIN_VOYAGERTO_AFNI_METADATA = Metadata(
    id="5d5cc8a86b7568d260e0630ce59dd774a116e190.boutiques",
    name="3dBRAIN_VOYAGERtoAFNI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dBrainVoyagertoAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_brain_voyagerto_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik_file: OutputPathType
    """Output BRIK file"""
    output_head_file: OutputPathType
    """Output HEAD file"""


def v_3d_brain_voyagerto_afni(
    input_file: InputPathType,
    force_byte_swap: bool = False,
    brainvoyager_qx: bool = False,
    tlrc_space: bool = False,
    acpc_space: bool = False,
    orig_space: bool = False,
    prefix: str | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    set_environment: str | None = None,
    trace_debugging: bool = False,
    trace_extreme_debugging: bool = False,
    turn_off_memory_tracing: bool = False,
    turn_on_memory_tracing: bool = False,
    runner: Runner | None = None,
) -> V3dBrainVoyagertoAfniOutputs:
    """
    Converts a BrainVoyager vmr dataset to AFNI's BRIK format based on information
    from BrainVoyager's website.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dBRAIN_VOYAGERtoAFNI.html
    
    Args:
        input_file: Input BrainVoyager VMR file.
        force_byte_swap: Force byte swapping.
        brainvoyager_qx: .vmr file is from BrainVoyager QX.
        tlrc_space: Dset in tlrc space.
        acpc_space: Dset in acpc-aligned space.
        orig_space: Dset in orig space.
        prefix: Prefix for output files.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        set_environment: Set environment variable ENVname to be ENVvalue.\
            Quotes are necessary.
        trace_debugging: Turns on In/Out debug and Memory tracing.
        trace_extreme_debugging: Turns on extreme tracing.
        turn_off_memory_tracing: Turn off memory tracing.
        turn_on_memory_tracing: Turn on memory tracing (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBrainVoyagertoAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BRAIN_VOYAGERTO_AFNI_METADATA)
    cargs = []
    cargs.append("3dBRAIN_VOYAGERtoAFNI")
    cargs.append("--input")
    cargs.extend([
        "--input",
        execution.input_file(input_file)
    ])
    if force_byte_swap:
        cargs.append("-bs")
    if brainvoyager_qx:
        cargs.append("-qx")
    if tlrc_space:
        cargs.append("-tlrc")
    if acpc_space:
        cargs.append("-acpc")
    if orig_space:
        cargs.append("-orig")
    if prefix is not None:
        cargs.extend([
            "--prefix",
            prefix
        ])
    if novolreg:
        cargs.append("-novolreg")
    if noxform:
        cargs.append("-noxform")
    if set_environment is not None:
        cargs.extend([
            "-setenv",
            set_environment
        ])
    if trace_debugging:
        cargs.append("-trace")
    if trace_extreme_debugging:
        cargs.append("-TRACE")
    if turn_off_memory_tracing:
        cargs.append("-nomall")
    if turn_on_memory_tracing:
        cargs.append("-yesmall")
    cargs.append("[HELP_FLAG]")
    cargs.append("[HELP_EXTREME_FLAG]")
    cargs.append("[HELP_MINI_FLAG]")
    cargs.append("[H_VIEW_FLAG]")
    cargs.append("[H_WEB_FLAG]")
    cargs.append("[H_FIND]")
    cargs.append("[H_RAW_FLAG]")
    cargs.append("[H_SPHINX_FLAG]")
    cargs.append("[H_ASPHINX_FLAG]")
    cargs.append("[ALL_OPTS_FLAG]")
    ret = V3dBrainVoyagertoAfniOutputs(
        root=execution.output_file("."),
        output_brik_file=execution.output_file("output.BRIK"),
        output_head_file=execution.output_file("output.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBrainVoyagertoAfniOutputs",
    "V_3D_BRAIN_VOYAGERTO_AFNI_METADATA",
    "v_3d_brain_voyagerto_afni",
]

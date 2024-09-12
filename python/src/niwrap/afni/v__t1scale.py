# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__T1SCALE_METADATA = Metadata(
    id="6742db233e7f7fe985fd582e9532fb9d1711e98a.boutiques",
    name="@T1scale",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VT1scaleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__t1scale(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    uniformized_t1_output: OutputPathType
    """Uniformized T1 volume output file"""
    masked_uniformized_t1_output: OutputPathType
    """Masked Uniformized T1 volume output file"""
    aligned_pd_output: OutputPathType
    """Aligned PD volume output file in alignment with T1+orig"""


def v__t1scale(
    align: bool = False,
    head_mask: bool = False,
    unmasked_uni: bool = False,
    masked_uni: bool = False,
    echo: bool = False,
    help_: bool = False,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find_word: str | None = None,
    runner: Runner | None = None,
) -> VT1scaleOutputs:
    """
    Fix bias field shading in T1 by scaling it with PD image. You can also get a
    decent result even without the PD volume.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@T1scale.html
    
    Args:
        align: Align PD volume to T1. Without this option, PDvol is assumed in\
            alignment with T1vol.
        head_mask: Create mask using 3dSkullStrip's -head option.
        unmasked_uni: Do not apply masking to uniformized volume (default).
        masked_uni: Apply masking to uniformized volume.
        echo: Set echo.
        help_: Display this help message and exit.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find_word: Search for lines containing WORD in -help output. Search\
            is approximate.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VT1scaleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__T1SCALE_METADATA)
    cargs = []
    cargs.append("@T1scale")
    cargs.append("<-T1")
    cargs.append("T1vol>")
    cargs.append("<-PD")
    cargs.append("PDvol>")
    cargs.append("[OUTPUT_DIR]")
    if align:
        cargs.append("-align")
    cargs.append("[MASK_FILE]")
    if head_mask:
        cargs.append("-head_mask")
    if unmasked_uni:
        cargs.append("-unmasked_uni")
    if masked_uni:
        cargs.append("-masked_uni")
    if echo:
        cargs.append("-echo")
    if help_:
        cargs.append("-help")
    if h_web:
        cargs.append("-h_web")
    if h_view:
        cargs.append("-hview")
    if all_opts:
        cargs.append("-all_opts")
    if h_find_word is not None:
        cargs.extend([
            "-h_find",
            h_find_word
        ])
    ret = VT1scaleOutputs(
        root=execution.output_file("."),
        uniformized_t1_output=execution.output_file("T1.uni+orig"),
        masked_uniformized_t1_output=execution.output_file("T1_uni_masked+orig"),
        aligned_pd_output=execution.output_file("PD+orig"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VT1scaleOutputs",
    "V__T1SCALE_METADATA",
    "v__t1scale",
]

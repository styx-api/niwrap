# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__MAKE_PLUG_DIFF_METADATA = Metadata(
    id="200b2bad7859588d6da46076583215217ba300d1.boutiques",
    name="@make_plug_diff",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VMakePlugDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__make_plug_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__make_plug_diff(
    vtk_dir: str,
    xm_dir: str,
    afni_src_dir: str,
    afni_bin_dir: str,
    diff_dir: str,
    comments: bool = False,
    linux: bool = False,
    runner: Runner | None = None,
) -> VMakePlugDiffOutputs:
    """
    Compiles AFNI's diffusion plugin.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        vtk_dir: Directory where vtk is installed.
        xm_dir: Directory where motif is installed.
        afni_src_dir: Full path to AFNI's src/ directory.
        afni_bin_dir: Path, relative to ASRCDIR, to abin.
        diff_dir: Name of directory containing diffusion code.
        comments: Output comments only.
        linux: Flag for doing linuxy things.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMakePlugDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MAKE_PLUG_DIFF_METADATA)
    cargs = []
    cargs.append("@make_plug_diff")
    cargs.extend([
        "-vtk",
        vtk_dir
    ])
    cargs.extend([
        "-xm",
        xm_dir
    ])
    cargs.extend([
        "-asrc",
        afni_src_dir
    ])
    cargs.extend([
        "-abin",
        afni_bin_dir
    ])
    if comments:
        cargs.append("-comments")
    if linux:
        cargs.append("-linux")
    cargs.extend([
        "-diff",
        diff_dir
    ])
    ret = VMakePlugDiffOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VMakePlugDiffOutputs",
    "V__MAKE_PLUG_DIFF_METADATA",
    "v__make_plug_diff",
]

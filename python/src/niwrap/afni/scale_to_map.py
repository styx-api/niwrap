# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCALE_TO_MAP_METADATA = Metadata(
    id="4a1d74a930d355aa079195294527818a83948e47.boutiques",
    name="ScaleToMap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ScaleToMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scale_to_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scale_to_map(
    input_file: InputPathType,
    icol: float,
    vcol: float,
    cmap: str | None = None,
    cmapfile: InputPathType | None = None,
    cmapdb: InputPathType | None = None,
    frf: bool = False,
    clp: list[float] | None = None,
    perc_clp: list[float] | None = None,
    apr: float | None = None,
    anr: float | None = None,
    interp: bool = False,
    nointerp: bool = False,
    direct: bool = False,
    msk_zero: bool = False,
    msk: list[float] | None = None,
    msk_col: list[float] | None = None,
    nomsk_col: bool = False,
    br: float | None = None,
    help_: bool = False,
    verbose: bool = False,
    showmap: bool = False,
    showdb: bool = False,
    novolreg: bool = False,
    noxform: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    trace_2: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    runner: Runner | None = None,
) -> ScaleToMapOutputs:
    """
    Tool to scale values to a color map.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/ScaleToMap.html
    
    Args:
        input_file: Input file in 1D formatted ascii containing node values.
        icol: Index of node index column (-1 if node index is implicit).
        vcol: Index of node value column.
        cmap: Choose one of the standard colormaps available with SUMA.
        cmapfile: Read color map from a Mapfile.
        cmapdb: Read color maps from an AFNI .pal file.
        frf: Indicate that the first row in the file is the first color.
        clp: Clip values in IntVect to specified range.
        perc_clp: Percentile clip values in IntVect to specified range.
        apr: Clip values in IntVect to [0 range].
        anr: Clip values in IntVect to [-range range].
        interp: Use color interpolation between colors in colormap (default).
        nointerp: Turn off color interpolation within the colormap.
        direct: Directly map values to index of color in colormap.
        msk_zero: Mask values that are 0.
        msk: Mask values in vcol between specified range.
        msk_col: Set color of masked voxels.
        nomsk_col: Do not output nodes that got masked.
        br: Apply a brightness factor to colormap and mask color.
        help_: Display help message.
        verbose: Verbose mode.
        showmap: Print colormap to screen and quit.
        showdb: Print colors and colormaps of AFNI along with any loaded from\
            Palfile.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        noxform: Same as -novolreg.
        setenv: Set environment variable ENVname to ENVvalue. Quotes are\
            necessary.
        trace_: Turn on extreme tracing.
        trace_2: Turn on extreme tracing.
        nomall: Turn off memory tracing.
        yesmall: Turn on memory tracing (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ScaleToMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCALE_TO_MAP_METADATA)
    cargs = []
    cargs.append("ScaleToMap")
    cargs.append(execution.input_file(input_file))
    cargs.append(str(icol))
    cargs.append(str(vcol))
    if cmap is not None:
        cargs.extend([
            "-cmap",
            cmap
        ])
    if cmapfile is not None:
        cargs.extend([
            "-cmapfile",
            execution.input_file(cmapfile)
        ])
    if cmapdb is not None:
        cargs.extend([
            "-cmapdb",
            execution.input_file(cmapdb)
        ])
    if frf:
        cargs.append("-frf")
    if clp is not None:
        cargs.extend([
            "-clp",
            *map(str, clp)
        ])
    if perc_clp is not None:
        cargs.extend([
            "-perc_clp",
            *map(str, perc_clp)
        ])
    if apr is not None:
        cargs.extend([
            "-apr",
            str(apr)
        ])
    if anr is not None:
        cargs.extend([
            "-anr",
            str(anr)
        ])
    if interp:
        cargs.append("-interp")
    if nointerp:
        cargs.append("-nointerp")
    if direct:
        cargs.append("-direct")
    if msk_zero:
        cargs.append("-msk_zero")
    if msk is not None:
        cargs.extend([
            "-msk",
            *map(str, msk)
        ])
    if msk_col is not None:
        cargs.extend([
            "-msk_col",
            *map(str, msk_col)
        ])
    if nomsk_col:
        cargs.append("-nomsk_col")
    if br is not None:
        cargs.extend([
            "-br",
            str(br)
        ])
    if help_:
        cargs.append("-h")
    if verbose:
        cargs.append("-verb")
    if showmap:
        cargs.append("-showmap")
    if showdb:
        cargs.append("-showdb")
    if novolreg:
        cargs.append("-novolreg")
    if noxform:
        cargs.append("-noxform")
    if setenv is not None:
        cargs.extend([
            "-setenv",
            setenv
        ])
    if trace_:
        cargs.append("-TRACE")
    if trace_2:
        cargs.append("-TRACE")
    if nomall:
        cargs.append("-nomall")
    if yesmall:
        cargs.append("-yesmall")
    ret = ScaleToMapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCALE_TO_MAP_METADATA",
    "ScaleToMapOutputs",
    "scale_to_map",
]

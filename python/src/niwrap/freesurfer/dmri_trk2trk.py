# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_TRK2TRK_METADATA = Metadata(
    id="b816b98bf35fa91e6d950ed6560d2f32cb5baa59.boutiques",
    name="dmri_trk2trk",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriTrk2trkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_trk2trk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_trk_file: OutputPathType | None
    """Transformed output .trk file"""
    out_asc_file: OutputPathType | None
    """Transformed output ASCII text file"""
    out_vol_file: OutputPathType | None
    """Transformed output volume"""


def dmri_trk2trk(
    in_trk: list[InputPathType],
    in_asc: list[InputPathType] | None = None,
    in_dir: str | None = None,
    out_trk: str | None = None,
    out_asc: str | None = None,
    out_vol: str | None = None,
    out_dir: str | None = None,
    in_ref: InputPathType | None = None,
    out_ref: InputPathType | None = None,
    reg_file: InputPathType | None = None,
    regnl_file: InputPathType | None = None,
    inv_flag: bool = False,
    fill_flag: bool = False,
    overlay: list[InputPathType] | None = None,
    inclusion_mask: list[InputPathType] | None = None,
    exclusion_mask: list[InputPathType] | None = None,
    terminal_inclusion_mask: list[InputPathType] | None = None,
    terminal_exclusion_mask: list[InputPathType] | None = None,
    length_min: float | None = None,
    length_max: float | None = None,
    mean_flag: bool = False,
    nearmean_flag: bool = False,
    nth_streamline: float | None = None,
    every_nth_streamline: float | None = None,
    smooth_flag: bool = False,
    debug_flag: bool = False,
    check_opts: bool = False,
    runner: Runner | None = None,
) -> DmriTrk2trkOutputs:
    """
    A tool for transforming and analyzing tractography data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        in_trk: Input .trk file(s).
        in_asc: Input ASCII plain text file(s), as an alternative to .trk.
        in_dir: Input directory (optional).
        out_trk: Output .trk file(s), as many as inputs (or 1 to merge inputs).
        out_asc: Output ASCII plain text file(s), as many as inputs (or 1 to\
            merge inputs).
        out_vol: Output volume(s), as many as inputs (or 1 to merge inputs).
        out_dir: Output directory (optional).
        in_ref: Input reference volume (needed for --reg/--regnl).
        out_ref: Output reference volume (needed for --reg/--regnl/--outvol).
        reg_file: Affine registration file (.lta or .mat), applied first.
        regnl_file: Nonlinear registration file (.m3z), applied second.
        inv_flag: Apply inverse of registration (default: no).
        fill_flag: Fill gaps b/w mapped points by linear interpolation.
        overlay: Scalar overlay 1D volume(s), applied to all input .trk files.
        inclusion_mask: Inclusion mask(s), applied to all input .trk files.
        exclusion_mask: Exclusion mask(s), applied to all input .trk files.
        terminal_inclusion_mask: Terminal inclusion mask(s), applied to all\
            input .trk files.
        terminal_exclusion_mask: Terminal exclusion mask(s), applied to all\
            input .trk files.
        length_min: Only save streamlines with length greater than this number.
        length_max: Only save streamlines with length smaller than this number.
        mean_flag: Only save the mean of the streamlines (Default: save all).
        nearmean_flag: Only save the streamline nearest to the mean (Default:\
            save all).
        nth_streamline: Only save the n-th (0-based) streamline (Default: save\
            all).
        every_nth_streamline: Only save every n-th streamline (Default: save\
            all).
        smooth_flag: Smooth streamlines (default: no).
        debug_flag: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriTrk2trkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_TRK2TRK_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/dmri_trk2trk")
    cargs.extend([
        "--in",
        *[execution.input_file(f) for f in in_trk]
    ])
    if in_asc is not None:
        cargs.extend([
            "--inasc",
            *[execution.input_file(f) for f in in_asc]
        ])
    if in_dir is not None:
        cargs.extend([
            "--indir",
            in_dir
        ])
    if out_trk is not None:
        cargs.extend([
            "--out",
            out_trk
        ])
    if out_asc is not None:
        cargs.extend([
            "--outasc",
            out_asc
        ])
    if out_vol is not None:
        cargs.extend([
            "--outvol",
            out_vol
        ])
    if out_dir is not None:
        cargs.extend([
            "--outdir",
            out_dir
        ])
    if in_ref is not None:
        cargs.extend([
            "--inref",
            execution.input_file(in_ref)
        ])
    if out_ref is not None:
        cargs.extend([
            "--outref",
            execution.input_file(out_ref)
        ])
    if reg_file is not None:
        cargs.extend([
            "--reg",
            execution.input_file(reg_file)
        ])
    if regnl_file is not None:
        cargs.extend([
            "--regnl",
            execution.input_file(regnl_file)
        ])
    if inv_flag:
        cargs.append("--inv")
    if fill_flag:
        cargs.append("--fill")
    if overlay is not None:
        cargs.extend([
            "--over",
            *[execution.input_file(f) for f in overlay]
        ])
    if inclusion_mask is not None:
        cargs.extend([
            "--imask",
            *[execution.input_file(f) for f in inclusion_mask]
        ])
    if exclusion_mask is not None:
        cargs.extend([
            "--emask",
            *[execution.input_file(f) for f in exclusion_mask]
        ])
    if terminal_inclusion_mask is not None:
        cargs.extend([
            "--itmask",
            *[execution.input_file(f) for f in terminal_inclusion_mask]
        ])
    if terminal_exclusion_mask is not None:
        cargs.extend([
            "--etmask",
            *[execution.input_file(f) for f in terminal_exclusion_mask]
        ])
    if length_min is not None:
        cargs.extend([
            "--lmin",
            str(length_min)
        ])
    if length_max is not None:
        cargs.extend([
            "--lmax",
            str(length_max)
        ])
    if mean_flag:
        cargs.append("--mean")
    if nearmean_flag:
        cargs.append("--nearmean")
    if nth_streamline is not None:
        cargs.extend([
            "--nth",
            str(nth_streamline)
        ])
    if every_nth_streamline is not None:
        cargs.extend([
            "--every",
            str(every_nth_streamline)
        ])
    if smooth_flag:
        cargs.append("--smooth")
    if debug_flag:
        cargs.append("--debug")
    if check_opts:
        cargs.append("--checkopts")
    ret = DmriTrk2trkOutputs(
        root=execution.output_file("."),
        out_trk_file=execution.output_file(out_trk) if (out_trk is not None) else None,
        out_asc_file=execution.output_file(out_asc) if (out_asc is not None) else None,
        out_vol_file=execution.output_file(out_vol) if (out_vol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_TRK2TRK_METADATA",
    "DmriTrk2trkOutputs",
    "dmri_trk2trk",
]

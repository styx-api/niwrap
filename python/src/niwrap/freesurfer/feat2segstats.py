# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FEAT2SEGSTATS_METADATA = Metadata(
    id="114184bb1194b9afe4e61335055b6aca221f94fc.boutiques",
    name="feat2segstats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Feat2segstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `feat2segstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segstats_output: OutputPathType | None
    """Output segmentation statistics file"""


def feat2segstats(
    feat_dir: str,
    stat_: str,
    featdirfile: InputPathType | None = None,
    seg_vol: str | None = None,
    aseg_flag: bool = False,
    aparc_aseg_flag: bool = False,
    ctab: InputPathType | None = None,
    all_segs_flag: bool = False,
    copes_flag: bool = False,
    varcopes_flag: bool = False,
    zstats_flag: bool = False,
    pes_flag: bool = False,
    rvar: str | None = None,
    example_func: str | None = None,
    mask: str | None = None,
    mean_func: str | None = None,
    version_flag: bool = False,
    help_flag: bool = False,
    debug_flag: bool = False,
    nolog_flag: bool = False,
    runner: Runner | None = None,
) -> Feat2segstatsOutputs:
    """
    Computes segmentation summaries and stores output in
    featdir/freesurfer/segstats/segvol/statname.dat.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_dir: Feat output directory.
        stat_: Statistical output.
        featdirfile: File with a list of feat directories.
        seg_vol: Segmentation volume.
        aseg_flag: Use aseg segmentation.
        aparc_aseg_flag: Use aparc+aseg segmentation.
        ctab: Color lookup table, default is\
            FREESURFER_HOME/FreeSurferColorLUT.txt.
        all_segs_flag: Report on all segments, even empty ones.
        copes_flag: Do all copes.
        varcopes_flag: Do all varcopes.
        zstats_flag: Do all zstats.
        pes_flag: Do all pes.
        rvar: Sigma squared values.
        example_func: Example function.
        mask: Probably not too useful.
        mean_func: Mean function.
        version_flag: Print version and exit.
        help_flag: Print help and exit.
        debug_flag: Turn on debugging.
        nolog_flag: Do not create a log file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Feat2segstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEAT2SEGSTATS_METADATA)
    cargs = []
    cargs.append("feat2segstats")
    cargs.extend([
        "--feat",
        feat_dir
    ])
    if featdirfile is not None:
        cargs.extend([
            "--featdirfile",
            execution.input_file(featdirfile)
        ])
    if seg_vol is not None:
        cargs.extend([
            "--seg",
            seg_vol
        ])
    if aseg_flag:
        cargs.append("--aseg")
    if aparc_aseg_flag:
        cargs.append("--aparc+aseg")
    if ctab is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(ctab)
        ])
    if all_segs_flag:
        cargs.append("--all-segs")
    if copes_flag:
        cargs.append("--copes")
    if varcopes_flag:
        cargs.append("--varcopes")
    if zstats_flag:
        cargs.append("--zstats")
    if pes_flag:
        cargs.append("--pes")
    if rvar is not None:
        cargs.extend([
            "--rvar",
            rvar
        ])
    if example_func is not None:
        cargs.extend([
            "--exf",
            example_func
        ])
    if mask is not None:
        cargs.extend([
            "--mask",
            mask
        ])
    if mean_func is not None:
        cargs.extend([
            "--mean_func",
            mean_func
        ])
    cargs.extend([
        "--stat",
        stat_
    ])
    if version_flag:
        cargs.append("--version")
    if help_flag:
        cargs.append("--help")
    if debug_flag:
        cargs.append("--debug")
    if nolog_flag:
        cargs.append("--nolog")
    ret = Feat2segstatsOutputs(
        root=execution.output_file("."),
        segstats_output=execution.output_file(feat_dir + "/freesurfer/segstats/" + seg_vol + "/" + stat_ + ".dat") if (seg_vol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FEAT2SEGSTATS_METADATA",
    "Feat2segstatsOutputs",
    "feat2segstats",
]

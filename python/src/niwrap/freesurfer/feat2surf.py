# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FEAT2SURF_METADATA = Metadata(
    id="470484160f35305380e418e8513cf141bd3564e2.boutiques",
    name="feat2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Feat2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `feat2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_output: OutputPathType | None
    """Output statistics on the left hemisphere for the subject"""
    rh_output: OutputPathType | None
    """Output statistics on the right hemisphere for the subject"""
    lh_target_output: OutputPathType | None
    """Output statistics on the left hemisphere for the target subject"""
    rh_target_output: OutputPathType | None
    """Output statistics on the right hemisphere for the target subject"""


def feat2surf(
    feat_dirs: list[str],
    feat_dirfile: InputPathType | None = None,
    proj_frac: float | None = None,
    hemi: str | None = None,
    target: str | None = None,
    surf: str | None = None,
    cope_only: bool = False,
    debug_flag: bool = False,
    nolog_flag: bool = False,
    out_dir: str | None = None,
    runner: Runner | None = None,
) -> Feat2surfOutputs:
    """
    Resamples Feat statistics onto the surface of the subject and onto a
    stereo-taxic surface atlas.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        feat_dirs: Directory where Feat results are stored. Can specify\
            multiple directories.
        feat_dirfile: File with a list of Feat directories.
        proj_frac: Sample functional a fraction of the cortical thickness\
            normal to the surface. Default is 0.
        hemi: Run on specified hemisphere (lh or rh) only. Default is both\
            hemispheres.
        target: Subject used to define common surface space. Default is\
            fsaverage.
        surf: Surface to resample to. Default is white.
        cope_only: Only map the copes and varcopes to the common surface space.
        debug_flag: Turn on debugging.
        nolog_flag: Do not create a log file.
        out_dir: Output directory to use instead of default\
            feat/reg_surf-?h/stats.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Feat2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEAT2SURF_METADATA)
    cargs = []
    cargs.append("feat2surf")
    cargs.extend([
        "--feat",
        *feat_dirs
    ])
    if feat_dirfile is not None:
        cargs.extend([
            "--featdirfile",
            execution.input_file(feat_dirfile)
        ])
    if proj_frac is not None:
        cargs.extend([
            "--projfrac",
            str(proj_frac)
        ])
    if hemi is not None:
        cargs.extend([
            "--hemi",
            hemi
        ])
    if target is not None:
        cargs.extend([
            "--target",
            target
        ])
    if surf is not None:
        cargs.extend([
            "--surf",
            surf
        ])
    if cope_only:
        cargs.append("--cope-only")
    if debug_flag:
        cargs.append("--debug")
    if nolog_flag:
        cargs.append("--nolog")
    if out_dir is not None:
        cargs.extend([
            "--out",
            out_dir
        ])
    ret = Feat2surfOutputs(
        root=execution.output_file("."),
        lh_output=execution.output_file(out_dir + "/reg_surf-lh-Subject/stats") if (out_dir is not None) else None,
        rh_output=execution.output_file(out_dir + "/reg_surf-rh-Subject/stats") if (out_dir is not None) else None,
        lh_target_output=execution.output_file(out_dir + "/reg_surf-lh-targid/stats") if (out_dir is not None) else None,
        rh_target_output=execution.output_file(out_dir + "/reg_surf-rh-targid/stats") if (out_dir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FEAT2SURF_METADATA",
    "Feat2surfOutputs",
    "feat2surf",
]

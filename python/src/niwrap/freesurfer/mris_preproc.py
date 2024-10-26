# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_PREPROC_METADATA = Metadata(
    id="2bb4886135fce5b3651f3050a69d2251f17b9700.boutiques",
    name="mris_preproc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisPreprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_preproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_preproc(
    outfile: str,
    target_subject: str,
    hemi: str,
    meas: str | None = None,
    label: str | None = None,
    measdir: str | None = None,
    subjects: list[str] | None = None,
    fsgd: InputPathType | None = None,
    subjectlist: InputPathType | None = None,
    qdec: InputPathType | None = None,
    qdec_long: InputPathType | None = None,
    surfmeasfile: list[InputPathType] | None = None,
    projfrac: float | None = None,
    projfrac_max: list[float] | None = None,
    projfrac_avg: list[float] | None = None,
    no_mask_non_cortex: bool = False,
    session_file: InputPathType | None = None,
    dir_file: InputPathType | None = None,
    analysis: str | None = None,
    contrast: str | None = None,
    cvar_flag: bool = False,
    offset_flag: bool = False,
    map_: str | None = None,
    etiv_flag: bool = False,
    fwhm: float | None = None,
    fwhm_src: float | None = None,
    niters: float | None = None,
    niters_src: float | None = None,
    cortex_only: bool = False,
    mgz_flag: bool = False,
    no_jac_flag: bool = False,
    paired_diff_flag: bool = False,
    cache_out: str | None = None,
    cache_in: str | None = None,
    cache_out_only: str | None = None,
    no_prune_flag: bool = False,
    mean_flag: bool = False,
    std_flag: bool = False,
    reshape_flag: bool = False,
    surfreg: str | None = None,
    subjects_dir: str | None = None,
    synth_flag: bool = False,
    tmpdir: str | None = None,
    nocleanup_flag: bool = False,
    cleanup_flag: bool = False,
    log: str | None = None,
    nolog_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MrisPreprocOutputs:
    """
    Script to prepare surface-based data for high-level analysis by resampling
    surface or volume source data to a common subject and concatenating them into
    one file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outfile: Save output here.
        target_subject: Subject to use as the common-space. All input data will\
            be resampled to the surface of this subject.
        hemi: Use hemisphere for source and target surfaces. Can be lh or rh.
        meas: Use subject/surf/hemi.surfmeasure as input. Implies --srcfmt\
            curv.
        label: Look in label/hemi.annotname.(annot,mgz) and use mapmethod nnf.
        measdir: Look in subdir instead of surf.
        subjects: Specify an input subject on the command-line. All subjects\
            must be specified in this way.
        fsgd: Specify the list of input subjects from the fsgd file.
        subjectlist: List all subjects separated by white space in\
            subjlistfile.
        qdec: Specify list of subjects via qdec table file. Assumes the first\
            column is the "fsid".
        qdec_long: Specify list of subjects via longitudinal qdec table file.
        surfmeasfile: Specify full path to input surface measure file.
        projfrac: When sampling a volume onto the surface, sample a fraction of\
            the thickness along the surface normal.
        projfrac_max: When sampling a volume onto the surface, find max along\
            projection for vol2surf.
        projfrac_avg: Compute average along projection for vol2surf.
        no_mask_non_cortex: Do not mask out non-cortex in vol2surf.
        session_file: FS-FAST session file.
        dir_file: FS-FAST session directory file.
        analysis: FS-FAST analysis.
        contrast: FS-FAST contrast.
        cvar_flag: Use fsfast contrast variance (cesvar).
        offset_flag: Use fsfast mean offset (h-offset).
        map_: Use fsfast contrast/map.
        etiv_flag: Divide each subject's value by the Estimated Total Intra\
            Cranial Volume as found in aseg.stats.
        fwhm: Smooth by fwhm mm on the target surface.
        fwhm_src: Smooth by fwhm mm on the source surface.
        niters: Smooth by niters on the target surface.
        niters_src: Smooth by niters on the source surface.
        cortex_only: Exclude medial wall.
        mgz_flag: Use mgz format internally.
        no_jac_flag: Turn off jacobian correction.
        paired_diff_flag: Compute paired differences after concatenating all\
            inputs together.
        cache_out: Cache the output in the specified cache file.
        cache_in: Use the pre-computed cached data from the specified cache\
            file.
        cache_out_only: Cache data without actually creating an output.
        no_prune_flag: Do not prune the inputs.
        mean_flag: Compute the mean of all inputs.
        std_flag: Compute the standard deviation of all inputs.
        reshape_flag: Reshape spatial dimensions.
        surfreg: Use specified surface registration to the common space.
        subjects_dir: Set SUBJECTS_DIR environment variable.
        synth_flag: Synthesize the input data with white gaussian noise.
        tmpdir: Use specified temporary directory.
        nocleanup_flag: Do not delete temporary files.
        cleanup_flag: Delete temporary files (default).
        log: Specify log file.
        nolog_flag: Do not create a log file.
        debug_flag: Enable debug mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisPreprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_PREPROC_METADATA)
    cargs = []
    cargs.append("mris_preproc")
    cargs.append("--out")
    cargs.extend([
        "--out",
        outfile
    ])
    cargs.append("--target")
    cargs.extend([
        "--target",
        target_subject
    ])
    cargs.append("--hemi")
    cargs.extend([
        "--hemi",
        hemi
    ])
    if meas is not None:
        cargs.extend([
            "--meas",
            meas
        ])
    if label is not None:
        cargs.extend([
            "--label",
            label
        ])
    if measdir is not None:
        cargs.extend([
            "--measdir",
            measdir
        ])
    if subjects is not None:
        cargs.extend([
            "--s",
            *subjects
        ])
    if fsgd is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(fsgd)
        ])
    if subjectlist is not None:
        cargs.extend([
            "--f",
            execution.input_file(subjectlist)
        ])
    if qdec is not None:
        cargs.extend([
            "--qdec",
            execution.input_file(qdec)
        ])
    if qdec_long is not None:
        cargs.extend([
            "--qdec-long",
            execution.input_file(qdec_long)
        ])
    if surfmeasfile is not None:
        cargs.extend([
            "--is",
            *[execution.input_file(f) for f in surfmeasfile]
        ])
    cargs.append("[VOLMEASFILE]")
    if projfrac is not None:
        cargs.extend([
            "--projfrac",
            str(projfrac)
        ])
    if projfrac_max is not None:
        cargs.extend([
            "--projfrac-max",
            *map(str, projfrac_max)
        ])
    if projfrac_avg is not None:
        cargs.extend([
            "--projfrac-avg",
            *map(str, projfrac_avg)
        ])
    if no_mask_non_cortex:
        cargs.append("--no-mask-non-cortex")
    if session_file is not None:
        cargs.extend([
            "--sf",
            execution.input_file(session_file)
        ])
    if dir_file is not None:
        cargs.extend([
            "--df",
            execution.input_file(dir_file)
        ])
    if analysis is not None:
        cargs.extend([
            "--analysis",
            analysis
        ])
    if contrast is not None:
        cargs.extend([
            "--contrast",
            contrast
        ])
    if cvar_flag:
        cargs.append("--cvar")
    if offset_flag:
        cargs.append("--offset")
    if map_ is not None:
        cargs.extend([
            "--map",
            map_
        ])
    if etiv_flag:
        cargs.append("--etiv")
    if fwhm is not None:
        cargs.extend([
            "--fwhm",
            str(fwhm)
        ])
    if fwhm_src is not None:
        cargs.extend([
            "--fwhm-src",
            str(fwhm_src)
        ])
    if niters is not None:
        cargs.extend([
            "--niters",
            str(niters)
        ])
    if niters_src is not None:
        cargs.extend([
            "--niters-src",
            str(niters_src)
        ])
    if cortex_only:
        cargs.append("--cortex-only")
    if mgz_flag:
        cargs.append("--mgz")
    if no_jac_flag:
        cargs.append("--no-jac")
    if paired_diff_flag:
        cargs.append("--paired-diff")
    if cache_out is not None:
        cargs.extend([
            "--cache-out",
            cache_out
        ])
    if cache_in is not None:
        cargs.extend([
            "--cache-in",
            cache_in
        ])
    if cache_out_only is not None:
        cargs.extend([
            "--cache-out-only",
            cache_out_only
        ])
    if no_prune_flag:
        cargs.append("--no-prune")
    if mean_flag:
        cargs.append("--mean")
    if std_flag:
        cargs.append("--std")
    if reshape_flag:
        cargs.append("--reshape")
    if surfreg is not None:
        cargs.extend([
            "--surfreg",
            surfreg
        ])
    if subjects_dir is not None:
        cargs.extend([
            "--SUBJECTS_DIR",
            subjects_dir
        ])
    if synth_flag:
        cargs.append("--synth")
    if tmpdir is not None:
        cargs.extend([
            "--tmpdir",
            tmpdir
        ])
    if nocleanup_flag:
        cargs.append("--nocleanup")
    if cleanup_flag:
        cargs.append("--cleanup")
    if log is not None:
        cargs.extend([
            "--log",
            log
        ])
    if nolog_flag:
        cargs.append("--nolog")
    if debug_flag:
        cargs.append("--debug")
    ret = MrisPreprocOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_PREPROC_METADATA",
    "MrisPreprocOutputs",
    "mris_preproc",
]

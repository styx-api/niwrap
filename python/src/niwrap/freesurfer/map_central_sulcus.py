# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAP_CENTRAL_SULCUS_METADATA = Metadata(
    id="ca8aeea364b75a5e16c0b6eafcdb6e7f1c756d05.boutiques",
    name="map_central_sulcus",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MapCentralSulcusOutputs(typing.NamedTuple):
    """
    Output object returned when calling `map_central_sulcus(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    log_file: OutputPathType
    """Log file from recon-all process."""
    status_log_file: OutputPathType
    """Status log file from recon-all process."""


def map_central_sulcus(
    subjid: str,
    process_directive: str,
    hemi_flag: str | None = None,
    expert_prefs_file: InputPathType | None = None,
    xopts_use: bool = False,
    xopts_clean: bool = False,
    xopts_overwrite: bool = False,
    watershed_cmd: str | None = None,
    xmask_file: InputPathType | None = None,
    wsless: bool = False,
    wsmore: bool = False,
    wsatlas: bool = False,
    no_wsatlas: bool = False,
    no_wsgcaatlas: bool = False,
    wsthresh: float | None = None,
    wsseed: str | None = None,
    norm3diters: float | None = None,
    normmaxgrad: float | None = None,
    norm1_b: float | None = None,
    norm2_b: float | None = None,
    norm1_n: float | None = None,
    norm2_n: float | None = None,
    cm_flag: bool = False,
    no_fix_with_ga: bool = False,
    fix_diag_only: bool = False,
    seg_wlo: float | None = None,
    seg_ghi: float | None = None,
    nothicken: bool = False,
    no_ca_align_after: bool = False,
    no_ca_align: bool = False,
    deface: bool = False,
    mprage: bool = False,
    washu_mprage: bool = False,
    schwartzya3t_atlas: bool = False,
    mail_username: str | None = None,
    threads: float | None = None,
    runner: Runner | None = None,
) -> MapCentralSulcusOutputs:
    """
    Performs all, or any part of, the FreeSurfer cortical reconstruction process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjid: FreeSurfer subject identification string which doubles as the\
            name of the reconstruction root directory for the subject.
        process_directive: Process directive for recon-all (e.g. -all,\
            -autorecon-all, -autorecon1).
        hemi_flag: Specify hemisphere processing (e.g., lh for left hemisphere\
            or rh for right hemisphere).
        expert_prefs_file: Read-in expert options file for processing.\
            Overrides default options.
        xopts_use: Use pre-existing expert options file.
        xopts_clean: Delete pre-existing expert options file.
        xopts_overwrite: Overwrite pre-existing expert options file.
        watershed_cmd: Controls how the skull stripping will be performed.
        xmask_file: Custom external brain mask to replace automated\
            skullstripping.
        wsless: Decrease watershed threshold (leaves less skull, but can strip\
            more brain).
        wsmore: Increase watershed threshold (leaves more skull, but can strip\
            less brain).
        wsatlas: Use atlas when skull stripping.
        no_wsatlas: Do not use atlas when skull stripping.
        no_wsgcaatlas: Do not use GCA atlas when skull stripping.
        wsthresh: Explicitly set watershed threshold.
        wsseed: Specify an index (C, R, S) point in the skull.
        norm3diters: Number of 3d iterations for mri_normalize.
        normmaxgrad: Max grad (-g) for mri_normalize. Default is 1.
        norm1_b: In the first usage of mri_normalize, use control point with\
            intensity N below target (default=10.0).
        norm2_b: In the second usage of mri_normalize, use control point with\
            intensity N below target (default=10.0).
        norm1_n: In the first usage of mri_normalize, do N number of\
            iterations.
        norm2_n: In the second usage of mri_normalize, do N number of\
            iterations.
        cm_flag: Conform volumes to the min voxel size.
        no_fix_with_ga: Do not use genetic algorithm when fixing topology.
        fix_diag_only: Topology fixer runs until ?h.defect_labels files are\
            created, then stops.
        seg_wlo: Set wlo value for mri_segment and mris_make_surfaces.
        seg_ghi: Set ghi value for mri_segment and mris_make_surfaces.
        nothicken: Pass '-thicken 0' to mri_segment.
        no_ca_align_after: Turn off -align-after with mri_ca_register.
        no_ca_align: Turn off -align with mri_ca_label.
        deface: Deface subject, written to orig_defaced.mgz.
        mprage: Assume scan parameters are MGH MP-RAGE protocol.
        washu_mprage: Assume scan parameters are Wash.U. MP-RAGE protocol.
        schwartzya3t_atlas: For tal reg, use special young adult 3T atlas.
        mail_username: Mail user when done.
        threads: Set number of threads to use.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MapCentralSulcusOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAP_CENTRAL_SULCUS_METADATA)
    cargs = []
    cargs.append("recon-all")
    cargs.extend([
        "-subjid",
        subjid
    ])
    cargs.append(process_directive)
    if hemi_flag is not None:
        cargs.extend([
            "-hemi",
            hemi_flag
        ])
    if expert_prefs_file is not None:
        cargs.extend([
            "-expert",
            execution.input_file(expert_prefs_file)
        ])
    if xopts_use:
        cargs.append("-xopts-use")
    if xopts_clean:
        cargs.append("-xopts-clean")
    if xopts_overwrite:
        cargs.append("-xopts-overwrite")
    if watershed_cmd is not None:
        cargs.extend([
            "-watershed",
            watershed_cmd
        ])
    if xmask_file is not None:
        cargs.extend([
            "-xmask",
            execution.input_file(xmask_file)
        ])
    if wsless:
        cargs.append("-wsless")
    if wsmore:
        cargs.append("-wsmore")
    if wsatlas:
        cargs.append("-wsatlas")
    if no_wsatlas:
        cargs.append("-no-wsatlas")
    if no_wsgcaatlas:
        cargs.append("-no-wsgcaatlas")
    if wsthresh is not None:
        cargs.extend([
            "-wsthresh",
            str(wsthresh)
        ])
    if wsseed is not None:
        cargs.extend([
            "-wsseed",
            wsseed
        ])
    if norm3diters is not None:
        cargs.extend([
            "-norm3diters",
            str(norm3diters)
        ])
    if normmaxgrad is not None:
        cargs.extend([
            "-normmaxgrad",
            str(normmaxgrad)
        ])
    if norm1_b is not None:
        cargs.extend([
            "-norm1-b",
            str(norm1_b)
        ])
    if norm2_b is not None:
        cargs.extend([
            "-norm2-b",
            str(norm2_b)
        ])
    if norm1_n is not None:
        cargs.extend([
            "-norm1-n",
            str(norm1_n)
        ])
    if norm2_n is not None:
        cargs.extend([
            "-norm2-n",
            str(norm2_n)
        ])
    if cm_flag:
        cargs.append("-cm")
    if no_fix_with_ga:
        cargs.append("-no-fix-with-ga")
    if fix_diag_only:
        cargs.append("-fix-diag-only")
    if seg_wlo is not None:
        cargs.extend([
            "-seg-wlo",
            str(seg_wlo)
        ])
    if seg_ghi is not None:
        cargs.extend([
            "-seg-ghi",
            str(seg_ghi)
        ])
    if nothicken:
        cargs.append("-nothicken")
    if no_ca_align_after:
        cargs.append("-no-ca-align-after")
    if no_ca_align:
        cargs.append("-no-ca-align")
    if deface:
        cargs.append("-deface")
    if mprage:
        cargs.append("-mprage")
    if washu_mprage:
        cargs.append("-washu_mprage")
    if schwartzya3t_atlas:
        cargs.append("-schwartzya3t-atlas")
    if mail_username is not None:
        cargs.extend([
            "-mail",
            mail_username
        ])
    if threads is not None:
        cargs.extend([
            "-threads",
            str(threads)
        ])
    ret = MapCentralSulcusOutputs(
        root=execution.output_file("."),
        log_file=execution.output_file(subjid + "/scripts/recon-all.log"),
        status_log_file=execution.output_file(subjid + "/scripts/recon-all-status.log"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAP_CENTRAL_SULCUS_METADATA",
    "MapCentralSulcusOutputs",
    "map_central_sulcus",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BMEDITS2SURF_METADATA = Metadata(
    id="cca406a5e86117c8b81172471f6910fd96a7caf1.boutiques",
    name="bmedits2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Bmedits2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bmedits2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lh_bmerase: OutputPathType
    """Binary mask of erased surface locations for the left hemisphere in
    fsaverage space."""
    rh_bmerase: OutputPathType
    """Binary mask of erased surface locations for the right hemisphere in
    fsaverage space."""
    lh_bmclone: OutputPathType
    """Binary mask of cloned surface locations for the left hemisphere in
    fsaverage space."""
    rh_bmclone: OutputPathType
    """Binary mask of cloned surface locations for the right hemisphere in
    fsaverage space."""
    bmclone_stats: OutputPathType
    """Statistics about the number of voxels cloned."""
    bmerase_stats: OutputPathType
    """Statistics about the number of voxels erased."""


def bmedits2surf(
    subject: str,
    self: bool = False,
    overwrite: bool = False,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    debug: bool = False,
    left_hemisphere: bool = False,
    right_hemisphere: bool = False,
    no_surfs: bool = False,
    runner: Runner | None = None,
) -> Bmedits2surfOutputs:
    """
    Computes a binary map of surface locations where the brainmask.mgz has been
    edited.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject for which the binary map will be computed.
        overwrite: Force overwriting of existing results.
        tmp_dir: Temporary directory.
        cleanup: Clean up temporary files.
        no_cleanup: Do not clean up temporary files.
        debug: Enable debug mode.
        left_hemisphere: Perform operation only on the left hemisphere.
        right_hemisphere: Perform operation only on the right hemisphere.
        no_surfs: Do not compute surfaces, only statistics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Bmedits2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BMEDITS2SURF_METADATA)
    cargs = []
    cargs.append("bmedits2surf")
    cargs.append("--s")
    cargs.append(subject)
    if self:
        cargs.append("--self")
    if overwrite:
        cargs.append("--overwrite")
    if tmp_dir is not None:
        cargs.extend([
            "--tmp",
            tmp_dir
        ])
    if cleanup:
        cargs.append("--cleanup")
    if no_cleanup:
        cargs.append("--no-cleanup")
    if debug:
        cargs.append("--debug")
    if left_hemisphere:
        cargs.append("--lh")
    if right_hemisphere:
        cargs.append("--rh")
    if no_surfs:
        cargs.append("--no-surfs")
    ret = Bmedits2surfOutputs(
        root=execution.output_file("."),
        lh_bmerase=execution.output_file(subject + "/surf/lh.bmerase.fsa.mgh"),
        rh_bmerase=execution.output_file(subject + "/surf/rh.bmerase.fsa.mgh"),
        lh_bmclone=execution.output_file(subject + "/surf/lh.bmclone.fsa.mgh"),
        rh_bmclone=execution.output_file(subject + "/surf/rh.bmclone.fsa.mgh"),
        bmclone_stats=execution.output_file(subject + "/stats/bmclone.dat"),
        bmerase_stats=execution.output_file(subject + "/stats/bmerase.dat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BMEDITS2SURF_METADATA",
    "Bmedits2surfOutputs",
    "bmedits2surf",
]

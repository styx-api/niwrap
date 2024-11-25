# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

WM_ANAT_SNR_METADATA = Metadata(
    id="bc76bbfe5bc73f815ba252ba2ec1d2b82838940c.boutiques",
    name="wm-anat-snr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class WmAnatSnrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wm_anat_snr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_datafile: OutputPathType
    """Output data file containing SNR and associated metrics"""


def wm_anat_snr(
    subject: str,
    output_file: str,
    force: bool = False,
    nerode: int | None = None,
    tmp_dir: str | None = None,
    cleanup: bool = False,
    no_cleanup: bool = False,
    runner: Runner | None = None,
) -> WmAnatSnrOutputs:
    """
    Measures the anatomical SNR in white matter (WM) for quality assurance (QA).
    This is an experimental metric.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject name.
        output_file: Output file.
        force: Force analysis even if output is up-to-date.
        nerode: Number of erosions for the WM mask.
        tmp_dir: Temporary directory.
        cleanup: Delete temporary directory after execution.
        no_cleanup: Do not delete temporary directory after execution.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WmAnatSnrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WM_ANAT_SNR_METADATA)
    cargs = []
    cargs.append("wm-anat-snr")
    cargs.extend([
        "--s",
        subject
    ])
    cargs.extend([
        "--o",
        output_file
    ])
    if force:
        cargs.append("--force")
    if nerode is not None:
        cargs.extend([
            "--nerode",
            str(nerode)
        ])
    if tmp_dir is not None:
        cargs.extend([
            "--tmp",
            tmp_dir
        ])
    if cleanup:
        cargs.append("--cleanup")
    if no_cleanup:
        cargs.append("--no-cleanup")
    ret = WmAnatSnrOutputs(
        root=execution.output_file("."),
        output_datafile=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WM_ANAT_SNR_METADATA",
    "WmAnatSnrOutputs",
    "wm_anat_snr",
]

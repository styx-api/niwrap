# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOL2SUBFIELD_METADATA = Metadata(
    id="ec503af3368509aa5b191ee5f77a6d7c5a57bc38.boutiques",
    name="vol2subfield",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Vol2subfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vol2subfield(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mapped_output_volume: OutputPathType | None
    """Output volume mapped into subfield volume space"""
    output_registration_file: OutputPathType | None
    """Output registration file"""
    segmentation_stats_file: OutputPathType | None
    """Statistics output file generated by mri_segstats"""
    average_waveform_file: OutputPathType | None
    """Average waveform output file"""
    average_waveform_volume_file: OutputPathType | None
    """Average waveform volume output file"""


def vol2subfield(
    input_volume: InputPathType,
    subfield_volume: InputPathType,
    registration_file: InputPathType,
    output_volume: str | None = None,
    output_registration: str | None = None,
    stats_output: str | None = None,
    avgwf_output: str | None = None,
    avgwfvol_output: str | None = None,
    color_table: InputPathType | None = None,
    interpolation_cubic: bool = False,
    tmp_directory: str | None = None,
    preset_subfield_brainstem: bool = False,
    runner: Runner | None = None,
) -> Vol2subfieldOutputs:
    """
    A tool for integrating arbitrary volumes with volumes that share a RAS space
    with the orig volume in the FreeSurfer mri folder.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        subfield_volume: Subfield volume (full path or relative to subject/mri).
        registration_file: Registration that maps input volume to conformed\
            space.
        output_volume: Output volume.
        output_registration: Registration between input volume and subfield.
        stats_output: Run mri_segstats with --sum output to this file.
        avgwf_output: Run mri_segstats with --avgwf output to this file.
        avgwfvol_output: Run mri_segstats with --avgwfvol output to this file.
        color_table: Color table to use with mri_segstats.
        interpolation_cubic: Use cubic interpolation.
        tmp_directory: Temporary directory for debugging.
        preset_subfield_brainstem: Set subfield to brainstemSsLabels.v12.mgz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Vol2subfieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOL2SUBFIELD_METADATA)
    cargs = []
    cargs.append("vol2subfield")
    cargs.extend([
        "--i",
        execution.input_file(input_volume)
    ])
    cargs.extend([
        "--sf",
        execution.input_file(subfield_volume)
    ])
    cargs.extend([
        "--reg",
        execution.input_file(registration_file)
    ])
    if output_volume is not None:
        cargs.extend([
            "--o",
            output_volume
        ])
    if output_registration is not None:
        cargs.extend([
            "--outreg",
            output_registration
        ])
    if stats_output is not None:
        cargs.extend([
            "--stats",
            stats_output
        ])
    if avgwf_output is not None:
        cargs.extend([
            "--avgwf",
            avgwf_output
        ])
    if avgwfvol_output is not None:
        cargs.extend([
            "--avgwfvol",
            avgwfvol_output
        ])
    if color_table is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(color_table)
        ])
    if interpolation_cubic:
        cargs.append("--cubic")
    if tmp_directory is not None:
        cargs.extend([
            "--tmp",
            tmp_directory
        ])
    if preset_subfield_brainstem:
        cargs.append("--brainstem")
    ret = Vol2subfieldOutputs(
        root=execution.output_file("."),
        mapped_output_volume=execution.output_file(output_volume) if (output_volume is not None) else None,
        output_registration_file=execution.output_file(output_registration) if (output_registration is not None) else None,
        segmentation_stats_file=execution.output_file(stats_output) if (stats_output is not None) else None,
        average_waveform_file=execution.output_file(avgwf_output) if (avgwf_output is not None) else None,
        average_waveform_volume_file=execution.output_file(avgwfvol_output) if (avgwfvol_output is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOL2SUBFIELD_METADATA",
    "Vol2subfieldOutputs",
    "vol2subfield",
]

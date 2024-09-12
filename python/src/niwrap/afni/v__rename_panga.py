# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__RENAME_PANGA_METADATA = Metadata(
    id="51f0ff41c0be1ae9dd7de0ea5bf011309bce0477.boutiques",
    name="@RenamePanga",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VRenamePangaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__rename_panga(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    head_file: OutputPathType | None
    """Main output file (HEAD)"""
    brik_file: OutputPathType | None
    """Main output file (BRIK)"""
    log_file: OutputPathType | None
    """Log file created in the current directory"""


def v__rename_panga(
    dir_number: str,
    first_image_number: str,
    num_slices: float,
    num_reps: float,
    output_root: str,
    keep_prefix: bool = False,
    interactive: bool = False,
    outliers_check: bool = False,
    slice_pattern: str | None = None,
    output_directory: str | None = None,
    runner: Runner | None = None,
) -> VRenamePangaOutputs:
    """
    Creates AFNI bricks from RealTime GE EPI series.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@RenamePanga.html
    
    Args:
        dir_number: The directory number where the first image of the series is\
            stored.
        first_image_number: The number of the first image in the series.
        num_slices: The number of slices making up the imaged volume.
        num_reps: The number of samples in your time series.
        output_root: The prefix for the output brick.
        keep_prefix: Forces @RenamePanga to use the prefix you designate\
            without modification.
        interactive: Launches to3d in interactive mode. This allows you to\
            double check the automated settings.
        outliers_check: Performs outliers check and writes the outliers to a\
            .1D file placed in the output directory.
        slice_pattern: Sets the slice acquisition pattern. The default option\
            is alt+z.
        output_directory: Directory where the output (bricks and 1D files) will\
            be stored. The default directory is ./afni.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRenamePangaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__RENAME_PANGA_METADATA)
    cargs = []
    cargs.append("@RenamePanga")
    cargs.append(dir_number)
    cargs.append(first_image_number)
    cargs.append(str(num_slices))
    cargs.append(str(num_reps))
    cargs.append(output_root)
    if keep_prefix:
        cargs.append("-kp")
    if interactive:
        cargs.append("-i")
    if outliers_check:
        cargs.append("-oc")
    if slice_pattern is not None:
        cargs.extend([
            "-sp",
            slice_pattern
        ])
    if output_directory is not None:
        cargs.extend([
            "-od",
            output_directory
        ])
    ret = VRenamePangaOutputs(
        root=execution.output_file("."),
        head_file=execution.output_file(output_directory + "/" + output_root + "_r#.HEAD") if (output_directory is not None) else None,
        brik_file=execution.output_file(output_directory + "/" + output_root + "_r#.BRIK") if (output_directory is not None) else None,
        log_file=execution.output_file(output_directory + "/MAPLOG_Panga") if (output_directory is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VRenamePangaOutputs",
    "V__RENAME_PANGA_METADATA",
    "v__rename_panga",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DIFF_FILES_METADATA = Metadata(
    id="06448df7b458fee6cb35a742b2693373b6f580ad.boutiques",
    name="@diff.files",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDiffFilesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__diff_files(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__diff_files(
    files: list[str],
    old_dir: str,
    runner: Runner | None = None,
) -> VDiffFilesOutputs:
    """
    Show file differences (between specified files and those in another directory).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@diff.files.html
    
    Args:
        files: List of files to compare.
        old_dir: Directory containing the files to compare against.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDiffFilesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DIFF_FILES_METADATA)
    cargs = []
    cargs.append("@diff.files")
    cargs.append("[OPTIONS]")
    cargs.extend(files)
    cargs.append(old_dir)
    ret = VDiffFilesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDiffFilesOutputs",
    "V__DIFF_FILES_METADATA",
    "v__diff_files",
]

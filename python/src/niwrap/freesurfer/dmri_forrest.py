# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_FORREST_METADATA = Metadata(
    id="a860992aadd3038f26abd4c931b85cc93ace621f.boutiques",
    name="dmri_forrest",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriForrestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_forrest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_forrest(
    test_dir: str,
    train_file: InputPathType,
    mask_file: InputPathType,
    tract_files: list[InputPathType],
    seg_file: InputPathType | None = None,
    diff_file: InputPathType | None = None,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> DmriForrestOutputs:
    """
    dmri_forrest is a tool for processing diffusion MRI data using a random
    forest-based method.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        test_dir: Directory containing the test subject data.
        train_file: File listing training subject directories, one per line.
        mask_file: Input brain mask volume name, relative to subject directory.
        tract_files: Input tract label volume(s), relative to subject directory.
        seg_file: Input aparc+aseg volume name, relative to subject directory.
        diff_file: Input diffusion orientation volume name, relative to subject\
            directory.
        debug: Turn on debugging mode.
        checkopts: Only check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriForrestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_FORREST_METADATA)
    cargs = []
    cargs.append("dmri_forrest")
    cargs.extend([
        "--test",
        test_dir
    ])
    cargs.extend([
        "--train",
        execution.input_file(train_file)
    ])
    cargs.extend([
        "--mask",
        execution.input_file(mask_file)
    ])
    cargs.extend([
        "--tract",
        *[execution.input_file(f) for f in tract_files]
    ])
    if seg_file is not None:
        cargs.extend([
            "--seg",
            execution.input_file(seg_file)
        ])
    if diff_file is not None:
        cargs.extend([
            "--diff",
            execution.input_file(diff_file)
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    ret = DmriForrestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_FORREST_METADATA",
    "DmriForrestOutputs",
    "dmri_forrest",
]

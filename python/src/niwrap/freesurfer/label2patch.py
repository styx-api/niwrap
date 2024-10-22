# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL2PATCH_METADATA = Metadata(
    id="4be15af9e7384c4c574e474c26c1566847f3a1ea.boutiques",
    name="label2patch",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Label2patchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label2patch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def label2patch(
    subject_name: str,
    hemisphere: str,
    label_file: InputPathType,
    output_patch: str,
    dilate: float | None = None,
    erode: float | None = None,
    close: float | None = None,
    subjects_dir: str | None = None,
    surface_name: str | None = None,
    write_surface: bool = False,
    runner: Runner | None = None,
) -> Label2patchOutputs:
    """
    Utility to create patches from label files in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name.
        hemisphere: Hemisphere (e.g. lh or rh).
        label_file: Label file name.
        output_patch: Output patch file.
        dilate: Dilate the label n times before creating the patch.
        erode: Erode the label n times before creating the patch.
        close: Close the label n times before creating the patch.
        subjects_dir: Use path as the SUBJECTS_DIR instead of environment.
        surface_name: Use name as the surface (default 'inflated').
        write_surface: Write output to a surface file (not a patch). Use .stl\
            in filename to only write the mesh covered by the label, saving it in\
            FS format will save full surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Label2patchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL2PATCH_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/label2patch")
    cargs.append(subject_name)
    cargs.append(hemisphere)
    cargs.append(execution.input_file(label_file))
    cargs.append(output_patch)
    if dilate is not None:
        cargs.extend([
            "-dilate",
            str(dilate)
        ])
    if erode is not None:
        cargs.extend([
            "-erode",
            str(erode)
        ])
    if close is not None:
        cargs.extend([
            "-close",
            str(close)
        ])
    if subjects_dir is not None:
        cargs.extend([
            "-sdir",
            subjects_dir
        ])
    if surface_name is not None:
        cargs.extend([
            "-surf",
            surface_name
        ])
    if write_surface:
        cargs.append("-writesurf")
    ret = Label2patchOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL2PATCH_METADATA",
    "Label2patchOutputs",
    "label2patch",
]

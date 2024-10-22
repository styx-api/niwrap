# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

HIAM_MAKE_TEMPLATE_METADATA = Metadata(
    id="c042ff7cafab058fc9686ab574e8045eece98767.boutiques",
    name="hiam_make_template",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class HiamMakeTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `hiam_make_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def hiam_make_template(
    hemi: str,
    surface_name: str,
    subjects: list[str],
    output_name: str,
    runner: Runner | None = None,
) -> HiamMakeTemplateOutputs:
    """
    This program adds a template into an average surface using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere to be processed (e.g. lh or rh).
        surface_name: Name of the surface.
        subjects: List of subject identifiers.
        output_name: Name of the output template.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HiamMakeTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HIAM_MAKE_TEMPLATE_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/hiam_make_template")
    cargs.append(hemi)
    cargs.append(surface_name)
    cargs.extend(subjects)
    cargs.append(output_name)
    ret = HiamMakeTemplateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "HIAM_MAKE_TEMPLATE_METADATA",
    "HiamMakeTemplateOutputs",
    "hiam_make_template",
]

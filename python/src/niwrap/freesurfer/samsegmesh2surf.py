# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SAMSEGMESH2SURF_METADATA = Metadata(
    id="4bfb2a17032b55c80252c7b21f77c717d6d385df.boutiques",
    name="samsegmesh2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Samsegmesh2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `samsegmesh2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType | None
    """FreeSurfer surface file generated from SAMSEG atlas mesh"""
    output_priors_file: OutputPathType | None
    """Priors MRI volume at each vertex"""


def samsegmesh2surf(
    atlas_mesh: InputPathType,
    template: InputPathType | None = None,
    lta_transform: InputPathType | None = None,
    output_surface: str | None = None,
    output_priors: str | None = None,
    invert_flag: bool = False,
    runner: Runner | None = None,
) -> Samsegmesh2surfOutputs:
    """
    Generate Freesurfer surface from a SAMSEG atlas mesh file and generate priors at
    each vertex as overlay MRI volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        atlas_mesh: Input SAMSEG atlas mesh collection file.
        template: Input atlas template volume.
        lta_transform: Input LTA transform to be applied to surface.
        output_surface: Output FreeSurfer surface file.
        output_priors: Output priors as MRI volume.
        invert_flag: Invert LTA transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Samsegmesh2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SAMSEGMESH2SURF_METADATA)
    cargs = []
    cargs.append("samsegmesh2surf")
    cargs.append("--atlasmesh")
    cargs.extend([
        "--atlasmesh",
        execution.input_file(atlas_mesh)
    ])
    if template is not None:
        cargs.extend([
            "--template",
            "(" + execution.input_file(template)
        ])
    cargs.append("|")
    if lta_transform is not None:
        cargs.extend([
            "--lta",
            execution.input_file(lta_transform) + ")"
        ])
    if output_surface is not None:
        cargs.extend([
            "--osurf",
            "(" + output_surface
        ])
    cargs.append("|")
    if output_priors is not None:
        cargs.extend([
            "--opriors",
            output_priors + ")"
        ])
    if invert_flag:
        cargs.append("--invert")
    ret = Samsegmesh2surfOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(output_surface) if (output_surface is not None) else None,
        output_priors_file=execution.output_file(output_priors) if (output_priors is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SAMSEGMESH2SURF_METADATA",
    "Samsegmesh2surfOutputs",
    "samsegmesh2surf",
]

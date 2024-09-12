# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_PATCH_METADATA = Metadata(
    id="bf694ee441e47bf6b816bf09ad6bc2d315d5f013.boutiques",
    name="SurfPatch",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SurfPatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_patch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outpatch_a: OutputPathType
    """Output patch for surface A"""
    outpatch_b: OutputPathType
    """Output patch for surface B"""
    out_stitched_surface: OutputPathType
    """Stitched surface file"""


def surf_patch(
    spec_file: InputPathType,
    surf_b: InputPathType,
    surf_b_: InputPathType,
    nodefile: InputPathType,
    inode: float,
    ilabel: float,
    prefix: str,
    runner: Runner | None = None,
) -> SurfPatchOutputs:
    """
    Creates a patch of surface formed by nodes in a nodefile and optionally
    calculates the volume between the same patch on two isotopic surfaces.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfPatch.html
    
    Args:
        spec_file: Spec file containing input surfaces.
        surf_b: Input surface B.
        surf_b_: Input surface B.
        nodefile: File containing nodes defining the patch.
        inode: Index of the column containing the nodes.
        ilabel: Index of the column containing labels of the nodes in column\
            inode.
        prefix: Prefix of output patch.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfPatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_PATCH_METADATA)
    cargs = []
    cargs.append("SurfPatch")
    cargs.append("-spec")
    cargs.append(execution.input_file(spec_file))
    cargs.append("-surf_A")
    cargs.extend([
        "-surf_B",
        execution.input_file(surf_b)
    ])
    cargs.append("-surf_B")
    cargs.extend([
        "-surf_B",
        execution.input_file(surf_b_)
    ])
    cargs.append("-input")
    cargs.extend([
        "-input",
        execution.input_file(nodefile)
    ])
    cargs.append(str(inode))
    cargs.append(str(ilabel))
    cargs.append("-prefix")
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.append("[OPTIONS]")
    ret = SurfPatchOutputs(
        root=execution.output_file("."),
        outpatch_a=execution.output_file(prefix + "_A"),
        outpatch_b=execution.output_file(prefix + "_B"),
        out_stitched_surface=execution.output_file(prefix + "_stitched"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_PATCH_METADATA",
    "SurfPatchOutputs",
    "surf_patch",
]

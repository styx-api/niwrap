# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DIFF_TREE_METADATA = Metadata(
    id="24b1cfac6f49e5c4ce8deeb925305286098b7e84.boutiques",
    name="@diff.tree",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDiffTreeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__diff_tree(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__diff_tree(
    runner: Runner | None = None,
) -> VDiffTreeOutputs:
    """
    Show file differences between 2 directories.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@diff.tree.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDiffTreeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DIFF_TREE_METADATA)
    cargs = []
    cargs.append("@diff.tree")
    cargs.append("[OPTIONS]")
    cargs.append("new_dir")
    cargs.append("old_dir")
    ret = VDiffTreeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDiffTreeOutputs",
    "V__DIFF_TREE_METADATA",
    "v__diff_tree",
]

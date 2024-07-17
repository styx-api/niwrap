# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_OVERLAP_METADATA = Metadata(
    id="ba884e0f6c89996eeec188d5abcc3b386ec6460c",
    name="3dOverlap",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """BRIK file with count of overlaps at each voxel (if -save is used)"""
    output_head: OutputPathType | None
    """HEAD file with count of overlaps at each voxel (if -save is used)"""


def v_3d_overlap(
    dataset1: InputPathType,
    dataset2: list[InputPathType],
    save_prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dOverlapOutputs:
    """
    3dOverlap by AFNI Development Team.
    
    Counts the number of voxels that are nonzero in all input datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dOverlap.html
    
    Args:
        dataset1: First input dataset (e.g. dset1+orig).
        dataset2: Second input dataset (e.g. dset2+orig).
        save_prefix: Save the count of overlaps at each voxel into a dataset\
            with the given prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_OVERLAP_METADATA)
    cargs = []
    cargs.append("3dOverlap")
    cargs.append("[OPTIONS]")
    cargs.append("[DATASET1]")
    cargs.append("[DATASET2]")
    ret = V3dOverlapOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(f"{save_prefix}+orig.BRIK", optional=True) if save_prefix is not None else None,
        output_head=execution.output_file(f"{save_prefix}+orig.HEAD", optional=True) if save_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dOverlapOutputs",
    "V_3D_OVERLAP_METADATA",
    "v_3d_overlap",
]

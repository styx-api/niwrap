# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_TO_VOLUME_MAPPING_METADATA = Metadata(
    id="3bba08ec366947b533a5d4e2659fb376a3ed626b.boutiques",
    name="label-to-volume-mapping",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class LabelToVolumeMappingRibbonConstrained:
    """
    use ribbon constrained mapping algorithm.
    """
    inner_surf: InputPathType
    """the inner surface of the ribbon"""
    outer_surf: InputPathType
    """the outer surface of the ribbon"""
    opt_voxel_subdiv_subdiv_num: int | None = None
    """voxel divisions while estimating voxel weights: number of subdivisions,
    default 3"""
    opt_greedy: bool = False
    """also put labels in voxels with less than 50% partial volume (legacy
    behavior)"""
    opt_thick_columns: bool = False
    """use overlapping columns (legacy method)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-ribbon-constrained")
        cargs.append(execution.input_file(self.inner_surf))
        cargs.append(execution.input_file(self.outer_surf))
        if self.opt_voxel_subdiv_subdiv_num is not None:
            cargs.extend([
                "-voxel-subdiv",
                str(self.opt_voxel_subdiv_subdiv_num)
            ])
        if self.opt_greedy:
            cargs.append("-greedy")
        if self.opt_thick_columns:
            cargs.append("-thick-columns")
        return cargs


class LabelToVolumeMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_to_volume_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume file"""


def label_to_volume_mapping(
    label: InputPathType,
    surface: InputPathType,
    volume_space: InputPathType,
    volume_out: str,
    opt_nearest_vertex_distance: float | None = None,
    ribbon_constrained: LabelToVolumeMappingRibbonConstrained | None = None,
    runner: Runner | None = None,
) -> LabelToVolumeMappingOutputs:
    """
    Map label file to volume.
    
    Maps labels from a gifti label file into a volume file. You must specify
    exactly one mapping method option. The -nearest-vertex method uses the label
    from the vertex closest to the voxel center. The -ribbon-constrained method
    uses the same method as in -volume-to-surface-mapping, then uses the weights
    in reverse, with popularity logic to decide on a label to use.
    
    Author: Washington University School of Medicin
    
    Args:
        label: the input label file.
        surface: the surface to use coordinates from.
        volume_space: a volume file in the desired output volume space.
        volume_out: the output volume file.
        opt_nearest_vertex_distance: use the label from the vertex closest to\
            the voxel center: how far from the surface to map labels to voxels, in\
            mm.
        ribbon_constrained: use ribbon constrained mapping algorithm.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelToVolumeMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_TO_VOLUME_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-to-volume-mapping")
    cargs.append(execution.input_file(label))
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(volume_space))
    cargs.append(volume_out)
    if opt_nearest_vertex_distance is not None:
        cargs.extend([
            "-nearest-vertex",
            str(opt_nearest_vertex_distance)
        ])
    if ribbon_constrained is not None:
        cargs.extend(ribbon_constrained.run(execution))
    ret = LabelToVolumeMappingOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(volume_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_TO_VOLUME_MAPPING_METADATA",
    "LabelToVolumeMappingOutputs",
    "LabelToVolumeMappingRibbonConstrained",
    "label_to_volume_mapping",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_SET_SPACE_METADATA = Metadata(
    id="644c144fc79521282c1695ea02e9c2099bb1ae50.boutiques",
    name="volume-set-space",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class VolumeSetSpacePlumb:
    """
    set via axis order and spacing/offset.
    """
    axis_order: str
    """a string like 'XYZ' that specifies which index is along which spatial
    dimension"""
    x_spacing: float
    """change in x-coordinate from incrementing the relevant index"""
    y_spacing: float
    """change in y-coordinate from incrementing the relevant index"""
    z_spacing: float
    """change in z-coordinate from incrementing the relevant index"""
    x_offset: float
    """the x-coordinate of the first voxel"""
    y_offset: float
    """the y-coordinate of the first voxel"""
    z_offset: float
    """the z-coordinate of the first voxel"""
    
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
        cargs.append("-plumb")
        cargs.append(self.axis_order)
        cargs.append(str(self.x_spacing))
        cargs.append(str(self.y_spacing))
        cargs.append(str(self.z_spacing))
        cargs.append(str(self.x_offset))
        cargs.append(str(self.y_offset))
        cargs.append(str(self.z_offset))
        return cargs


@dataclasses.dataclass
class VolumeSetSpaceSform:
    """
    set via a nifti sform.
    """
    xi_spacing: float
    """increase in x coordinate from incrementing the i index"""
    xj_spacing: float
    """increase in x coordinate from incrementing the j index"""
    xk_spacing: float
    """increase in x coordinate from incrementing the k index"""
    x_offset: float
    """x coordinate of first voxel"""
    yi_spacing: float
    """increase in y coordinate from incrementing the i index"""
    yj_spacing: float
    """increase in y coordinate from incrementing the j index"""
    yk_spacing: float
    """increase in y coordinate from incrementing the k index"""
    y_offset: float
    """y coordinate of first voxel"""
    zi_spacing: float
    """increase in z coordinate from incrementing the i index"""
    zj_spacing: float
    """increase in z coordinate from incrementing the j index"""
    zk_spacing: float
    """increase in z coordinate from incrementing the k index"""
    z_offset: float
    """z coordinate of first voxel"""
    
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
        cargs.append("-sform")
        cargs.append(str(self.xi_spacing))
        cargs.append(str(self.xj_spacing))
        cargs.append(str(self.xk_spacing))
        cargs.append(str(self.x_offset))
        cargs.append(str(self.yi_spacing))
        cargs.append(str(self.yj_spacing))
        cargs.append(str(self.yk_spacing))
        cargs.append(str(self.y_offset))
        cargs.append(str(self.zi_spacing))
        cargs.append(str(self.zj_spacing))
        cargs.append(str(self.zk_spacing))
        cargs.append(str(self.z_offset))
        return cargs


@dataclasses.dataclass
class VolumeSetSpaceFile:
    """
    copy spacing info from volume file with matching dimensions.
    """
    volume_ref: str
    """volume file to use for reference space"""
    opt_ignore_dims: bool = False
    """copy the spacing info even if the dimensions don't match"""
    
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
        cargs.append("-file")
        cargs.append(self.volume_ref)
        if self.opt_ignore_dims:
            cargs.append("-ignore-dims")
        return cargs


class VolumeSetSpaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_set_space(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_set_space(
    volume_in: InputPathType,
    volume_out: str,
    plumb: VolumeSetSpacePlumb | None = None,
    sform: VolumeSetSpaceSform | None = None,
    file: VolumeSetSpaceFile | None = None,
    runner: Runner | None = None,
) -> VolumeSetSpaceOutputs:
    """
    Change volume space information.
    
    Writes a copy of the volume file, with the spacing information changed as
    specified. No reordering of the voxel data occurs, see -volume-reorient to
    change the volume indexing order and reorder the voxels to match. Exactly
    one of -plumb, -sform, or -file must be specified.
    
    Author: Washington University School of Medicin
    
    Args:
        volume_in: the input volume.
        volume_out: output - the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
        file: copy spacing info from volume file with matching dimensions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeSetSpaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_SET_SPACE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-set-space")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    if plumb is not None:
        cargs.extend(plumb.run(execution))
    if sform is not None:
        cargs.extend(sform.run(execution))
    if file is not None:
        cargs.extend(file.run(execution))
    ret = VolumeSetSpaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_SET_SPACE_METADATA",
    "VolumeSetSpaceFile",
    "VolumeSetSpaceOutputs",
    "VolumeSetSpacePlumb",
    "VolumeSetSpaceSform",
    "volume_set_space",
]

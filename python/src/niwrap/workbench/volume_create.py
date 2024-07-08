# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_CREATE_METADATA = Metadata(
    id="6d7a31cc395e63434667d3b3cb9fde145f269c44",
    name="volume-create",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeCreatePlumb:
    """
    set via axis order and spacing/offset
    """
    axis_order: str
    """a string like 'XYZ' that specifies which index is along which spatial
    dimension"""
    x_spacing: float | int
    """change in x-coordinate from incrementing the relevant index"""
    y_spacing: float | int
    """change in y-coordinate from incrementing the relevant index"""
    z_spacing: float | int
    """change in z-coordinate from incrementing the relevant index"""
    x_offset: float | int
    """the x-coordinate of the center of the first voxel"""
    y_offset: float | int
    """the y-coordinate of the center of the first voxel"""
    z_offset: float | int
    """the z-coordinate of the center of the first voxel"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
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
class VolumeCreateSform:
    """
    set via a nifti sform
    """
    xi_spacing: float | int
    """increase in x coordinate from incrementing the i index"""
    xj_spacing: float | int
    """increase in x coordinate from incrementing the j index"""
    xk_spacing: float | int
    """increase in x coordinate from incrementing the k index"""
    x_offset: float | int
    """x coordinate of first voxel"""
    yi_spacing: float | int
    """increase in y coordinate from incrementing the i index"""
    yj_spacing: float | int
    """increase in y coordinate from incrementing the j index"""
    yk_spacing: float | int
    """increase in y coordinate from incrementing the k index"""
    y_offset: float | int
    """y coordinate of first voxel"""
    zi_spacing: float | int
    """increase in z coordinate from incrementing the i index"""
    zj_spacing: float | int
    """increase in z coordinate from incrementing the j index"""
    zk_spacing: float | int
    """increase in z coordinate from incrementing the k index"""
    z_offset: float | int
    """z coordinate of first voxel"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
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


class VolumeCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_create(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_create(
    i_dim: int,
    j_dim: int,
    k_dim: int,
    volume_out: str,
    plumb: VolumeCreatePlumb | None = None,
    sform: VolumeCreateSform | None = None,
    runner: Runner = None,
) -> VolumeCreateOutputs:
    """
    volume-create by Washington University School of Medicin.
    
    Create a blank volume file.
    
    Creates a volume file full of zeros. Exactly one of -plumb or -sform must be
    specified.
    
    Args:
        i_dim: length of first dimension.
        j_dim: length of second dimension.
        k_dim: length of third dimension.
        volume_out: the output volume.
        plumb: set via axis order and spacing/offset.
        sform: set via a nifti sform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeCreateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_CREATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-create")
    cargs.append(str(i_dim))
    cargs.append(str(j_dim))
    cargs.append(str(k_dim))
    cargs.append(volume_out)
    if plumb is not None:
        cargs.extend(plumb.run(execution))
    if sform is not None:
        cargs.extend(sform.run(execution))
    ret = VolumeCreateOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_CREATE_METADATA",
    "VolumeCreateOutputs",
    "VolumeCreatePlumb",
    "VolumeCreateSform",
    "volume_create",
]

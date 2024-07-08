# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

VOLUME_ERODE_METADATA = Metadata(
    id="e1cb4129f0c3fe7bcb336afacfec9ea9c89e9325",
    name="volume-erode",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_erode(
    volume: InputPathType,
    distance: float | int,
    volume_out: str,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    runner: Runner = None,
) -> VolumeErodeOutputs:
    """
    volume-erode by Washington University School of Medicin.
    
    Erode a volume file.
    
    Around each voxel with a value of zero, set surrounding voxels to zero. The
    surrounding voxels are all face neighbors and all voxels within the
    specified distance (center to center).
    
    Args:
        volume: the volume to erode.
        distance: distance in mm to erode.
        volume_out: the output volume.
        opt_roi_roi_volume: assume voxels outside this roi are nonzero: volume\
            file, positive values denote voxels that have data.
        opt_subvolume_subvol: select a single subvolume to dilate: the\
            subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_ERODE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-erode")
    cargs.append(execution.input_file(volume))
    cargs.append(str(distance))
    cargs.append(volume_out)
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeErodeOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_ERODE_METADATA",
    "VolumeErodeOutputs",
    "volume_erode",
]

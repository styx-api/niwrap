# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.856509

import typing

from ..styxdefs import *


VOLUME_FIND_CLUSTERS_METADATA = Metadata(
    id="7ed9052b5b2cfaa5cef7e04ba68f567e8ff3719a",
    name="volume-find-clusters",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeFindClustersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_find_clusters(...)`.
    """
    volume_out: OutputPathType
    """the output volume"""


def volume_find_clusters(
    runner: Runner,
    volume_in: InputPathType,
    value_threshold: float | int,
    minimum_volume: float | int,
    volume_out: InputPathType,
    opt_less_than: bool = False,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_size_ratio_ratio: float | int | None = None,
    opt_distance_distance: float | int | None = None,
    opt_start_startval: float | int | None = None,
) -> VolumeFindClustersOutputs:
    """
    FILTER CLUSTERS BY VOLUME.
    
    Outputs a volume with nonzero integers for all voxels within a large enough
    cluster, and zeros elsewhere. The integers denote cluster membership (by
    default, first cluster found will use value 1, second cluster 2, etc).
    Cluster values are not reused across frames of the output, but instead keep
    counting up. By default, values greater than <value-threshold> are
    considered to be in a cluster, use -less-than to test for values less than
    the threshold. To apply this as a mask to the data, or to do more
    complicated thresholding, see -volume-math.
    
    Args:
        runner: Command runner
        volume_in: the input volume
        value_threshold: threshold for data values
        minimum_volume: threshold for cluster volume, in mm^3
        volume_out: the output volume
        opt_less_than: find values less than <value-threshold>, rather than
            greater
        opt_roi_roi_volume: select a region of interest: the roi, as a volume
            file
        opt_subvolume_subvol: select a single subvolume: the subvolume number or
            name
        opt_size_ratio_ratio: ignore clusters smaller than a given fraction of
            the largest cluster in map: fraction of the largest cluster's volume
        opt_distance_distance: ignore clusters further than a given distance
            from the largest cluster: how far from the largest cluster a cluster can
            be, edge to edge, in mm
        opt_start_startval: start labeling clusters from a value other than 1:
            the value to give the first cluster found
    Returns:
        NamedTuple of outputs (described in `VolumeFindClustersOutputs`).
    """
    execution = runner.start_execution(VOLUME_FIND_CLUSTERS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-find-clusters")
    cargs.append(execution.input_file(volume_in))
    cargs.append(str(value_threshold))
    cargs.append(str(minimum_volume))
    cargs.append(execution.input_file(volume_out))
    if opt_less_than:
        cargs.append("-less-than")
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    if opt_size_ratio_ratio is not None:
        cargs.extend(["-size-ratio", str(opt_size_ratio_ratio)])
    if opt_distance_distance is not None:
        cargs.extend(["-distance", str(opt_distance_distance)])
    if opt_start_startval is not None:
        cargs.extend(["-start", str(opt_start_startval)])
    ret = VolumeFindClustersOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret

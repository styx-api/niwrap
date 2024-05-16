# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.865072

import typing

from ..styxdefs import *


VOLUME_WEIGHTED_STATS_METADATA = Metadata(
    id="55514eee29cd3864519d2e1d5348075c2e644a54",
    name="volume-weighted-stats",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeWeightedStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_weighted_stats(...)`.
    """


def volume_weighted_stats(
    runner: Runner,
    volume_in: InputPathType,
    opt_weight_volume_weight_volume: InputPathType | None = None,
    opt_subvolume_subvolume: str | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_mean: bool = False,
    opt_stdev: bool = False,
    opt_percentile_percent: float | int | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
) -> VolumeWeightedStatsOutputs:
    """
    WEIGHTED SPATIAL STATISTICS ON A VOLUME FILE.
    
    For each subvolume of the input, a line of text is printed, resulting from
    the specified operation. If -weight-volume is not specified, each voxel's
    volume is used. Use -subvolume to only give output for a single subvolume.
    If the -roi option is used without -match-maps, then each line will contain
    as many numbers as there are maps in the ROI file, separated by tab
    characters. Exactly one of -mean, -stdev, -percentile or -sum must be
    specified.
    
    Using -sum without -weight-volume is equivalent to integrating with respect
    to volume.
    
    Args:
        runner: Command runner
        volume_in: the input volume
        opt_weight_volume_weight_volume: use weights from a volume file: volume
            file containing the weights
        opt_subvolume_subvolume: only display output for one subvolume: the
            subvolume number or name
        opt_roi_roi_volume: only consider data inside an roi: the roi, as a
            volume file
        opt_mean: compute weighted mean
        opt_stdev: compute weighted standard deviation
        opt_percentile_percent: compute weighted percentile: the percentile to
            find, must be between 0 and 100
        opt_sum: compute weighted sum
        opt_show_map_name: print map index and name before each output
    Returns:
        NamedTuple of outputs (described in `VolumeWeightedStatsOutputs`).
    """
    execution = runner.start_execution(VOLUME_WEIGHTED_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-weighted-stats")
    cargs.append(execution.input_file(volume_in))
    if opt_weight_volume_weight_volume is not None:
        cargs.extend(["-weight-volume", execution.input_file(opt_weight_volume_weight_volume)])
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_mean:
        cargs.append("-mean")
    if opt_stdev:
        cargs.append("-stdev")
    if opt_percentile_percent is not None:
        cargs.extend(["-percentile", str(opt_percentile_percent)])
    if opt_sum:
        cargs.append("-sum")
    if opt_show_map_name:
        cargs.append("-show-map-name")
    ret = VolumeWeightedStatsOutputs(
    )
    execution.run(cargs)
    return ret

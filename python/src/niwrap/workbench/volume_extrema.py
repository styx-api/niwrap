# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_EXTREMA_METADATA = Metadata(
    id="9e7499496b90bc55ce78c7099fff5c33d5bb32b6.boutiques",
    name="volume-extrema",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class VolumeExtremaPresmooth:
    """
    smooth the volume before finding extrema.
    """
    kernel: float
    """the size of the gaussian smoothing kernel in mm, as sigma by default"""
    opt_fwhm: bool = False
    """kernel size is FWHM, not sigma"""
    
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
        cargs.append("-presmooth")
        cargs.append(str(self.kernel))
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs


@dataclasses.dataclass
class VolumeExtremaThreshold:
    """
    ignore small extrema.
    """
    low: float
    """the largest value to consider for being a minimum"""
    high: float
    """the smallest value to consider for being a maximum"""
    
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
        cargs.append("-threshold")
        cargs.append(str(self.low))
        cargs.append(str(self.high))
        return cargs


class VolumeExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output extrema volume"""


def volume_extrema(
    volume_in: InputPathType,
    distance: float,
    volume_out: str,
    presmooth: VolumeExtremaPresmooth | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    threshold: VolumeExtremaThreshold | None = None,
    opt_sum_subvols: bool = False,
    opt_consolidate_mode: bool = False,
    opt_only_maxima: bool = False,
    opt_only_minima: bool = False,
    opt_subvolume_subvolume: str | None = None,
    runner: Runner | None = None,
) -> VolumeExtremaOutputs:
    """
    Find extrema in a volume file.
    
    Finds extrema in a volume file, such that no two extrema of the same type
    are within <distance> of each other. The extrema are labeled as -1 for
    minima, 1 for maxima, 0 otherwise. If -only-maxima or -only-minima is
    specified, then it will ignore extrema not of the specified type. These
    options are mutually exclusive.
    
    If -sum-subvols is specified, these extrema subvolumes are summed, and the
    output has a single subvolume with this result.
    
    By default, a datapoint is an extrema only if it is more extreme than every
    other datapoint that is within <distance> from it. If -consolidate-mode is
    used, it instead starts by finding all datapoints that are more extreme than
    their immediate neighbors, then while there are any extrema within
    <distance> of each other, take the two extrema closest to each other and
    merge them into one by a weighted average based on how many original extrema
    have been merged into each.
    
    By default, all input subvolumes are used with no smoothing, use -subvolume
    to specify a single subvolume to use, and -presmooth to smooth the input
    before finding the extrema.
    
    Author: Washington University School of Medicin
    
    Args:
        volume_in: volume file to find the extrema of.
        distance: the minimum distance between identified extrema of the same\
            type.
        volume_out: the output extrema volume.
        presmooth: smooth the volume before finding extrema.
        opt_roi_roi_volume: ignore values outside the selected area: the area\
            to find extrema in.
        threshold: ignore small extrema.
        opt_sum_subvols: output the sum of the extrema subvolumes instead of\
            each subvolume separately.
        opt_consolidate_mode: use consolidation of local minima instead of a\
            large neighborhood.
        opt_only_maxima: only find the maxima.
        opt_only_minima: only find the minima.
        opt_subvolume_subvolume: select a single subvolume to find extrema in:\
            the subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-extrema")
    cargs.append(execution.input_file(volume_in))
    cargs.append(str(distance))
    cargs.append(volume_out)
    if presmooth is not None:
        cargs.extend(presmooth.run(execution))
    if opt_roi_roi_volume is not None:
        cargs.extend([
            "-roi",
            execution.input_file(opt_roi_roi_volume)
        ])
    if threshold is not None:
        cargs.extend(threshold.run(execution))
    if opt_sum_subvols:
        cargs.append("-sum-subvols")
    if opt_consolidate_mode:
        cargs.append("-consolidate-mode")
    if opt_only_maxima:
        cargs.append("-only-maxima")
    if opt_only_minima:
        cargs.append("-only-minima")
    if opt_subvolume_subvolume is not None:
        cargs.extend([
            "-subvolume",
            opt_subvolume_subvolume
        ])
    ret = VolumeExtremaOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(volume_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_EXTREMA_METADATA",
    "VolumeExtremaOutputs",
    "VolumeExtremaPresmooth",
    "VolumeExtremaThreshold",
    "volume_extrema",
]

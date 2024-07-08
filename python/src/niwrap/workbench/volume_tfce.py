# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_TFCE_METADATA = Metadata(
    id="263d00f80ced89206d79fbb4027ba4e9c7a5fec7",
    name="volume-tfce",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeTfcePresmooth:
    """
    smooth the volume before running TFCE
    """
    kernel: float | int
    """the size of the gaussian smoothing kernel in mm, as sigma by default"""
    opt_fwhm: bool = False
    """smoothing kernel size is FWHM, not sigma"""
    
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
        cargs.append("-presmooth")
        cargs.append(str(self.kernel))
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs


@dataclasses.dataclass
class VolumeTfceParameters:
    """
    set parameters for TFCE integral
    """
    e: float | int
    """exponent for cluster volume (default 0.5)"""
    h: float | int
    """exponent for threshold value (default 2.0)"""
    
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
        cargs.append("-parameters")
        cargs.append(str(self.e))
        cargs.append(str(self.h))
        return cargs


class VolumeTfceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_tfce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_tfce(
    volume_in: InputPathType,
    volume_out: str,
    presmooth: VolumeTfcePresmooth | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    parameters: VolumeTfceParameters | None = None,
    opt_subvolume_subvolume: str | None = None,
    runner: Runner = None,
) -> VolumeTfceOutputs:
    """
    volume-tfce by Washington University School of Medicin.
    
    Do tfce on a volume file.
    
    This command does not do any statistical analysis. Please use something like
    PALM if you are just trying to do statistics on your data.
    
    Threshold-free cluster enhancement is a method to increase the relative
    value of regions that would form clusters in a standard thresholding test.
    This is accomplished by evaluating the integral of:
    
    e(h, p)^E * h^H * dh
    
    at each voxel p, where h ranges from 0 to the maximum value in the data, and
    e(h, p) is the extent of the cluster containing voxel p at threshold h.
    Negative values are similarly enhanced by negating the data, running the
    same process, and negating the result.
    
    This method is explained in: Smith SM, Nichols TE., "Threshold-free cluster
    enhancement: addressing problems of smoothing, threshold dependence and
    localisation in cluster inference." Neuroimage. 2009 Jan 1;44(1):83-98.
    PMID: 18501637.
    
    Args:
        volume_in: the volume to run TFCE on.
        volume_out: the output volume.
        presmooth: smooth the volume before running TFCE.
        opt_roi_roi_volume: select a region of interest to run TFCE on: the\
            area to run TFCE on, as a volume.
        parameters: set parameters for TFCE integral.
        opt_subvolume_subvolume: select a single subvolume: the subvolume\
            number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeTfceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_TFCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-tfce")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    if presmooth is not None:
        cargs.extend(presmooth.run(execution))
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if parameters is not None:
        cargs.extend(parameters.run(execution))
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
    ret = VolumeTfceOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_TFCE_METADATA",
    "VolumeTfceOutputs",
    "VolumeTfceParameters",
    "VolumeTfcePresmooth",
    "volume_tfce",
]

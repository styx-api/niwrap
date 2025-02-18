# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_ESTIMATE_FWHM_METADATA = Metadata(
    id="5fcfc75e7e632e5ba205f400361a1c93167286ec.boutiques",
    name="volume-estimate-fwhm",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeEstimateFwhmWholeFileParameters = typing.TypedDict('VolumeEstimateFwhmWholeFileParameters', {
    "__STYX_TYPE__": typing.Literal["whole_file"],
    "opt_demean": bool,
})
VolumeEstimateFwhmParameters = typing.TypedDict('VolumeEstimateFwhmParameters', {
    "__STYX_TYPE__": typing.Literal["volume-estimate-fwhm"],
    "volume": InputPathType,
    "opt_roi_roivol": typing.NotRequired[InputPathType | None],
    "opt_subvolume_subvol": typing.NotRequired[str | None],
    "whole_file": typing.NotRequired[VolumeEstimateFwhmWholeFileParameters | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "volume-estimate-fwhm": volume_estimate_fwhm_cargs,
        "whole_file": volume_estimate_fwhm_whole_file_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


def volume_estimate_fwhm_whole_file_params(
    opt_demean: bool = False,
) -> VolumeEstimateFwhmWholeFileParameters:
    """
    Build parameters.
    
    Args:
        opt_demean: subtract the mean image before estimating smoothness.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "whole_file",
        "opt_demean": opt_demean,
    }
    return params


def volume_estimate_fwhm_whole_file_cargs(
    params: VolumeEstimateFwhmWholeFileParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-whole-file")
    if params.get("opt_demean"):
        cargs.append("-demean")
    return cargs


class VolumeEstimateFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_estimate_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_estimate_fwhm_params(
    volume: InputPathType,
    opt_roi_roivol: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    whole_file: VolumeEstimateFwhmWholeFileParameters | None = None,
) -> VolumeEstimateFwhmParameters:
    """
    Build parameters.
    
    Args:
        volume: the input volume.
        opt_roi_roivol: use only data within an ROI: the volume to use as an\
            ROI.
        opt_subvolume_subvol: select a single subvolume to estimate smoothness\
            of: the subvolume number or name.
        whole_file: estimate for the whole file at once, not each subvolume\
            separately.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-estimate-fwhm",
        "volume": volume,
    }
    if opt_roi_roivol is not None:
        params["opt_roi_roivol"] = opt_roi_roivol
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    if whole_file is not None:
        params["whole_file"] = whole_file
    return params


def volume_estimate_fwhm_cargs(
    params: VolumeEstimateFwhmParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-estimate-fwhm")
    cargs.append(execution.input_file(params.get("volume")))
    if params.get("opt_roi_roivol") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roivol"))
        ])
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    if params.get("whole_file") is not None:
        cargs.extend(dyn_cargs(params.get("whole_file")["__STYXTYPE__"])(params.get("whole_file"), execution))
    return cargs


def volume_estimate_fwhm_outputs(
    params: VolumeEstimateFwhmParameters,
    execution: Execution,
) -> VolumeEstimateFwhmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeEstimateFwhmOutputs(
        root=execution.output_file("."),
    )
    return ret


def volume_estimate_fwhm_execute(
    params: VolumeEstimateFwhmParameters,
    execution: Execution,
) -> VolumeEstimateFwhmOutputs:
    """
    Estimate fwhm smoothness of a volume.
    
    Estimates the smoothness of the input volume in X, Y, and Z directions
    separately, printing the estimates to standard output, in mm as FWHM. If
    -subvolume or -whole-file are not specified, each subvolume is estimated and
    displayed separately.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeEstimateFwhmOutputs`).
    """
    cargs = volume_estimate_fwhm_cargs(params, execution)
    ret = volume_estimate_fwhm_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def volume_estimate_fwhm(
    volume: InputPathType,
    opt_roi_roivol: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    whole_file: VolumeEstimateFwhmWholeFileParameters | None = None,
    runner: Runner | None = None,
) -> VolumeEstimateFwhmOutputs:
    """
    Estimate fwhm smoothness of a volume.
    
    Estimates the smoothness of the input volume in X, Y, and Z directions
    separately, printing the estimates to standard output, in mm as FWHM. If
    -subvolume or -whole-file are not specified, each subvolume is estimated and
    displayed separately.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume: the input volume.
        opt_roi_roivol: use only data within an ROI: the volume to use as an\
            ROI.
        opt_subvolume_subvol: select a single subvolume to estimate smoothness\
            of: the subvolume number or name.
        whole_file: estimate for the whole file at once, not each subvolume\
            separately.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeEstimateFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_ESTIMATE_FWHM_METADATA)
    params = volume_estimate_fwhm_params(volume=volume, opt_roi_roivol=opt_roi_roivol, opt_subvolume_subvol=opt_subvolume_subvol, whole_file=whole_file)
    return volume_estimate_fwhm_execute(params, execution)


__all__ = [
    "VOLUME_ESTIMATE_FWHM_METADATA",
    "VolumeEstimateFwhmOutputs",
    "VolumeEstimateFwhmParameters",
    "VolumeEstimateFwhmWholeFileParameters",
    "volume_estimate_fwhm",
    "volume_estimate_fwhm_params",
    "volume_estimate_fwhm_whole_file_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_VOLDIFF_METADATA = Metadata(
    id="049ba42a8da17fa9e060b046adb2f02031ce75c5.boutiques",
    name="mri_voldiff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriVoldiffParameters = typing.TypedDict('MriVoldiffParameters', {
    "__STYX_TYPE__": typing.Literal["mri_voldiff"],
    "volume1": InputPathType,
    "volume2": InputPathType,
    "vox2ras_thresh": typing.NotRequired[float | None],
    "pix_thresh": typing.NotRequired[float | None],
    "allow_precision": bool,
    "allow_resolution": bool,
    "allow_vox2ras": bool,
    "debug": bool,
    "checkopts": bool,
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
        "mri_voldiff": mri_voldiff_cargs,
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


class MriVoldiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_voldiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_voldiff_params(
    volume1: InputPathType,
    volume2: InputPathType,
    vox2ras_thresh: float | None = None,
    pix_thresh: float | None = None,
    allow_precision: bool = False,
    allow_resolution: bool = False,
    allow_vox2ras: bool = False,
    debug: bool = False,
    checkopts: bool = False,
) -> MriVoldiffParameters:
    """
    Build parameters.
    
    Args:
        volume1: First input volume.
        volume2: Second input volume.
        vox2ras_thresh: Vox2RAS threshold value.
        pix_thresh: Pixel threshold value.
        allow_precision: Allow differences in precision.
        allow_resolution: Allow differences in resolution.
        allow_vox2ras: Allow differences in Vox2RAS.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_voldiff",
        "volume1": volume1,
        "volume2": volume2,
        "allow_precision": allow_precision,
        "allow_resolution": allow_resolution,
        "allow_vox2ras": allow_vox2ras,
        "debug": debug,
        "checkopts": checkopts,
    }
    if vox2ras_thresh is not None:
        params["vox2ras_thresh"] = vox2ras_thresh
    if pix_thresh is not None:
        params["pix_thresh"] = pix_thresh
    return params


def mri_voldiff_cargs(
    params: MriVoldiffParameters,
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
    cargs.append("mri_voldiff")
    cargs.extend([
        "-v1",
        execution.input_file(params.get("volume1"))
    ])
    cargs.extend([
        "-v2",
        execution.input_file(params.get("volume2"))
    ])
    if params.get("vox2ras_thresh") is not None:
        cargs.extend([
            "--vox2ras",
            str(params.get("vox2ras_thresh"))
        ])
    if params.get("pix_thresh") is not None:
        cargs.extend([
            "--pix",
            str(params.get("pix_thresh"))
        ])
    if params.get("allow_precision"):
        cargs.append("--allow-prec")
    if params.get("allow_resolution"):
        cargs.append("--allow-res")
    if params.get("allow_vox2ras"):
        cargs.append("--allow-vox2ras")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    return cargs


def mri_voldiff_outputs(
    params: MriVoldiffParameters,
    execution: Execution,
) -> MriVoldiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriVoldiffOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_voldiff_execute(
    params: MriVoldiffParameters,
    execution: Execution,
) -> MriVoldiffOutputs:
    """
    Determines whether two volumes are different in terms of pixel data, dimension,
    precision, resolution, or geometry.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriVoldiffOutputs`).
    """
    cargs = mri_voldiff_cargs(params, execution)
    ret = mri_voldiff_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_voldiff(
    volume1: InputPathType,
    volume2: InputPathType,
    vox2ras_thresh: float | None = None,
    pix_thresh: float | None = None,
    allow_precision: bool = False,
    allow_resolution: bool = False,
    allow_vox2ras: bool = False,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriVoldiffOutputs:
    """
    Determines whether two volumes are different in terms of pixel data, dimension,
    precision, resolution, or geometry.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume1: First input volume.
        volume2: Second input volume.
        vox2ras_thresh: Vox2RAS threshold value.
        pix_thresh: Pixel threshold value.
        allow_precision: Allow differences in precision.
        allow_resolution: Allow differences in resolution.
        allow_vox2ras: Allow differences in Vox2RAS.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVoldiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOLDIFF_METADATA)
    params = mri_voldiff_params(volume1=volume1, volume2=volume2, vox2ras_thresh=vox2ras_thresh, pix_thresh=pix_thresh, allow_precision=allow_precision, allow_resolution=allow_resolution, allow_vox2ras=allow_vox2ras, debug=debug, checkopts=checkopts)
    return mri_voldiff_execute(params, execution)


__all__ = [
    "MRI_VOLDIFF_METADATA",
    "MriVoldiffOutputs",
    "MriVoldiffParameters",
    "mri_voldiff",
    "mri_voldiff_params",
]

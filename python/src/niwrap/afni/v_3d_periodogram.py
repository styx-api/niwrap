# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_PERIODOGRAM_METADATA = Metadata(
    id="9a68bd8e7aa1c6c39962b274d89b8ea010ab603e.boutiques",
    name="3dPeriodogram",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dPeriodogramParameters = typing.TypedDict('V3dPeriodogramParameters', {
    "__STYX_TYPE__": typing.Literal["3dPeriodogram"],
    "prefix": typing.NotRequired[str | None],
    "taper": typing.NotRequired[float | None],
    "nfft": typing.NotRequired[float | None],
    "dataset": InputPathType,
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
        "3dPeriodogram": v_3d_periodogram_cargs,
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
        "3dPeriodogram": v_3d_periodogram_outputs,
    }.get(t)


class V3dPeriodogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_periodogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_header: OutputPathType | None
    """Output dataset header file"""
    output_brick: OutputPathType | None
    """Output dataset brick file"""


def v_3d_periodogram_params(
    dataset: InputPathType,
    prefix: str | None = None,
    taper: float | None = None,
    nfft: float | None = None,
) -> V3dPeriodogramParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset.
        prefix: Prefix for the output dataset.
        taper: Fraction of data to taper.
        nfft: Set FFT length to a specific number of points.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dPeriodogram",
        "dataset": dataset,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if taper is not None:
        params["taper"] = taper
    if nfft is not None:
        params["nfft"] = nfft
    return params


def v_3d_periodogram_cargs(
    params: V3dPeriodogramParameters,
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
    cargs.append("3dPeriodogram")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("taper") is not None:
        cargs.extend([
            "-taper",
            str(params.get("taper"))
        ])
    if params.get("nfft") is not None:
        cargs.extend([
            "-nfft",
            str(params.get("nfft"))
        ])
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_periodogram_outputs(
    params: V3dPeriodogramParameters,
    execution: Execution,
) -> V3dPeriodogramOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dPeriodogramOutputs(
        root=execution.output_file("."),
        output_header=execution.output_file(params.get("prefix") + ".HEAD") if (params.get("prefix") is not None) else None,
        output_brick=execution.output_file(params.get("prefix") + ".BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_periodogram_execute(
    params: V3dPeriodogramParameters,
    execution: Execution,
) -> V3dPeriodogramOutputs:
    """
    Computes the periodogram of each voxel time series. The periodogram is a crude
    estimate of the power spectrum.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dPeriodogramOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_periodogram_cargs(params, execution)
    ret = v_3d_periodogram_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_periodogram(
    dataset: InputPathType,
    prefix: str | None = None,
    taper: float | None = None,
    nfft: float | None = None,
    runner: Runner | None = None,
) -> V3dPeriodogramOutputs:
    """
    Computes the periodogram of each voxel time series. The periodogram is a crude
    estimate of the power spectrum.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        prefix: Prefix for the output dataset.
        taper: Fraction of data to taper.
        nfft: Set FFT length to a specific number of points.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dPeriodogramOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_PERIODOGRAM_METADATA)
    params = v_3d_periodogram_params(
        prefix=prefix,
        taper=taper,
        nfft=nfft,
        dataset=dataset,
    )
    return v_3d_periodogram_execute(params, execution)


__all__ = [
    "V3dPeriodogramOutputs",
    "V3dPeriodogramParameters",
    "V_3D_PERIODOGRAM_METADATA",
    "v_3d_periodogram",
    "v_3d_periodogram_params",
]

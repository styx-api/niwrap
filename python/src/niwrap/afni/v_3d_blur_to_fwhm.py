# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_BLUR_TO_FWHM_METADATA = Metadata(
    id="f4b40fc76ce4b806bbbbfa509356f57bb656233d.boutiques",
    name="3dBlurToFWHM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dBlurToFwhmParameters = typing.TypedDict('V3dBlurToFwhmParameters', {
    "__STYX_TYPE__": typing.Literal["3dBlurToFWHM"],
    "automask": bool,
    "blurmaster": typing.NotRequired[InputPathType | None],
    "fwhm": typing.NotRequired[float | None],
    "fwhmxy": typing.NotRequired[float | None],
    "in_file": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "prefix": typing.NotRequired[str | None],
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
        "3dBlurToFWHM": v_3d_blur_to_fwhm_cargs,
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
        "3dBlurToFWHM": v_3d_blur_to_fwhm_outputs,
    }.get(t)


class V3dBlurToFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_blur_to_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output image file name."""


def v_3d_blur_to_fwhm_params(
    in_file: InputPathType,
    automask: bool = False,
    blurmaster: InputPathType | None = None,
    fwhm: float | None = None,
    fwhmxy: float | None = None,
    mask: InputPathType | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    prefix: str | None = None,
) -> V3dBlurToFwhmParameters:
    """
    Build parameters.
    
    Args:
        in_file: The dataset that will be smoothed.
        automask: Create an automask from the input dataset.
        blurmaster: The dataset whose smoothness controls the process.
        fwhm: Blur until the 3d fwhm reaches this value (in mm).
        fwhmxy: Blur until the 2d (x,y)-plane fwhm reaches this value (in mm).
        mask: Mask dataset, if desired. voxels not in mask will be set to zero\
            in output.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        prefix: Prefix for output dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dBlurToFWHM",
        "automask": automask,
        "in_file": in_file,
    }
    if blurmaster is not None:
        params["blurmaster"] = blurmaster
    if fwhm is not None:
        params["fwhm"] = fwhm
    if fwhmxy is not None:
        params["fwhmxy"] = fwhmxy
    if mask is not None:
        params["mask"] = mask
    if outputtype is not None:
        params["outputtype"] = outputtype
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_blur_to_fwhm_cargs(
    params: V3dBlurToFwhmParameters,
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
    cargs.append("3dBlurToFWHM")
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("blurmaster") is not None:
        cargs.extend([
            "-blurmaster",
            execution.input_file(params.get("blurmaster"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "-FWHM",
            str(params.get("fwhm"))
        ])
    if params.get("fwhmxy") is not None:
        cargs.extend([
            "-FWHMxy",
            str(params.get("fwhmxy"))
        ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("in_file"))
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def v_3d_blur_to_fwhm_outputs(
    params: V3dBlurToFwhmParameters,
    execution: Execution,
) -> V3dBlurToFwhmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dBlurToFwhmOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_blur_to_fwhm_execute(
    params: V3dBlurToFwhmParameters,
    execution: Execution,
) -> V3dBlurToFwhmOutputs:
    """
    Blurs a 'master' dataset until it reaches a specified FWHM smoothness
    (approximately).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dBlurToFwhmOutputs`).
    """
    cargs = v_3d_blur_to_fwhm_cargs(params, execution)
    ret = v_3d_blur_to_fwhm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_blur_to_fwhm(
    in_file: InputPathType,
    automask: bool = False,
    blurmaster: InputPathType | None = None,
    fwhm: float | None = None,
    fwhmxy: float | None = None,
    mask: InputPathType | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dBlurToFwhmOutputs:
    """
    Blurs a 'master' dataset until it reaches a specified FWHM smoothness
    (approximately).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: The dataset that will be smoothed.
        automask: Create an automask from the input dataset.
        blurmaster: The dataset whose smoothness controls the process.
        fwhm: Blur until the 3d fwhm reaches this value (in mm).
        fwhmxy: Blur until the 2d (x,y)-plane fwhm reaches this value (in mm).
        mask: Mask dataset, if desired. voxels not in mask will be set to zero\
            in output.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        prefix: Prefix for output dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBlurToFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BLUR_TO_FWHM_METADATA)
    params = v_3d_blur_to_fwhm_params(automask=automask, blurmaster=blurmaster, fwhm=fwhm, fwhmxy=fwhmxy, in_file=in_file, mask=mask, outputtype=outputtype, prefix=prefix)
    return v_3d_blur_to_fwhm_execute(params, execution)


__all__ = [
    "V3dBlurToFwhmOutputs",
    "V3dBlurToFwhmParameters",
    "V_3D_BLUR_TO_FWHM_METADATA",
    "v_3d_blur_to_fwhm",
    "v_3d_blur_to_fwhm_params",
]

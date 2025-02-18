# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOL2SEGAVG_METADATA = Metadata(
    id="9d9d31cfe51a606166834e1114b170012714797f.boutiques",
    name="vol2segavg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Vol2segavgParameters = typing.TypedDict('Vol2segavgParameters', {
    "__STYX_TYPE__": typing.Literal["vol2segavg"],
    "output_file": str,
    "input_volume": InputPathType,
    "registration": str,
    "segmentation_file": InputPathType,
    "aparc_aseg_flag": bool,
    "subject_id": typing.NotRequired[str | None],
    "segmentation_id": typing.NotRequired[list[float] | None],
    "multiply_value": typing.NotRequired[float | None],
    "no_bb_flag": bool,
    "erode_value": typing.NotRequired[float | None],
    "dilate_value": typing.NotRequired[float | None],
    "wm_flag": bool,
    "vcsf_flag": bool,
    "xcsf_flag": bool,
    "remove_mean_flag": bool,
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
        "vol2segavg": vol2segavg_cargs,
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
        "vol2segavg": vol2segavg_outputs,
    }.get(t)


class Vol2segavgOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vol2segavg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file containing the computed average"""


def vol2segavg_params(
    output_file: str,
    input_volume: InputPathType,
    registration: str,
    segmentation_file: InputPathType,
    aparc_aseg_flag: bool = False,
    subject_id: str | None = None,
    segmentation_id: list[float] | None = None,
    multiply_value: float | None = None,
    no_bb_flag: bool = False,
    erode_value: float | None = None,
    dilate_value: float | None = None,
    wm_flag: bool = False,
    vcsf_flag: bool = False,
    xcsf_flag: bool = False,
    remove_mean_flag: bool = False,
) -> Vol2segavgParameters:
    """
    Build parameters.
    
    Args:
        output_file: Output file, can be .txt or a binary (e.g., .nii, .mgh).
        input_volume: Input volume file (e.g., vol.nii).
        registration: Registration file, can be reg.dat or use --regheader.
        segmentation_file: Segmentation file (e.g., seg.mgz).
        aparc_aseg_flag: Use aparc+aseg flag.
        subject_id: Subject ID, may be needed if --reg not supplied.
        segmentation_id: Segmentation ID(s). Multiple IDs can be supplied.
        multiply_value: Multiply input by MulVal.
        no_bb_flag: Do not use bounding box.
        erode_value: Erode segmentation.
        dilate_value: Dilate segmentation.
        wm_flag: Sets segid to 2, 41, 7, 46, 251, 252, 253, 254, 255, 77, 78,\
            79 and use aparc+aseg.
        vcsf_flag: Sets segid to 4, 5, 43, 44, 31, 63 and use aparc+aseg.
        xcsf_flag: Sets segid to 257 and use apas+head.
        remove_mean_flag: Remove mean from time course.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "vol2segavg",
        "output_file": output_file,
        "input_volume": input_volume,
        "registration": registration,
        "segmentation_file": segmentation_file,
        "aparc_aseg_flag": aparc_aseg_flag,
        "no_bb_flag": no_bb_flag,
        "wm_flag": wm_flag,
        "vcsf_flag": vcsf_flag,
        "xcsf_flag": xcsf_flag,
        "remove_mean_flag": remove_mean_flag,
    }
    if subject_id is not None:
        params["subject_id"] = subject_id
    if segmentation_id is not None:
        params["segmentation_id"] = segmentation_id
    if multiply_value is not None:
        params["multiply_value"] = multiply_value
    if erode_value is not None:
        params["erode_value"] = erode_value
    if dilate_value is not None:
        params["dilate_value"] = dilate_value
    return params


def vol2segavg_cargs(
    params: Vol2segavgParameters,
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
    cargs.append("vol2segavg")
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--reg",
        params.get("registration")
    ])
    cargs.extend([
        "--seg",
        execution.input_file(params.get("segmentation_file"))
    ])
    if params.get("aparc_aseg_flag"):
        cargs.append("--aparc+aseg")
    if params.get("subject_id") is not None:
        cargs.extend([
            "--s",
            params.get("subject_id")
        ])
    if params.get("segmentation_id") is not None:
        cargs.extend([
            "--segid",
            *map(str, params.get("segmentation_id"))
        ])
    if params.get("multiply_value") is not None:
        cargs.extend([
            "--mul",
            str(params.get("multiply_value"))
        ])
    if params.get("no_bb_flag"):
        cargs.append("--no-bb")
    if params.get("erode_value") is not None:
        cargs.extend([
            "--erode",
            str(params.get("erode_value"))
        ])
    if params.get("dilate_value") is not None:
        cargs.extend([
            "--dilate",
            str(params.get("dilate_value"))
        ])
    if params.get("wm_flag"):
        cargs.append("--wm")
    if params.get("vcsf_flag"):
        cargs.append("--vcsf")
    if params.get("xcsf_flag"):
        cargs.append("--xcsf")
    if params.get("remove_mean_flag"):
        cargs.append("--remove-mean")
    return cargs


def vol2segavg_outputs(
    params: Vol2segavgParameters,
    execution: Execution,
) -> Vol2segavgOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Vol2segavgOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def vol2segavg_execute(
    params: Vol2segavgParameters,
    execution: Execution,
) -> Vol2segavgOutputs:
    """
    Computes the average of a volume inside a given segment of a segmentation
    resampling the input volume to the segmentation space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Vol2segavgOutputs`).
    """
    cargs = vol2segavg_cargs(params, execution)
    ret = vol2segavg_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def vol2segavg(
    output_file: str,
    input_volume: InputPathType,
    registration: str,
    segmentation_file: InputPathType,
    aparc_aseg_flag: bool = False,
    subject_id: str | None = None,
    segmentation_id: list[float] | None = None,
    multiply_value: float | None = None,
    no_bb_flag: bool = False,
    erode_value: float | None = None,
    dilate_value: float | None = None,
    wm_flag: bool = False,
    vcsf_flag: bool = False,
    xcsf_flag: bool = False,
    remove_mean_flag: bool = False,
    runner: Runner | None = None,
) -> Vol2segavgOutputs:
    """
    Computes the average of a volume inside a given segment of a segmentation
    resampling the input volume to the segmentation space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_file: Output file, can be .txt or a binary (e.g., .nii, .mgh).
        input_volume: Input volume file (e.g., vol.nii).
        registration: Registration file, can be reg.dat or use --regheader.
        segmentation_file: Segmentation file (e.g., seg.mgz).
        aparc_aseg_flag: Use aparc+aseg flag.
        subject_id: Subject ID, may be needed if --reg not supplied.
        segmentation_id: Segmentation ID(s). Multiple IDs can be supplied.
        multiply_value: Multiply input by MulVal.
        no_bb_flag: Do not use bounding box.
        erode_value: Erode segmentation.
        dilate_value: Dilate segmentation.
        wm_flag: Sets segid to 2, 41, 7, 46, 251, 252, 253, 254, 255, 77, 78,\
            79 and use aparc+aseg.
        vcsf_flag: Sets segid to 4, 5, 43, 44, 31, 63 and use aparc+aseg.
        xcsf_flag: Sets segid to 257 and use apas+head.
        remove_mean_flag: Remove mean from time course.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Vol2segavgOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOL2SEGAVG_METADATA)
    params = vol2segavg_params(output_file=output_file, input_volume=input_volume, registration=registration, segmentation_file=segmentation_file, aparc_aseg_flag=aparc_aseg_flag, subject_id=subject_id, segmentation_id=segmentation_id, multiply_value=multiply_value, no_bb_flag=no_bb_flag, erode_value=erode_value, dilate_value=dilate_value, wm_flag=wm_flag, vcsf_flag=vcsf_flag, xcsf_flag=xcsf_flag, remove_mean_flag=remove_mean_flag)
    return vol2segavg_execute(params, execution)


__all__ = [
    "VOL2SEGAVG_METADATA",
    "Vol2segavgOutputs",
    "Vol2segavgParameters",
    "vol2segavg",
    "vol2segavg_params",
]

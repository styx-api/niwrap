# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SIENAX_METADATA = Metadata(
    id="24815e75293ede1a0cd5e50db5d38a8535b21678.boutiques",
    name="sienax",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SienaxParameters = typing.TypedDict('SienaxParameters', {
    "__STYX_TYPE__": typing.Literal["sienax"],
    "infile": InputPathType,
    "output_dir": typing.NotRequired[str | None],
    "debug_flag": bool,
    "bet_options": typing.NotRequired[str | None],
    "twoclass_segment_flag": bool,
    "t2_flag": bool,
    "top_threshold": typing.NotRequired[float | None],
    "bottom_threshold": typing.NotRequired[float | None],
    "regional_flag": bool,
    "lesion_mask": typing.NotRequired[InputPathType | None],
    "fast_options": typing.NotRequired[str | None],
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
        "sienax": sienax_cargs,
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
        "sienax": sienax_outputs,
    }.get(t)


class SienaxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sienax(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType | None
    """Segmentation output file"""
    report_output: OutputPathType | None
    """Summary report file"""


def sienax_params(
    infile: InputPathType,
    output_dir: str | None = None,
    debug_flag: bool = False,
    bet_options: str | None = None,
    twoclass_segment_flag: bool = False,
    t2_flag: bool = False,
    top_threshold: float | None = None,
    bottom_threshold: float | None = None,
    regional_flag: bool = False,
    lesion_mask: InputPathType | None = None,
    fast_options: str | None = None,
) -> SienaxParameters:
    """
    Build parameters.
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        output_dir: Output directory (default output is <input>_sienax).
        debug_flag: Debug (don't delete intermediate files).
        bet_options: Options to pass to BET brain extraction (inside\
            double-quotes), e.g. -B "-f 0.3".
        twoclass_segment_flag: Two-class segmentation (don't segment grey and\
            white matter separately).
        t2_flag: Input image is T2-weighted (default is T1-weighted).
        top_threshold: Ignore from t (mm) upwards in MNI152/Talairach space.
        bottom_threshold: Ignore from b (mm) downwards in MNI152/Talairach\
            space (b should probably be negative).
        regional_flag: Regional - use standard-space masks to give peripheral\
            cortex GM volume (3-class segmentation only) and ventricular CSF volume.
        lesion_mask: Use lesion (or lesion+CSF) mask to remove incorrectly\
            labelled 'grey matter' voxels.
        fast_options: Options to pass to FAST segmentation (inside\
            double-quotes), e.g. -S "I 20".
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sienax",
        "infile": infile,
        "debug_flag": debug_flag,
        "twoclass_segment_flag": twoclass_segment_flag,
        "t2_flag": t2_flag,
        "regional_flag": regional_flag,
    }
    if output_dir is not None:
        params["output_dir"] = output_dir
    if bet_options is not None:
        params["bet_options"] = bet_options
    if top_threshold is not None:
        params["top_threshold"] = top_threshold
    if bottom_threshold is not None:
        params["bottom_threshold"] = bottom_threshold
    if lesion_mask is not None:
        params["lesion_mask"] = lesion_mask
    if fast_options is not None:
        params["fast_options"] = fast_options
    return params


def sienax_cargs(
    params: SienaxParameters,
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
    cargs.append("sienax")
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("output_dir") is not None:
        cargs.extend([
            "-o",
            params.get("output_dir")
        ])
    if params.get("debug_flag"):
        cargs.append("-d")
    if params.get("bet_options") is not None:
        cargs.extend([
            "-B",
            params.get("bet_options")
        ])
    if params.get("twoclass_segment_flag"):
        cargs.append("-2")
    if params.get("t2_flag"):
        cargs.append("-t2")
    if params.get("top_threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("top_threshold"))
        ])
    if params.get("bottom_threshold") is not None:
        cargs.extend([
            "-b",
            str(params.get("bottom_threshold"))
        ])
    if params.get("regional_flag"):
        cargs.append("-r")
    if params.get("lesion_mask") is not None:
        cargs.extend([
            "-lm",
            execution.input_file(params.get("lesion_mask"))
        ])
    if params.get("fast_options") is not None:
        cargs.extend([
            "-S",
            params.get("fast_options")
        ])
    return cargs


def sienax_outputs(
    params: SienaxParameters,
    execution: Execution,
) -> SienaxOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SienaxOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(params.get("output_dir") + "/segmentation.nii.gz") if (params.get("output_dir") is not None) else None,
        report_output=execution.output_file(params.get("output_dir") + "/report.txt") if (params.get("output_dir") is not None) else None,
    )
    return ret


def sienax_execute(
    params: SienaxParameters,
    execution: Execution,
) -> SienaxOutputs:
    """
    A tool to estimate brain tissue volume from a single MR image and to compare it
    to an external standard.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SienaxOutputs`).
    """
    cargs = sienax_cargs(params, execution)
    ret = sienax_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def sienax(
    infile: InputPathType,
    output_dir: str | None = None,
    debug_flag: bool = False,
    bet_options: str | None = None,
    twoclass_segment_flag: bool = False,
    t2_flag: bool = False,
    top_threshold: float | None = None,
    bottom_threshold: float | None = None,
    regional_flag: bool = False,
    lesion_mask: InputPathType | None = None,
    fast_options: str | None = None,
    runner: Runner | None = None,
) -> SienaxOutputs:
    """
    A tool to estimate brain tissue volume from a single MR image and to compare it
    to an external standard.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        output_dir: Output directory (default output is <input>_sienax).
        debug_flag: Debug (don't delete intermediate files).
        bet_options: Options to pass to BET brain extraction (inside\
            double-quotes), e.g. -B "-f 0.3".
        twoclass_segment_flag: Two-class segmentation (don't segment grey and\
            white matter separately).
        t2_flag: Input image is T2-weighted (default is T1-weighted).
        top_threshold: Ignore from t (mm) upwards in MNI152/Talairach space.
        bottom_threshold: Ignore from b (mm) downwards in MNI152/Talairach\
            space (b should probably be negative).
        regional_flag: Regional - use standard-space masks to give peripheral\
            cortex GM volume (3-class segmentation only) and ventricular CSF volume.
        lesion_mask: Use lesion (or lesion+CSF) mask to remove incorrectly\
            labelled 'grey matter' voxels.
        fast_options: Options to pass to FAST segmentation (inside\
            double-quotes), e.g. -S "I 20".
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENAX_METADATA)
    params = sienax_params(infile=infile, output_dir=output_dir, debug_flag=debug_flag, bet_options=bet_options, twoclass_segment_flag=twoclass_segment_flag, t2_flag=t2_flag, top_threshold=top_threshold, bottom_threshold=bottom_threshold, regional_flag=regional_flag, lesion_mask=lesion_mask, fast_options=fast_options)
    return sienax_execute(params, execution)


__all__ = [
    "SIENAX_METADATA",
    "SienaxOutputs",
    "SienaxParameters",
    "sienax",
    "sienax_params",
]

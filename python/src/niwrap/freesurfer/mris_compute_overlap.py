# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_COMPUTE_OVERLAP_METADATA = Metadata(
    id="a5b5b5d3058860c230b1e6a107208c5201cd453b.boutiques",
    name="mris_compute_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisComputeOverlapParameters = typing.TypedDict('MrisComputeOverlapParameters', {
    "__STYX_TYPE__": typing.Literal["mris_compute_overlap"],
    "subject": str,
    "hemi": str,
    "surface": str,
    "annotation": str,
    "labels": list[str],
    "percentage": bool,
    "log_file": typing.NotRequired[str | None],
    "brain_volume": typing.NotRequired[InputPathType | None],
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
        "mris_compute_overlap": mris_compute_overlap_cargs,
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


class MrisComputeOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_compute_overlap_params(
    subject: str,
    hemi: str,
    surface: str,
    annotation: str,
    labels: list[str],
    percentage: bool = False,
    log_file: str | None = None,
    brain_volume: InputPathType | None = None,
) -> MrisComputeOverlapParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject name.
        hemi: Hemisphere (e.g. lh or rh).
        surface: Surface name.
        annotation: Annotation name.
        labels: Labels to compute overlap for.
        percentage: Compute brain area as a percentage of all brain labels.
        log_file: Log results to file, where %d will include label number.
        brain_volume: Load brain volume and use it to normalize areas.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_compute_overlap",
        "subject": subject,
        "hemi": hemi,
        "surface": surface,
        "annotation": annotation,
        "labels": labels,
        "percentage": percentage,
    }
    if log_file is not None:
        params["log_file"] = log_file
    if brain_volume is not None:
        params["brain_volume"] = brain_volume
    return params


def mris_compute_overlap_cargs(
    params: MrisComputeOverlapParameters,
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
    cargs.append("mris_compute_overlap")
    cargs.append(params.get("subject"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surface"))
    cargs.append(params.get("annotation"))
    cargs.extend(params.get("labels"))
    if params.get("percentage"):
        cargs.append("-p")
    if params.get("log_file") is not None:
        cargs.extend([
            "-l",
            params.get("log_file")
        ])
    if params.get("brain_volume") is not None:
        cargs.extend([
            "-b",
            execution.input_file(params.get("brain_volume"))
        ])
    return cargs


def mris_compute_overlap_outputs(
    params: MrisComputeOverlapParameters,
    execution: Execution,
) -> MrisComputeOverlapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisComputeOverlapOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_compute_overlap_execute(
    params: MrisComputeOverlapParameters,
    execution: Execution,
) -> MrisComputeOverlapOutputs:
    """
    Tool to compute the overlap between two or more labels on a cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisComputeOverlapOutputs`).
    """
    cargs = mris_compute_overlap_cargs(params, execution)
    ret = mris_compute_overlap_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_compute_overlap(
    subject: str,
    hemi: str,
    surface: str,
    annotation: str,
    labels: list[str],
    percentage: bool = False,
    log_file: str | None = None,
    brain_volume: InputPathType | None = None,
    runner: Runner | None = None,
) -> MrisComputeOverlapOutputs:
    """
    Tool to compute the overlap between two or more labels on a cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject name.
        hemi: Hemisphere (e.g. lh or rh).
        surface: Surface name.
        annotation: Annotation name.
        labels: Labels to compute overlap for.
        percentage: Compute brain area as a percentage of all brain labels.
        log_file: Log results to file, where %d will include label number.
        brain_volume: Load brain volume and use it to normalize areas.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_OVERLAP_METADATA)
    params = mris_compute_overlap_params(subject=subject, hemi=hemi, surface=surface, annotation=annotation, labels=labels, percentage=percentage, log_file=log_file, brain_volume=brain_volume)
    return mris_compute_overlap_execute(params, execution)


__all__ = [
    "MRIS_COMPUTE_OVERLAP_METADATA",
    "MrisComputeOverlapOutputs",
    "MrisComputeOverlapParameters",
    "mris_compute_overlap",
    "mris_compute_overlap_params",
]

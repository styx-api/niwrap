# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_SAVE_HISTOGRAMS_METADATA = Metadata(
    id="ee8d1ca09c1b2241dc168157801f106029c44920.boutiques",
    name="dmri_saveHistograms",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriSaveHistogramsParameters = typing.TypedDict('DmriSaveHistogramsParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_saveHistograms"],
    "parcellation": InputPathType,
    "number_of_bundles": float,
    "vtk_bundle_list": list[InputPathType],
    "output_csv": str,
    "brain_bundle_flag": bool,
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
        "dmri_saveHistograms": dmri_save_histograms_cargs,
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
        "dmri_saveHistograms": dmri_save_histograms_outputs,
    }.get(t)


class DmriSaveHistogramsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_save_histograms(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    histogram_csv: OutputPathType
    """CSV file containing the output histograms."""


def dmri_save_histograms_params(
    parcellation: InputPathType,
    number_of_bundles: float,
    vtk_bundle_list: list[InputPathType],
    output_csv: str,
    brain_bundle_flag: bool = False,
) -> DmriSaveHistogramsParameters:
    """
    Build parameters.
    
    Args:
        parcellation: Parcellation file for the tractography data.
        number_of_bundles: Number of bundles in the tractography data.
        vtk_bundle_list: List of VTK bundles for creating histograms.
        output_csv: Output CSV file to save histograms.
        brain_bundle_flag: Brain Bundle flag.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_saveHistograms",
        "parcellation": parcellation,
        "number_of_bundles": number_of_bundles,
        "vtk_bundle_list": vtk_bundle_list,
        "output_csv": output_csv,
        "brain_bundle_flag": brain_bundle_flag,
    }
    return params


def dmri_save_histograms_cargs(
    params: DmriSaveHistogramsParameters,
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
    cargs.append("dmri_saveHistograms")
    cargs.extend([
        "-p",
        execution.input_file(params.get("parcellation"))
    ])
    cargs.extend([
        "-f",
        str(params.get("number_of_bundles"))
    ])
    cargs.extend([execution.input_file(f) for f in params.get("vtk_bundle_list")])
    cargs.extend([
        "-o",
        params.get("output_csv")
    ])
    if params.get("brain_bundle_flag"):
        cargs.append("-bb")
    return cargs


def dmri_save_histograms_outputs(
    params: DmriSaveHistogramsParameters,
    execution: Execution,
) -> DmriSaveHistogramsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriSaveHistogramsOutputs(
        root=execution.output_file("."),
        histogram_csv=execution.output_file("histograms.csv"),
    )
    return ret


def dmri_save_histograms_execute(
    params: DmriSaveHistogramsParameters,
    execution: Execution,
) -> DmriSaveHistogramsOutputs:
    """
    A tool to save histograms from diffusion MRI tractography data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriSaveHistogramsOutputs`).
    """
    cargs = dmri_save_histograms_cargs(params, execution)
    ret = dmri_save_histograms_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_save_histograms(
    parcellation: InputPathType,
    number_of_bundles: float,
    vtk_bundle_list: list[InputPathType],
    output_csv: str,
    brain_bundle_flag: bool = False,
    runner: Runner | None = None,
) -> DmriSaveHistogramsOutputs:
    """
    A tool to save histograms from diffusion MRI tractography data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        parcellation: Parcellation file for the tractography data.
        number_of_bundles: Number of bundles in the tractography data.
        vtk_bundle_list: List of VTK bundles for creating histograms.
        output_csv: Output CSV file to save histograms.
        brain_bundle_flag: Brain Bundle flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriSaveHistogramsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_SAVE_HISTOGRAMS_METADATA)
    params = dmri_save_histograms_params(parcellation=parcellation, number_of_bundles=number_of_bundles, vtk_bundle_list=vtk_bundle_list, output_csv=output_csv, brain_bundle_flag=brain_bundle_flag)
    return dmri_save_histograms_execute(params, execution)


__all__ = [
    "DMRI_SAVE_HISTOGRAMS_METADATA",
    "DmriSaveHistogramsOutputs",
    "DmriSaveHistogramsParameters",
    "dmri_save_histograms",
    "dmri_save_histograms_params",
]

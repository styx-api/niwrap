# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_RELABEL_HYPOINTENSITIES_METADATA = Metadata(
    id="fdccbcea8d0b7d6372e7bb2e7e4ef70fd6f7ab26.boutiques",
    name="mri_relabel_hypointensities",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriRelabelHypointensitiesParameters = typing.TypedDict('MriRelabelHypointensitiesParameters', {
    "__STYX_TYPE__": typing.Literal["mri_relabel_hypointensities"],
    "input_aseg": InputPathType,
    "surface_directory": str,
    "output_aseg": str,
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
        "mri_relabel_hypointensities": mri_relabel_hypointensities_cargs,
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
        "mri_relabel_hypointensities": mri_relabel_hypointensities_outputs,
    }.get(t)


class MriRelabelHypointensitiesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_relabel_hypointensities(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_aseg_file: OutputPathType
    """The relabeled output aseg file"""


def mri_relabel_hypointensities_params(
    input_aseg: InputPathType,
    surface_directory: str,
    output_aseg: str,
) -> MriRelabelHypointensitiesParameters:
    """
    Build parameters.
    
    Args:
        input_aseg: Input aseg file.
        surface_directory: Directory containing surfaces.
        output_aseg: Output aseg file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_relabel_hypointensities",
        "input_aseg": input_aseg,
        "surface_directory": surface_directory,
        "output_aseg": output_aseg,
    }
    return params


def mri_relabel_hypointensities_cargs(
    params: MriRelabelHypointensitiesParameters,
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
    cargs.append("mri_relabel_hypointensities")
    cargs.append(execution.input_file(params.get("input_aseg")))
    cargs.append(params.get("surface_directory"))
    cargs.append(params.get("output_aseg"))
    return cargs


def mri_relabel_hypointensities_outputs(
    params: MriRelabelHypointensitiesParameters,
    execution: Execution,
) -> MriRelabelHypointensitiesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRelabelHypointensitiesOutputs(
        root=execution.output_file("."),
        output_aseg_file=execution.output_file(params.get("output_aseg")),
    )
    return ret


def mri_relabel_hypointensities_execute(
    params: MriRelabelHypointensitiesParameters,
    execution: Execution,
) -> MriRelabelHypointensitiesOutputs:
    """
    Tool for relabeling hypointensities in FreeSurfer's aseg files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRelabelHypointensitiesOutputs`).
    """
    params = execution.params(params)
    cargs = mri_relabel_hypointensities_cargs(params, execution)
    ret = mri_relabel_hypointensities_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_relabel_hypointensities(
    input_aseg: InputPathType,
    surface_directory: str,
    output_aseg: str,
    runner: Runner | None = None,
) -> MriRelabelHypointensitiesOutputs:
    """
    Tool for relabeling hypointensities in FreeSurfer's aseg files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_aseg: Input aseg file.
        surface_directory: Directory containing surfaces.
        output_aseg: Output aseg file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRelabelHypointensitiesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RELABEL_HYPOINTENSITIES_METADATA)
    params = mri_relabel_hypointensities_params(
        input_aseg=input_aseg,
        surface_directory=surface_directory,
        output_aseg=output_aseg,
    )
    return mri_relabel_hypointensities_execute(params, execution)


__all__ = [
    "MRI_RELABEL_HYPOINTENSITIES_METADATA",
    "MriRelabelHypointensitiesOutputs",
    "MriRelabelHypointensitiesParameters",
    "mri_relabel_hypointensities",
    "mri_relabel_hypointensities_params",
]

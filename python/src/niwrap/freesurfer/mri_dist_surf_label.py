# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_DIST_SURF_LABEL_METADATA = Metadata(
    id="72b4cdbb35a27d1559099cff0310255f2417fec4.boutiques",
    name="mri_dist_surf_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriDistSurfLabelParameters = typing.TypedDict('MriDistSurfLabelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_dist_surf_label"],
    "surface": InputPathType,
    "label_file": InputPathType,
    "output": str,
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
        "mri_dist_surf_label": mri_dist_surf_label_cargs,
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
        "mri_dist_surf_label": mri_dist_surf_label_outputs,
    }.get(t)


class MriDistSurfLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_dist_surf_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """Output file containing computed distances."""


def mri_dist_surf_label_params(
    surface: InputPathType,
    label_file: InputPathType,
    output: str,
) -> MriDistSurfLabelParameters:
    """
    Build parameters.
    
    Args:
        surface: Input surface file.
        label_file: Input label file.
        output: Output file for distances.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_dist_surf_label",
        "surface": surface,
        "label_file": label_file,
        "output": output,
    }
    return params


def mri_dist_surf_label_cargs(
    params: MriDistSurfLabelParameters,
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
    cargs.append("mri_dist_surf_label")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("label_file")))
    cargs.append(params.get("output"))
    return cargs


def mri_dist_surf_label_outputs(
    params: MriDistSurfLabelParameters,
    execution: Execution,
) -> MriDistSurfLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriDistSurfLabelOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def mri_dist_surf_label_execute(
    params: MriDistSurfLabelParameters,
    execution: Execution,
) -> MriDistSurfLabelOutputs:
    """
    Computes distances from input surface to label points or waypoints.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriDistSurfLabelOutputs`).
    """
    cargs = mri_dist_surf_label_cargs(params, execution)
    ret = mri_dist_surf_label_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_dist_surf_label(
    surface: InputPathType,
    label_file: InputPathType,
    output: str,
    runner: Runner | None = None,
) -> MriDistSurfLabelOutputs:
    """
    Computes distances from input surface to label points or waypoints.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface file.
        label_file: Input label file.
        output: Output file for distances.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDistSurfLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DIST_SURF_LABEL_METADATA)
    params = mri_dist_surf_label_params(surface=surface, label_file=label_file, output=output)
    return mri_dist_surf_label_execute(params, execution)


__all__ = [
    "MRI_DIST_SURF_LABEL_METADATA",
    "MriDistSurfLabelOutputs",
    "MriDistSurfLabelParameters",
    "mri_dist_surf_label",
    "mri_dist_surf_label_params",
]

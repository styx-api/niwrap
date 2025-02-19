# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAP_ALL_LABELS_METADATA = Metadata(
    id="7e86c136e5dca86f55d15560397ec44a7f6e3348.boutiques",
    name="map_all_labels",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MapAllLabelsParameters = typing.TypedDict('MapAllLabelsParameters', {
    "__STYX_TYPE__": typing.Literal["map_all_labels"],
    "which": str,
    "fname": str,
    "hemi": str,
    "spherical_surf": str,
    "subjects": list[str],
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
        "map_all_labels": map_all_labels_cargs,
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
        "map_all_labels": map_all_labels_outputs,
    }.get(t)


class MapAllLabelsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `map_all_labels(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output of the mapping process"""


def map_all_labels_params(
    which: str,
    fname: str,
    hemi: str,
    spherical_surf: str,
    subjects: list[str],
    output: str,
) -> MapAllLabelsParameters:
    """
    Build parameters.
    
    Args:
        which: Select what to map (e.g. coords, label, vals, curv, area).
        fname: Filename related to the mapping.
        hemi: Hemisphere to process (e.g. lh, rh).
        spherical_surf: Spherical surface to use.
        subjects: List of subject identifiers.
        output: Output path.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "map_all_labels",
        "which": which,
        "fname": fname,
        "hemi": hemi,
        "spherical_surf": spherical_surf,
        "subjects": subjects,
        "output": output,
    }
    return params


def map_all_labels_cargs(
    params: MapAllLabelsParameters,
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
    cargs.append("map_all_labels")
    cargs.append(params.get("which"))
    cargs.append(params.get("fname"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("spherical_surf"))
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output"))
    return cargs


def map_all_labels_outputs(
    params: MapAllLabelsParameters,
    execution: Execution,
) -> MapAllLabelsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MapAllLabelsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output")),
    )
    return ret


def map_all_labels_execute(
    params: MapAllLabelsParameters,
    execution: Execution,
) -> MapAllLabelsOutputs:
    """
    Tool for mapping labels onto subject surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MapAllLabelsOutputs`).
    """
    params = execution.params(params)
    cargs = map_all_labels_cargs(params, execution)
    ret = map_all_labels_outputs(params, execution)
    execution.run(cargs)
    return ret


def map_all_labels(
    which: str,
    fname: str,
    hemi: str,
    spherical_surf: str,
    subjects: list[str],
    output: str,
    runner: Runner | None = None,
) -> MapAllLabelsOutputs:
    """
    Tool for mapping labels onto subject surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        which: Select what to map (e.g. coords, label, vals, curv, area).
        fname: Filename related to the mapping.
        hemi: Hemisphere to process (e.g. lh, rh).
        spherical_surf: Spherical surface to use.
        subjects: List of subject identifiers.
        output: Output path.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MapAllLabelsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAP_ALL_LABELS_METADATA)
    params = map_all_labels_params(
        which=which,
        fname=fname,
        hemi=hemi,
        spherical_surf=spherical_surf,
        subjects=subjects,
        output=output,
    )
    return map_all_labels_execute(params, execution)


__all__ = [
    "MAP_ALL_LABELS_METADATA",
    "MapAllLabelsOutputs",
    "MapAllLabelsParameters",
    "map_all_labels",
    "map_all_labels_params",
]

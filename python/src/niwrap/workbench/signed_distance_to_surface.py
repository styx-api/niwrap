# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SIGNED_DISTANCE_TO_SURFACE_METADATA = Metadata(
    id="8c742ccb7ded65823db6e22f82d38fb5ff077472.boutiques",
    name="signed-distance-to-surface",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SignedDistanceToSurfaceParameters = typing.TypedDict('SignedDistanceToSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["signed-distance-to-surface"],
    "surface_comp": InputPathType,
    "surface_ref": InputPathType,
    "metric": str,
    "opt_winding_method": typing.NotRequired[str | None],
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
        "signed-distance-to-surface": signed_distance_to_surface_cargs,
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
        "signed-distance-to-surface": signed_distance_to_surface_outputs,
    }.get(t)


class SignedDistanceToSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `signed_distance_to_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric: OutputPathType
    """the output metric"""


def signed_distance_to_surface_params(
    surface_comp: InputPathType,
    surface_ref: InputPathType,
    metric: str,
    opt_winding_method: str | None = None,
) -> SignedDistanceToSurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface_comp: the comparison surface to measure the signed distance on.
        surface_ref: the reference surface that defines the signed distance\
            function.
        metric: the output metric.
        opt_winding_method: winding method for point inside surface test: name\
            of the method (default EVEN_ODD).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "signed-distance-to-surface",
        "surface_comp": surface_comp,
        "surface_ref": surface_ref,
        "metric": metric,
    }
    if opt_winding_method is not None:
        params["opt_winding_method"] = opt_winding_method
    return params


def signed_distance_to_surface_cargs(
    params: SignedDistanceToSurfaceParameters,
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
    cargs.append("wb_command")
    cargs.append("-signed-distance-to-surface")
    cargs.append(execution.input_file(params.get("surface_comp")))
    cargs.append(execution.input_file(params.get("surface_ref")))
    cargs.append(params.get("metric"))
    if params.get("opt_winding_method") is not None:
        cargs.extend([
            "-winding",
            params.get("opt_winding_method")
        ])
    return cargs


def signed_distance_to_surface_outputs(
    params: SignedDistanceToSurfaceParameters,
    execution: Execution,
) -> SignedDistanceToSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SignedDistanceToSurfaceOutputs(
        root=execution.output_file("."),
        metric=execution.output_file(params.get("metric")),
    )
    return ret


def signed_distance_to_surface_execute(
    params: SignedDistanceToSurfaceParameters,
    execution: Execution,
) -> SignedDistanceToSurfaceOutputs:
    """
    Compute signed distance from one surface to another.
    
    Compute the signed distance function of the reference surface at every
    vertex on the comparison surface. NOTE: this relation is NOT symmetric, the
    line from a vertex to the closest point on the 'ref' surface (the one that
    defines the signed distance function) will only align with the normal of the
    'ref' surface. Valid specifiers for winding methods are as follows:
    
    EVEN_ODD (default)
    NEGATIVE
    NONZERO
    NORMALS
    
    The NORMALS method uses the normals of triangles and edges, or the closest
    triangle hit by a ray from the point. This method may be slightly faster,
    but is only reliable for a closed surface that does not cross through
    itself. All other methods count entry (positive) and exit (negative)
    crossings of a vertical ray from the point, then counts as inside if the
    total is odd, negative, or nonzero, respectively.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SignedDistanceToSurfaceOutputs`).
    """
    cargs = signed_distance_to_surface_cargs(params, execution)
    ret = signed_distance_to_surface_outputs(params, execution)
    execution.run(cargs)
    return ret


def signed_distance_to_surface(
    surface_comp: InputPathType,
    surface_ref: InputPathType,
    metric: str,
    opt_winding_method: str | None = None,
    runner: Runner | None = None,
) -> SignedDistanceToSurfaceOutputs:
    """
    Compute signed distance from one surface to another.
    
    Compute the signed distance function of the reference surface at every
    vertex on the comparison surface. NOTE: this relation is NOT symmetric, the
    line from a vertex to the closest point on the 'ref' surface (the one that
    defines the signed distance function) will only align with the normal of the
    'ref' surface. Valid specifiers for winding methods are as follows:
    
    EVEN_ODD (default)
    NEGATIVE
    NONZERO
    NORMALS
    
    The NORMALS method uses the normals of triangles and edges, or the closest
    triangle hit by a ray from the point. This method may be slightly faster,
    but is only reliable for a closed surface that does not cross through
    itself. All other methods count entry (positive) and exit (negative)
    crossings of a vertical ray from the point, then counts as inside if the
    total is odd, negative, or nonzero, respectively.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_comp: the comparison surface to measure the signed distance on.
        surface_ref: the reference surface that defines the signed distance\
            function.
        metric: the output metric.
        opt_winding_method: winding method for point inside surface test: name\
            of the method (default EVEN_ODD).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SignedDistanceToSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGNED_DISTANCE_TO_SURFACE_METADATA)
    params = signed_distance_to_surface_params(surface_comp=surface_comp, surface_ref=surface_ref, metric=metric, opt_winding_method=opt_winding_method)
    return signed_distance_to_surface_execute(params, execution)


__all__ = [
    "SIGNED_DISTANCE_TO_SURFACE_METADATA",
    "SignedDistanceToSurfaceOutputs",
    "SignedDistanceToSurfaceParameters",
    "signed_distance_to_surface",
    "signed_distance_to_surface_params",
]

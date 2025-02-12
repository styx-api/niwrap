# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_QUAL_METADATA = Metadata(
    id="26998942504c3f8916ff5647525cc6689776bf8d.boutiques",
    name="SurfQual",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfQualParameters = typing.TypedDict('SurfQualParameters', {
    "__STYX_TYPE__": typing.Literal["SurfQual"],
    "spec_file": InputPathType,
    "surface_a": list[InputPathType],
    "sphere_flag": bool,
    "summary_flag": bool,
    "self_intersect_flag": bool,
    "output_prefix": typing.NotRequired[str | None],
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
        "SurfQual": surf_qual_cargs,
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
        "SurfQual": surf_qual_outputs,
    }.get(t)


class SurfQualOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_qual(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dist_output: OutputPathType | None
    """File containing distances of nodes from the surface's center."""
    dist_color_output: OutputPathType | None
    """Colorized file containing distances of nodes from the surface's
    center."""
    bad_nodes_output: OutputPathType | None
    """File containing nodes with bad dot product values."""
    bad_nodes_color_output: OutputPathType | None
    """Colorized file containing nodes with bad dot product values."""
    dotprod_output: OutputPathType | None
    """File containing dot product values for all nodes."""
    dotprod_color_output: OutputPathType | None
    """Colorized file containing dot product values for all nodes."""
    intersect_nodes_output: OutputPathType | None
    """File containing indices of nodes forming segments that intersect the
    surface."""


def surf_qual_params(
    spec_file: InputPathType,
    surface_a: list[InputPathType],
    sphere_flag: bool = False,
    summary_flag: bool = False,
    self_intersect_flag: bool = False,
    output_prefix: str | None = None,
) -> SurfQualParameters:
    """
    Build parameters.
    
    Args:
        spec_file: Spec file containing input surfaces.
        surface_a: Name of input surface A.
        sphere_flag: Indicates that surfaces read are spherical.
        summary_flag: Provide summary of results to stdout.
        self_intersect_flag: Check if surface is self intersecting.
        output_prefix: Prefix of output files. Default is the surface's label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfQual",
        "spec_file": spec_file,
        "surface_a": surface_a,
        "sphere_flag": sphere_flag,
        "summary_flag": summary_flag,
        "self_intersect_flag": self_intersect_flag,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def surf_qual_cargs(
    params: SurfQualParameters,
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
    cargs.append("SurfQual")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("spec_file"))
    ])
    cargs.extend([
        "-surf_A",
        *[execution.input_file(f) for f in params.get("surface_a")]
    ])
    if params.get("sphere_flag"):
        cargs.append("-sphere")
    if params.get("summary_flag"):
        cargs.append("-summary")
    if params.get("self_intersect_flag"):
        cargs.append("-self_intersect")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    return cargs


def surf_qual_outputs(
    params: SurfQualParameters,
    execution: Execution,
) -> SurfQualOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfQualOutputs(
        root=execution.output_file("."),
        dist_output=execution.output_file(params.get("output_prefix") + "_Dist.1D.dset") if (params.get("output_prefix") is not None) else None,
        dist_color_output=execution.output_file(params.get("output_prefix") + "_Dist.1D.col") if (params.get("output_prefix") is not None) else None,
        bad_nodes_output=execution.output_file(params.get("output_prefix") + "_BadNodes.1D.dset") if (params.get("output_prefix") is not None) else None,
        bad_nodes_color_output=execution.output_file(params.get("output_prefix") + "_BadNodes.1D.col") if (params.get("output_prefix") is not None) else None,
        dotprod_output=execution.output_file(params.get("output_prefix") + "_dotprod.1D.dset") if (params.get("output_prefix") is not None) else None,
        dotprod_color_output=execution.output_file(params.get("output_prefix") + "_dotprod.1D.col") if (params.get("output_prefix") is not None) else None,
        intersect_nodes_output=execution.output_file(params.get("output_prefix") + "_IntersNodes.1D.dset") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def surf_qual_execute(
    params: SurfQualParameters,
    execution: Execution,
) -> SurfQualOutputs:
    """
    A program to check the quality of surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfQualOutputs`).
    """
    cargs = surf_qual_cargs(params, execution)
    ret = surf_qual_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_qual(
    spec_file: InputPathType,
    surface_a: list[InputPathType],
    sphere_flag: bool = False,
    summary_flag: bool = False,
    self_intersect_flag: bool = False,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> SurfQualOutputs:
    """
    A program to check the quality of surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_file: Spec file containing input surfaces.
        surface_a: Name of input surface A.
        sphere_flag: Indicates that surfaces read are spherical.
        summary_flag: Provide summary of results to stdout.
        self_intersect_flag: Check if surface is self intersecting.
        output_prefix: Prefix of output files. Default is the surface's label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfQualOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_QUAL_METADATA)
    params = surf_qual_params(spec_file=spec_file, surface_a=surface_a, sphere_flag=sphere_flag, summary_flag=summary_flag, self_intersect_flag=self_intersect_flag, output_prefix=output_prefix)
    return surf_qual_execute(params, execution)


__all__ = [
    "SURF_QUAL_METADATA",
    "SurfQualOutputs",
    "SurfQualParameters",
    "surf_qual",
    "surf_qual_params",
]

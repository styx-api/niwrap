# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CREATE_ICOSAHEDRON_METADATA = Metadata(
    id="0c5ed33e6d9371f02ee960933e1903bb9350e470.boutiques",
    name="CreateIcosahedron",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


CreateIcosahedronParameters = typing.TypedDict('CreateIcosahedronParameters', {
    "__STYX_TYPE__": typing.Literal["CreateIcosahedron"],
    "rad": typing.NotRequired[float | None],
    "rec_depth": typing.NotRequired[float | None],
    "lin_depth": typing.NotRequired[float | None],
    "min_nodes": typing.NotRequired[float | None],
    "nums": bool,
    "nums_quiet": bool,
    "center_coordinates": typing.NotRequired[list[float] | None],
    "to_sphere": bool,
    "output_prefix": typing.NotRequired[str | None],
    "help": bool,
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
        "CreateIcosahedron": create_icosahedron_cargs,
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


class CreateIcosahedronOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_icosahedron(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def create_icosahedron_params(
    rad: float | None = None,
    rec_depth: float | None = None,
    lin_depth: float | None = None,
    min_nodes: float | None = None,
    nums: bool = False,
    nums_quiet: bool = False,
    center_coordinates: list[float] | None = None,
    to_sphere: bool = False,
    output_prefix: str | None = None,
    help_: bool = False,
) -> CreateIcosahedronParameters:
    """
    Build parameters.
    
    Args:
        rad: Size of icosahedron.
        rec_depth: Recursive tessellation depth for icosahedron.
        lin_depth: Number of edge divides for linear icosahedron tessellation.
        min_nodes: Automatically select the -ld value which produces an\
            icosahedron of at least MIN_NODES nodes.
        nums: Output the number of nodes (vertices), triangles, edges, total\
            volume, and total area then quit.
        nums_quiet: Output numbers in a less verbose manner.
        center_coordinates: Coordinates of the center of the icosahedron.
        to_sphere: Project nodes to sphere.
        output_prefix: Prefix for output files.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "CreateIcosahedron",
        "nums": nums,
        "nums_quiet": nums_quiet,
        "to_sphere": to_sphere,
        "help": help_,
    }
    if rad is not None:
        params["rad"] = rad
    if rec_depth is not None:
        params["rec_depth"] = rec_depth
    if lin_depth is not None:
        params["lin_depth"] = lin_depth
    if min_nodes is not None:
        params["min_nodes"] = min_nodes
    if center_coordinates is not None:
        params["center_coordinates"] = center_coordinates
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def create_icosahedron_cargs(
    params: CreateIcosahedronParameters,
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
    cargs.append("CreateIcosahedron")
    if params.get("rad") is not None:
        cargs.extend([
            "-rad",
            str(params.get("rad"))
        ])
    if params.get("rec_depth") is not None:
        cargs.extend([
            "-rd",
            str(params.get("rec_depth"))
        ])
    if params.get("lin_depth") is not None:
        cargs.extend([
            "-ld",
            str(params.get("lin_depth"))
        ])
    if params.get("min_nodes") is not None:
        cargs.extend([
            "-min_nodes",
            str(params.get("min_nodes"))
        ])
    if params.get("nums"):
        cargs.append("-nums")
    if params.get("nums_quiet"):
        cargs.append("-nums_quiet")
    if params.get("center_coordinates") is not None:
        cargs.extend([
            "-ctr",
            *map(str, params.get("center_coordinates"))
        ])
    if params.get("to_sphere"):
        cargs.append("-tosphere")
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("help"):
        cargs.append("-help")
    return cargs


def create_icosahedron_outputs(
    params: CreateIcosahedronParameters,
    execution: Execution,
) -> CreateIcosahedronOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CreateIcosahedronOutputs(
        root=execution.output_file("."),
    )
    return ret


def create_icosahedron_execute(
    params: CreateIcosahedronParameters,
    execution: Execution,
) -> CreateIcosahedronOutputs:
    """
    Tool to create an icosahedron with optional tessellation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CreateIcosahedronOutputs`).
    """
    params = execution.params(params)
    cargs = create_icosahedron_cargs(params, execution)
    ret = create_icosahedron_outputs(params, execution)
    execution.run(cargs)
    return ret


def create_icosahedron(
    rad: float | None = None,
    rec_depth: float | None = None,
    lin_depth: float | None = None,
    min_nodes: float | None = None,
    nums: bool = False,
    nums_quiet: bool = False,
    center_coordinates: list[float] | None = None,
    to_sphere: bool = False,
    output_prefix: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> CreateIcosahedronOutputs:
    """
    Tool to create an icosahedron with optional tessellation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        rad: Size of icosahedron.
        rec_depth: Recursive tessellation depth for icosahedron.
        lin_depth: Number of edge divides for linear icosahedron tessellation.
        min_nodes: Automatically select the -ld value which produces an\
            icosahedron of at least MIN_NODES nodes.
        nums: Output the number of nodes (vertices), triangles, edges, total\
            volume, and total area then quit.
        nums_quiet: Output numbers in a less verbose manner.
        center_coordinates: Coordinates of the center of the icosahedron.
        to_sphere: Project nodes to sphere.
        output_prefix: Prefix for output files.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateIcosahedronOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CREATE_ICOSAHEDRON_METADATA)
    params = create_icosahedron_params(
        rad=rad,
        rec_depth=rec_depth,
        lin_depth=lin_depth,
        min_nodes=min_nodes,
        nums=nums,
        nums_quiet=nums_quiet,
        center_coordinates=center_coordinates,
        to_sphere=to_sphere,
        output_prefix=output_prefix,
        help_=help_,
    )
    return create_icosahedron_execute(params, execution)


__all__ = [
    "CREATE_ICOSAHEDRON_METADATA",
    "CreateIcosahedronOutputs",
    "CreateIcosahedronParameters",
    "create_icosahedron",
    "create_icosahedron_params",
]

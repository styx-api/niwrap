# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_RANK_METADATA = Metadata(
    id="05c7817af68d191ce35831e8d5e9772041297b36.boutiques",
    name="3dRank",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dRankParameters = typing.TypedDict('V3dRankParameters', {
    "__STYX_TYPE__": typing.Literal["3dRank"],
    "input_datasets": list[InputPathType],
    "output_prefix": typing.NotRequired[str | None],
    "version_info": bool,
    "help_info": bool,
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
        "3dRank": v_3d_rank_cargs,
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
        "3dRank": v_3d_rank_outputs,
    }.get(t)


class V3dRankOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_rank(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType | None
    """Main output dataset in AFNI format (.HEAD file)"""
    output_dataset_brik: OutputPathType | None
    """Main output dataset in AFNI format (.BRIK file)"""
    rank_map_file: OutputPathType | None
    """Rank map 1D file showing the mapping from the rank to the integral values
    in the input dataset"""


def v_3d_rank_params(
    input_datasets: list[InputPathType],
    output_prefix: str | None = None,
    version_info: bool = False,
    help_info: bool = False,
) -> V3dRankParameters:
    """
    Build parameters.
    
    Args:
        input_datasets: Input datasets. Acceptable data types are: byte, short,\
            and floats.
        output_prefix: Output prefix. If you have multiple datasets on input,\
            the prefix is preceded by r00., r01., etc. If no prefix is given, the\
            default is rank.DATASET1, rank.DATASET2, etc.
        version_info: Print author and version info.
        help_info: Print this help screen.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dRank",
        "input_datasets": input_datasets,
        "version_info": version_info,
        "help_info": help_info,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def v_3d_rank_cargs(
    params: V3dRankParameters,
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
    cargs.append("3dRank")
    cargs.extend([execution.input_file(f) for f in params.get("input_datasets")])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("version_info"):
        cargs.append("-ver")
    if params.get("help_info"):
        cargs.append("-help")
    return cargs


def v_3d_rank_outputs(
    params: V3dRankParameters,
    execution: Execution,
) -> V3dRankOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRankOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(params.get("output_prefix") + "*.HEAD") if (params.get("output_prefix") is not None) else None,
        output_dataset_brik=execution.output_file(params.get("output_prefix") + "*.BRIK") if (params.get("output_prefix") is not None) else None,
        rank_map_file=execution.output_file(params.get("output_prefix") + "*.1D") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_rank_execute(
    params: V3dRankParameters,
    execution: Execution,
) -> V3dRankOutputs:
    """
    Replaces voxel values by their rank in the set of values collected over all
    voxels in all input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRankOutputs`).
    """
    cargs = v_3d_rank_cargs(params, execution)
    ret = v_3d_rank_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_rank(
    input_datasets: list[InputPathType],
    output_prefix: str | None = None,
    version_info: bool = False,
    help_info: bool = False,
    runner: Runner | None = None,
) -> V3dRankOutputs:
    """
    Replaces voxel values by their rank in the set of values collected over all
    voxels in all input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_datasets: Input datasets. Acceptable data types are: byte, short,\
            and floats.
        output_prefix: Output prefix. If you have multiple datasets on input,\
            the prefix is preceded by r00., r01., etc. If no prefix is given, the\
            default is rank.DATASET1, rank.DATASET2, etc.
        version_info: Print author and version info.
        help_info: Print this help screen.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRankOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_RANK_METADATA)
    params = v_3d_rank_params(input_datasets=input_datasets, output_prefix=output_prefix, version_info=version_info, help_info=help_info)
    return v_3d_rank_execute(params, execution)


__all__ = [
    "V3dRankOutputs",
    "V3dRankParameters",
    "V_3D_RANK_METADATA",
    "v_3d_rank",
    "v_3d_rank_params",
]

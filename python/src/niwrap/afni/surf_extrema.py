# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_EXTREMA_METADATA = Metadata(
    id="84b854a87242a5d67c86897020fb70cd6c8e1945.boutiques",
    name="SurfExtrema",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfExtremaParameters = typing.TypedDict('SurfExtremaParameters', {
    "__STYX_TYPE__": typing.Literal["SurfExtrema"],
    "input": typing.NotRequired[InputPathType | None],
    "hood": typing.NotRequired[float | None],
    "thresh": typing.NotRequired[float | None],
    "gthresh": typing.NotRequired[float | None],
    "gscale": typing.NotRequired[typing.Literal["NONE", "LMEAN", "GMEAN"] | None],
    "extype": typing.NotRequired[typing.Literal["MAX", "MIN", "ABS"] | None],
    "prefix": str,
    "table": typing.NotRequired[str | None],
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
        "SurfExtrema": surf_extrema_cargs,
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
        "SurfExtrema": surf_extrema_outputs,
    }.get(t)


class SurfExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_grd: OutputPathType
    """Output file containing the scaled average gradient values."""
    output_ext: OutputPathType
    """Output file containing the nodes with maximum values."""


def surf_extrema_params(
    prefix: str,
    input_: InputPathType | None = None,
    hood: float | None = None,
    thresh: float | None = None,
    gthresh: float | None = None,
    gscale: typing.Literal["NONE", "LMEAN", "GMEAN"] | None = None,
    extype: typing.Literal["MAX", "MIN", "ABS"] | None = None,
    table: str | None = None,
) -> SurfExtremaParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for the output datasets.
        input_: Input dataset in which Extrema are to be identified.
        hood: Neighborhood radius (R) in mm. Default is 8 mm.
        thresh: Do not consider nodes with value less than this threshold.\
            Default is 0.
        gthresh: Do not consider nodes with gradient less than this threshold.\
            Default is 0.01.
        gscale: Scaling to apply to gradient computation.
        extype: Find maxima, minima, or extrema. Options are MAX (default),\
            MIN, ABS.
        table: Name of file in which to store a record of the extrema found.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfExtrema",
        "prefix": prefix,
    }
    if input_ is not None:
        params["input"] = input_
    if hood is not None:
        params["hood"] = hood
    if thresh is not None:
        params["thresh"] = thresh
    if gthresh is not None:
        params["gthresh"] = gthresh
    if gscale is not None:
        params["gscale"] = gscale
    if extype is not None:
        params["extype"] = extype
    if table is not None:
        params["table"] = table
    return params


def surf_extrema_cargs(
    params: SurfExtremaParameters,
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
    cargs.append("SurfExtrema")
    if params.get("input") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("input"))
        ])
    if params.get("hood") is not None:
        cargs.extend([
            "-nbhd_rad",
            str(params.get("hood"))
        ])
    if params.get("thresh") is not None:
        cargs.extend([
            "-thresh",
            str(params.get("thresh"))
        ])
    if params.get("gthresh") is not None:
        cargs.extend([
            "-gthresh",
            str(params.get("gthresh"))
        ])
    if params.get("gscale") is not None:
        cargs.extend([
            "-gscale",
            params.get("gscale")
        ])
    if params.get("extype") is not None:
        cargs.extend([
            "-extype",
            params.get("extype")
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("table") is not None:
        cargs.extend([
            "-table",
            params.get("table")
        ])
    return cargs


def surf_extrema_outputs(
    params: SurfExtremaParameters,
    execution: Execution,
) -> SurfExtremaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfExtremaOutputs(
        root=execution.output_file("."),
        output_grd=execution.output_file(params.get("prefix") + ".grd"),
        output_ext=execution.output_file(params.get("prefix") + ".ext"),
    )
    return ret


def surf_extrema_execute(
    params: SurfExtremaParameters,
    execution: Execution,
) -> SurfExtremaOutputs:
    """
    A program finding the local extrema in a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfExtremaOutputs`).
    """
    cargs = surf_extrema_cargs(params, execution)
    ret = surf_extrema_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def surf_extrema(
    prefix: str,
    input_: InputPathType | None = None,
    hood: float | None = None,
    thresh: float | None = None,
    gthresh: float | None = None,
    gscale: typing.Literal["NONE", "LMEAN", "GMEAN"] | None = None,
    extype: typing.Literal["MAX", "MIN", "ABS"] | None = None,
    table: str | None = None,
    runner: Runner | None = None,
) -> SurfExtremaOutputs:
    """
    A program finding the local extrema in a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for the output datasets.
        input_: Input dataset in which Extrema are to be identified.
        hood: Neighborhood radius (R) in mm. Default is 8 mm.
        thresh: Do not consider nodes with value less than this threshold.\
            Default is 0.
        gthresh: Do not consider nodes with gradient less than this threshold.\
            Default is 0.01.
        gscale: Scaling to apply to gradient computation.
        extype: Find maxima, minima, or extrema. Options are MAX (default),\
            MIN, ABS.
        table: Name of file in which to store a record of the extrema found.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_EXTREMA_METADATA)
    params = surf_extrema_params(input_=input_, hood=hood, thresh=thresh, gthresh=gthresh, gscale=gscale, extype=extype, prefix=prefix, table=table)
    return surf_extrema_execute(params, execution)


__all__ = [
    "SURF_EXTREMA_METADATA",
    "SurfExtremaOutputs",
    "SurfExtremaParameters",
    "surf_extrema",
    "surf_extrema_params",
]

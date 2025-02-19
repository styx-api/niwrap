# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLROI_METADATA = Metadata(
    id="45183ec4bb8a750b44a18fccbebc359100289e66.boutiques",
    name="fslroi",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslroiParameters = typing.TypedDict('FslroiParameters', {
    "__STYX_TYPE__": typing.Literal["fslroi"],
    "infile": InputPathType,
    "outfile": str,
    "xmin": typing.NotRequired[float | None],
    "xsize": typing.NotRequired[float | None],
    "ymin": typing.NotRequired[float | None],
    "ysize": typing.NotRequired[float | None],
    "zmin": typing.NotRequired[float | None],
    "zsize": typing.NotRequired[float | None],
    "tmin": typing.NotRequired[float | None],
    "tsize": typing.NotRequired[float | None],
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
        "fslroi": fslroi_cargs,
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
        "fslroi": fslroi_outputs,
    }.get(t)


class FslroiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslroi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the extracted ROI"""


def fslroi_params(
    infile: InputPathType,
    outfile: str,
    xmin: float | None = None,
    xsize: float | None = None,
    ymin: float | None = None,
    ysize: float | None = None,
    zmin: float | None = None,
    zsize: float | None = None,
    tmin: float | None = None,
    tsize: float | None = None,
) -> FslroiParameters:
    """
    Build parameters.
    
    Args:
        infile: Input image file.
        outfile: Output image file.
        xmin: Minimum X coordinate for ROI (indexing starts at 0).
        xsize: Size of the ROI in X direction.
        ymin: Minimum Y coordinate for ROI (indexing starts at 0).
        ysize: Size of the ROI in Y direction.
        zmin: Minimum Z coordinate for ROI (indexing starts at 0).
        zsize: Size of the ROI in Z direction.
        tmin: Minimum T coordinate for ROI (indexing starts at 0).
        tsize: Size of the ROI in T direction.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslroi",
        "infile": infile,
        "outfile": outfile,
    }
    if xmin is not None:
        params["xmin"] = xmin
    if xsize is not None:
        params["xsize"] = xsize
    if ymin is not None:
        params["ymin"] = ymin
    if ysize is not None:
        params["ysize"] = ysize
    if zmin is not None:
        params["zmin"] = zmin
    if zsize is not None:
        params["zsize"] = zsize
    if tmin is not None:
        params["tmin"] = tmin
    if tsize is not None:
        params["tsize"] = tsize
    return params


def fslroi_cargs(
    params: FslroiParameters,
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
    cargs.append("fslroi")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(params.get("outfile"))
    if params.get("xmin") is not None:
        cargs.append(str(params.get("xmin")))
    if params.get("xsize") is not None:
        cargs.append(str(params.get("xsize")))
    if params.get("ymin") is not None:
        cargs.append(str(params.get("ymin")))
    if params.get("ysize") is not None:
        cargs.append(str(params.get("ysize")))
    if params.get("zmin") is not None:
        cargs.append(str(params.get("zmin")))
    if params.get("zsize") is not None:
        cargs.append(str(params.get("zsize")))
    if params.get("tmin") is not None:
        cargs.append(str(params.get("tmin")))
    if params.get("tsize") is not None:
        cargs.append(str(params.get("tsize")))
    return cargs


def fslroi_outputs(
    params: FslroiParameters,
    execution: Execution,
) -> FslroiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslroiOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("outfile")),
    )
    return ret


def fslroi_execute(
    params: FslroiParameters,
    execution: Execution,
) -> FslroiOutputs:
    """
    Extracts a region of interest (ROI) from an image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslroiOutputs`).
    """
    params = execution.params(params)
    cargs = fslroi_cargs(params, execution)
    ret = fslroi_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslroi(
    infile: InputPathType,
    outfile: str,
    xmin: float | None = None,
    xsize: float | None = None,
    ymin: float | None = None,
    ysize: float | None = None,
    zmin: float | None = None,
    zsize: float | None = None,
    tmin: float | None = None,
    tsize: float | None = None,
    runner: Runner | None = None,
) -> FslroiOutputs:
    """
    Extracts a region of interest (ROI) from an image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input image file.
        outfile: Output image file.
        xmin: Minimum X coordinate for ROI (indexing starts at 0).
        xsize: Size of the ROI in X direction.
        ymin: Minimum Y coordinate for ROI (indexing starts at 0).
        ysize: Size of the ROI in Y direction.
        zmin: Minimum Z coordinate for ROI (indexing starts at 0).
        zsize: Size of the ROI in Z direction.
        tmin: Minimum T coordinate for ROI (indexing starts at 0).
        tsize: Size of the ROI in T direction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslroiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLROI_METADATA)
    params = fslroi_params(
        infile=infile,
        outfile=outfile,
        xmin=xmin,
        xsize=xsize,
        ymin=ymin,
        ysize=ysize,
        zmin=zmin,
        zsize=zsize,
        tmin=tmin,
        tsize=tsize,
    )
    return fslroi_execute(params, execution)


__all__ = [
    "FSLROI_METADATA",
    "FslroiOutputs",
    "FslroiParameters",
    "fslroi",
    "fslroi_params",
]

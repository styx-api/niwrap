# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

T4IMG_4DFP_METADATA = Metadata(
    id="57020555f03db47bd822a3164b665430a2020fd9.boutiques",
    name="t4img_4dfp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


T4img4dfpParameters = typing.TypedDict('T4img4dfpParameters', {
    "__STYX_TYPE__": typing.Literal["t4img_4dfp"],
    "t4file": InputPathType,
    "imgfile": InputPathType,
    "outfile": typing.NotRequired[str | None],
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
        "t4img_4dfp": t4img_4dfp_cargs,
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
        "t4img_4dfp": t4img_4dfp_outputs,
    }.get(t)


class T4img4dfpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `t4img_4dfp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_image: OutputPathType | None
    """The transformed output image file in 4dfp format."""


def t4img_4dfp_params(
    t4file: InputPathType,
    imgfile: InputPathType,
    outfile: str | None = None,
) -> T4img4dfpParameters:
    """
    Build parameters.
    
    Args:
        t4file: Transformation matrix file (t4 file format).
        imgfile: Input image file (4dfp format).
        outfile: Output image file (optional, defaults to <imgfile>t if not\
            provided).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "t4img_4dfp",
        "t4file": t4file,
        "imgfile": imgfile,
    }
    if outfile is not None:
        params["outfile"] = outfile
    return params


def t4img_4dfp_cargs(
    params: T4img4dfpParameters,
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
    cargs.append("t4img_4dfp")
    cargs.append(execution.input_file(params.get("t4file")))
    cargs.append(execution.input_file(params.get("imgfile")))
    if params.get("outfile") is not None:
        cargs.append(params.get("outfile"))
    return cargs


def t4img_4dfp_outputs(
    params: T4img4dfpParameters,
    execution: Execution,
) -> T4img4dfpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = T4img4dfpOutputs(
        root=execution.output_file("."),
        transformed_image=execution.output_file(params.get("outfile") + ".4dfp.img") if (params.get("outfile") is not None) else None,
    )
    return ret


def t4img_4dfp_execute(
    params: T4img4dfpParameters,
    execution: Execution,
) -> T4img4dfpOutputs:
    """
    Transforms a 4dfp image using a specified t4 file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `T4img4dfpOutputs`).
    """
    params = execution.params(params)
    cargs = t4img_4dfp_cargs(params, execution)
    ret = t4img_4dfp_outputs(params, execution)
    execution.run(cargs)
    return ret


def t4img_4dfp(
    t4file: InputPathType,
    imgfile: InputPathType,
    outfile: str | None = None,
    runner: Runner | None = None,
) -> T4img4dfpOutputs:
    """
    Transforms a 4dfp image using a specified t4 file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t4file: Transformation matrix file (t4 file format).
        imgfile: Input image file (4dfp format).
        outfile: Output image file (optional, defaults to <imgfile>t if not\
            provided).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `T4img4dfpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(T4IMG_4DFP_METADATA)
    params = t4img_4dfp_params(
        t4file=t4file,
        imgfile=imgfile,
        outfile=outfile,
    )
    return t4img_4dfp_execute(params, execution)


__all__ = [
    "T4IMG_4DFP_METADATA",
    "T4img4dfpOutputs",
    "T4img4dfpParameters",
    "t4img_4dfp",
    "t4img_4dfp_params",
]

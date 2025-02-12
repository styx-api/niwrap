# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WHIRLGIF_METADATA = Metadata(
    id="e4c0871988c7cdc7bddc466fe2124de7c556f8a7.boutiques",
    name="whirlgif",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
WhirlgifParameters = typing.TypedDict('WhirlgifParameters', {
    "__STYX_TYPE__": typing.Literal["whirlgif"],
    "verbose": bool,
    "loop": typing.NotRequired[str | None],
    "transparency_index": typing.NotRequired[float | None],
    "inter_frame_delay": typing.NotRequired[float | None],
    "outfile": typing.NotRequired[str | None],
    "infile": typing.NotRequired[InputPathType | None],
    "gif_files": list[InputPathType],
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
        "whirlgif": whirlgif_cargs,
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
        "whirlgif": whirlgif_outputs,
    }.get(t)


class WhirlgifOutputs(typing.NamedTuple):
    """
    Output object returned when calling `whirlgif(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_gif: OutputPathType | None
    """The output GIF file"""


def whirlgif_params(
    gif_files: list[InputPathType],
    verbose: bool = False,
    loop: str | None = None,
    transparency_index: float | None = None,
    inter_frame_delay: float | None = None,
    outfile: str | None = None,
    infile: InputPathType | None = None,
) -> WhirlgifParameters:
    """
    Build parameters.
    
    Args:
        gif_files: Input GIF files to be combined into a single GIF file.
        verbose: Verbose mode.
        loop: Add the Netscape 'loop' extension. Optionally specify a loop\
            count.
        transparency_index: Set the colormap index 'index' to be transparent.
        inter_frame_delay: Inter-frame timing delay.
        outfile: Specify the output file to write the results to.
        infile: Read a list of filenames from a file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "whirlgif",
        "verbose": verbose,
        "gif_files": gif_files,
    }
    if loop is not None:
        params["loop"] = loop
    if transparency_index is not None:
        params["transparency_index"] = transparency_index
    if inter_frame_delay is not None:
        params["inter_frame_delay"] = inter_frame_delay
    if outfile is not None:
        params["outfile"] = outfile
    if infile is not None:
        params["infile"] = infile
    return params


def whirlgif_cargs(
    params: WhirlgifParameters,
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
    cargs.append("whirlgif")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("loop") is not None:
        cargs.extend([
            "-loop",
            params.get("loop")
        ])
    if params.get("transparency_index") is not None:
        cargs.extend([
            "-trans",
            str(params.get("transparency_index"))
        ])
    if params.get("inter_frame_delay") is not None:
        cargs.extend([
            "-time",
            str(params.get("inter_frame_delay"))
        ])
    if params.get("outfile") is not None:
        cargs.extend([
            "-o",
            params.get("outfile")
        ])
    if params.get("infile") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("infile"))
        ])
    cargs.extend([execution.input_file(f) for f in params.get("gif_files")])
    return cargs


def whirlgif_outputs(
    params: WhirlgifParameters,
    execution: Execution,
) -> WhirlgifOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WhirlgifOutputs(
        root=execution.output_file("."),
        output_gif=execution.output_file(params.get("outfile")) if (params.get("outfile") is not None) else None,
    )
    return ret


def whirlgif_execute(
    params: WhirlgifParameters,
    execution: Execution,
) -> WhirlgifOutputs:
    """
    A quick program that reads a series of GIF files and produces a single GIF file
    composed of those images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WhirlgifOutputs`).
    """
    cargs = whirlgif_cargs(params, execution)
    ret = whirlgif_outputs(params, execution)
    execution.run(cargs)
    return ret


def whirlgif(
    gif_files: list[InputPathType],
    verbose: bool = False,
    loop: str | None = None,
    transparency_index: float | None = None,
    inter_frame_delay: float | None = None,
    outfile: str | None = None,
    infile: InputPathType | None = None,
    runner: Runner | None = None,
) -> WhirlgifOutputs:
    """
    A quick program that reads a series of GIF files and produces a single GIF file
    composed of those images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        gif_files: Input GIF files to be combined into a single GIF file.
        verbose: Verbose mode.
        loop: Add the Netscape 'loop' extension. Optionally specify a loop\
            count.
        transparency_index: Set the colormap index 'index' to be transparent.
        inter_frame_delay: Inter-frame timing delay.
        outfile: Specify the output file to write the results to.
        infile: Read a list of filenames from a file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WhirlgifOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WHIRLGIF_METADATA)
    params = whirlgif_params(verbose=verbose, loop=loop, transparency_index=transparency_index, inter_frame_delay=inter_frame_delay, outfile=outfile, infile=infile, gif_files=gif_files)
    return whirlgif_execute(params, execution)


__all__ = [
    "WHIRLGIF_METADATA",
    "WhirlgifOutputs",
    "WhirlgifParameters",
    "whirlgif",
    "whirlgif_params",
]

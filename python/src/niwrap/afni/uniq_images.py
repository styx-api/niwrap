# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UNIQ_IMAGES_METADATA = Metadata(
    id="78da67a816d6d0b1ae55b072a61c7cc76bbe87da.boutiques",
    name="uniq_images",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
UniqImagesParameters = typing.TypedDict('UniqImagesParameters', {
    "__STYX_TYPE__": typing.Literal["uniq_images"],
    "input_files": list[InputPathType],
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
        "uniq_images": uniq_images_cargs,
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
        "uniq_images": uniq_images_outputs,
    }.get(t)


class UniqImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uniq_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unique_files_list: OutputPathType
    """Generated list of filenames with unique images"""


def uniq_images_params(
    input_files: list[InputPathType],
) -> UniqImagesParameters:
    """
    Build parameters.
    
    Args:
        input_files: List of image filenames to be processed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "uniq_images",
        "input_files": input_files,
    }
    return params


def uniq_images_cargs(
    params: UniqImagesParameters,
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
    cargs.append("uniq_images")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def uniq_images_outputs(
    params: UniqImagesParameters,
    execution: Execution,
) -> UniqImagesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UniqImagesOutputs(
        root=execution.output_file("."),
        unique_files_list=execution.output_file("unique_images_list.txt"),
    )
    return ret


def uniq_images_execute(
    params: UniqImagesParameters,
    execution: Execution,
) -> UniqImagesOutputs:
    """
    Simple program to read in a list of image filenames, determine which files have
    unique images inside, and echo out only a list of the filenames with unique
    images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UniqImagesOutputs`).
    """
    cargs = uniq_images_cargs(params, execution)
    ret = uniq_images_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def uniq_images(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> UniqImagesOutputs:
    """
    Simple program to read in a list of image filenames, determine which files have
    unique images inside, and echo out only a list of the filenames with unique
    images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: List of image filenames to be processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UniqImagesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNIQ_IMAGES_METADATA)
    params = uniq_images_params(input_files=input_files)
    return uniq_images_execute(params, execution)


__all__ = [
    "UNIQ_IMAGES_METADATA",
    "UniqImagesOutputs",
    "UniqImagesParameters",
    "uniq_images",
    "uniq_images_params",
]

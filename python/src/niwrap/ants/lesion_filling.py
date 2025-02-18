# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LESION_FILLING_METADATA = Metadata(
    id="e67424ecd9a0c5e13dd9b069bccb2e63e4348726.boutiques",
    name="LesionFilling",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
LesionFillingParameters = typing.TypedDict('LesionFillingParameters', {
    "__STYX_TYPE__": typing.Literal["LesionFilling"],
    "image_dimension": int,
    "t1_image": InputPathType,
    "lesion_mask": InputPathType,
    "output_lesion_filled": str,
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
        "LesionFilling": lesion_filling_cargs,
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
        "LesionFilling": lesion_filling_outputs,
    }.get(t)


class LesionFillingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `lesion_filling(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    lesion_filled_output: OutputPathType
    """Output image with filled lesions."""


def lesion_filling_params(
    image_dimension: int,
    t1_image: InputPathType,
    lesion_mask: InputPathType,
    output_lesion_filled: str,
) -> LesionFillingParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Dimensionality of the image (e.g., 2, 3).
        t1_image: Path to the T1 image file.
        lesion_mask: Path to the lesion mask image file.
        output_lesion_filled: Path for the output file with lesions filled.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "LesionFilling",
        "image_dimension": image_dimension,
        "t1_image": t1_image,
        "lesion_mask": lesion_mask,
        "output_lesion_filled": output_lesion_filled,
    }
    return params


def lesion_filling_cargs(
    params: LesionFillingParameters,
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
    cargs.append("LesionFilling")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("t1_image")))
    cargs.append(execution.input_file(params.get("lesion_mask")))
    cargs.append(params.get("output_lesion_filled"))
    return cargs


def lesion_filling_outputs(
    params: LesionFillingParameters,
    execution: Execution,
) -> LesionFillingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LesionFillingOutputs(
        root=execution.output_file("."),
        lesion_filled_output=execution.output_file(params.get("output_lesion_filled")),
    )
    return ret


def lesion_filling_execute(
    params: LesionFillingParameters,
    execution: Execution,
) -> LesionFillingOutputs:
    """
    A tool for filling lesions in T1 images using a mask.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LesionFillingOutputs`).
    """
    cargs = lesion_filling_cargs(params, execution)
    ret = lesion_filling_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def lesion_filling(
    image_dimension: int,
    t1_image: InputPathType,
    lesion_mask: InputPathType,
    output_lesion_filled: str,
    runner: Runner | None = None,
) -> LesionFillingOutputs:
    """
    A tool for filling lesions in T1 images using a mask.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimensionality of the image (e.g., 2, 3).
        t1_image: Path to the T1 image file.
        lesion_mask: Path to the lesion mask image file.
        output_lesion_filled: Path for the output file with lesions filled.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LesionFillingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LESION_FILLING_METADATA)
    params = lesion_filling_params(image_dimension=image_dimension, t1_image=t1_image, lesion_mask=lesion_mask, output_lesion_filled=output_lesion_filled)
    return lesion_filling_execute(params, execution)


__all__ = [
    "LESION_FILLING_METADATA",
    "LesionFillingOutputs",
    "LesionFillingParameters",
    "lesion_filling",
    "lesion_filling_params",
]

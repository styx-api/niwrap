# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ROTCOM_METADATA = Metadata(
    id="65366e1283781ddcf84d07b0c61d20c1cdbf07ba.boutiques",
    name="rotcom",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
RotcomParameters = typing.TypedDict('RotcomParameters', {
    "__STYX_TYPE__": typing.Literal["rotcom"],
    "rotate_ashift": str,
    "dataset": typing.NotRequired[InputPathType | None],
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
        "rotcom": rotcom_cargs,
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
        "rotcom": rotcom_outputs,
    }.get(t)


class RotcomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rotcom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout: OutputPathType
    """The 4x3 transformation matrix+vector output"""


def rotcom_params(
    rotate_ashift: str,
    dataset: InputPathType | None = None,
) -> RotcomParameters:
    """
    Build parameters.
    
    Args:
        rotate_ashift: Combination of rotate and ashift options in a single\
            quoted string (e.g., '-rotate 10I 0R 0A -ashift 5S 0 0').
        dataset: Input dataset for determining coordinate order.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rotcom",
        "rotate_ashift": rotate_ashift,
    }
    if dataset is not None:
        params["dataset"] = dataset
    return params


def rotcom_cargs(
    params: RotcomParameters,
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
    cargs.append("rotcom")
    cargs.append(params.get("rotate_ashift"))
    if params.get("dataset") is not None:
        cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def rotcom_outputs(
    params: RotcomParameters,
    execution: Execution,
) -> RotcomOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RotcomOutputs(
        root=execution.output_file("."),
        stdout=execution.output_file("stdout"),
    )
    return ret


def rotcom_execute(
    params: RotcomParameters,
    execution: Execution,
) -> RotcomOutputs:
    """
    Prints to stdout the 4x3 transformation matrix+vector that would be applied by
    3drotate to the given dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RotcomOutputs`).
    """
    cargs = rotcom_cargs(params, execution)
    ret = rotcom_outputs(params, execution)
    execution.run(cargs)
    return ret


def rotcom(
    rotate_ashift: str,
    dataset: InputPathType | None = None,
    runner: Runner | None = None,
) -> RotcomOutputs:
    """
    Prints to stdout the 4x3 transformation matrix+vector that would be applied by
    3drotate to the given dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        rotate_ashift: Combination of rotate and ashift options in a single\
            quoted string (e.g., '-rotate 10I 0R 0A -ashift 5S 0 0').
        dataset: Input dataset for determining coordinate order.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RotcomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ROTCOM_METADATA)
    params = rotcom_params(rotate_ashift=rotate_ashift, dataset=dataset)
    return rotcom_execute(params, execution)


__all__ = [
    "ROTCOM_METADATA",
    "RotcomOutputs",
    "RotcomParameters",
    "rotcom",
    "rotcom_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BASIL_VAR_METADATA = Metadata(
    id="ef2d05e150b63d8d6121c52d86fea7583edc0338.boutiques",
    name="basil_var",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


BasilVarParameters = typing.TypedDict('BasilVarParameters', {
    "__STYX_TYPE__": typing.Literal["basil_var"],
    "results_dir": str,
    "mask_image": InputPathType,
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
        "basil_var": basil_var_cargs,
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


class BasilVarOutputs(typing.NamedTuple):
    """
    Output object returned when calling `basil_var(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def basil_var_params(
    results_dir: str,
    mask_image: InputPathType,
) -> BasilVarParameters:
    """
    Build parameters.
    
    Args:
        results_dir: BASIL results directory.
        mask_image: Mask image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "basil_var",
        "results_dir": results_dir,
        "mask_image": mask_image,
    }
    return params


def basil_var_cargs(
    params: BasilVarParameters,
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
    cargs.append("basil_var")
    cargs.extend([
        "-d",
        params.get("results_dir")
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask_image"))
    ])
    return cargs


def basil_var_outputs(
    params: BasilVarParameters,
    execution: Execution,
) -> BasilVarOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BasilVarOutputs(
        root=execution.output_file("."),
    )
    return ret


def basil_var_execute(
    params: BasilVarParameters,
    execution: Execution,
) -> BasilVarOutputs:
    """
    Variance calculator for BASIL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BasilVarOutputs`).
    """
    params = execution.params(params)
    cargs = basil_var_cargs(params, execution)
    ret = basil_var_outputs(params, execution)
    execution.run(cargs)
    return ret


def basil_var(
    results_dir: str,
    mask_image: InputPathType,
    runner: Runner | None = None,
) -> BasilVarOutputs:
    """
    Variance calculator for BASIL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        results_dir: BASIL results directory.
        mask_image: Mask image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BasilVarOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BASIL_VAR_METADATA)
    params = basil_var_params(
        results_dir=results_dir,
        mask_image=mask_image,
    )
    return basil_var_execute(params, execution)


__all__ = [
    "BASIL_VAR_METADATA",
    "BasilVarOutputs",
    "BasilVarParameters",
    "basil_var",
    "basil_var_params",
]

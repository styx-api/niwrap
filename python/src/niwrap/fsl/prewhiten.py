# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PREWHITEN_METADATA = Metadata(
    id="7908b2674351c8eda706fea6c142d2b26d298d0f.boutiques",
    name="prewhiten",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PrewhitenParameters = typing.TypedDict('PrewhitenParameters', {
    "__STYX_TYPE__": typing.Literal["prewhiten"],
    "feat_directory": str,
    "output_directory": typing.NotRequired[str | None],
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
        "prewhiten": prewhiten_cargs,
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
        "prewhiten": prewhiten_outputs,
    }.get(t)


class PrewhitenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prewhiten(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Output files generated in the specified output directory"""


def prewhiten_params(
    feat_directory: str,
    output_directory: str | None = None,
) -> PrewhitenParameters:
    """
    Build parameters.
    
    Args:
        feat_directory: Input FEAT directory.
        output_directory: Change output directory from default of input FEAT\
            directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "prewhiten",
        "feat_directory": feat_directory,
    }
    if output_directory is not None:
        params["output_directory"] = output_directory
    return params


def prewhiten_cargs(
    params: PrewhitenParameters,
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
    cargs.append("prewhiten")
    cargs.append(params.get("feat_directory"))
    if params.get("output_directory") is not None:
        cargs.extend([
            "-o",
            params.get("output_directory")
        ])
    return cargs


def prewhiten_outputs(
    params: PrewhitenParameters,
    execution: Execution,
) -> PrewhitenOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PrewhitenOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("output_directory") + "/*") if (params.get("output_directory") is not None) else None,
    )
    return ret


def prewhiten_execute(
    params: PrewhitenParameters,
    execution: Execution,
) -> PrewhitenOutputs:
    """
    Prewhitening tool for FEAT directories.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PrewhitenOutputs`).
    """
    cargs = prewhiten_cargs(params, execution)
    ret = prewhiten_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def prewhiten(
    feat_directory: str,
    output_directory: str | None = None,
    runner: Runner | None = None,
) -> PrewhitenOutputs:
    """
    Prewhitening tool for FEAT directories.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        feat_directory: Input FEAT directory.
        output_directory: Change output directory from default of input FEAT\
            directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PrewhitenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PREWHITEN_METADATA)
    params = prewhiten_params(feat_directory=feat_directory, output_directory=output_directory)
    return prewhiten_execute(params, execution)


__all__ = [
    "PREWHITEN_METADATA",
    "PrewhitenOutputs",
    "PrewhitenParameters",
    "prewhiten",
    "prewhiten_params",
]

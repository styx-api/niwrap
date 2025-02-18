# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_INIT_GLOBAL_TRACTOGRAPHY_METADATA = Metadata(
    id="67eb4585ff3c986788ed4212a3618bb647f3bf08.boutiques",
    name="mris_init_global_tractography",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisInitGlobalTractographyParameters = typing.TypedDict('MrisInitGlobalTractographyParameters', {
    "__STYX_TYPE__": typing.Literal["mris_init_global_tractography"],
    "subject": str,
    "parcellation": str,
    "output_volume": str,
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
        "mris_init_global_tractography": mris_init_global_tractography_cargs,
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


class MrisInitGlobalTractographyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_init_global_tractography(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_init_global_tractography_params(
    subject: str,
    parcellation: str,
    output_volume: str,
) -> MrisInitGlobalTractographyParameters:
    """
    Build parameters.
    
    Args:
        subject: The subject on which to perform tractography.
        parcellation: The parcellation to use for tractography.
        output_volume: Output volume of the initialized global tractography.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_init_global_tractography",
        "subject": subject,
        "parcellation": parcellation,
        "output_volume": output_volume,
    }
    return params


def mris_init_global_tractography_cargs(
    params: MrisInitGlobalTractographyParameters,
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
    cargs.append("mris_init_global_tractography")
    cargs.append(params.get("subject"))
    cargs.append(params.get("parcellation"))
    cargs.append(params.get("output_volume"))
    return cargs


def mris_init_global_tractography_outputs(
    params: MrisInitGlobalTractographyParameters,
    execution: Execution,
) -> MrisInitGlobalTractographyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisInitGlobalTractographyOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_init_global_tractography_execute(
    params: MrisInitGlobalTractographyParameters,
    execution: Execution,
) -> MrisInitGlobalTractographyOutputs:
    """
    Initializes global tractography for a given subject and parcellation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisInitGlobalTractographyOutputs`).
    """
    cargs = mris_init_global_tractography_cargs(params, execution)
    ret = mris_init_global_tractography_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_init_global_tractography(
    subject: str,
    parcellation: str,
    output_volume: str,
    runner: Runner | None = None,
) -> MrisInitGlobalTractographyOutputs:
    """
    Initializes global tractography for a given subject and parcellation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject on which to perform tractography.
        parcellation: The parcellation to use for tractography.
        output_volume: Output volume of the initialized global tractography.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisInitGlobalTractographyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_INIT_GLOBAL_TRACTOGRAPHY_METADATA)
    params = mris_init_global_tractography_params(subject=subject, parcellation=parcellation, output_volume=output_volume)
    return mris_init_global_tractography_execute(params, execution)


__all__ = [
    "MRIS_INIT_GLOBAL_TRACTOGRAPHY_METADATA",
    "MrisInitGlobalTractographyOutputs",
    "MrisInitGlobalTractographyParameters",
    "mris_init_global_tractography",
    "mris_init_global_tractography_params",
]

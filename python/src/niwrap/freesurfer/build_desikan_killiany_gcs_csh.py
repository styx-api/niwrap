# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BUILD_DESIKAN_KILLIANY_GCS_CSH_METADATA = Metadata(
    id="533d45cdbfae4bc58aadf050a7461db1dc6a6914.boutiques",
    name="build_desikan_killiany_gcs.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
BuildDesikanKillianyGcsCshParameters = typing.TypedDict('BuildDesikanKillianyGcsCshParameters', {
    "__STYX_TYPE__": typing.Literal["build_desikan_killiany_gcs.csh"],
    "hemi": str,
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
        "build_desikan_killiany_gcs.csh": build_desikan_killiany_gcs_csh_cargs,
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


class BuildDesikanKillianyGcsCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `build_desikan_killiany_gcs_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def build_desikan_killiany_gcs_csh_params(
    hemi: str,
) -> BuildDesikanKillianyGcsCshParameters:
    """
    Build parameters.
    
    Args:
        hemi: Hemisphere designation for the operation. Should be 'rh' for\
            right hemisphere or 'lh' for left hemisphere.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "build_desikan_killiany_gcs.csh",
        "hemi": hemi,
    }
    return params


def build_desikan_killiany_gcs_csh_cargs(
    params: BuildDesikanKillianyGcsCshParameters,
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
    cargs.append("build_desikan_killiany_gcs.csh")
    cargs.append(params.get("hemi"))
    return cargs


def build_desikan_killiany_gcs_csh_outputs(
    params: BuildDesikanKillianyGcsCshParameters,
    execution: Execution,
) -> BuildDesikanKillianyGcsCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BuildDesikanKillianyGcsCshOutputs(
        root=execution.output_file("."),
    )
    return ret


def build_desikan_killiany_gcs_csh_execute(
    params: BuildDesikanKillianyGcsCshParameters,
    execution: Execution,
) -> BuildDesikanKillianyGcsCshOutputs:
    """
    Tool to build Desikan-Killiany cortical parcellation in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BuildDesikanKillianyGcsCshOutputs`).
    """
    cargs = build_desikan_killiany_gcs_csh_cargs(params, execution)
    ret = build_desikan_killiany_gcs_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def build_desikan_killiany_gcs_csh(
    hemi: str,
    runner: Runner | None = None,
) -> BuildDesikanKillianyGcsCshOutputs:
    """
    Tool to build Desikan-Killiany cortical parcellation in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere designation for the operation. Should be 'rh' for\
            right hemisphere or 'lh' for left hemisphere.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BuildDesikanKillianyGcsCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BUILD_DESIKAN_KILLIANY_GCS_CSH_METADATA)
    params = build_desikan_killiany_gcs_csh_params(hemi=hemi)
    return build_desikan_killiany_gcs_csh_execute(params, execution)


__all__ = [
    "BUILD_DESIKAN_KILLIANY_GCS_CSH_METADATA",
    "BuildDesikanKillianyGcsCshOutputs",
    "BuildDesikanKillianyGcsCshParameters",
    "build_desikan_killiany_gcs_csh",
    "build_desikan_killiany_gcs_csh_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__NO_POUND_METADATA = Metadata(
    id="27d35f86a77d04034e08074da72efd10ccb9fa51.boutiques",
    name="@NoPound",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VNoPoundParameters = typing.TypedDict('VNoPoundParameters', {
    "__STYX_TYPE__": typing.Literal["@NoPound"],
    "afni_files": list[str],
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
        "@NoPound": v__no_pound_cargs,
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


class VNoPoundOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__no_pound(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__no_pound_params(
    afni_files: list[str],
) -> VNoPoundParameters:
    """
    Build parameters.
    
    Args:
        afni_files: List of AFNI files where # characters should be replaced\
            with -.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@NoPound",
        "afni_files": afni_files,
    }
    return params


def v__no_pound_cargs(
    params: VNoPoundParameters,
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
    cargs.append("@NoPound")
    cargs.extend(params.get("afni_files"))
    return cargs


def v__no_pound_outputs(
    params: VNoPoundParameters,
    execution: Execution,
) -> VNoPoundOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VNoPoundOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__no_pound_execute(
    params: VNoPoundParameters,
    execution: Execution,
) -> VNoPoundOutputs:
    """
    Replaces all # characters in AFNI filenames with a -.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VNoPoundOutputs`).
    """
    cargs = v__no_pound_cargs(params, execution)
    ret = v__no_pound_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__no_pound(
    afni_files: list[str],
    runner: Runner | None = None,
) -> VNoPoundOutputs:
    """
    Replaces all # characters in AFNI filenames with a -.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        afni_files: List of AFNI files where # characters should be replaced\
            with -.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VNoPoundOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__NO_POUND_METADATA)
    params = v__no_pound_params(afni_files=afni_files)
    return v__no_pound_execute(params, execution)


__all__ = [
    "VNoPoundOutputs",
    "VNoPoundParameters",
    "V__NO_POUND_METADATA",
    "v__no_pound",
    "v__no_pound_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FLOAT_FIX_METADATA = Metadata(
    id="69c8566d3c52dcfb93a135adaaa38398077c4bc6.boutiques",
    name="@float_fix",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VFloatFixParameters = typing.TypedDict('VFloatFixParameters', {
    "__STYX_TYPE__": typing.Literal["@float_fix"],
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
        "@float_fix": v__float_fix_cargs,
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


class VFloatFixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__float_fix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__float_fix_params(
    input_files: list[InputPathType],
) -> VFloatFixParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input files to be checked for illegal IEEE floating point\
            values. Wildcards can be used, but filenames must end with .HEAD.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@float_fix",
        "input_files": input_files,
    }
    return params


def v__float_fix_cargs(
    params: VFloatFixParameters,
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
    cargs.append("@float_fix")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def v__float_fix_outputs(
    params: VFloatFixParameters,
    execution: Execution,
) -> VFloatFixOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFloatFixOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__float_fix_execute(
    params: VFloatFixParameters,
    execution: Execution,
) -> VFloatFixOutputs:
    """
    Check whether the input files have any IEEE floating point numbers for illegal
    values: infinities and not-a-number (NaN) values.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFloatFixOutputs`).
    """
    cargs = v__float_fix_cargs(params, execution)
    ret = v__float_fix_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__float_fix(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> VFloatFixOutputs:
    """
    Check whether the input files have any IEEE floating point numbers for illegal
    values: infinities and not-a-number (NaN) values.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input files to be checked for illegal IEEE floating point\
            values. Wildcards can be used, but filenames must end with .HEAD.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFloatFixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FLOAT_FIX_METADATA)
    params = v__float_fix_params(input_files=input_files)
    return v__float_fix_execute(params, execution)


__all__ = [
    "VFloatFixOutputs",
    "VFloatFixParameters",
    "V__FLOAT_FIX_METADATA",
    "v__float_fix",
    "v__float_fix_params",
]

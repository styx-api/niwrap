# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SUMA_MAKE_SPEC_CARET_METADATA = Metadata(
    id="950a20d0f240b4840873e5b78497c9b7e5e19277.boutiques",
    name="@SUMA_Make_Spec_Caret",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VSumaMakeSpecCaretParameters = typing.TypedDict('VSumaMakeSpecCaretParameters', {
    "__STYX_TYPE__": typing.Literal["@SUMA_Make_Spec_Caret"],
    "subject_id": str,
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
        "@SUMA_Make_Spec_Caret": v__suma_make_spec_caret_cargs,
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
        "@SUMA_Make_Spec_Caret": v__suma_make_spec_caret_outputs,
    }.get(t)


class VSumaMakeSpecCaretOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_make_spec_caret(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    left_hemisphere_spec: OutputPathType
    """Output spec file for the left hemisphere"""
    right_hemisphere_spec: OutputPathType
    """Output spec file for the right hemisphere"""


def v__suma_make_spec_caret_params(
    subject_id: str,
) -> VSumaMakeSpecCaretParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject ID for file naming.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@SUMA_Make_Spec_Caret",
        "subject_id": subject_id,
    }
    return params


def v__suma_make_spec_caret_cargs(
    params: VSumaMakeSpecCaretParameters,
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
    cargs.append("@SUMA_Make_Spec_Caret")
    cargs.append("[OPTIONS]")
    cargs.extend([
        "-sid",
        params.get("subject_id")
    ])
    return cargs


def v__suma_make_spec_caret_outputs(
    params: VSumaMakeSpecCaretParameters,
    execution: Execution,
) -> VSumaMakeSpecCaretOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSumaMakeSpecCaretOutputs(
        root=execution.output_file("."),
        left_hemisphere_spec=execution.output_file(params.get("subject_id") + "_lh.spec"),
        right_hemisphere_spec=execution.output_file(params.get("subject_id") + "_rh.spec"),
    )
    return ret


def v__suma_make_spec_caret_execute(
    params: VSumaMakeSpecCaretParameters,
    execution: Execution,
) -> VSumaMakeSpecCaretOutputs:
    """
    Prepare surfaces for viewing in SUMA, tested with Caret-5.2 surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecCaretOutputs`).
    """
    params = execution.params(params)
    cargs = v__suma_make_spec_caret_cargs(params, execution)
    ret = v__suma_make_spec_caret_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__suma_make_spec_caret(
    subject_id: str,
    runner: Runner | None = None,
) -> VSumaMakeSpecCaretOutputs:
    """
    Prepare surfaces for viewing in SUMA, tested with Caret-5.2 surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        subject_id: Subject ID for file naming.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecCaretOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_MAKE_SPEC_CARET_METADATA)
    params = v__suma_make_spec_caret_params(
        subject_id=subject_id,
    )
    return v__suma_make_spec_caret_execute(params, execution)


__all__ = [
    "VSumaMakeSpecCaretOutputs",
    "VSumaMakeSpecCaretParameters",
    "V__SUMA_MAKE_SPEC_CARET_METADATA",
    "v__suma_make_spec_caret",
    "v__suma_make_spec_caret_params",
]

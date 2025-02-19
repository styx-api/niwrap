# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__AFNI_REFACER_MAKE_ONEBIG_A12_METADATA = Metadata(
    id="9bef1fa50af4572410be32739de25ad17fe8544e.boutiques",
    name="@afni_refacer_make_onebigA12",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VAfniRefacerMakeOnebigA12Parameters = typing.TypedDict('VAfniRefacerMakeOnebigA12Parameters', {
    "__STYX_TYPE__": typing.Literal["@afni_refacer_make_onebigA12"],
    "t1w_dataset": InputPathType,
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
        "@afni_refacer_make_onebigA12": v__afni_refacer_make_onebig_a12_cargs,
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
        "@afni_refacer_make_onebigA12": v__afni_refacer_make_onebig_a12_outputs,
    }.get(t)


class VAfniRefacerMakeOnebigA12Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_refacer_make_onebig_a12(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_output: OutputPathType
    """Aligned T1w dataset to MNI template with expanded 'big' grid"""


def v__afni_refacer_make_onebig_a12_params(
    t1w_dataset: InputPathType,
) -> VAfniRefacerMakeOnebigA12Parameters:
    """
    Build parameters.
    
    Args:
        t1w_dataset: Input T1w dataset name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@afni_refacer_make_onebigA12",
        "t1w_dataset": t1w_dataset,
    }
    return params


def v__afni_refacer_make_onebig_a12_cargs(
    params: VAfniRefacerMakeOnebigA12Parameters,
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
    cargs.append("@afni_refacer_make_onebigA12")
    cargs.append(execution.input_file(params.get("t1w_dataset")))
    return cargs


def v__afni_refacer_make_onebig_a12_outputs(
    params: VAfniRefacerMakeOnebigA12Parameters,
    execution: Execution,
) -> VAfniRefacerMakeOnebigA12Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAfniRefacerMakeOnebigA12Outputs(
        root=execution.output_file("."),
        aligned_output=execution.output_file(pathlib.Path(params.get("t1w_dataset")).name + "_aligned_to_MNI.nii.gz"),
    )
    return ret


def v__afni_refacer_make_onebig_a12_execute(
    params: VAfniRefacerMakeOnebigA12Parameters,
    execution: Execution,
) -> VAfniRefacerMakeOnebigA12Outputs:
    """
    Script to align a single T1w dataset to the MNI template and expand it to a
    'big' grid.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAfniRefacerMakeOnebigA12Outputs`).
    """
    params = execution.params(params)
    cargs = v__afni_refacer_make_onebig_a12_cargs(params, execution)
    ret = v__afni_refacer_make_onebig_a12_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__afni_refacer_make_onebig_a12(
    t1w_dataset: InputPathType,
    runner: Runner | None = None,
) -> VAfniRefacerMakeOnebigA12Outputs:
    """
    Script to align a single T1w dataset to the MNI template and expand it to a
    'big' grid.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        t1w_dataset: Input T1w dataset name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRefacerMakeOnebigA12Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_REFACER_MAKE_ONEBIG_A12_METADATA)
    params = v__afni_refacer_make_onebig_a12_params(
        t1w_dataset=t1w_dataset,
    )
    return v__afni_refacer_make_onebig_a12_execute(params, execution)


__all__ = [
    "VAfniRefacerMakeOnebigA12Outputs",
    "VAfniRefacerMakeOnebigA12Parameters",
    "V__AFNI_REFACER_MAKE_ONEBIG_A12_METADATA",
    "v__afni_refacer_make_onebig_a12",
    "v__afni_refacer_make_onebig_a12_params",
]

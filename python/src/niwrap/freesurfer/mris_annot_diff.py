# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ANNOT_DIFF_METADATA = Metadata(
    id="66fc64b92af2b8d25899007f79214682b156e3d3.boutiques",
    name="mris_annot_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisAnnotDiffParameters = typing.TypedDict('MrisAnnotDiffParameters', {
    "__STYX_TYPE__": typing.Literal["mris_annot_diff"],
    "annot1": InputPathType,
    "annot2": InputPathType,
    "diff_ctab": bool,
    "verbose": bool,
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
        "mris_annot_diff": mris_annot_diff_cargs,
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


class MrisAnnotDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_annot_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_annot_diff_params(
    annot1: InputPathType,
    annot2: InputPathType,
    diff_ctab: bool = False,
    verbose: bool = False,
) -> MrisAnnotDiffParameters:
    """
    Build parameters.
    
    Args:
        annot1: Input .annot file 1.
        annot2: Input .annot file 2.
        diff_ctab: Diff colortable included in .annot.
        verbose: Print details of annotation/colortable differences.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_annot_diff",
        "annot1": annot1,
        "annot2": annot2,
        "diff_ctab": diff_ctab,
        "verbose": verbose,
    }
    return params


def mris_annot_diff_cargs(
    params: MrisAnnotDiffParameters,
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
    cargs.append("mris_annot_diff")
    cargs.append(execution.input_file(params.get("annot1")))
    cargs.append(execution.input_file(params.get("annot2")))
    if params.get("diff_ctab"):
        cargs.append("--diff-ctab")
    if params.get("verbose"):
        cargs.append("--verbose")
    return cargs


def mris_annot_diff_outputs(
    params: MrisAnnotDiffParameters,
    execution: Execution,
) -> MrisAnnotDiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisAnnotDiffOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_annot_diff_execute(
    params: MrisAnnotDiffParameters,
    execution: Execution,
) -> MrisAnnotDiffOutputs:
    """
    Compare two surface annotation files. The program works with .annot only.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisAnnotDiffOutputs`).
    """
    cargs = mris_annot_diff_cargs(params, execution)
    ret = mris_annot_diff_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_annot_diff(
    annot1: InputPathType,
    annot2: InputPathType,
    diff_ctab: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> MrisAnnotDiffOutputs:
    """
    Compare two surface annotation files. The program works with .annot only.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        annot1: Input .annot file 1.
        annot2: Input .annot file 2.
        diff_ctab: Diff colortable included in .annot.
        verbose: Print details of annotation/colortable differences.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisAnnotDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ANNOT_DIFF_METADATA)
    params = mris_annot_diff_params(annot1=annot1, annot2=annot2, diff_ctab=diff_ctab, verbose=verbose)
    return mris_annot_diff_execute(params, execution)


__all__ = [
    "MRIS_ANNOT_DIFF_METADATA",
    "MrisAnnotDiffOutputs",
    "MrisAnnotDiffParameters",
    "mris_annot_diff",
    "mris_annot_diff_params",
]

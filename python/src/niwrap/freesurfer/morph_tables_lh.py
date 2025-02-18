# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MORPH_TABLES_LH_METADATA = Metadata(
    id="e50487cf18790588cbef4e2983a79d88589f3cc3.boutiques",
    name="morph_tables-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MorphTablesLhParameters = typing.TypedDict('MorphTablesLhParameters', {
    "__STYX_TYPE__": typing.Literal["morph_tables-lh"],
    "input_file": InputPathType,
    "some_flag": bool,
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
        "morph_tables-lh": morph_tables_lh_cargs,
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
        "morph_tables-lh": morph_tables_lh_outputs,
    }.get(t)


class MorphTablesLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_tables_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output results from morphological analysis (example, adjust as needed)"""


def morph_tables_lh_params(
    input_file: InputPathType,
    some_flag: bool = False,
) -> MorphTablesLhParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file for morphological analysis.
        some_flag: Example flag (replace with actual options from tool if\
            known).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_tables-lh",
        "input_file": input_file,
        "some_flag": some_flag,
    }
    return params


def morph_tables_lh_cargs(
    params: MorphTablesLhParameters,
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
    cargs.extend([
        "-lh",
        "morph_tables" + execution.input_file(params.get("input_file"))
    ])
    if params.get("some_flag"):
        cargs.append("--some-flag")
    return cargs


def morph_tables_lh_outputs(
    params: MorphTablesLhParameters,
    execution: Execution,
) -> MorphTablesLhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphTablesLhOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(params.get("input_file")).name + "_output.txt"),
    )
    return ret


def morph_tables_lh_execute(
    params: MorphTablesLhParameters,
    execution: Execution,
) -> MorphTablesLhOutputs:
    """
    Morphological analysis tool for left hemisphere in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphTablesLhOutputs`).
    """
    cargs = morph_tables_lh_cargs(params, execution)
    ret = morph_tables_lh_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def morph_tables_lh(
    input_file: InputPathType,
    some_flag: bool = False,
    runner: Runner | None = None,
) -> MorphTablesLhOutputs:
    """
    Morphological analysis tool for left hemisphere in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input file for morphological analysis.
        some_flag: Example flag (replace with actual options from tool if\
            known).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphTablesLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_TABLES_LH_METADATA)
    params = morph_tables_lh_params(input_file=input_file, some_flag=some_flag)
    return morph_tables_lh_execute(params, execution)


__all__ = [
    "MORPH_TABLES_LH_METADATA",
    "MorphTablesLhOutputs",
    "MorphTablesLhParameters",
    "morph_tables_lh",
    "morph_tables_lh_params",
]

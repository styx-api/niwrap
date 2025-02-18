# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CLUST_EXP_HIST_TABLE_PY_METADATA = Metadata(
    id="a706e0c184974ad6ed86360994f032d1d4e5296f.boutiques",
    name="ClustExp_HistTable.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ClustExpHistTablePyParameters = typing.TypedDict('ClustExpHistTablePyParameters', {
    "__STYX_TYPE__": typing.Literal["ClustExp_HistTable.py"],
    "stat_dset": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "session": typing.NotRequired[str | None],
    "overwrite": bool,
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
        "ClustExp_HistTable.py": clust_exp_hist_table_py_cargs,
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
        "ClustExp_HistTable.py": clust_exp_hist_table_py_outputs,
    }.get(t)


class ClustExpHistTablePyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `clust_exp_hist_table_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    group_table: OutputPathType | None
    """Table with information parsed from the statistics dataset history."""


def clust_exp_hist_table_py_params(
    stat_dset: InputPathType,
    prefix: str | None = None,
    session: str | None = None,
    overwrite: bool = False,
) -> ClustExpHistTablePyParameters:
    """
    Build parameters.
    
    Args:
        stat_dset: Statistics dataset.
        prefix: Name for output (no path). Default is GroupOut.
        session: Output parent folder if you don't want the current working\
            directory. Default is ./.
        overwrite: Remove previous folder with same PREFIX.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ClustExp_HistTable.py",
        "stat_dset": stat_dset,
        "overwrite": overwrite,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if session is not None:
        params["session"] = session
    return params


def clust_exp_hist_table_py_cargs(
    params: ClustExpHistTablePyParameters,
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
    cargs.append("ClustExp_HistTable.py")
    cargs.extend([
        "-StatDSET",
        execution.input_file(params.get("stat_dset"))
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("session") is not None:
        cargs.extend([
            "-session",
            params.get("session")
        ])
    if params.get("overwrite"):
        cargs.append("-overwrite")
    return cargs


def clust_exp_hist_table_py_outputs(
    params: ClustExpHistTablePyParameters,
    execution: Execution,
) -> ClustExpHistTablePyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ClustExpHistTablePyOutputs(
        root=execution.output_file("."),
        group_table=execution.output_file(params.get("prefix") + "_GroupTable.csv") if (params.get("prefix") is not None) else None,
    )
    return ret


def clust_exp_hist_table_py_execute(
    params: ClustExpHistTablePyParameters,
    execution: Execution,
) -> ClustExpHistTablePyOutputs:
    """
    Script to extract the data table from history of datasets from 3dttest++, 3dMVM,
    or 3dLME.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ClustExpHistTablePyOutputs`).
    """
    cargs = clust_exp_hist_table_py_cargs(params, execution)
    ret = clust_exp_hist_table_py_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def clust_exp_hist_table_py(
    stat_dset: InputPathType,
    prefix: str | None = None,
    session: str | None = None,
    overwrite: bool = False,
    runner: Runner | None = None,
) -> ClustExpHistTablePyOutputs:
    """
    Script to extract the data table from history of datasets from 3dttest++, 3dMVM,
    or 3dLME.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        stat_dset: Statistics dataset.
        prefix: Name for output (no path). Default is GroupOut.
        session: Output parent folder if you don't want the current working\
            directory. Default is ./.
        overwrite: Remove previous folder with same PREFIX.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ClustExpHistTablePyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CLUST_EXP_HIST_TABLE_PY_METADATA)
    params = clust_exp_hist_table_py_params(stat_dset=stat_dset, prefix=prefix, session=session, overwrite=overwrite)
    return clust_exp_hist_table_py_execute(params, execution)


__all__ = [
    "CLUST_EXP_HIST_TABLE_PY_METADATA",
    "ClustExpHistTablePyOutputs",
    "ClustExpHistTablePyParameters",
    "clust_exp_hist_table_py",
    "clust_exp_hist_table_py_params",
]

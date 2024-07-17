# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1D_TOOL_PY_METADATA = Metadata(
    id="84c70b153679c88e3aabe522b1fe8a517034734a",
    name="1d_tool.py",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V1dToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Resulting 1D file"""


def v_1d_tool_py(
    infile: InputPathType,
    write: str | None = None,
    select_cols: str | None = None,
    select_rows: str | None = None,
    select_groups: str | None = None,
    censor_motion: float | int | None = None,
    pad_into_many_runs: str | None = None,
    set_nruns: float | int | None = None,
    set_run_lengths: str | None = None,
    show_rows_cols: bool = False,
    transpose: bool = False,
    reverse: bool = False,
    show_max_displace: bool = False,
    runner: Runner | None = None,
) -> V1dToolPyOutputs:
    """
    1d_tool.py by R Reynolds.
    
    A tool for manipulating and evaluating 1D files.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/1d_tool.py.html
    
    Args:
        infile: Input 1D file.
        write: Output file to write results.
        select_cols: Select specific columns.
        select_rows: Select specific rows.
        select_groups: Select columns by group numbers.
        censor_motion: Generate a boolean censor file.
        pad_into_many_runs: Pad a 1D file into many runs.
        set_nruns: Set number of runs.
        set_run_lengths: Set run lengths.
        show_rows_cols: Show the number of rows and columns.
        transpose: Transpose the input matrix.
        reverse: Reverse the data over time.
        show_max_displace: Show the maximum pairwise displacement.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_TOOL_PY_METADATA)
    cargs = []
    cargs.append("1d_tool.py")
    cargs.append("[OPTIONS]")
    ret = V1dToolPyOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{write}", optional=True) if write is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dToolPyOutputs",
    "V_1D_TOOL_PY_METADATA",
    "v_1d_tool_py",
]

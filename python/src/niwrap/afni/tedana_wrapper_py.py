# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TEDANA_WRAPPER_PY_METADATA = Metadata(
    id="d6c5a3ec49020146985dd43c3c2921059545cbf9.boutiques",
    name="tedana_wrapper.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class TedanaWrapperPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tedana_wrapper_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tedana_output: OutputPathType | None
    """Output directory for tedana results."""
    tedana_report: OutputPathType | None
    """Tedana report file."""


def tedana_wrapper_py(
    input_files: list[InputPathType],
    echo_times: list[float],
    mask: InputPathType,
    results_dir: str | None = None,
    prefix: str | None = None,
    save_all: bool = False,
    prep_only: bool = False,
    tedana_prog: str | None = None,
    tedana_is_exec: bool = False,
    ted_label: str | None = None,
    tedana_opts: str | None = None,
    runner: Runner | None = None,
) -> TedanaWrapperPyOutputs:
    """
    Internal wrapper to run tedana.py, typically used within afni_proc.py.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/tedana_wrapper.py.html
    
    Args:
        input_files: 4D dataset for each echo.
        echo_times: Echo time (ms) for each echo.
        mask: Mask in same space/grid as the input datasets.
        results_dir: Folder to be created for all outputs. Default\
            [./Bunnymen].
        prefix: Prefix for dataset names. Default [Bunnymen].
        save_all: Save intermediate datasets. Default is to save only the\
            3dZcat stacked dataset (and tedana stuff).
        prep_only: Do not run tedana.py, stop at 3dZcat.
        tedana_prog: Path and name of the version of tedana.py that will be\
            run. Default is meica.libs/tedana.py in the afni binaries directory.
        tedana_is_exec: Run 'tedana.py' rather than 'python tedana.py'.
        ted_label: Suffix for output folder. Adds suffix like TED.LABEL (NOT A\
            PATH).
        tedana_opts: Additional options to pass to tedana.py. (In quotes)\
            Example: '--initcost=tanh --conv=2.5e-5'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TedanaWrapperPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEDANA_WRAPPER_PY_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/tedana_wrapper.py")
    cargs.extend([
        "-input",
        *[execution.input_file(f) for f in input_files]
    ])
    cargs.extend([
        "-TE",
        *map(str, echo_times)
    ])
    cargs.extend([
        "-mask",
        execution.input_file(mask)
    ])
    if results_dir is not None:
        cargs.extend([
            "-results_dir",
            results_dir
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if save_all:
        cargs.append("-save_all")
    if prep_only:
        cargs.append("-prep_only")
    if tedana_prog is not None:
        cargs.extend([
            "-tedana_prog",
            tedana_prog
        ])
    if tedana_is_exec:
        cargs.append("-tedana_is_exec")
    if ted_label is not None:
        cargs.extend([
            "-ted_label",
            ted_label
        ])
    if tedana_opts is not None:
        cargs.extend([
            "-tedana_opts",
            tedana_opts
        ])
    ret = TedanaWrapperPyOutputs(
        root=execution.output_file("."),
        tedana_output=execution.output_file(results_dir + "/" + prefix + "_ted_output") if (results_dir is not None and prefix is not None) else None,
        tedana_report=execution.output_file(results_dir + "/" + prefix + "_tedana_report.txt") if (results_dir is not None and prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TEDANA_WRAPPER_PY_METADATA",
    "TedanaWrapperPyOutputs",
    "tedana_wrapper_py",
]

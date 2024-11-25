# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_MAKE_SCRIPT_AND_RST_PY_METADATA = Metadata(
    id="31c33a4af534292502b71342782645e0cb0ac41e.boutiques",
    name="adjunct_make_script_and_rst.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctMakeScriptAndRstPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_make_script_and_rst_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    rst_file: OutputPathType
    """Generated RST documentation file."""
    script_file: OutputPathType
    """Generated script file."""
    output_directory: OutputPathType
    """Output directory in Sphinx tree."""


def adjunct_make_script_and_rst_py(
    input_script: InputPathType,
    prefix_rst: str,
    prefix_script: str,
    reflink: str,
    execute_script: bool = False,
    runner: Runner | None = None,
) -> AdjunctMakeScriptAndRstPyOutputs:
    """
    Program to take a script with some special markup and turn it into both an RST
    page and a script for the online Sphinx documentation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_script: Input script file with special markup.
        prefix_rst: Output filename including any path of the RST/Sphinx file.\
            Must include file extension '.rst'.
        prefix_script: Output filename of the script file. Should include file\
            extension such as '.tcsh'.
        reflink: A string tag that will serve as the subdirectory name holding\
            images for the given demo, and the RST internal reference label.
        execute_script: Flag to create the RST and script files, and also\
            execute the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctMakeScriptAndRstPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_MAKE_SCRIPT_AND_RST_PY_METADATA)
    cargs = []
    cargs.append("adjunct_make_script_and_rst.py")
    cargs.append("--input")
    cargs.append(execution.input_file(input_script))
    cargs.extend([
        "--prefix_rst",
        prefix_rst
    ])
    cargs.extend([
        "--prefix_script",
        prefix_script
    ])
    cargs.extend([
        "--reflink",
        reflink
    ])
    if execute_script:
        cargs.append("--execute_script")
    ret = AdjunctMakeScriptAndRstPyOutputs(
        root=execution.output_file("."),
        rst_file=execution.output_file(prefix_rst),
        script_file=execution.output_file(prefix_script),
        output_directory=execution.output_file(prefix_rst + "/media/" + reflink),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_MAKE_SCRIPT_AND_RST_PY_METADATA",
    "AdjunctMakeScriptAndRstPyOutputs",
    "adjunct_make_script_and_rst_py",
]

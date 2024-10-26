# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SCRIPT_CHECK_METADATA = Metadata(
    id="1ec7bab89de6f0062a23a1361628a4abde50ae24.boutiques",
    name="@ScriptCheck",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VScriptCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__script_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    uncleaned_file: OutputPathType
    """Uncleaned original file with specified suffix"""
    cleaned_file: OutputPathType
    """Cleaned file if -clean option is used"""


def v__script_check(
    scripts: list[InputPathType],
    clean: bool = False,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> VScriptCheckOutputs:
    """
    Checks scripts for improperly terminated lines and optionally cleans them.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        scripts: Scripts to be checked for improperly terminated lines.
        clean: Clean bad line breaks.
        suffix: Rename uncleaned file with specified suffix. Default is .uncln.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VScriptCheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SCRIPT_CHECK_METADATA)
    cargs = []
    cargs.append("@ScriptCheck")
    if clean:
        cargs.append("-clean")
    if suffix is not None:
        cargs.extend([
            "-suffix",
            suffix
        ])
    cargs.extend([execution.input_file(f) for f in scripts])
    ret = VScriptCheckOutputs(
        root=execution.output_file("."),
        uncleaned_file=execution.output_file("{SCRIPT}.uncln"),
        cleaned_file=execution.output_file("{SCRIPT}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VScriptCheckOutputs",
    "V__SCRIPT_CHECK_METADATA",
    "v__script_check",
]

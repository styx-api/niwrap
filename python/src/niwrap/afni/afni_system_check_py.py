# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_SYSTEM_CHECK_PY_METADATA = Metadata(
    id="561605c39b2a296b2c61c5f34bc02b377a92937a.boutiques",
    name="afni_system_check.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AfniSystemCheckPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_system_check_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_system_check_py(
    runner: Runner | None = None,
) -> AfniSystemCheckPyOutputs:
    """
    Perform various system checks for figuring out AFNI installation issues.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_system_check.py.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniSystemCheckPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_SYSTEM_CHECK_PY_METADATA)
    cargs = []
    cargs.append("afni_system_check.py")
    cargs.append("[TERMINAL_OPTS]")
    cargs.append("[ACTION_OPTS]")
    cargs.append("[OTHER_OPTS]")
    ret = AfniSystemCheckPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_SYSTEM_CHECK_PY_METADATA",
    "AfniSystemCheckPyOutputs",
    "afni_system_check_py",
]

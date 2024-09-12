# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

UBER_ALIGN_TEST_PY_METADATA = Metadata(
    id="ae56a4b4e64a9fd681065c6aac82cf43606fd468.boutiques",
    name="uber_align_test.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class UberAlignTestPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uber_align_test_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def uber_align_test_py(
    runner: Runner | None = None,
) -> UberAlignTestPyOutputs:
    """
    Generate script to test anatomical/EPI alignment.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/uber_align_test.py.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UberAlignTestPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UBER_ALIGN_TEST_PY_METADATA)
    cargs = []
    cargs.append("uber_align_test.py")
    cargs.append("[COMMANDS]")
    cargs.append("[OPTIONS]")
    ret = UberAlignTestPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UBER_ALIGN_TEST_PY_METADATA",
    "UberAlignTestPyOutputs",
    "uber_align_test_py",
]

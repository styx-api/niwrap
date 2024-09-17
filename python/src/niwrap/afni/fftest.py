# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FFTEST_METADATA = Metadata(
    id="adb332c4d453963a3cbe42d90b66afd866626a79.boutiques",
    name="fftest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FftestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fftest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fftest(
    length: float,
    num_tests: float,
    vector_size: float,
    quiet_mode: bool = False,
    runner: Runner | None = None,
) -> FftestOutputs:
    """
    A command line tool for testing purposes.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/fftest.html
    
    Args:
        length: Length of the test.
        num_tests: Number of tests to run.
        vector_size: Vector size for the test.
        quiet_mode: Quiet mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FftestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FFTEST_METADATA)
    cargs = []
    cargs.append("fftest")
    cargs.append(str(length))
    cargs.append(str(num_tests))
    cargs.append(str(vector_size))
    if quiet_mode:
        cargs.append("-q")
    ret = FftestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FFTEST_METADATA",
    "FftestOutputs",
    "fftest",
]

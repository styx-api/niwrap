# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.802373

import typing

from ..styxdefs import *


SPEC_FILE_RELOCATE_METADATA = Metadata(
    id="d345adce5d9eaaa82b446d0dcdd45489b92e46fb",
    name="spec-file-relocate",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SpecFileRelocateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spec_file_relocate(...)`.
    """


def spec_file_relocate(
    runner: Runner,
    input_spec: str,
    output_spec: str,
) -> SpecFileRelocateOutputs:
    """
    RECREATE SPEC FILE IN NEW LOCATION.
    
    Spec files contain internal relative paths, such that moving or copying a
    spec file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the spec file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Args:
        runner: Command runner
        input_spec: the spec file to use
        output_spec: output - the new spec file to create
    Returns:
        NamedTuple of outputs (described in `SpecFileRelocateOutputs`).
    """
    execution = runner.start_execution(SPEC_FILE_RELOCATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-spec-file-relocate")
    cargs.append(input_spec)
    cargs.append(output_spec)
    ret = SpecFileRelocateOutputs(
    )
    execution.run(cargs)
    return ret

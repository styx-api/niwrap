# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BREC_METADATA = Metadata(
    id="926878e94d713380f9f820e8daf052c7f36030e8.boutiques",
    name="brec",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class BrecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `brec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def brec(
    my_file: str,
    depth_limit: bool = False,
    runner: Runner | None = None,
) -> BrecOutputs:
    """
    A description for brec tool could not be retrieved.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        my_file: Input file with .rec extension.
        depth_limit: Optional depth limit flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BrecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BREC_METADATA)
    cargs = []
    cargs.append("brec")
    cargs.append(my_file)
    if depth_limit:
        cargs.append("-depth_limit")
    ret = BrecOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BREC_METADATA",
    "BrecOutputs",
    "brec",
]

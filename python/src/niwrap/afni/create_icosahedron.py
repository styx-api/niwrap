# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CREATE_ICOSAHEDRON_METADATA = Metadata(
    id="e53f40ccc9791a6287b72adf8bd45877deb824ec.boutiques",
    name="CreateIcosahedron",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class CreateIcosahedronOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_icosahedron(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def create_icosahedron(
    runner: Runner | None = None,
) -> CreateIcosahedronOutputs:
    """
    Tool to create an icosahedron with optional tessellation.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/CreateIcosahedron.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateIcosahedronOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CREATE_ICOSAHEDRON_METADATA)
    cargs = []
    cargs.append("CreateIcosahedron")
    cargs.append("[-rad")
    cargs.append("r]")
    cargs.append("[-rd")
    cargs.append("recDepth]")
    cargs.append("[-ld")
    cargs.append("linDepth]")
    cargs.append("[-ctr")
    cargs.append("ctr]")
    cargs.append("[-prefix")
    cargs.append("fout]")
    cargs.append("[-min_nodes")
    cargs.append("MIN_NODES]")
    cargs.append("[-nums]")
    cargs.append("[-nums_quiet]")
    cargs.append("[-tosphere]")
    cargs.append("[-help]")
    ret = CreateIcosahedronOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CREATE_ICOSAHEDRON_METADATA",
    "CreateIcosahedronOutputs",
    "create_icosahedron",
]

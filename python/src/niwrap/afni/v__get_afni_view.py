# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__GET_AFNI_VIEW_METADATA = Metadata(
    id="7a3936ebb978e01b7a83696901a1ad7e6bad42f0.boutiques",
    name="@GetAfniView",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VGetAfniViewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_view(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    afni_view: OutputPathType
    """The AFNI view extension retrieved from the dataset name"""


def v__get_afni_view(
    dataset_name: str,
    runner: Runner | None = None,
) -> VGetAfniViewOutputs:
    """
    A tool to retrieve the AFNI view of a given dataset name.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset_name: Name of the dataset (including path) from which to\
            retrieve the AFNI view (+orig, +acpc, etc.).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniViewOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_VIEW_METADATA)
    cargs = []
    cargs.append("@GetAfniView")
    cargs.append(dataset_name)
    ret = VGetAfniViewOutputs(
        root=execution.output_file("."),
        afni_view=execution.output_file("view_extension.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VGetAfniViewOutputs",
    "V__GET_AFNI_VIEW_METADATA",
    "v__get_afni_view",
]

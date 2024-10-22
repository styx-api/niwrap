# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_ADD_XFORM_TO_HEADER_METADATA = Metadata(
    id="9210b26db2a9849240481e01beacbf5ccc757e19.boutiques",
    name="mri_add_xform_to_header",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriAddXformToHeaderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_add_xform_to_header(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Volume output with added transformation."""


def mri_add_xform_to_header(
    xfm_file: InputPathType,
    input_volume: InputPathType,
    output_volume: str,
    verbose: bool = False,
    copy_name: bool = False,
    runner: Runner | None = None,
) -> MriAddXformToHeaderOutputs:
    """
    Program to add specified transformation to the volume header.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        xfm_file: Transformation file to be added to the volume header.
        input_volume: Input volume to which the transformation is added.
        output_volume: Output volume with the transformation included.
        verbose: Enable verbose output for more detailed logging.
        copy_name: Copy the name of the xfm file without loading it.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAddXformToHeaderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ADD_XFORM_TO_HEADER_METADATA)
    cargs = []
    cargs.append("mri_add_xform_to_header")
    cargs.append(execution.input_file(xfm_file))
    cargs.append(execution.input_file(input_volume))
    cargs.append(output_volume)
    if verbose:
        cargs.append("-v")
    if copy_name:
        cargs.append("-c")
    ret = MriAddXformToHeaderOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_ADD_XFORM_TO_HEADER_METADATA",
    "MriAddXformToHeaderOutputs",
    "mri_add_xform_to_header",
]

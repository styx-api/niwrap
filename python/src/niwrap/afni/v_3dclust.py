# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DCLUST_METADATA = Metadata(
    id="af5ec3a11927a6c957d30f3fa58051ca30dde8d5.boutiques",
    name="3dclust",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dclustOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dclust(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    prefixed_output: OutputPathType
    """New dataset with clusters set to zero based on prefix."""
    ordered_mask_output: OutputPathType
    """Ordered mask dataset based on savemask prefix."""


def v_3dclust(
    datasets: list[InputPathType],
    runner: Runner | None = None,
) -> V3dclustOutputs:
    """
    Performs simple-minded cluster detection in 3D datasets.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dclust.html
    
    Args:
        datasets: Input dataset(s). More than one allowed, but only the first\
            sub-brick of the dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dclustOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DCLUST_METADATA)
    cargs = []
    cargs.append("3dclust")
    cargs.append("[EDITING_OPTIONS]")
    cargs.append("[OTHER_OPTIONS]")
    cargs.append("[CLUSTERING_TYPE]")
    cargs.extend([execution.input_file(f) for f in datasets])
    ret = V3dclustOutputs(
        root=execution.output_file("."),
        prefixed_output=execution.output_file("[PREFIX].nii.gz"),
        ordered_mask_output=execution.output_file("[SAVEMASK].nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dclustOutputs",
    "V_3DCLUST_METADATA",
    "v_3dclust",
]

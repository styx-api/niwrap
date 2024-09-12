# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LOCAL_HISTOG_METADATA = Metadata(
    id="15de7373d7efff509716e5d6e31df5725696bf4a.boutiques",
    name="3dLocalHistog",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dLocalHistogOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_histog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType
    """The output dataset with the specified prefix"""
    output_dataset_brik: OutputPathType
    """The output dataset with the specified prefix"""
    histogram_file: OutputPathType | None
    """The overall histogram saved into the specified file"""


def v_3d_local_histog(
    prefix: str,
    input_datasets: list[InputPathType],
    nbhd_option: str | None = None,
    hsave: str | None = None,
    lab_file: InputPathType | None = None,
    exclude: list[str] | None = None,
    mincount: float | None = None,
    runner: Runner | None = None,
) -> V3dLocalHistogOutputs:
    """
    This program computes a local histogram at each voxel in the input datasets.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLocalHistog.html
    
    Args:
        prefix: Use string 'ppp' as the prefix for the output dataset.
        input_datasets: Input dataset(s) for the 3dLocalHistog tool.
        nbhd_option: Defines the region around each voxel to be used for the\
            statistics calculation. Available formats: 'SPHERE(r)', 'RECT(a,b,c)',\
            'RHDD(a)', 'TOHD(a)'.
        hsave: Save the overall histogram into file 'sss'. This file will have\
            2 columns: value and count.
        lab_file: Use file 'LL' as a label file.
        exclude: Exclude values from 'a' to 'b' from the counting. This option\
            can be used more than once.
        mincount: Exclude values which appear in the overall histogram fewer\
            than 'mm' times.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalHistogOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_HISTOG_METADATA)
    cargs = []
    cargs.append("3dLocalHistog")
    if nbhd_option is not None:
        cargs.extend([
            "-nbhd",
            nbhd_option
        ])
    cargs.append("-prefix")
    cargs.extend([
        "-prefix",
        prefix
    ])
    if hsave is not None:
        cargs.extend([
            "-hsave",
            hsave
        ])
    if lab_file is not None:
        cargs.extend([
            "-lab_file",
            execution.input_file(lab_file)
        ])
    if exclude is not None:
        cargs.extend([
            "-exclude",
            *exclude
        ])
    if mincount is not None:
        cargs.extend([
            "-mincount",
            str(mincount)
        ])
    cargs.extend([execution.input_file(f) for f in input_datasets])
    ret = V3dLocalHistogOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(prefix + "+orig.HEAD"),
        output_dataset_brik=execution.output_file(prefix + "+orig.BRIK"),
        histogram_file=execution.output_file(hsave) if (hsave is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLocalHistogOutputs",
    "V_3D_LOCAL_HISTOG_METADATA",
    "v_3d_local_histog",
]

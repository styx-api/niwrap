# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_KRUSKAL_WALLIS_METADATA = Metadata(
    id="9f0d0fcbf82afbc8e1259e9cf3edf1708b9f11b3",
    name="3dKruskalWallis",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_container:latest",
)


class V3dKruskalWallisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_kruskal_wallis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_prefix: OutputPathType
    """Output file containing Kruskal-Wallis statistics"""


def v_3d_kruskal_wallis(
    levels: int,
    datasets: list[str],
    output: str,
    workmem: int | None = None,
    voxel: int | None = None,
    runner: Runner | None = None,
) -> V3dKruskalWallisOutputs:
    """
    3dKruskalWallis by AFNI Development Team.
    
    This program performs nonparametric Kruskal-Wallis test for comparison of
    multiple treatments.
    
    More information: https://afni.nimh.nih.gov
    
    Args:
        levels: Number of treatments.
        datasets: Data set for treatment #1 through to treatment #s. Specify\
            sub-brick if more than one present.
        output: Kruskal-Wallis statistics are written to file prefixname.
        workmem: Number of megabytes of RAM to use for statistical workspace.
        voxel: Screen output for voxel # num.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dKruskalWallisOutputs`).
    """
    runner = runner or get_global_runner()
    if not (2 <= levels): 
        raise ValueError(f"'levels' must be greater than 2 <= x but was {levels}")
    execution = runner.start_execution(V_3D_KRUSKAL_WALLIS_METADATA)
    cargs = []
    cargs.append("3dKruskalWallis")
    cargs.extend(["-levels", str(levels)])
    cargs.extend(["-dset", *datasets])
    if workmem is not None:
        cargs.extend(["-workmem", str(workmem)])
    if voxel is not None:
        cargs.extend(["-voxel", str(voxel)])
    cargs.extend(["-out", output])
    ret = V3dKruskalWallisOutputs(
        root=execution.output_file("."),
        outfile_prefix=execution.output_file(f"{output}+tlrc"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dKruskalWallisOutputs",
    "V_3D_KRUSKAL_WALLIS_METADATA",
    "v_3d_kruskal_wallis",
]

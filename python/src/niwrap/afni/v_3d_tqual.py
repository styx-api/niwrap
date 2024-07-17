# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_TQUAL_METADATA = Metadata(
    id="6237d5f61fdfaeae8013ae54cf1d7f034bcbfa71",
    name="3dTqual",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dTqualOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tqual(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    time_series: OutputPathType
    """The 1D time series with the quality index for each sub-brick"""


def v_3d_tqual(
    dataset: InputPathType,
    spearman: bool = False,
    quadrant: bool = False,
    autoclip: bool = False,
    automask: bool = False,
    clip: float | int | None = None,
    mask: InputPathType | None = None,
    range_: bool = False,
    runner: Runner | None = None,
) -> V3dTqualOutputs:
    """
    3dTqual by RWCox.
    
    Computes a quality index for each sub-brick in a 3D+time dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTqual.html
    
    Args:
        dataset: Input 3D+time dataset.
        spearman: Quality index is 1 minus the Spearman (rank) correlation\
            coefficient of each sub-brick with the median sub-brick (default\
            method).
        quadrant: Quality index is 1 minus the quadrant correlation coefficient\
            as the quality index.
        autoclip: Clip off low-intensity regions in the median sub-brick, only\
            compute correlation between high-intensity voxels.
        automask: Automatically mask and compute correlation only across\
            high-intensity (presumably brain) voxels.
        clip: Clip off values below given threshold in the median sub-brick.
        mask: Compute correlation only across masked voxels from the given\
            dataset.
        range_: Print the median-3.5*MAD and median+3.5*MAD values with each\
            quality index for plotting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTqualOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TQUAL_METADATA)
    cargs = []
    cargs.append("3dTqual")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dataset))
    ret = V3dTqualOutputs(
        root=execution.output_file("."),
        time_series=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTqualOutputs",
    "V_3D_TQUAL_METADATA",
    "v_3d_tqual",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_THREETO_RGB_METADATA = Metadata(
    id="6982ec958451163a320e4c7914790e815630e7e3",
    name="3dThreetoRGB",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dThreetoRgbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_threeto_rgb(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType | None
    """RGB-valued dataset output"""
    output_dataset_brik: OutputPathType | None
    """RGB-valued dataset output"""


def v_3d_threeto_rgb(
    input_dataset: InputPathType,
    input_dataset2: InputPathType | None = None,
    input_dataset3: InputPathType | None = None,
    output_prefix: str | None = None,
    scale_factor: float | int | None = None,
    mask_dataset: InputPathType | None = None,
    fim: bool = False,
    anat: bool = False,
    runner: Runner | None = None,
) -> V3dThreetoRgbOutputs:
    """
    3dThreetoRGB by RWCox.
    
    Converts 3 sub-bricks of input to an RGB-valued dataset.
    
    Args:
        input_dataset: Input dataset or first dataset if three datasets are\
            provided.
        input_dataset2: Second dataset, required only if three datasets are\
            provided.
        input_dataset3: Third dataset, required only if three datasets are\
            provided.
        output_prefix: Write output into dataset with specified prefix.
        scale_factor: Multiply input values by this factor before using as RGB.
        mask_dataset: Only output nonzero values where the mask dataset is\
            nonzero.
        fim: Write result as a 'fim' type dataset (default behavior).
        anat: Write result as a anatomical type dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dThreetoRgbOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_THREETO_RGB_METADATA)
    cargs = []
    cargs.append("3dThreetoRGB")
    if output_prefix is not None:
        cargs.extend(["-prefix", output_prefix])
    if scale_factor is not None:
        cargs.extend(["-scale", str(scale_factor)])
    if mask_dataset is not None:
        cargs.extend(["-mask", execution.input_file(mask_dataset)])
    if fim:
        cargs.append("-fim")
    if anat:
        cargs.append("-anat")
    cargs.append(execution.input_file(input_dataset))
    cargs.append("[DATASET1]")
    if input_dataset2 is not None:
        cargs.append(execution.input_file(input_dataset2))
    if input_dataset3 is not None:
        cargs.append(execution.input_file(input_dataset3))
    ret = V3dThreetoRgbOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(f"{output_prefix}+rgb.HEAD") if output_prefix is not None else None,
        output_dataset_brik=execution.output_file(f"{output_prefix}+rgb.BRIK") if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dThreetoRgbOutputs",
    "V_3D_THREETO_RGB_METADATA",
    "v_3d_threeto_rgb",
]

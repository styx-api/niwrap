# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.981463

import typing

from ..styxdefs import *


CONVERT_AFFINE_METADATA = Metadata(
    id="a6c47486ff4283c4d2e0d027d87aff0cec2a7a61",
    name="convert-affine",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class ConvertAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_affine(...)`.
    """


def convert_affine(
    runner: Runner,
    opt_from_world_input: str | None = None,
    opt_from_itk_input: str | None = None,
    opt_to_world_output: str | None = None,
    opt_to_itk_output: str | None = None,
) -> ConvertAffineOutputs:
    """
    CONVERT AN AFFINE FILE BETWEEN CONVENTIONS.
    
    NIFTI world matrices can be used directly on mm coordinates via matrix
    multiplication, they use the NIFTI coordinate system, that is, positive X is
    right, positive Y is anterior, and positive Z is superior. Note that
    wb_command assumes that world matrices transform source coordinates to
    target coordinates, while other tools may use affines that transform target
    coordinates to source coordinates.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-flirt may be specified more than once.
    
    Args:
        runner: Command runner
        opt_from_world_input: input is a NIFTI 'world' affine: the input affine
        opt_from_itk_input: input is an ITK matrix: the input affine
        opt_to_world_output: write output as a NIFTI 'world' affine: output -
            the output affine
        opt_to_itk_output: write output as an ITK affine: output - the output
            affine
    Returns:
        NamedTuple of outputs (described in `ConvertAffineOutputs`).
    """
    execution = runner.start_execution(CONVERT_AFFINE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-affine")
    if opt_from_world_input is not None:
        cargs.extend(["-from-world", opt_from_world_input])
    if opt_from_itk_input is not None:
        cargs.extend(["-from-itk", opt_from_itk_input])
    if opt_to_world_output is not None:
        cargs.extend(["-to-world", opt_to_world_output])
    if opt_to_itk_output is not None:
        cargs.extend(["-to-itk", opt_to_itk_output])
    ret = ConvertAffineOutputs(
    )
    execution.run(cargs)
    return ret

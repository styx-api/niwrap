# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.787299

import typing

from ..styxdefs import *


VOLUME_VECTOR_OPERATION_METADATA = Metadata(
    id="d428250905ad6db73c68a9e916cbc177597ee718",
    name="volume-vector-operation",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeVectorOperationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_vector_operation(...)`.
    """
    volume_out: OutputPathType
    """the output file"""


def volume_vector_operation(
    runner: Runner,
    vectors_a: InputPathType,
    vectors_b: InputPathType,
    operation: str,
    volume_out: InputPathType,
    opt_normalize_a: bool = False,
    opt_normalize_b: bool = False,
    opt_normalize_output: bool = False,
    opt_magnitude: bool = False,
) -> VolumeVectorOperationOutputs:
    """
    DO A VECTOR OPERATION ON VOLUME FILES.
    
    Does a vector operation on two volume files (that must have a multiple of 3
    subvolumes). Either of the inputs may have multiple vectors (more than 3
    subvolumes), but not both (at least one must have exactly 3 subvolumes). The
    -magnitude and -normalize-output options may not be specified together, or
    with the DOT operation. The <operation> parameter must be one of the
    following:
    
    DOT
    CROSS
    ADD
    SUBTRACT
    
    Args:
        runner: Command runner
        vectors_a: first vector input file
        vectors_b: second vector input file
        operation: what vector operation to do
        volume_out: the output file
        opt_normalize_a: normalize vectors of first input
        opt_normalize_b: normalize vectors of second input
        opt_normalize_output: normalize output vectors (not valid for dot
            product)
        opt_magnitude: output the magnitude of the result (not valid for dot
            product)
    Returns:
        NamedTuple of outputs (described in `VolumeVectorOperationOutputs`).
    """
    execution = runner.start_execution(VOLUME_VECTOR_OPERATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-vector-operation")
    cargs.append(execution.input_file(vectors_a))
    cargs.append(execution.input_file(vectors_b))
    cargs.append(operation)
    cargs.append(execution.input_file(volume_out))
    if opt_normalize_a:
        cargs.append("-normalize-a")
    if opt_normalize_b:
        cargs.append("-normalize-b")
    if opt_normalize_output:
        cargs.append("-normalize-output")
    if opt_magnitude:
        cargs.append("-magnitude")
    ret = VolumeVectorOperationOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret

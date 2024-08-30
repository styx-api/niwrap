# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FIND_THE_BIGGEST_METADATA = Metadata(
    id="4223284ffaa6be319c644e5d1daaee7e360a61dc",
    name="find_the_biggest",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FindTheBiggestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `find_the_biggest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Index of the largest volume or surface"""


def find_the_biggest(
    volumes_surfaces: list[InputPathType],
    output_index: str,
    runner: Runner | None = None,
) -> FindTheBiggestOutputs:
    """
    find_the_biggest by Unknown.
    
    Tool to find the largest volume or surface from a set of inputs.
    
    Args:
        volumes_surfaces: List of input volumes or surfaces.
        output_index: Output index of the largest volume or surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FindTheBiggestOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        (volumes_surfaces is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "volumes_surfaces"
        )
    execution = runner.start_execution(FIND_THE_BIGGEST_METADATA)
    cargs = []
    cargs.append("find_the_biggest")
    cargs.extend([execution.input_file(f) for f in volumes_surfaces])
    cargs.append(output_index)
    ret = FindTheBiggestOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_index}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIND_THE_BIGGEST_METADATA",
    "FindTheBiggestOutputs",
    "find_the_biggest",
]

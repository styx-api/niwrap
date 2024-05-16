# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CONVERT_FIBER_ORIENTATIONS_METADATA = Metadata(
    id="1e91cfd8e9c2e79ad2c398109842ed3e8123ff5d",
    name="convert-fiber-orientations",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class ConvertFiberOrientationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_fiber_orientations(...)`.
    """
    fiber_out: OutputPathType
    """the output fiber orientation file"""


def convert_fiber_orientations(
    runner: Runner,
    label_volume: InputPathType,
    fiber_out: InputPathType,
) -> ConvertFiberOrientationsOutputs:
    """
    CONVERT BINGHAM PARAMETER VOLUMES TO FIBER ORIENTATION FILE.
    
    Takes precomputed bingham parameters from volume files and converts them to
    the format workbench uses for display. The <label-volume> argument must be a
    label volume, where the labels use these strings:
    
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT
    
    Args:
        runner: Command runner
        label_volume: volume of cifti structure labels
        fiber_out: the output fiber orientation file
    Returns:
        NamedTuple of outputs (described in `ConvertFiberOrientationsOutputs`).
    """
    execution = runner.start_execution(CONVERT_FIBER_ORIENTATIONS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-fiber-orientations")
    cargs.append(execution.input_file(label_volume))
    cargs.append(execution.input_file(fiber_out))
    ret = ConvertFiberOrientationsOutputs(
        fiber_out=execution.output_file(f"{fiber_out}"),
    )
    execution.run(cargs)
    return ret

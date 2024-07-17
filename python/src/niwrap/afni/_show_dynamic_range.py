# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SHOW_DYNAMIC_RANGE_METADATA = Metadata(
    id="c598df0511bbb06e5c829888f7ccf8acbd91615e",
    name="ShowDynamicRange",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class ShowDynamicRangeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `show_dynamic_range(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    minpercchange_file: OutputPathType
    """Dataset showing the percent signal change that an increment of 1 digitized value in the time series corresponds to."""
    range_file: OutputPathType
    """Dataset showing the number of discrete levels used to represent the time series."""


def show_dynamic_range(
    infile: InputPathType,
    runner: Runner | None = None,
) -> ShowDynamicRangeOutputs:
    """
    ShowDynamicRange by AFNI.
    
    The script checks the dynamic range of the time series data at locations
    inside the brain.
    
    Args:
        infile: Input EPI time series dataset (e.g. epi.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ShowDynamicRangeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SHOW_DYNAMIC_RANGE_METADATA)
    cargs = []
    cargs.append("@ShowDynamicRange")
    cargs.append(execution.input_file(infile))
    ret = ShowDynamicRangeOutputs(
        root=execution.output_file("."),
        minpercchange_file=execution.output_file(f"{pathlib.Path(infile).name}_minpercchange.nii.gz", optional=True),
        range_file=execution.output_file(f"{pathlib.Path(infile).name}.range.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SHOW_DYNAMIC_RANGE_METADATA",
    "ShowDynamicRangeOutputs",
    "show_dynamic_range",
]

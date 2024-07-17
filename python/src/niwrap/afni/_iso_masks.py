# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_ISO_MASKS_METADATA = Metadata(
    id="920610186c58e96fc14c6720b6c8de5ab38e621c",
    name="@IsoMasks",
)


class IsoMasksOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_iso_masks(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _iso_masks(
    input_dataset: InputPathType,
    isovals: list[float | int] | None = None,
    runner: Runner | None = None,
) -> IsoMasksOutputs:
    """
    @IsoMasks by unknown.
    
    Creates isosurfaces from isovolume envelopes.
    
    Args:
        input_dataset: Input dataset for creating isosurfaces.
        isovals: Isovalue thresholds for creating isosurfaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsoMasksOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_ISO_MASKS_METADATA)
    cargs = []
    cargs.append("@IsoMasks")
    cargs.append("-mask")
    cargs.extend(["-mask", execution.input_file(input_dataset)])
    if isovals is not None:
        cargs.extend(map(str, isovals))
    ret = IsoMasksOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IsoMasksOutputs",
    "_ISO_MASKS_METADATA",
    "_iso_masks",
]

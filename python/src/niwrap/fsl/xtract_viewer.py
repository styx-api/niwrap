# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

XTRACT_VIEWER_METADATA = Metadata(
    id="bd76f729ac54b26b22e247a3422cd7082ceff910",
    name="xtract_viewer",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class XtractViewerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xtract_viewer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def xtract_viewer(
    xtract_dir: str,
    species: typing.Literal["HUMAN", "MACAQUE"] | None = None,
    brain_image: InputPathType | None = None,
    structures: str | None = None,
    thresholds: list[float | int] | None = None,
    runner: Runner | None = None,
) -> XtractViewerOutputs:
    """
    xtract_viewer by FMRIB Centre, University of Oxford.
    
    Viewer tool for XTRACT output.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/XTRACT
    
    Args:
        xtract_dir: Path to XTRACT output folder.
        species: Species type (HUMAN or MACAQUE).
        brain_image: The brain image to use for the background overlay - must\
            be in the same space as tracts. Default is the FSL_HCP065_FA map for\
            HUMAN and F99 T1 brain for MACAQUE.
        structures: Structures (comma separated, default = display all that is\
            found in input folder).
        thresholds: The lower and upper thresholds applied to the tracts for\
            viewing. Default = 0.001 0.1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XtractViewerOutputs`).
    """
    runner = runner or get_global_runner()
    if thresholds is not None and not (len(thresholds) <= 2): 
        raise ValueError(f"Length of 'thresholds' must be less than 2 but was {len(thresholds)}")
    execution = runner.start_execution(XTRACT_VIEWER_METADATA)
    cargs = []
    cargs.append("xtract_viewer")
    cargs.append("-dir")
    cargs.extend(["-dir", xtract_dir])
    if species is not None:
        cargs.extend(["-species", species])
    if brain_image is not None:
        cargs.extend(["-brain", execution.input_file(brain_image)])
    if structures is not None:
        cargs.extend(["-str", structures])
    if thresholds is not None:
        cargs.extend(["-thr", *map(str, thresholds)])
    ret = XtractViewerOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XTRACT_VIEWER_METADATA",
    "XtractViewerOutputs",
    "xtract_viewer",
]

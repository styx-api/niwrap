# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_ANATOMI_CUTS_METADATA = Metadata(
    id="b3ae6660625cd9a73409943ca03518bf3c1e8760.boutiques",
    name="dmri_AnatomiCuts",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriAnatomiCutsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_anatomi_cuts(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_vtk: OutputPathType
    """Output VTK file of the segmentation"""


def dmri_anatomi_cuts(
    segmentation_file: InputPathType,
    fiber_file: InputPathType,
    clusters: float,
    points: float,
    fibers_eigen: float,
    output_folder: str,
    direction_flag: typing.Literal["s", "d", "a", "o"],
    runner: Runner | None = None,
) -> DmriAnatomiCutsOutputs:
    """
    AnatomiCuts tool for DTI fibers segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segmentation_file: Segmentation file.
        fiber_file: VTK fiber file.
        clusters: Number of clusters.
        points: Number of points.
        fibers_eigen: Number of fibers for eigen decomposition.
        output_folder: Output folder.
        direction_flag: Direction flag: 's' for straight, 'd' for diagonal, 'a'\
            for all, 'o' for none.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriAnatomiCutsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_ANATOMI_CUTS_METADATA)
    cargs = []
    cargs.append("dmri_AnatomiCuts")
    cargs.extend([
        "-s",
        execution.input_file(segmentation_file)
    ])
    cargs.extend([
        "-f",
        execution.input_file(fiber_file)
    ])
    cargs.extend([
        "-c",
        str(clusters)
    ])
    cargs.extend([
        "-n",
        str(points)
    ])
    cargs.extend([
        "-e",
        str(fibers_eigen)
    ])
    cargs.extend([
        "-o",
        output_folder
    ])
    cargs.extend([
        "-d",
        direction_flag
    ])
    ret = DmriAnatomiCutsOutputs(
        root=execution.output_file("."),
        output_vtk=execution.output_file(output_folder + "/output.vtk"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_ANATOMI_CUTS_METADATA",
    "DmriAnatomiCutsOutputs",
    "dmri_anatomi_cuts",
]

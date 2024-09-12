# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_QUAL_METADATA = Metadata(
    id="c927abddc75e51fcc598c15db923bc25092fa884.boutiques",
    name="SurfQual",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SurfQualOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_qual(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dist_output: OutputPathType
    """File containing distances of nodes from the surface's center."""
    dist_color_output: OutputPathType
    """Colorized file containing distances of nodes from the surface's
    center."""
    bad_nodes_output: OutputPathType
    """File containing nodes with bad dot product values."""
    bad_nodes_color_output: OutputPathType
    """Colorized file containing nodes with bad dot product values."""
    dotprod_output: OutputPathType
    """File containing dot product values for all nodes."""
    dotprod_color_output: OutputPathType
    """Colorized file containing dot product values for all nodes."""
    intersect_nodes_output: OutputPathType
    """File containing indices of nodes forming segments that intersect the
    surface."""


def surf_qual(
    spec_file: InputPathType,
    surface_a: list[InputPathType],
    runner: Runner | None = None,
) -> SurfQualOutputs:
    """
    A program to check the quality of surfaces.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfQual.html
    
    Args:
        spec_file: Spec file containing input surfaces.
        surface_a: Name of input surface A.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfQualOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_QUAL_METADATA)
    cargs = []
    cargs.append("SurfQual")
    cargs.append("-spec")
    cargs.extend([
        "-spec",
        execution.input_file(spec_file)
    ])
    cargs.extend([
        "-surf_A",
        *[execution.input_file(f) for f in surface_a]
    ])
    cargs.append("-sphere")
    cargs.append("[OPTIONS]")
    ret = SurfQualOutputs(
        root=execution.output_file("."),
        dist_output=execution.output_file("[OUTPREF]_Dist.1D.dset"),
        dist_color_output=execution.output_file("[OUTPREF]_Dist.1D.col"),
        bad_nodes_output=execution.output_file("[OUTPREF]_BadNodes.1D.dset"),
        bad_nodes_color_output=execution.output_file("[OUTPREF]_BadNodes.1D.col"),
        dotprod_output=execution.output_file("[OUTPREF]_dotprod.1D.dset"),
        dotprod_color_output=execution.output_file("[OUTPREF]_dotprod.1D.col"),
        intersect_nodes_output=execution.output_file("[OUTPREF]_IntersNodes.1D.dset"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_QUAL_METADATA",
    "SurfQualOutputs",
    "surf_qual",
]

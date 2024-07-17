# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CONVEX_HULL_TRIANGULATION_METADATA = Metadata(
    id="66340eefe4c016769c4490299f17fd2893c1a362",
    name="ConvexHullTriangulation",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_container:latest",
)


class ConvexHullTriangulationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convex_hull_triangulation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surf: OutputPathType | None
    """Output surface file"""


def convex_hull_triangulation(
    vol: InputPathType | None = None,
    isoval: float | int | None = None,
    isorange: list[float | int] | None = None,
    isocmask: str | None = None,
    xform: str | None = None,
    surface_input: InputPathType | None = None,
    surf_vol: InputPathType | None = None,
    input_1d: InputPathType | None = None,
    q_opt: str | None = None,
    proj_xy: bool = False,
    orig_coord: bool = False,
    these_coords: InputPathType | None = None,
    output_prefix: str | None = None,
    debug: str | None = None,
    novolreg: bool = False,
    setenv: str | None = None,
    runner: Runner | None = None,
) -> ConvexHullTriangulationOutputs:
    """
    ConvexHullTriangulation by Ziad S. Saad.
    
    A program to find the convex hull, or perform a Delaunay triangulation of a
    set of points.
    
    More information: https://afni.nimh.nih.gov/
    
    Args:
        vol: Input AFNI (or AFNI readable) volume.
        isoval: Create isosurface where volume = V.
        isorange: Create isosurface where V0 <= volume < V1.
        isocmask: Create isosurface where MASK_COM != 0. Example: -isocmask '-a\
            VOL+orig -expr (1-bool(a-V))' is equivalent to using -isoval V. NOTE:\
            Allowed only with -xform mask.
        xform: Transform to apply to volume values before searching for sign\
            change boundary. Options: mask, shift, none.
        surface_input: Input surface type.
        surf_vol: Specify a surface volume which contains a transform to apply\
            to the surface node coordinates.
        input_1d: Construct the triangulation of the points contained in 1D\
            file XYZ. Use AFNI's [] selectors to specify the XYZ columns.
        q_opt: Meshing option OPT. Options: convex_hull, triangulate_xy.
        proj_xy: Project points onto plane whose normal is the third principal\
            component. Then rotate projection so that plane is parallel to Z =\
            constant.
        orig_coord: Use original coordinates when writing surface, not\
            transformed ones.
        these_coords: Use coordinates in COORDS.1D when writing surface.
        output_prefix: Prefix of output surface. Specifies the format and\
            prefix of the surface.
        debug: Debugging level.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        setenv: Set environment variable ENVname to be ENVvalue.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvexHullTriangulationOutputs`).
    """
    runner = runner or get_global_runner()
    if isorange is not None and (len(isorange) != 2): 
        raise ValueError(f"Length of 'isorange' must be 2 but was {len(isorange)}")
    execution = runner.start_execution(CONVEX_HULL_TRIANGULATION_METADATA)
    cargs = []
    cargs.append("<main_flags>")
    cargs.append("<volume_flags>")
    cargs.append("<surface_flags>")
    cargs.append("<triangulation_flags>")
    cargs.append("<output_flags>")
    cargs.append("<debug_flags>")
    cargs.append("<global_flags>")
    ret = ConvexHullTriangulationOutputs(
        root=execution.output_file("."),
        out_surf=execution.output_file(f"{output_prefix}", optional=True) if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVEX_HULL_TRIANGULATION_METADATA",
    "ConvexHullTriangulationOutputs",
    "convex_hull_triangulation",
]

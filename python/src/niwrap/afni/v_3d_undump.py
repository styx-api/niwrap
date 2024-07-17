# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_UNDUMP_METADATA = Metadata(
    id="3982f5fc1ab386b46b629516b43b2dff4692eedd",
    name="3dUndump",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class V3dUndumpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_undump(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Main output dataset"""


def v_3d_undump(
    input_files: list[InputPathType],
    prefix: str | None = None,
    master: InputPathType | None = None,
    dimensions: list[float | int] | None = None,
    mask: InputPathType | None = None,
    datatype: str | None = None,
    dval: float | int | None = None,
    fval: float | int | None = None,
    ijk: bool = False,
    xyz: bool = False,
    sphere_radius: float | int | None = None,
    cube_mode: bool = False,
    orient: str | None = None,
    head_only: bool = False,
    roimask: InputPathType | None = None,
    allow_nan: bool = False,
    runner: Runner | None = None,
) -> V3dUndumpOutputs:
    """
    3dUndump by RWCox.
    
    Assembles a 3D dataset from an ASCII list of coordinates and optionally
    values.
    
    Args:
        input_files: Input ASCII file(s), with one voxel specification per\
            line.
        prefix: 'ppp' is the prefix for the output dataset [default = undump].
        master: 'mmm' is the master dataset, whose geometry will determine the\
            geometry of the output.
        dimensions: Sets the dimensions of the output dataset to be I by J by K\
            voxels.
        mask: Specifies a mask dataset 'MMM', which will control which voxels\
            are allowed to get values set.
        datatype: 'type' determines the voxel data type of the output, which\
            may be byte, short, or float [default = short].
        dval: 'vvv' is the default value stored in each input voxel that does\
            not have a value supplied in the input file [default = 1].
        fval: 'fff' is the fill value, used for each voxel in the output\
            dataset that is NOT listed in the input file [default = 0].
        ijk: Coordinates in the input file are (i,j,k) index triples.
        xyz: Coordinates in the input file are (x,y,z) spatial coordinates, in\
            mm.
        sphere_radius: Specifies that a sphere of radius 'rrr' will be filled\
            about each input (x,y,z) or (i,j,k) voxel.
        cube_mode: Put cubes down instead of spheres. The 'radius' then is half\
            the length of a side.
        orient: Specifies the coordinate order used by -xyz. The code must be 3\
            letters, one each from the pairs {R,L} {A,P} {I,S}.
        head_only: Creates only the .HEAD file.
        roimask: Specifies which voxels get what numbers by using a dataset\
            'rrr', instead of coordinates.
        allow_nan: Allow NaN (not-a-number) values to be entered.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dUndumpOutputs`).
    """
    runner = runner or get_global_runner()
    if dimensions is not None and not (len(dimensions) <= 3): 
        raise ValueError(f"Length of 'dimensions' must be less than 3 but was {len(dimensions)}")
    execution = runner.start_execution(V_3D_UNDUMP_METADATA)
    cargs = []
    cargs.append("3dUndump")
    cargs.extend([execution.input_file(f) for f in input_files])
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if master is not None:
        cargs.extend(["-master", execution.input_file(master)])
    if dimensions is not None:
        cargs.extend(["-dimen", *map(str, dimensions)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if datatype is not None:
        cargs.extend(["-datum", datatype])
    if dval is not None:
        cargs.extend(["-dval", str(dval)])
    if fval is not None:
        cargs.extend(["-fval", str(fval)])
    if xyz:
        cargs.append("-xyz")
    if sphere_radius is not None:
        cargs.extend(["-srad", str(sphere_radius)])
    if cube_mode:
        cargs.append("-cubes")
    if orient is not None:
        cargs.extend(["-orient", orient])
    if head_only:
        cargs.append("-head_only")
    if roimask is not None:
        cargs.extend(["-ROImask", execution.input_file(roimask)])
    if allow_nan:
        cargs.append("-allow_NaN")
    ret = V3dUndumpOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{prefix}.nii.gz", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dUndumpOutputs",
    "V_3D_UNDUMP_METADATA",
    "v_3d_undump",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_EMPTY_METADATA = Metadata(
    id="132e685d0d86e55bedd97f83b1ca0310470c62de",
    name="3dEmpty",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dEmptyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_empty(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output empty dataset header file"""


def v_3d_empty(
    prefix: str | None = None,
    nxyz: list[float | int] | None = None,
    geometry: str | None = None,
    nt_: float | int | None = None,
    runner: Runner | None = None,
) -> V3dEmptyOutputs:
    """
    3dEmpty by AFNI Team.
    
    Tool to create an 'empty' dataset .HEAD file.
    
    More information: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix name for output file (default = 'Empty').
        nxyz: Set number of voxels to 'x', 'y', and 'z' along the 3 axes\
            [defaults=64].
        geometry: Set the 3D geometry of the grid using a string of the form\
            'MATRIX(a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34):nx,ny,nz'.
        nt_: Number of time points [default=1].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEmptyOutputs`).
    """
    runner = runner or get_global_runner()
    if nxyz is not None and (len(nxyz) != 3): 
        raise ValueError(f"Length of 'nxyz' must be 3 but was {len(nxyz)}")
    execution = runner.start_execution(V_3D_EMPTY_METADATA)
    cargs = []
    cargs.append("3dEmpty")
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if geometry is not None:
        cargs.extend(["-geometry", geometry])
    if nxyz is not None:
        cargs.extend(["-nxyz", *map(str, nxyz)])
    if nt_ is not None:
        cargs.extend(["-nt", str(nt_)])
    ret = V3dEmptyOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{prefix}.HEAD") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dEmptyOutputs",
    "V_3D_EMPTY_METADATA",
    "v_3d_empty",
]

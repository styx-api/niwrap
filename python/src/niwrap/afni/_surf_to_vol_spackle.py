# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_SURF_TO_VOL_SPACKLE_METADATA = Metadata(
    id="84514d49922187b8e5825105ac897079904a011d",
    name="@surf_to_vol_spackle",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="example/image:latest",
)


class SurfToVolSpackleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_surf_to_vol_spackle(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """The primary output volume file with surface measures projected."""


def _surf_to_vol_spackle(
    maskset: InputPathType,
    spec: InputPathType,
    surf_a: str,
    surfset: InputPathType,
    prefix: str,
    surf_b: str | None = None,
    normal_vector_length: float | int | None = None,
    search_radius: float | int | None = None,
    num_steps: float | int | None = None,
    keep_temp_files: bool = False,
    max_iters: float | int | None = None,
    use_mode: bool = False,
    datum_type: str | None = None,
    ignore_unknown_options: bool = False,
    runner: Runner | None = None,
) -> SurfToVolSpackleOutputs:
    """
    @surf_to_vol_spackle by Author Name.
    
    Project data from a surface dataset into a volume primarily using 3dSurf2Vol
    but then filling any holes with an iterative smoothing procedure.
    
    Args:
        maskset: Mask dataset in which to project surface measures.
        spec: Surface specification file with list of surfaces.
        surf_a: Name of the first surface, e.g., smoothwm, pial, etc.
        surfset: Dataset of surface measures.
        prefix: Basename of output. Final name used is prefix.nii.gz.
        surf_b: Name of the second surface. If not included, computes using\
            normal vector.
        normal_vector_length: Normal vector length if only using a single\
            surface (default 2 mm).
        search_radius: Radius for search for mean to fill holes (default 2 mm).
        num_steps: Number of steps on line segments (default 10).
        keep_temp_files: Do not remove any of the temporary files (default is\
            to remove them).
        max_iters: Maximum number of smoothing and filling iterations (default\
            is 4).
        use_mode: Use mode instead of non-zero median (appropriate for ROIs).
        datum_type: Set datum type to byte, short, or float instead of maskset\
            type. Mode triggers -datum short.
        ignore_unknown_options: Ignore additional options that are not needed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfToVolSpackleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_SURF_TO_VOL_SPACKLE_METADATA)
    cargs = []
    cargs.append("@surf_to_vol_spackle")
    cargs.append(execution.input_file(maskset))
    cargs.append(execution.input_file(spec))
    cargs.append(surf_a)
    if surf_b is not None:
        cargs.append(surf_b)
    cargs.append(execution.input_file(surfset))
    cargs.append(prefix)
    if normal_vector_length is not None:
        cargs.extend(["-f_pn_mm", str(normal_vector_length)])
    if search_radius is not None:
        cargs.extend(["-meanrad", str(search_radius)])
    if num_steps is not None:
        cargs.extend(["-nsteps", str(num_steps)])
    if keep_temp_files:
        cargs.append("-keep_temp_files")
    if max_iters is not None:
        cargs.extend(["-maxiters", str(max_iters)])
    if use_mode:
        cargs.append("-mode")
    if datum_type is not None:
        cargs.extend(["-datum", datum_type])
    if ignore_unknown_options:
        cargs.append("-ignore_unknown_options")
    ret = SurfToVolSpackleOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(f"{prefix}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SurfToVolSpackleOutputs",
    "_SURF_TO_VOL_SPACKLE_METADATA",
    "_surf_to_vol_spackle",
]

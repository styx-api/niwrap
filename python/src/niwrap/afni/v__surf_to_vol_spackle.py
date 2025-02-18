# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SURF_TO_VOL_SPACKLE_METADATA = Metadata(
    id="b0444f30cf6b3a9a0996f5b8c66a1134d87d5052.boutiques",
    name="@surf_to_vol_spackle",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VSurfToVolSpackleParameters = typing.TypedDict('VSurfToVolSpackleParameters', {
    "__STYX_TYPE__": typing.Literal["@surf_to_vol_spackle"],
    "maskset": InputPathType,
    "spec": InputPathType,
    "surfA": str,
    "surfB": typing.NotRequired[str | None],
    "surfset": InputPathType,
    "prefix": str,
    "normal_vector_length": typing.NotRequired[float | None],
    "search_radius": typing.NotRequired[float | None],
    "num_steps": typing.NotRequired[float | None],
    "keep_temp_files": bool,
    "max_iters": typing.NotRequired[float | None],
    "use_mode": bool,
    "datum_type": typing.NotRequired[str | None],
    "ignore_unknown_options": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "@surf_to_vol_spackle": v__surf_to_vol_spackle_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "@surf_to_vol_spackle": v__surf_to_vol_spackle_outputs,
    }.get(t)


class VSurfToVolSpackleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__surf_to_vol_spackle(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """The primary output volume file with surface measures projected."""


def v__surf_to_vol_spackle_params(
    maskset: InputPathType,
    spec: InputPathType,
    surf_a: str,
    surfset: InputPathType,
    prefix: str,
    surf_b: str | None = None,
    normal_vector_length: float | None = None,
    search_radius: float | None = None,
    num_steps: float | None = None,
    keep_temp_files: bool = False,
    max_iters: float | None = None,
    use_mode: bool = False,
    datum_type: str | None = None,
    ignore_unknown_options: bool = False,
) -> VSurfToVolSpackleParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@surf_to_vol_spackle",
        "maskset": maskset,
        "spec": spec,
        "surfA": surf_a,
        "surfset": surfset,
        "prefix": prefix,
        "keep_temp_files": keep_temp_files,
        "use_mode": use_mode,
        "ignore_unknown_options": ignore_unknown_options,
    }
    if surf_b is not None:
        params["surfB"] = surf_b
    if normal_vector_length is not None:
        params["normal_vector_length"] = normal_vector_length
    if search_radius is not None:
        params["search_radius"] = search_radius
    if num_steps is not None:
        params["num_steps"] = num_steps
    if max_iters is not None:
        params["max_iters"] = max_iters
    if datum_type is not None:
        params["datum_type"] = datum_type
    return params


def v__surf_to_vol_spackle_cargs(
    params: VSurfToVolSpackleParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("@surf_to_vol_spackle")
    cargs.append(execution.input_file(params.get("maskset")))
    cargs.append(execution.input_file(params.get("spec")))
    cargs.append(params.get("surfA"))
    if params.get("surfB") is not None:
        cargs.append(params.get("surfB"))
    cargs.append(execution.input_file(params.get("surfset")))
    cargs.append(params.get("prefix"))
    if params.get("normal_vector_length") is not None:
        cargs.extend([
            "-f_pn_mm",
            str(params.get("normal_vector_length"))
        ])
    if params.get("search_radius") is not None:
        cargs.extend([
            "-meanrad",
            str(params.get("search_radius"))
        ])
    if params.get("num_steps") is not None:
        cargs.extend([
            "-nsteps",
            str(params.get("num_steps"))
        ])
    if params.get("keep_temp_files"):
        cargs.append("-keep_temp_files")
    if params.get("max_iters") is not None:
        cargs.extend([
            "-maxiters",
            str(params.get("max_iters"))
        ])
    if params.get("use_mode"):
        cargs.append("-mode")
    if params.get("datum_type") is not None:
        cargs.extend([
            "-datum",
            params.get("datum_type")
        ])
    if params.get("ignore_unknown_options"):
        cargs.append("-ignore_unknown_options")
    return cargs


def v__surf_to_vol_spackle_outputs(
    params: VSurfToVolSpackleParameters,
    execution: Execution,
) -> VSurfToVolSpackleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VSurfToVolSpackleOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("prefix") + ".nii.gz"),
    )
    return ret


def v__surf_to_vol_spackle_execute(
    params: VSurfToVolSpackleParameters,
    execution: Execution,
) -> VSurfToVolSpackleOutputs:
    """
    Project data from a surface dataset into a volume primarily using 3dSurf2Vol but
    then filling any holes with an iterative smoothing procedure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VSurfToVolSpackleOutputs`).
    """
    cargs = v__surf_to_vol_spackle_cargs(params, execution)
    ret = v__surf_to_vol_spackle_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__surf_to_vol_spackle(
    maskset: InputPathType,
    spec: InputPathType,
    surf_a: str,
    surfset: InputPathType,
    prefix: str,
    surf_b: str | None = None,
    normal_vector_length: float | None = None,
    search_radius: float | None = None,
    num_steps: float | None = None,
    keep_temp_files: bool = False,
    max_iters: float | None = None,
    use_mode: bool = False,
    datum_type: str | None = None,
    ignore_unknown_options: bool = False,
    runner: Runner | None = None,
) -> VSurfToVolSpackleOutputs:
    """
    Project data from a surface dataset into a volume primarily using 3dSurf2Vol but
    then filling any holes with an iterative smoothing procedure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
        NamedTuple of outputs (described in `VSurfToVolSpackleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SURF_TO_VOL_SPACKLE_METADATA)
    params = v__surf_to_vol_spackle_params(maskset=maskset, spec=spec, surf_a=surf_a, surf_b=surf_b, surfset=surfset, prefix=prefix, normal_vector_length=normal_vector_length, search_radius=search_radius, num_steps=num_steps, keep_temp_files=keep_temp_files, max_iters=max_iters, use_mode=use_mode, datum_type=datum_type, ignore_unknown_options=ignore_unknown_options)
    return v__surf_to_vol_spackle_execute(params, execution)


__all__ = [
    "VSurfToVolSpackleOutputs",
    "VSurfToVolSpackleParameters",
    "V__SURF_TO_VOL_SPACKLE_METADATA",
    "v__surf_to_vol_spackle",
    "v__surf_to_vol_spackle_params",
]

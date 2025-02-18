# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_NORMALIZE_METADATA = Metadata(
    id="600d2e82bac484d0fa09b08fc06b759b58c55a5b.boutiques",
    name="mri_normalize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriNormalizeParameters = typing.TypedDict('MriNormalizeParameters', {
    "__STYX_TYPE__": typing.Literal["mri_normalize"],
    "input_vol": InputPathType,
    "output_vol": str,
    "norm_iters": typing.NotRequired[float | None],
    "disable_1d": bool,
    "nonmax_suppress": typing.NotRequired[float | None],
    "conform": bool,
    "nonconform": bool,
    "gentle": bool,
    "control_points": typing.NotRequired[InputPathType | None],
    "fonly_control_points": typing.NotRequired[InputPathType | None],
    "lonly_labels": typing.NotRequired[InputPathType | None],
    "labels": typing.NotRequired[InputPathType | None],
    "write_volumes": typing.NotRequired[str | None],
    "intensity_above": typing.NotRequired[float | None],
    "intensity_below": typing.NotRequired[float | None],
    "intensity_gradient": typing.NotRequired[float | None],
    "prune": bool,
    "no_gentle_cp": bool,
    "mask_file": typing.NotRequired[InputPathType | None],
    "atlas_transform": typing.NotRequired[str | None],
    "noskull": bool,
    "monkey": bool,
    "nosnr": bool,
    "sigma_smooth": typing.NotRequired[float | None],
    "aseg_file": typing.NotRequired[InputPathType | None],
    "debug_v": typing.NotRequired[str | None],
    "debug_d": typing.NotRequired[str | None],
    "renorm_vol": typing.NotRequired[InputPathType | None],
    "checknorm_vol": typing.NotRequired[str | None],
    "load_read_cp": typing.NotRequired[str | None],
    "cp_output_vol": typing.NotRequired[InputPathType | None],
    "surface_transform": typing.NotRequired[str | None],
    "seed_value": typing.NotRequired[float | None],
    "print_help": bool,
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
        "mri_normalize": mri_normalize_cargs,
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
        "mri_normalize": mri_normalize_outputs,
    }.get(t)


class MriNormalizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_normalize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Normalized output volume"""
    controlpoints_output: OutputPathType
    """Output final control points as a volume, applicable only with -aseg"""


def mri_normalize_params(
    input_vol: InputPathType,
    output_vol: str,
    norm_iters: float | None = None,
    disable_1d: bool = False,
    nonmax_suppress: float | None = None,
    conform: bool = False,
    nonconform: bool = False,
    gentle: bool = False,
    control_points: InputPathType | None = None,
    fonly_control_points: InputPathType | None = None,
    lonly_labels: InputPathType | None = None,
    labels: InputPathType | None = None,
    write_volumes: str | None = None,
    intensity_above: float | None = None,
    intensity_below: float | None = None,
    intensity_gradient: float | None = None,
    prune: bool = False,
    no_gentle_cp: bool = False,
    mask_file: InputPathType | None = None,
    atlas_transform: str | None = None,
    noskull: bool = False,
    monkey: bool = False,
    nosnr: bool = False,
    sigma_smooth: float | None = None,
    aseg_file: InputPathType | None = None,
    debug_v: str | None = None,
    debug_d: str | None = None,
    renorm_vol: InputPathType | None = None,
    checknorm_vol: str | None = None,
    load_read_cp: str | None = None,
    cp_output_vol: InputPathType | None = None,
    surface_transform: str | None = None,
    seed_value: float | None = None,
    print_help: bool = False,
) -> MriNormalizeParameters:
    """
    Build parameters.
    
    Args:
        input_vol: Input MRI volume file.
        output_vol: Output MRI volume file.
        norm_iters: Use n 3D normalization iterations (default=2).
        disable_1d: Disable 1D normalization.
        nonmax_suppress: Turn non-maximum suppression on (1) or off (0) when\
            using interior of surfaces.
        conform: Interpolate and embed volume to be 256^3.
        nonconform: Do not conform the volume.
        gentle: Perform kinder gentler normalization.
        control_points: Use control points file (usually control.dat).
        fonly_control_points: Use only control points file.
        lonly_labels: Use only control points in label file.
        labels: Use control points in label file.
        write_volumes: Write control point (c) and bias field (b) volumes.
        intensity_above: Use control point with intensity above target\
            (default=25.0).
        intensity_below: Use control point with intensity below target\
            (default=10.0).
        intensity_gradient: Use max intensity/mm gradient (default=1.000).
        prune: Turn pruning of control points on/off (default=off).
        no_gentle_cp: Do not use gentle normalization with control points file.
        mask_file: Mask file to use.
        atlas_transform: Use atlas to exclude control points from being in\
            non-brain regions.
        noskull: Do not consider skull regions.
        monkey: Turns off 1D, sets num_3d_iter=1.
        nosnr: Disable SNR normalization.
        sigma_smooth: Smooth bias field with given sigma.
        aseg_file: Aseg file for processing.
        debug_v: For debugging.
        debug_d: For debugging.
        renorm_vol: Load volume and use all points in it that are exactly 110\
            as control points.
        checknorm_vol: Load volume and remove all control points that aren't in\
            [min max].
        load_read_cp: For reading control points and bias field.
        cp_output_vol: Output final control points as a volume (only with\
            -aseg).
        surface_transform: Normalize based on the skeleton of the interior of\
            the transformed surface.
        seed_value: Set random number generator to seed N.
        print_help: Print usage.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_normalize",
        "input_vol": input_vol,
        "output_vol": output_vol,
        "disable_1d": disable_1d,
        "conform": conform,
        "nonconform": nonconform,
        "gentle": gentle,
        "prune": prune,
        "no_gentle_cp": no_gentle_cp,
        "noskull": noskull,
        "monkey": monkey,
        "nosnr": nosnr,
        "print_help": print_help,
    }
    if norm_iters is not None:
        params["norm_iters"] = norm_iters
    if nonmax_suppress is not None:
        params["nonmax_suppress"] = nonmax_suppress
    if control_points is not None:
        params["control_points"] = control_points
    if fonly_control_points is not None:
        params["fonly_control_points"] = fonly_control_points
    if lonly_labels is not None:
        params["lonly_labels"] = lonly_labels
    if labels is not None:
        params["labels"] = labels
    if write_volumes is not None:
        params["write_volumes"] = write_volumes
    if intensity_above is not None:
        params["intensity_above"] = intensity_above
    if intensity_below is not None:
        params["intensity_below"] = intensity_below
    if intensity_gradient is not None:
        params["intensity_gradient"] = intensity_gradient
    if mask_file is not None:
        params["mask_file"] = mask_file
    if atlas_transform is not None:
        params["atlas_transform"] = atlas_transform
    if sigma_smooth is not None:
        params["sigma_smooth"] = sigma_smooth
    if aseg_file is not None:
        params["aseg_file"] = aseg_file
    if debug_v is not None:
        params["debug_v"] = debug_v
    if debug_d is not None:
        params["debug_d"] = debug_d
    if renorm_vol is not None:
        params["renorm_vol"] = renorm_vol
    if checknorm_vol is not None:
        params["checknorm_vol"] = checknorm_vol
    if load_read_cp is not None:
        params["load_read_cp"] = load_read_cp
    if cp_output_vol is not None:
        params["cp_output_vol"] = cp_output_vol
    if surface_transform is not None:
        params["surface_transform"] = surface_transform
    if seed_value is not None:
        params["seed_value"] = seed_value
    return params


def mri_normalize_cargs(
    params: MriNormalizeParameters,
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
    cargs.append("mri_normalize")
    cargs.append(execution.input_file(params.get("input_vol")))
    cargs.append(params.get("output_vol"))
    if params.get("norm_iters") is not None:
        cargs.extend([
            "-n",
            str(params.get("norm_iters"))
        ])
    if params.get("disable_1d"):
        cargs.append("-no1d")
    if params.get("nonmax_suppress") is not None:
        cargs.extend([
            "-nonmax_suppress",
            str(params.get("nonmax_suppress"))
        ])
    if params.get("conform"):
        cargs.append("-conform")
    if params.get("nonconform"):
        cargs.append("-noconform")
    if params.get("gentle"):
        cargs.append("-gentle")
    if params.get("control_points") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("control_points"))
        ])
    if params.get("fonly_control_points") is not None:
        cargs.extend([
            "-fonly",
            execution.input_file(params.get("fonly_control_points"))
        ])
    if params.get("lonly_labels") is not None:
        cargs.extend([
            "-lonly",
            execution.input_file(params.get("lonly_labels"))
        ])
    if params.get("labels") is not None:
        cargs.extend([
            "-label",
            execution.input_file(params.get("labels"))
        ])
    if params.get("write_volumes") is not None:
        cargs.extend([
            "-w",
            params.get("write_volumes")
        ])
    if params.get("intensity_above") is not None:
        cargs.extend([
            "-a",
            str(params.get("intensity_above"))
        ])
    if params.get("intensity_below") is not None:
        cargs.extend([
            "-b",
            str(params.get("intensity_below"))
        ])
    if params.get("intensity_gradient") is not None:
        cargs.extend([
            "-g",
            str(params.get("intensity_gradient"))
        ])
    if params.get("prune"):
        cargs.append("-prune")
    if params.get("no_gentle_cp"):
        cargs.append("-no-gentle-cp")
    if params.get("mask_file") is not None:
        cargs.extend([
            "-MASK",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("atlas_transform") is not None:
        cargs.extend([
            "-atlas",
            params.get("atlas_transform")
        ])
    if params.get("noskull"):
        cargs.append("-noskull")
    if params.get("monkey"):
        cargs.append("-monkey")
    if params.get("nosnr"):
        cargs.append("-nosnr")
    if params.get("sigma_smooth") is not None:
        cargs.extend([
            "-sigma",
            str(params.get("sigma_smooth"))
        ])
    if params.get("aseg_file") is not None:
        cargs.extend([
            "-aseg",
            execution.input_file(params.get("aseg_file"))
        ])
    if params.get("debug_v") is not None:
        cargs.extend([
            "-v",
            params.get("debug_v")
        ])
    if params.get("debug_d") is not None:
        cargs.extend([
            "-d",
            params.get("debug_d")
        ])
    if params.get("renorm_vol") is not None:
        cargs.extend([
            "-renorm",
            execution.input_file(params.get("renorm_vol"))
        ])
    if params.get("checknorm_vol") is not None:
        cargs.extend([
            "-checknorm",
            params.get("checknorm_vol")
        ])
    if params.get("load_read_cp") is not None:
        cargs.extend([
            "-r",
            params.get("load_read_cp")
        ])
    if params.get("cp_output_vol") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("cp_output_vol"))
        ])
    if params.get("surface_transform") is not None:
        cargs.extend([
            "-surface",
            params.get("surface_transform")
        ])
    if params.get("seed_value") is not None:
        cargs.extend([
            "-seed",
            str(params.get("seed_value"))
        ])
    if params.get("print_help"):
        cargs.append("-u")
    return cargs


def mri_normalize_outputs(
    params: MriNormalizeParameters,
    execution: Execution,
) -> MriNormalizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriNormalizeOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("output_vol")),
        controlpoints_output=execution.output_file("controlpoints_volume.nii.gz"),
    )
    return ret


def mri_normalize_execute(
    params: MriNormalizeParameters,
    execution: Execution,
) -> MriNormalizeOutputs:
    """
    Normalize the white-matter, optionally based on control points. The input volume
    is converted into a new volume where white matter image values all range around
    110.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriNormalizeOutputs`).
    """
    cargs = mri_normalize_cargs(params, execution)
    ret = mri_normalize_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_normalize(
    input_vol: InputPathType,
    output_vol: str,
    norm_iters: float | None = None,
    disable_1d: bool = False,
    nonmax_suppress: float | None = None,
    conform: bool = False,
    nonconform: bool = False,
    gentle: bool = False,
    control_points: InputPathType | None = None,
    fonly_control_points: InputPathType | None = None,
    lonly_labels: InputPathType | None = None,
    labels: InputPathType | None = None,
    write_volumes: str | None = None,
    intensity_above: float | None = None,
    intensity_below: float | None = None,
    intensity_gradient: float | None = None,
    prune: bool = False,
    no_gentle_cp: bool = False,
    mask_file: InputPathType | None = None,
    atlas_transform: str | None = None,
    noskull: bool = False,
    monkey: bool = False,
    nosnr: bool = False,
    sigma_smooth: float | None = None,
    aseg_file: InputPathType | None = None,
    debug_v: str | None = None,
    debug_d: str | None = None,
    renorm_vol: InputPathType | None = None,
    checknorm_vol: str | None = None,
    load_read_cp: str | None = None,
    cp_output_vol: InputPathType | None = None,
    surface_transform: str | None = None,
    seed_value: float | None = None,
    print_help: bool = False,
    runner: Runner | None = None,
) -> MriNormalizeOutputs:
    """
    Normalize the white-matter, optionally based on control points. The input volume
    is converted into a new volume where white matter image values all range around
    110.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input MRI volume file.
        output_vol: Output MRI volume file.
        norm_iters: Use n 3D normalization iterations (default=2).
        disable_1d: Disable 1D normalization.
        nonmax_suppress: Turn non-maximum suppression on (1) or off (0) when\
            using interior of surfaces.
        conform: Interpolate and embed volume to be 256^3.
        nonconform: Do not conform the volume.
        gentle: Perform kinder gentler normalization.
        control_points: Use control points file (usually control.dat).
        fonly_control_points: Use only control points file.
        lonly_labels: Use only control points in label file.
        labels: Use control points in label file.
        write_volumes: Write control point (c) and bias field (b) volumes.
        intensity_above: Use control point with intensity above target\
            (default=25.0).
        intensity_below: Use control point with intensity below target\
            (default=10.0).
        intensity_gradient: Use max intensity/mm gradient (default=1.000).
        prune: Turn pruning of control points on/off (default=off).
        no_gentle_cp: Do not use gentle normalization with control points file.
        mask_file: Mask file to use.
        atlas_transform: Use atlas to exclude control points from being in\
            non-brain regions.
        noskull: Do not consider skull regions.
        monkey: Turns off 1D, sets num_3d_iter=1.
        nosnr: Disable SNR normalization.
        sigma_smooth: Smooth bias field with given sigma.
        aseg_file: Aseg file for processing.
        debug_v: For debugging.
        debug_d: For debugging.
        renorm_vol: Load volume and use all points in it that are exactly 110\
            as control points.
        checknorm_vol: Load volume and remove all control points that aren't in\
            [min max].
        load_read_cp: For reading control points and bias field.
        cp_output_vol: Output final control points as a volume (only with\
            -aseg).
        surface_transform: Normalize based on the skeleton of the interior of\
            the transformed surface.
        seed_value: Set random number generator to seed N.
        print_help: Print usage.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNormalizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NORMALIZE_METADATA)
    params = mri_normalize_params(input_vol=input_vol, output_vol=output_vol, norm_iters=norm_iters, disable_1d=disable_1d, nonmax_suppress=nonmax_suppress, conform=conform, nonconform=nonconform, gentle=gentle, control_points=control_points, fonly_control_points=fonly_control_points, lonly_labels=lonly_labels, labels=labels, write_volumes=write_volumes, intensity_above=intensity_above, intensity_below=intensity_below, intensity_gradient=intensity_gradient, prune=prune, no_gentle_cp=no_gentle_cp, mask_file=mask_file, atlas_transform=atlas_transform, noskull=noskull, monkey=monkey, nosnr=nosnr, sigma_smooth=sigma_smooth, aseg_file=aseg_file, debug_v=debug_v, debug_d=debug_d, renorm_vol=renorm_vol, checknorm_vol=checknorm_vol, load_read_cp=load_read_cp, cp_output_vol=cp_output_vol, surface_transform=surface_transform, seed_value=seed_value, print_help=print_help)
    return mri_normalize_execute(params, execution)


__all__ = [
    "MRI_NORMALIZE_METADATA",
    "MriNormalizeOutputs",
    "MriNormalizeParameters",
    "mri_normalize",
    "mri_normalize_params",
]

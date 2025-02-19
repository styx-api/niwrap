# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CC_METADATA = Metadata(
    id="15e13320aa7ce00fbf8db493c28c6884f3b1ec76.boutiques",
    name="mri_cc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCcParameters = typing.TypedDict('MriCcParameters', {
    "__STYX_TYPE__": typing.Literal["mri_cc"],
    "subject_name": str,
    "output_file": typing.NotRequired[str | None],
    "aseg_file": typing.NotRequired[InputPathType | None],
    "norm_file": typing.NotRequired[InputPathType | None],
    "sdir": typing.NotRequired[str | None],
    "rotation_lta": typing.NotRequired[InputPathType | None],
    "force_flag": bool,
    "include_fornix": bool,
    "compartments": typing.NotRequired[float | None],
    "thickness": typing.NotRequired[float | None],
    "skip_voxels": typing.NotRequired[float | None],
    "max_rotation": typing.NotRequired[float | None],
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
        "mri_cc": mri_cc_cargs,
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
        "mri_cc": mri_cc_outputs,
    }.get(t)


class MriCcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType | None
    """Output volume including CC segmentation results."""


def mri_cc_params(
    subject_name: str,
    output_file: str | None = None,
    aseg_file: InputPathType | None = None,
    norm_file: InputPathType | None = None,
    sdir: str | None = None,
    rotation_lta: InputPathType | None = None,
    force_flag: bool = False,
    include_fornix: bool = False,
    compartments: float | None = None,
    thickness: float | None = None,
    skip_voxels: float | None = None,
    max_rotation: float | None = 7.0,
) -> MriCcParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name used in processing.
        output_file: Write aseg including CC to SDIR/mri/<fname>.
        aseg_file: Read aseg from SDIR/mri/<fname>.
        norm_file: Read norm from SDIR/mri/<fname>.
        sdir: Set SUBJECTS_DIR to <dname>.
        rotation_lta: Write rotation lta to global <fname>.
        force_flag: Process regardless of existing CC in input.
        include_fornix: Include fornix in segmentation.
        compartments: Subdivide into <int> compartments.
        thickness: Setting CC thickness to <int> mm.
        skip_voxels: Skipping <int> voxels in rotational align.
        max_rotation: Set max of rotations to be searched (default=7deg).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_cc",
        "subject_name": subject_name,
        "force_flag": force_flag,
        "include_fornix": include_fornix,
    }
    if output_file is not None:
        params["output_file"] = output_file
    if aseg_file is not None:
        params["aseg_file"] = aseg_file
    if norm_file is not None:
        params["norm_file"] = norm_file
    if sdir is not None:
        params["sdir"] = sdir
    if rotation_lta is not None:
        params["rotation_lta"] = rotation_lta
    if compartments is not None:
        params["compartments"] = compartments
    if thickness is not None:
        params["thickness"] = thickness
    if skip_voxels is not None:
        params["skip_voxels"] = skip_voxels
    if max_rotation is not None:
        params["max_rotation"] = max_rotation
    return params


def mri_cc_cargs(
    params: MriCcParameters,
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
    cargs.append("mri_cc")
    cargs.append(params.get("subject_name"))
    if params.get("output_file") is not None:
        cargs.extend([
            "-o",
            params.get("output_file")
        ])
    if params.get("aseg_file") is not None:
        cargs.extend([
            "-aseg",
            execution.input_file(params.get("aseg_file"))
        ])
    if params.get("norm_file") is not None:
        cargs.extend([
            "-norm",
            execution.input_file(params.get("norm_file"))
        ])
    if params.get("sdir") is not None:
        cargs.extend([
            "-sdir",
            params.get("sdir")
        ])
    if params.get("rotation_lta") is not None:
        cargs.extend([
            "-lta",
            execution.input_file(params.get("rotation_lta"))
        ])
    if params.get("force_flag"):
        cargs.append("-force")
    if params.get("include_fornix"):
        cargs.append("-f")
    if params.get("compartments") is not None:
        cargs.extend([
            "-d",
            str(params.get("compartments"))
        ])
    if params.get("thickness") is not None:
        cargs.extend([
            "-t",
            str(params.get("thickness"))
        ])
    if params.get("skip_voxels") is not None:
        cargs.extend([
            "-s",
            str(params.get("skip_voxels"))
        ])
    if params.get("max_rotation") is not None:
        cargs.extend([
            "-m",
            str(params.get("max_rotation"))
        ])
    return cargs


def mri_cc_outputs(
    params: MriCcParameters,
    execution: Execution,
) -> MriCcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCcOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file("SDIR/mri/" + params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def mri_cc_execute(
    params: MriCcParameters,
    execution: Execution,
) -> MriCcOutputs:
    """
    Segments the corpus callosum into five separate labels in the subcortical
    segmentation volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCcOutputs`).
    """
    params = execution.params(params)
    cargs = mri_cc_cargs(params, execution)
    ret = mri_cc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_cc(
    subject_name: str,
    output_file: str | None = None,
    aseg_file: InputPathType | None = None,
    norm_file: InputPathType | None = None,
    sdir: str | None = None,
    rotation_lta: InputPathType | None = None,
    force_flag: bool = False,
    include_fornix: bool = False,
    compartments: float | None = None,
    thickness: float | None = None,
    skip_voxels: float | None = None,
    max_rotation: float | None = 7.0,
    runner: Runner | None = None,
) -> MriCcOutputs:
    """
    Segments the corpus callosum into five separate labels in the subcortical
    segmentation volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name used in processing.
        output_file: Write aseg including CC to SDIR/mri/<fname>.
        aseg_file: Read aseg from SDIR/mri/<fname>.
        norm_file: Read norm from SDIR/mri/<fname>.
        sdir: Set SUBJECTS_DIR to <dname>.
        rotation_lta: Write rotation lta to global <fname>.
        force_flag: Process regardless of existing CC in input.
        include_fornix: Include fornix in segmentation.
        compartments: Subdivide into <int> compartments.
        thickness: Setting CC thickness to <int> mm.
        skip_voxels: Skipping <int> voxels in rotational align.
        max_rotation: Set max of rotations to be searched (default=7deg).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CC_METADATA)
    params = mri_cc_params(
        subject_name=subject_name,
        output_file=output_file,
        aseg_file=aseg_file,
        norm_file=norm_file,
        sdir=sdir,
        rotation_lta=rotation_lta,
        force_flag=force_flag,
        include_fornix=include_fornix,
        compartments=compartments,
        thickness=thickness,
        skip_voxels=skip_voxels,
        max_rotation=max_rotation,
    )
    return mri_cc_execute(params, execution)


__all__ = [
    "MRI_CC_METADATA",
    "MriCcOutputs",
    "MriCcParameters",
    "mri_cc",
    "mri_cc_params",
]

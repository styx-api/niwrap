# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_GRADUNWARP_METADATA = Metadata(
    id="b0cc1536d78ca9cef5fa233e1c04b509599e2a82.boutiques",
    name="mri_gradunwarp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriGradunwarpParameters = typing.TypedDict('MriGradunwarpParameters', {
    "__STYX_TYPE__": typing.Literal["mri_gradunwarp"],
    "gradient_coeff": typing.NotRequired[InputPathType | None],
    "load_transtbl": typing.NotRequired[InputPathType | None],
    "input_file": InputPathType,
    "output_file": typing.NotRequired[str | None],
    "out_transtbl": typing.NotRequired[str | None],
    "save_transtbl_only": bool,
    "interpolation_type": typing.NotRequired[str | None],
    "nthreads": typing.NotRequired[float | None],
    "checkopts": bool,
    "version": bool,
    "help": bool,
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
        "mri_gradunwarp": mri_gradunwarp_cargs,
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
        "mri_gradunwarp": mri_gradunwarp_outputs,
    }.get(t)


class MriGradunwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gradunwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unwarped_output: OutputPathType | None
    """Unwarped output volume or surface"""
    output_transform_table: OutputPathType | None
    """Saved unwarp transform table in m3z format"""


def mri_gradunwarp_params(
    input_file: InputPathType,
    gradient_coeff: InputPathType | None = None,
    load_transtbl: InputPathType | None = None,
    output_file: str | None = None,
    out_transtbl: str | None = None,
    save_transtbl_only: bool = False,
    interpolation_type: str | None = "trilinear",
    nthreads: float | None = None,
    checkopts: bool = False,
    version: bool = False,
    help_: bool = False,
) -> MriGradunwarpParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input warped volume or surface.
        gradient_coeff: Gradient coefficient input file (not to be used with\
            --load_transtbl).
        load_transtbl: Load unwarp transform table in m3z format (not to be\
            used with --gradcoeff).
        output_file: Output unwarped volume or surface.
        out_transtbl: Save unwarp transform table in m3z format.
        save_transtbl_only: Just save unwarp transform table in m3z format,\
            requires --gradcoeff.
        interpolation_type: Interpolation method: nearest | trilinear | cubic\
            (default is trilinear).
        nthreads: Number of threads to run.
        checkopts: Don't run anything, just check options and exit.
        version: Print out version and exit.
        help_: Print out information on how to use this program.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_gradunwarp",
        "input_file": input_file,
        "save_transtbl_only": save_transtbl_only,
        "checkopts": checkopts,
        "version": version,
        "help": help_,
    }
    if gradient_coeff is not None:
        params["gradient_coeff"] = gradient_coeff
    if load_transtbl is not None:
        params["load_transtbl"] = load_transtbl
    if output_file is not None:
        params["output_file"] = output_file
    if out_transtbl is not None:
        params["out_transtbl"] = out_transtbl
    if interpolation_type is not None:
        params["interpolation_type"] = interpolation_type
    if nthreads is not None:
        params["nthreads"] = nthreads
    return params


def mri_gradunwarp_cargs(
    params: MriGradunwarpParameters,
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
    cargs.append("mri_gradunwarp")
    if params.get("gradient_coeff") is not None:
        cargs.extend([
            "--gradcoeff",
            execution.input_file(params.get("gradient_coeff"))
        ])
    if params.get("load_transtbl") is not None:
        cargs.extend([
            "--load_transtbl",
            execution.input_file(params.get("load_transtbl"))
        ])
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("output_file") is not None:
        cargs.extend([
            "--o",
            params.get("output_file")
        ])
    if params.get("out_transtbl") is not None:
        cargs.extend([
            "--out_transtbl",
            params.get("out_transtbl")
        ])
    if params.get("save_transtbl_only"):
        cargs.append("--save_transtbl_only")
    if params.get("interpolation_type") is not None:
        cargs.extend([
            "--interp",
            params.get("interpolation_type")
        ])
    if params.get("nthreads") is not None:
        cargs.extend([
            "--nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mri_gradunwarp_outputs(
    params: MriGradunwarpParameters,
    execution: Execution,
) -> MriGradunwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGradunwarpOutputs(
        root=execution.output_file("."),
        unwarped_output=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
        output_transform_table=execution.output_file(params.get("out_transtbl")) if (params.get("out_transtbl") is not None) else None,
    )
    return ret


def mri_gradunwarp_execute(
    params: MriGradunwarpParameters,
    execution: Execution,
) -> MriGradunwarpOutputs:
    """
    Tool to correct gradient non-linearity distortions in MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGradunwarpOutputs`).
    """
    cargs = mri_gradunwarp_cargs(params, execution)
    ret = mri_gradunwarp_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_gradunwarp(
    input_file: InputPathType,
    gradient_coeff: InputPathType | None = None,
    load_transtbl: InputPathType | None = None,
    output_file: str | None = None,
    out_transtbl: str | None = None,
    save_transtbl_only: bool = False,
    interpolation_type: str | None = "trilinear",
    nthreads: float | None = None,
    checkopts: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriGradunwarpOutputs:
    """
    Tool to correct gradient non-linearity distortions in MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input warped volume or surface.
        gradient_coeff: Gradient coefficient input file (not to be used with\
            --load_transtbl).
        load_transtbl: Load unwarp transform table in m3z format (not to be\
            used with --gradcoeff).
        output_file: Output unwarped volume or surface.
        out_transtbl: Save unwarp transform table in m3z format.
        save_transtbl_only: Just save unwarp transform table in m3z format,\
            requires --gradcoeff.
        interpolation_type: Interpolation method: nearest | trilinear | cubic\
            (default is trilinear).
        nthreads: Number of threads to run.
        checkopts: Don't run anything, just check options and exit.
        version: Print out version and exit.
        help_: Print out information on how to use this program.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGradunwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GRADUNWARP_METADATA)
    params = mri_gradunwarp_params(gradient_coeff=gradient_coeff, load_transtbl=load_transtbl, input_file=input_file, output_file=output_file, out_transtbl=out_transtbl, save_transtbl_only=save_transtbl_only, interpolation_type=interpolation_type, nthreads=nthreads, checkopts=checkopts, version=version, help_=help_)
    return mri_gradunwarp_execute(params, execution)


__all__ = [
    "MRI_GRADUNWARP_METADATA",
    "MriGradunwarpOutputs",
    "MriGradunwarpParameters",
    "mri_gradunwarp",
    "mri_gradunwarp_params",
]

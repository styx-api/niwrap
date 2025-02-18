# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APPLYWARP_METADATA = Metadata(
    id="af3d683241808436d501919df0347e718d9aee29.boutiques",
    name="applywarp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
ApplywarpParameters = typing.TypedDict('ApplywarpParameters', {
    "__STYX_TYPE__": typing.Literal["applywarp"],
    "interp": typing.NotRequired[typing.Literal["nn", "trilinear", "sinc", "spline"] | None],
    "in_file": InputPathType,
    "ref_file": InputPathType,
    "out_file": typing.NotRequired[str | None],
    "relwarp": bool,
    "abswarp": bool,
    "datatype": typing.NotRequired[typing.Literal["char", "short", "int", "float", "double"] | None],
    "field_file": typing.NotRequired[InputPathType | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "output_type": typing.NotRequired[typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None],
    "postmat": typing.NotRequired[InputPathType | None],
    "premat": typing.NotRequired[InputPathType | None],
    "superlevel_2": typing.NotRequired[int | None],
    "supersample": bool,
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
        "applywarp": applywarp_cargs,
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
        "applywarp": applywarp_outputs,
    }.get(t)


class ApplywarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `applywarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file_outfile: OutputPathType | None
    """Warped output file."""


def applywarp_params(
    in_file: InputPathType,
    ref_file: InputPathType,
    interp: typing.Literal["nn", "trilinear", "sinc", "spline"] | None = None,
    out_file: str | None = None,
    relwarp: bool = False,
    abswarp: bool = False,
    datatype: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    field_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    postmat: InputPathType | None = None,
    premat: InputPathType | None = None,
    superlevel_2: int | None = None,
    supersample: bool = False,
) -> ApplywarpParameters:
    """
    Build parameters.
    
    Args:
        in_file: Image to be warped.
        ref_file: Reference image.
        interp: 'nn' or 'trilinear' or 'sinc' or 'spline'. Interpolation\
            method.
        out_file: Output filename.
        relwarp: Treat warp field as relative: x' = x + w(x).
        abswarp: Treat warp field as absolute: x' = w(x).
        datatype: 'char' or 'short' or 'int' or 'float' or 'double'. Force\
            output data type [char short int float double].
        field_file: File containing warp field.
        mask_file: Filename for mask image (in reference space).
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        postmat: Filename for post-transform (affine matrix).
        premat: Filename for pre-transform (affine matrix).
        superlevel_2: 'a' or an integer. Level of intermediary supersampling, a\
            for 'automatic' or integer level. default = 2.
        supersample: Intermediary supersampling of output, default is off.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "applywarp",
        "in_file": in_file,
        "ref_file": ref_file,
        "relwarp": relwarp,
        "abswarp": abswarp,
        "supersample": supersample,
    }
    if interp is not None:
        params["interp"] = interp
    if out_file is not None:
        params["out_file"] = out_file
    if datatype is not None:
        params["datatype"] = datatype
    if field_file is not None:
        params["field_file"] = field_file
    if mask_file is not None:
        params["mask_file"] = mask_file
    if output_type is not None:
        params["output_type"] = output_type
    if postmat is not None:
        params["postmat"] = postmat
    if premat is not None:
        params["premat"] = premat
    if superlevel_2 is not None:
        params["superlevel_2"] = superlevel_2
    return params


def applywarp_cargs(
    params: ApplywarpParameters,
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
    cargs.append("applywarp")
    if params.get("interp") is not None:
        cargs.append("--interp=" + params.get("interp"))
    cargs.append("--in=" + execution.input_file(params.get("in_file")))
    cargs.append("--ref=" + execution.input_file(params.get("ref_file")))
    if params.get("out_file") is not None:
        cargs.append("--out=" + params.get("out_file"))
    if params.get("relwarp"):
        cargs.append("--rel")
    if params.get("abswarp"):
        cargs.append("--abs")
    if params.get("datatype") is not None:
        cargs.append("--datatype=" + params.get("datatype"))
    if params.get("field_file") is not None:
        cargs.append("--warp=" + execution.input_file(params.get("field_file")))
    if params.get("mask_file") is not None:
        cargs.append("--mask=" + execution.input_file(params.get("mask_file")))
    if params.get("output_type") is not None:
        cargs.append(params.get("output_type"))
    if params.get("postmat") is not None:
        cargs.append("--postmat=" + execution.input_file(params.get("postmat")))
    if params.get("premat") is not None:
        cargs.append("--premat=" + execution.input_file(params.get("premat")))
    if params.get("superlevel_2") is not None:
        cargs.append("--superlevel=" + str(params.get("superlevel_2")))
    if params.get("supersample"):
        cargs.append("--super")
    return cargs


def applywarp_outputs(
    params: ApplywarpParameters,
    execution: Execution,
) -> ApplywarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ApplywarpOutputs(
        root=execution.output_file("."),
        out_file_outfile=execution.output_file(params.get("out_file")) if (params.get("out_file") is not None) else None,
    )
    return ret


def applywarp_execute(
    params: ApplywarpParameters,
    execution: Execution,
) -> ApplywarpOutputs:
    """
    Apply warps estimated by FNIRT (or some other software) to some image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ApplywarpOutputs`).
    """
    cargs = applywarp_cargs(params, execution)
    ret = applywarp_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def applywarp(
    in_file: InputPathType,
    ref_file: InputPathType,
    interp: typing.Literal["nn", "trilinear", "sinc", "spline"] | None = None,
    out_file: str | None = None,
    relwarp: bool = False,
    abswarp: bool = False,
    datatype: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    field_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    postmat: InputPathType | None = None,
    premat: InputPathType | None = None,
    superlevel_2: int | None = None,
    supersample: bool = False,
    runner: Runner | None = None,
) -> ApplywarpOutputs:
    """
    Apply warps estimated by FNIRT (or some other software) to some image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Image to be warped.
        ref_file: Reference image.
        interp: 'nn' or 'trilinear' or 'sinc' or 'spline'. Interpolation\
            method.
        out_file: Output filename.
        relwarp: Treat warp field as relative: x' = x + w(x).
        abswarp: Treat warp field as absolute: x' = w(x).
        datatype: 'char' or 'short' or 'int' or 'float' or 'double'. Force\
            output data type [char short int float double].
        field_file: File containing warp field.
        mask_file: Filename for mask image (in reference space).
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        postmat: Filename for post-transform (affine matrix).
        premat: Filename for pre-transform (affine matrix).
        superlevel_2: 'a' or an integer. Level of intermediary supersampling, a\
            for 'automatic' or integer level. default = 2.
        supersample: Intermediary supersampling of output, default is off.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApplywarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APPLYWARP_METADATA)
    params = applywarp_params(interp=interp, in_file=in_file, ref_file=ref_file, out_file=out_file, relwarp=relwarp, abswarp=abswarp, datatype=datatype, field_file=field_file, mask_file=mask_file, output_type=output_type, postmat=postmat, premat=premat, superlevel_2=superlevel_2, supersample=supersample)
    return applywarp_execute(params, execution)


__all__ = [
    "APPLYWARP_METADATA",
    "ApplywarpOutputs",
    "ApplywarpParameters",
    "applywarp",
    "applywarp_params",
]

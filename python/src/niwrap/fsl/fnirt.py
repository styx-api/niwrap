# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FNIRT_METADATA = Metadata(
    id="e595d42b3f6e67fad59b883d737a927f3f3b91ec.boutiques",
    name="fnirt",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FnirtParameters = typing.TypedDict('FnirtParameters', {
    "__STYX_TYPE__": typing.Literal["fnirt"],
    "affine_file": typing.NotRequired[InputPathType | None],
    "config_file": typing.NotRequired[typing.Literal["T1_2_MNI152_2mm", "FA_2_FMRIB58_1mm"] | None],
    "field_file": typing.NotRequired[InputPathType | None],
    "fieldcoeff_file": typing.NotRequired[InputPathType | None],
    "in_file": InputPathType,
    "jacobian_file": typing.NotRequired[InputPathType | None],
    "log_file": typing.NotRequired[InputPathType | None],
    "modulatedref_file": typing.NotRequired[str | None],
    "ref_file": InputPathType,
    "refmask_file": typing.NotRequired[InputPathType | None],
    "warped_file": typing.NotRequired[InputPathType | None],
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
        "fnirt": fnirt_cargs,
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
        "fnirt": fnirt_outputs,
    }.get(t)


class FnirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fnirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    field_file_outfile: OutputPathType | None
    """File with warp field."""
    fieldcoeff_file_outfile: OutputPathType | None
    """File with field coefficients."""
    jacobian_file_outfile: OutputPathType | None
    """File containing jacobian of the field."""
    log_file_outfile: OutputPathType | None
    """Name of log-file."""
    modulatedref_file_outfile: OutputPathType | None
    """File containing intensity modulated --ref."""
    warped_file_outfile: OutputPathType | None
    """Warped image."""


def fnirt_params(
    in_file: InputPathType,
    ref_file: InputPathType,
    affine_file: InputPathType | None = None,
    config_file: typing.Literal["T1_2_MNI152_2mm", "FA_2_FMRIB58_1mm"] | None = None,
    field_file: InputPathType | None = None,
    fieldcoeff_file: InputPathType | None = None,
    jacobian_file: InputPathType | None = None,
    log_file: InputPathType | None = None,
    modulatedref_file: str | None = None,
    refmask_file: InputPathType | None = None,
    warped_file: InputPathType | None = None,
) -> FnirtParameters:
    """
    Build parameters.
    
    Args:
        in_file: Name of input image.
        ref_file: Name of reference image.
        affine_file: Name of file containing affine transform.
        config_file: 't1_2_mni152_2mm' or 'fa_2_fmrib58_1mm' or file or string.\
            Name of config file specifying command line arguments.
        field_file: file. Name of output file with field.
        fieldcoeff_file: string representing a file. Name of output file with\
            field coefficients.
        jacobian_file: A file. Name of file for writing out the jacobian of the\
            field (for diagnostic or vbm purposes).
        log_file: Name of log-file.
        modulatedref_file: string representing a file. Name of file for writing\
            out intensity modulated --ref (for diagnostic purposes).
        refmask_file: Name of file with mask in reference space.
        warped_file: Name of output-file containing the --in image after it has\
            been warped to the --ref image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fnirt",
        "in_file": in_file,
        "ref_file": ref_file,
    }
    if affine_file is not None:
        params["affine_file"] = affine_file
    if config_file is not None:
        params["config_file"] = config_file
    if field_file is not None:
        params["field_file"] = field_file
    if fieldcoeff_file is not None:
        params["fieldcoeff_file"] = fieldcoeff_file
    if jacobian_file is not None:
        params["jacobian_file"] = jacobian_file
    if log_file is not None:
        params["log_file"] = log_file
    if modulatedref_file is not None:
        params["modulatedref_file"] = modulatedref_file
    if refmask_file is not None:
        params["refmask_file"] = refmask_file
    if warped_file is not None:
        params["warped_file"] = warped_file
    return params


def fnirt_cargs(
    params: FnirtParameters,
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
    cargs.append("fnirt")
    if params.get("affine_file") is not None:
        cargs.append("--aff=" + execution.input_file(params.get("affine_file")))
    if params.get("config_file") is not None:
        cargs.append("--config=" + params.get("config_file"))
    if params.get("field_file") is not None:
        cargs.append("--fout=" + execution.input_file(params.get("field_file")))
    if params.get("fieldcoeff_file") is not None:
        cargs.append("--cout=" + execution.input_file(params.get("fieldcoeff_file")))
    cargs.append("--in=" + execution.input_file(params.get("in_file")))
    if params.get("jacobian_file") is not None:
        cargs.append("--jout=" + execution.input_file(params.get("jacobian_file")))
    if params.get("log_file") is not None:
        cargs.append("--logout=" + execution.input_file(params.get("log_file")))
    if params.get("modulatedref_file") is not None:
        cargs.append("--refout=" + params.get("modulatedref_file"))
    cargs.append("--ref=" + execution.input_file(params.get("ref_file")))
    if params.get("refmask_file") is not None:
        cargs.append("--refmask=" + execution.input_file(params.get("refmask_file")))
    if params.get("warped_file") is not None:
        cargs.append("--iout=" + execution.input_file(params.get("warped_file")))
    return cargs


def fnirt_outputs(
    params: FnirtParameters,
    execution: Execution,
) -> FnirtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FnirtOutputs(
        root=execution.output_file("."),
        field_file_outfile=execution.output_file(pathlib.Path(params.get("field_file")).name + ".nii.gz") if (params.get("field_file") is not None) else None,
        fieldcoeff_file_outfile=execution.output_file(pathlib.Path(params.get("fieldcoeff_file")).name + ".nii.gz") if (params.get("fieldcoeff_file") is not None) else None,
        jacobian_file_outfile=execution.output_file(pathlib.Path(params.get("jacobian_file")).name + ".mat") if (params.get("jacobian_file") is not None) else None,
        log_file_outfile=execution.output_file(pathlib.Path(params.get("log_file")).name + ".txt") if (params.get("log_file") is not None) else None,
        modulatedref_file_outfile=execution.output_file(params.get("modulatedref_file") + ".nii.gz") if (params.get("modulatedref_file") is not None) else None,
        warped_file_outfile=execution.output_file(pathlib.Path(params.get("warped_file")).name + ".nii.gz") if (params.get("warped_file") is not None) else None,
    )
    return ret


def fnirt_execute(
    params: FnirtParameters,
    execution: Execution,
) -> FnirtOutputs:
    """
    FSL non-linear registration.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FnirtOutputs`).
    """
    cargs = fnirt_cargs(params, execution)
    ret = fnirt_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fnirt(
    in_file: InputPathType,
    ref_file: InputPathType,
    affine_file: InputPathType | None = None,
    config_file: typing.Literal["T1_2_MNI152_2mm", "FA_2_FMRIB58_1mm"] | None = None,
    field_file: InputPathType | None = None,
    fieldcoeff_file: InputPathType | None = None,
    jacobian_file: InputPathType | None = None,
    log_file: InputPathType | None = None,
    modulatedref_file: str | None = None,
    refmask_file: InputPathType | None = None,
    warped_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> FnirtOutputs:
    """
    FSL non-linear registration.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Name of input image.
        ref_file: Name of reference image.
        affine_file: Name of file containing affine transform.
        config_file: 't1_2_mni152_2mm' or 'fa_2_fmrib58_1mm' or file or string.\
            Name of config file specifying command line arguments.
        field_file: file. Name of output file with field.
        fieldcoeff_file: string representing a file. Name of output file with\
            field coefficients.
        jacobian_file: A file. Name of file for writing out the jacobian of the\
            field (for diagnostic or vbm purposes).
        log_file: Name of log-file.
        modulatedref_file: string representing a file. Name of file for writing\
            out intensity modulated --ref (for diagnostic purposes).
        refmask_file: Name of file with mask in reference space.
        warped_file: Name of output-file containing the --in image after it has\
            been warped to the --ref image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FnirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FNIRT_METADATA)
    params = fnirt_params(affine_file=affine_file, config_file=config_file, field_file=field_file, fieldcoeff_file=fieldcoeff_file, in_file=in_file, jacobian_file=jacobian_file, log_file=log_file, modulatedref_file=modulatedref_file, ref_file=ref_file, refmask_file=refmask_file, warped_file=warped_file)
    return fnirt_execute(params, execution)


__all__ = [
    "FNIRT_METADATA",
    "FnirtOutputs",
    "FnirtParameters",
    "fnirt",
    "fnirt_params",
]

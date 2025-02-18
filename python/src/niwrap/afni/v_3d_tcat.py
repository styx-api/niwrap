# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TCAT_METADATA = Metadata(
    id="857f0c4b1d6c6ff7212eb0f219b0756a253e1817.boutiques",
    name="3dTcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTcatParameters = typing.TypedDict('V3dTcatParameters', {
    "__STYX_TYPE__": typing.Literal["3dTcat"],
    "rlt": typing.NotRequired[typing.Literal["", "+", "++"] | None],
    "in_files": InputPathType,
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "verbose": bool,
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
        "3dTcat": v_3d_tcat_cargs,
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
        "3dTcat": v_3d_tcat_outputs,
    }.get(t)


class V3dTcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_tcat_params(
    in_files: InputPathType,
    rlt: typing.Literal["", "+", "++"] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    verbose: bool = False,
) -> V3dTcatParameters:
    """
    Build parameters.
    
    Args:
        in_files: Input file to 3dtcat.
        rlt: '' or '+' or '++'. Remove linear trends in each voxel time series\
            loaded from each input dataset, separately. option -rlt removes the\
            least squares fit of 'a+b*t' to each voxel time series. option -rlt+\
            adds dataset mean back in. option -rlt++ adds overall mean of all\
            dataset timeseries back in.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        verbose: Print out some verbose output as the program.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTcat",
        "in_files": in_files,
        "verbose": verbose,
    }
    if rlt is not None:
        params["rlt"] = rlt
    if outputtype is not None:
        params["outputtype"] = outputtype
    return params


def v_3d_tcat_cargs(
    params: V3dTcatParameters,
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
    cargs.append("3dTcat")
    if params.get("rlt") is not None:
        cargs.extend([
            "-rlt",
            params.get("rlt") + execution.input_file(params.get("in_files"))
        ])
    cargs.append("[OUT_FILE]")
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("verbose"):
        cargs.append("-verb")
    return cargs


def v_3d_tcat_outputs(
    params: V3dTcatParameters,
    execution: Execution,
) -> V3dTcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTcatOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("in_files")).name + "_tcat"),
        out_file_=execution.output_file("out_file"),
    )
    return ret


def v_3d_tcat_execute(
    params: V3dTcatParameters,
    execution: Execution,
) -> V3dTcatOutputs:
    """
    Concatenate sub-bricks from input datasets into one big 3D+time dataset.
    TODO Replace InputMultiPath in_files with Traits.List, if possible. Current
    version adds extra whitespace.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTcatOutputs`).
    """
    cargs = v_3d_tcat_cargs(params, execution)
    ret = v_3d_tcat_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v_3d_tcat(
    in_files: InputPathType,
    rlt: typing.Literal["", "+", "++"] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dTcatOutputs:
    """
    Concatenate sub-bricks from input datasets into one big 3D+time dataset.
    TODO Replace InputMultiPath in_files with Traits.List, if possible. Current
    version adds extra whitespace.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_files: Input file to 3dtcat.
        rlt: '' or '+' or '++'. Remove linear trends in each voxel time series\
            loaded from each input dataset, separately. option -rlt removes the\
            least squares fit of 'a+b*t' to each voxel time series. option -rlt+\
            adds dataset mean back in. option -rlt++ adds overall mean of all\
            dataset timeseries back in.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        verbose: Print out some verbose output as the program.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCAT_METADATA)
    params = v_3d_tcat_params(rlt=rlt, in_files=in_files, outputtype=outputtype, verbose=verbose)
    return v_3d_tcat_execute(params, execution)


__all__ = [
    "V3dTcatOutputs",
    "V3dTcatParameters",
    "V_3D_TCAT_METADATA",
    "v_3d_tcat",
    "v_3d_tcat_params",
]

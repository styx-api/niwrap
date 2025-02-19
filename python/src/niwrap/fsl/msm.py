# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MSM_METADATA = Metadata(
    id="36c2f1fd7109d0e69b48c213ae952c4422d9c88f.boutiques",
    name="msm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


MsmParameters = typing.TypedDict('MsmParameters', {
    "__STYX_TYPE__": typing.Literal["msm"],
    "inmesh": InputPathType,
    "out": str,
    "refmesh": typing.NotRequired[InputPathType | None],
    "indata": typing.NotRequired[InputPathType | None],
    "refdata": typing.NotRequired[InputPathType | None],
    "trans": typing.NotRequired[InputPathType | None],
    "in_register": typing.NotRequired[InputPathType | None],
    "inweight": typing.NotRequired[InputPathType | None],
    "refweight": typing.NotRequired[InputPathType | None],
    "format": typing.NotRequired[str | None],
    "conf": typing.NotRequired[InputPathType | None],
    "levels": typing.NotRequired[float | None],
    "smoothout": typing.NotRequired[float | None],
    "help": bool,
    "verbose": bool,
    "printoptions": bool,
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
        "msm": msm_cargs,
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
        "msm": msm_outputs,
    }.get(t)


class MsmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `msm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file from MSM"""


def msm_params(
    inmesh: InputPathType,
    out: str,
    refmesh: InputPathType | None = None,
    indata: InputPathType | None = None,
    refdata: InputPathType | None = None,
    trans: InputPathType | None = None,
    in_register: InputPathType | None = None,
    inweight: InputPathType | None = None,
    refweight: InputPathType | None = None,
    format_: str | None = None,
    conf: InputPathType | None = None,
    levels: float | None = None,
    smoothout: float | None = None,
    help_: bool = False,
    verbose: bool = False,
    printoptions: bool = False,
) -> MsmParameters:
    """
    Build parameters.
    
    Args:
        inmesh: Input mesh (available formats: VTK, ASCII, GIFTI). Needs to be\
            a sphere.
        out: Output basename.
        refmesh: Reference mesh (available formats: VTK, ASCII, GIFTI). Needs\
            to be a sphere. If not included algorithm assumes reference mesh is\
            equivalent input.
        indata: Scalar or multivariate data for input - can be ASCII\
            (.asc,.dpv,.txt) or GIFTI (.func.gii or .shape.gii).
        refdata: Scalar or multivariate data for reference - can be ASCII\
            (.asc,.dpv,.txt) or GIFTI (.func.gii or .shape.gii).
        trans: Transformed source mesh (output of a previous registration). Use\
            this to initialise the current registration.
        in_register: Input mesh at data resolution. Used to resample data onto\
            input mesh if data is supplied at a different resolution. Note this\
            mesh HAS to be in alignment with either the input_mesh of (if supplied)\
            the transformed source mesh. Use with supreme caution.
        inweight: Cost function weighting for input - weights data in these\
            vertices when calculating similarity (ASCII or GIFTI). Can be\
            multivariate provided dimension equals that of data.
        refweight: Cost function weighting for reference - weights data in\
            these vertices when calculating similarity (ASCII or GIFTI). Can be\
            multivariate provided dimension equals that of data.
        format_: Format of output files, can be: GIFTI, VTK, ASCII or ASCII_MAT\
            (for full details of output file formats see MSM wiki).
        conf: Configuration file.
        levels: Number of resolution levels (default = number of resolution\
            levels specified by --opt in config file).
        smoothout: Smooth transformed output with this sigma (default=0).
        help_: Display help message.
        verbose: Switch on diagnostic messages.
        printoptions: Print configuration file options.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "msm",
        "inmesh": inmesh,
        "out": out,
        "help": help_,
        "verbose": verbose,
        "printoptions": printoptions,
    }
    if refmesh is not None:
        params["refmesh"] = refmesh
    if indata is not None:
        params["indata"] = indata
    if refdata is not None:
        params["refdata"] = refdata
    if trans is not None:
        params["trans"] = trans
    if in_register is not None:
        params["in_register"] = in_register
    if inweight is not None:
        params["inweight"] = inweight
    if refweight is not None:
        params["refweight"] = refweight
    if format_ is not None:
        params["format"] = format_
    if conf is not None:
        params["conf"] = conf
    if levels is not None:
        params["levels"] = levels
    if smoothout is not None:
        params["smoothout"] = smoothout
    return params


def msm_cargs(
    params: MsmParameters,
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
    cargs.append("msm")
    cargs.append(execution.input_file(params.get("inmesh")))
    cargs.extend([
        "-out",
        "-" + params.get("out")
    ])
    if params.get("refmesh") is not None:
        cargs.extend([
            "--refmesh",
            execution.input_file(params.get("refmesh"))
        ])
    if params.get("indata") is not None:
        cargs.extend([
            "--indata",
            execution.input_file(params.get("indata"))
        ])
    if params.get("refdata") is not None:
        cargs.extend([
            "--refdata",
            execution.input_file(params.get("refdata"))
        ])
    if params.get("trans") is not None:
        cargs.extend([
            "--trans",
            execution.input_file(params.get("trans"))
        ])
    if params.get("in_register") is not None:
        cargs.extend([
            "--in_register",
            execution.input_file(params.get("in_register"))
        ])
    if params.get("inweight") is not None:
        cargs.extend([
            "--inweight",
            execution.input_file(params.get("inweight"))
        ])
    if params.get("refweight") is not None:
        cargs.extend([
            "--refweight",
            execution.input_file(params.get("refweight"))
        ])
    if params.get("format") is not None:
        cargs.extend([
            "-f",
            params.get("format")
        ])
    if params.get("conf") is not None:
        cargs.extend([
            "--conf",
            execution.input_file(params.get("conf"))
        ])
    if params.get("levels") is not None:
        cargs.extend([
            "--levels",
            str(params.get("levels"))
        ])
    if params.get("smoothout") is not None:
        cargs.extend([
            "--smoothout",
            str(params.get("smoothout"))
        ])
    if params.get("help"):
        cargs.append("-h")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("printoptions"):
        cargs.append("-p")
    return cargs


def msm_outputs(
    params: MsmParameters,
    execution: Execution,
) -> MsmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MsmOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("out") + "_output.ext"),
    )
    return ret


def msm_execute(
    params: MsmParameters,
    execution: Execution,
) -> MsmOutputs:
    """
    MSM (Multimodal Surface Matching) is a tool for aligning brain surface scans
    based on their cortical folding patterns or functional/structural data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MsmOutputs`).
    """
    params = execution.params(params)
    cargs = msm_cargs(params, execution)
    ret = msm_outputs(params, execution)
    execution.run(cargs)
    return ret


def msm(
    inmesh: InputPathType,
    out: str,
    refmesh: InputPathType | None = None,
    indata: InputPathType | None = None,
    refdata: InputPathType | None = None,
    trans: InputPathType | None = None,
    in_register: InputPathType | None = None,
    inweight: InputPathType | None = None,
    refweight: InputPathType | None = None,
    format_: str | None = None,
    conf: InputPathType | None = None,
    levels: float | None = None,
    smoothout: float | None = None,
    help_: bool = False,
    verbose: bool = False,
    printoptions: bool = False,
    runner: Runner | None = None,
) -> MsmOutputs:
    """
    MSM (Multimodal Surface Matching) is a tool for aligning brain surface scans
    based on their cortical folding patterns or functional/structural data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        inmesh: Input mesh (available formats: VTK, ASCII, GIFTI). Needs to be\
            a sphere.
        out: Output basename.
        refmesh: Reference mesh (available formats: VTK, ASCII, GIFTI). Needs\
            to be a sphere. If not included algorithm assumes reference mesh is\
            equivalent input.
        indata: Scalar or multivariate data for input - can be ASCII\
            (.asc,.dpv,.txt) or GIFTI (.func.gii or .shape.gii).
        refdata: Scalar or multivariate data for reference - can be ASCII\
            (.asc,.dpv,.txt) or GIFTI (.func.gii or .shape.gii).
        trans: Transformed source mesh (output of a previous registration). Use\
            this to initialise the current registration.
        in_register: Input mesh at data resolution. Used to resample data onto\
            input mesh if data is supplied at a different resolution. Note this\
            mesh HAS to be in alignment with either the input_mesh of (if supplied)\
            the transformed source mesh. Use with supreme caution.
        inweight: Cost function weighting for input - weights data in these\
            vertices when calculating similarity (ASCII or GIFTI). Can be\
            multivariate provided dimension equals that of data.
        refweight: Cost function weighting for reference - weights data in\
            these vertices when calculating similarity (ASCII or GIFTI). Can be\
            multivariate provided dimension equals that of data.
        format_: Format of output files, can be: GIFTI, VTK, ASCII or ASCII_MAT\
            (for full details of output file formats see MSM wiki).
        conf: Configuration file.
        levels: Number of resolution levels (default = number of resolution\
            levels specified by --opt in config file).
        smoothout: Smooth transformed output with this sigma (default=0).
        help_: Display help message.
        verbose: Switch on diagnostic messages.
        printoptions: Print configuration file options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MsmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MSM_METADATA)
    params = msm_params(
        inmesh=inmesh,
        out=out,
        refmesh=refmesh,
        indata=indata,
        refdata=refdata,
        trans=trans,
        in_register=in_register,
        inweight=inweight,
        refweight=refweight,
        format_=format_,
        conf=conf,
        levels=levels,
        smoothout=smoothout,
        help_=help_,
        verbose=verbose,
        printoptions=printoptions,
    )
    return msm_execute(params, execution)


__all__ = [
    "MSM_METADATA",
    "MsmOutputs",
    "MsmParameters",
    "msm",
    "msm_params",
]

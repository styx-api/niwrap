# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIRST_METADATA = Metadata(
    id="c4a03ae0d22afadc00267f860cc2f855e085bed1.boutiques",
    name="first",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FirstParameters = typing.TypedDict('FirstParameters', {
    "__STYX_TYPE__": typing.Literal["first"],
    "input_file": InputPathType,
    "output_name": str,
    "input_model": InputPathType,
    "flirt_matrix": InputPathType,
    "verbose": bool,
    "help": bool,
    "input_model2": typing.NotRequired[InputPathType | None],
    "nmodes": typing.NotRequired[float | None],
    "intref": bool,
    "multi_image_input": bool,
    "binary_surface_output": bool,
    "bmap_name": typing.NotRequired[InputPathType | None],
    "bvars": typing.NotRequired[InputPathType | None],
    "shcond": bool,
    "loadbvars": bool,
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
        "first": first_cargs,
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
        "first": first_outputs,
    }.get(t)


class FirstOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_output_image: OutputPathType
    """Segmented output image"""


def first_params(
    input_file: InputPathType,
    output_name: str,
    input_model: InputPathType,
    flirt_matrix: InputPathType,
    verbose: bool = False,
    help_: bool = False,
    input_model2: InputPathType | None = None,
    nmodes: float | None = None,
    intref: bool = False,
    multi_image_input: bool = False,
    binary_surface_output: bool = False,
    bmap_name: InputPathType | None = None,
    bvars: InputPathType | None = None,
    shcond: bool = False,
    loadbvars: bool = False,
) -> FirstParameters:
    """
    Build parameters.
    
    Args:
        input_file: Filename of input image to be segmented.
        output_name: Output name.
        input_model: Filename of input model (the structure to be segmented).
        flirt_matrix: Filename of flirt matrix that transform input image to\
            MNI space (output of first_flirt).
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        input_model2: Filename of second input model (the structure to be\
            segmented).
        nmodes: Specifies number of modes used.
        intref: Use structure specified by modelname2 as intensity reference.
        multi_image_input: Use structure specified by modelname2 as intensity\
            reference.
        binary_surface_output: Use structure specified by modelname2 as\
            intensity reference.
        bmap_name: Filename of conditional mapping matrix.
        bvars: Initialize using bvars from a previous segmentation. When using\
            with --shcond specifies the shape of the structure we are conditioning\
            on.
        shcond: Use conditional shape probability.
        loadbvars: Load initial parameter estimates from a previous\
            segmentation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "first",
        "input_file": input_file,
        "output_name": output_name,
        "input_model": input_model,
        "flirt_matrix": flirt_matrix,
        "verbose": verbose,
        "help": help_,
        "intref": intref,
        "multi_image_input": multi_image_input,
        "binary_surface_output": binary_surface_output,
        "shcond": shcond,
        "loadbvars": loadbvars,
    }
    if input_model2 is not None:
        params["input_model2"] = input_model2
    if nmodes is not None:
        params["nmodes"] = nmodes
    if bmap_name is not None:
        params["bmap_name"] = bmap_name
    if bvars is not None:
        params["bvars"] = bvars
    return params


def first_cargs(
    params: FirstParameters,
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
    cargs.append("first")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-k",
        params.get("output_name")
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("input_model"))
    ])
    cargs.extend([
        "-l",
        execution.input_file(params.get("flirt_matrix"))
    ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("help"):
        cargs.append("-h")
    if params.get("input_model2") is not None:
        cargs.extend([
            "-p",
            execution.input_file(params.get("input_model2"))
        ])
    if params.get("nmodes") is not None:
        cargs.extend([
            "-n",
            str(params.get("nmodes"))
        ])
    if params.get("intref"):
        cargs.append("--intref")
    if params.get("multi_image_input"):
        cargs.append("--multiImageInput")
    if params.get("binary_surface_output"):
        cargs.append("--binarySurfaceOutput")
    if params.get("bmap_name") is not None:
        cargs.extend([
            "-b",
            execution.input_file(params.get("bmap_name"))
        ])
    if params.get("bvars") is not None:
        cargs.extend([
            "-o",
            execution.input_file(params.get("bvars"))
        ])
    if params.get("shcond"):
        cargs.append("--shcond")
    if params.get("loadbvars"):
        cargs.append("--loadbvars")
    return cargs


def first_outputs(
    params: FirstParameters,
    execution: Execution,
) -> FirstOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FirstOutputs(
        root=execution.output_file("."),
        segmented_output_image=execution.output_file(params.get("output_name") + "_seg.nii.gz"),
    )
    return ret


def first_execute(
    params: FirstParameters,
    execution: Execution,
) -> FirstOutputs:
    """
    A command-line tool for segmenting subcortical structures in MRI images using
    models and transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FirstOutputs`).
    """
    cargs = first_cargs(params, execution)
    ret = first_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def first(
    input_file: InputPathType,
    output_name: str,
    input_model: InputPathType,
    flirt_matrix: InputPathType,
    verbose: bool = False,
    help_: bool = False,
    input_model2: InputPathType | None = None,
    nmodes: float | None = None,
    intref: bool = False,
    multi_image_input: bool = False,
    binary_surface_output: bool = False,
    bmap_name: InputPathType | None = None,
    bvars: InputPathType | None = None,
    shcond: bool = False,
    loadbvars: bool = False,
    runner: Runner | None = None,
) -> FirstOutputs:
    """
    A command-line tool for segmenting subcortical structures in MRI images using
    models and transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Filename of input image to be segmented.
        output_name: Output name.
        input_model: Filename of input model (the structure to be segmented).
        flirt_matrix: Filename of flirt matrix that transform input image to\
            MNI space (output of first_flirt).
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        input_model2: Filename of second input model (the structure to be\
            segmented).
        nmodes: Specifies number of modes used.
        intref: Use structure specified by modelname2 as intensity reference.
        multi_image_input: Use structure specified by modelname2 as intensity\
            reference.
        binary_surface_output: Use structure specified by modelname2 as\
            intensity reference.
        bmap_name: Filename of conditional mapping matrix.
        bvars: Initialize using bvars from a previous segmentation. When using\
            with --shcond specifies the shape of the structure we are conditioning\
            on.
        shcond: Use conditional shape probability.
        loadbvars: Load initial parameter estimates from a previous\
            segmentation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_METADATA)
    params = first_params(input_file=input_file, output_name=output_name, input_model=input_model, flirt_matrix=flirt_matrix, verbose=verbose, help_=help_, input_model2=input_model2, nmodes=nmodes, intref=intref, multi_image_input=multi_image_input, binary_surface_output=binary_surface_output, bmap_name=bmap_name, bvars=bvars, shcond=shcond, loadbvars=loadbvars)
    return first_execute(params, execution)


__all__ = [
    "FIRST_METADATA",
    "FirstOutputs",
    "FirstParameters",
    "first",
    "first_params",
]

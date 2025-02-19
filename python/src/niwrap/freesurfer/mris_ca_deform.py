# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_CA_DEFORM_METADATA = Metadata(
    id="7a76a6060e94710386328206ab18f500335fc348.boutiques",
    name="mris_ca_deform",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisCaDeformParameters = typing.TypedDict('MrisCaDeformParameters', {
    "__STYX_TYPE__": typing.Literal["mris_ca_deform"],
    "input_surface": InputPathType,
    "label_vol": InputPathType,
    "transform": InputPathType,
    "intensity_vol": InputPathType,
    "output_surface": str,
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
        "mris_ca_deform": mris_ca_deform_cargs,
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
        "mris_ca_deform": mris_ca_deform_outputs,
    }.get(t)


class MrisCaDeformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_ca_deform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    deformed_surface: OutputPathType
    """The result of the deformation process, output surface file."""


def mris_ca_deform_params(
    input_surface: InputPathType,
    label_vol: InputPathType,
    transform: InputPathType,
    intensity_vol: InputPathType,
    output_surface: str,
) -> MrisCaDeformParameters:
    """
    Build parameters.
    
    Args:
        input_surface: The input surface file to be deformed.
        label_vol: The input volumetric label map.
        transform: The transform file, typically a matrix that aligns the\
            volumes.
        intensity_vol: The intensity volume that is used in the deformation\
            process.
        output_surface: The file name for the output, deformed surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_ca_deform",
        "input_surface": input_surface,
        "label_vol": label_vol,
        "transform": transform,
        "intensity_vol": intensity_vol,
        "output_surface": output_surface,
    }
    return params


def mris_ca_deform_cargs(
    params: MrisCaDeformParameters,
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
    cargs.append("mris_ca_deform")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("label_vol")))
    cargs.append(execution.input_file(params.get("transform")))
    cargs.append(execution.input_file(params.get("intensity_vol")))
    cargs.append(params.get("output_surface"))
    return cargs


def mris_ca_deform_outputs(
    params: MrisCaDeformParameters,
    execution: Execution,
) -> MrisCaDeformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisCaDeformOutputs(
        root=execution.output_file("."),
        deformed_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_ca_deform_execute(
    params: MrisCaDeformParameters,
    execution: Execution,
) -> MrisCaDeformOutputs:
    """
    Deforms a surface to match it to a volumetric map of cortical labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisCaDeformOutputs`).
    """
    params = execution.params(params)
    cargs = mris_ca_deform_cargs(params, execution)
    ret = mris_ca_deform_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_ca_deform(
    input_surface: InputPathType,
    label_vol: InputPathType,
    transform: InputPathType,
    intensity_vol: InputPathType,
    output_surface: str,
    runner: Runner | None = None,
) -> MrisCaDeformOutputs:
    """
    Deforms a surface to match it to a volumetric map of cortical labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: The input surface file to be deformed.
        label_vol: The input volumetric label map.
        transform: The transform file, typically a matrix that aligns the\
            volumes.
        intensity_vol: The intensity volume that is used in the deformation\
            process.
        output_surface: The file name for the output, deformed surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCaDeformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CA_DEFORM_METADATA)
    params = mris_ca_deform_params(
        input_surface=input_surface,
        label_vol=label_vol,
        transform=transform,
        intensity_vol=intensity_vol,
        output_surface=output_surface,
    )
    return mris_ca_deform_execute(params, execution)


__all__ = [
    "MRIS_CA_DEFORM_METADATA",
    "MrisCaDeformOutputs",
    "MrisCaDeformParameters",
    "mris_ca_deform",
    "mris_ca_deform_params",
]

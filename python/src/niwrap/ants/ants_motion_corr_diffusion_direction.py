# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_MOTION_CORR_DIFFUSION_DIRECTION_METADATA = Metadata(
    id="3f81491f1faf2e11f2fe0e69121f28544825a2d4.boutiques",
    name="antsMotionCorrDiffusionDirection",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsMotionCorrDiffusionDirectionParameters = typing.TypedDict('AntsMotionCorrDiffusionDirectionParameters', {
    "__STYX_TYPE__": typing.Literal["antsMotionCorrDiffusionDirection"],
    "scheme": InputPathType,
    "bvec": InputPathType,
    "physical": InputPathType,
    "moco": InputPathType,
    "output": str,
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
        "antsMotionCorrDiffusionDirection": ants_motion_corr_diffusion_direction_cargs,
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
        "antsMotionCorrDiffusionDirection": ants_motion_corr_diffusion_direction_outputs,
    }.get(t)


class AntsMotionCorrDiffusionDirectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_motion_corr_diffusion_direction(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_scheme: OutputPathType
    """The output file for corrected diffusion directions."""


def ants_motion_corr_diffusion_direction_params(
    scheme: InputPathType,
    bvec: InputPathType,
    physical: InputPathType,
    moco: InputPathType,
    output: str,
) -> AntsMotionCorrDiffusionDirectionParameters:
    """
    Build parameters.
    
    Args:
        scheme: Camino scheme file specify acquisition parameters.
        bvec: bvec image specifying diffusion directions.
        physical: 3D image in dwi space.
        moco: Motion correction parameters from antsMotionCorr.
        output: Specify the output file for corrected directions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsMotionCorrDiffusionDirection",
        "scheme": scheme,
        "bvec": bvec,
        "physical": physical,
        "moco": moco,
        "output": output,
    }
    return params


def ants_motion_corr_diffusion_direction_cargs(
    params: AntsMotionCorrDiffusionDirectionParameters,
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
    cargs.append("antsMotionCorrDiffusionDirection")
    cargs.extend([
        "-s",
        execution.input_file(params.get("scheme"))
    ])
    cargs.extend([
        "-b",
        execution.input_file(params.get("bvec"))
    ])
    cargs.extend([
        "-p",
        execution.input_file(params.get("physical"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("moco"))
    ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    return cargs


def ants_motion_corr_diffusion_direction_outputs(
    params: AntsMotionCorrDiffusionDirectionParameters,
    execution: Execution,
) -> AntsMotionCorrDiffusionDirectionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsMotionCorrDiffusionDirectionOutputs(
        root=execution.output_file("."),
        corrected_scheme=execution.output_file(params.get("output")),
    )
    return ret


def ants_motion_corr_diffusion_direction_execute(
    params: AntsMotionCorrDiffusionDirectionParameters,
    execution: Execution,
) -> AntsMotionCorrDiffusionDirectionOutputs:
    """
    This tool adjusts the diffusion scheme for motion correction.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrDiffusionDirectionOutputs`).
    """
    cargs = ants_motion_corr_diffusion_direction_cargs(params, execution)
    ret = ants_motion_corr_diffusion_direction_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_motion_corr_diffusion_direction(
    scheme: InputPathType,
    bvec: InputPathType,
    physical: InputPathType,
    moco: InputPathType,
    output: str,
    runner: Runner | None = None,
) -> AntsMotionCorrDiffusionDirectionOutputs:
    """
    This tool adjusts the diffusion scheme for motion correction.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        scheme: Camino scheme file specify acquisition parameters.
        bvec: bvec image specifying diffusion directions.
        physical: 3D image in dwi space.
        moco: Motion correction parameters from antsMotionCorr.
        output: Specify the output file for corrected directions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrDiffusionDirectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_MOTION_CORR_DIFFUSION_DIRECTION_METADATA)
    params = ants_motion_corr_diffusion_direction_params(scheme=scheme, bvec=bvec, physical=physical, moco=moco, output=output)
    return ants_motion_corr_diffusion_direction_execute(params, execution)


__all__ = [
    "ANTS_MOTION_CORR_DIFFUSION_DIRECTION_METADATA",
    "AntsMotionCorrDiffusionDirectionOutputs",
    "AntsMotionCorrDiffusionDirectionParameters",
    "ants_motion_corr_diffusion_direction",
    "ants_motion_corr_diffusion_direction_params",
]

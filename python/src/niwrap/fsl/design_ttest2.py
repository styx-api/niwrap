# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DESIGN_TTEST2_METADATA = Metadata(
    id="4f98cff1704b6243d344d536faebad9ca961f2af.boutiques",
    name="design_ttest2",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


DesignTtest2Parameters = typing.TypedDict('DesignTtest2Parameters', {
    "__STYX_TYPE__": typing.Literal["design_ttest2"],
    "design_files_rootname": str,
    "ngroupa": float,
    "ngroupb": float,
    "include_mean_contrasts": bool,
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
        "design_ttest2": design_ttest2_cargs,
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
    }.get(t)


class DesignTtest2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `design_ttest2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def design_ttest2_params(
    design_files_rootname: str,
    ngroupa: float,
    ngroupb: float,
    include_mean_contrasts: bool = False,
) -> DesignTtest2Parameters:
    """
    Build parameters.
    
    Args:
        design_files_rootname: Root name for design files.
        ngroupa: Number of subjects in group A.
        ngroupb: Number of subjects in group B.
        include_mean_contrasts: Include individual group mean contrasts.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "design_ttest2",
        "design_files_rootname": design_files_rootname,
        "ngroupa": ngroupa,
        "ngroupb": ngroupb,
        "include_mean_contrasts": include_mean_contrasts,
    }
    return params


def design_ttest2_cargs(
    params: DesignTtest2Parameters,
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
    cargs.append("design_ttest2")
    cargs.append(params.get("design_files_rootname"))
    cargs.append(str(params.get("ngroupa")))
    cargs.append(str(params.get("ngroupb")))
    if params.get("include_mean_contrasts"):
        cargs.append("-m")
    return cargs


def design_ttest2_outputs(
    params: DesignTtest2Parameters,
    execution: Execution,
) -> DesignTtest2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DesignTtest2Outputs(
        root=execution.output_file("."),
    )
    return ret


def design_ttest2_execute(
    params: DesignTtest2Parameters,
    execution: Execution,
) -> DesignTtest2Outputs:
    """
    Command for generating group mean contrasts for a two-sample t-test design.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DesignTtest2Outputs`).
    """
    params = execution.params(params)
    cargs = design_ttest2_cargs(params, execution)
    ret = design_ttest2_outputs(params, execution)
    execution.run(cargs)
    return ret


def design_ttest2(
    design_files_rootname: str,
    ngroupa: float,
    ngroupb: float,
    include_mean_contrasts: bool = False,
    runner: Runner | None = None,
) -> DesignTtest2Outputs:
    """
    Command for generating group mean contrasts for a two-sample t-test design.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        design_files_rootname: Root name for design files.
        ngroupa: Number of subjects in group A.
        ngroupb: Number of subjects in group B.
        include_mean_contrasts: Include individual group mean contrasts.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DesignTtest2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DESIGN_TTEST2_METADATA)
    params = design_ttest2_params(
        design_files_rootname=design_files_rootname,
        ngroupa=ngroupa,
        ngroupb=ngroupb,
        include_mean_contrasts=include_mean_contrasts,
    )
    return design_ttest2_execute(params, execution)


__all__ = [
    "DESIGN_TTEST2_METADATA",
    "DesignTtest2Outputs",
    "DesignTtest2Parameters",
    "design_ttest2",
    "design_ttest2_params",
]

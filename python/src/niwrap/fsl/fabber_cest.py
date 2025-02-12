# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FABBER_CEST_METADATA = Metadata(
    id="02b8cdea1646edd376c3e6590fd5b1de7b4522ff.boutiques",
    name="fabber_cest",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FabberCestParameters = typing.TypedDict('FabberCestParameters', {
    "__STYX_TYPE__": typing.Literal["fabber_cest"],
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
        "fabber_cest": fabber_cest_cargs,
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
        "fabber_cest": fabber_cest_outputs,
    }.get(t)


class FabberCestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_cest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    logfile: OutputPathType
    """Log file"""
    modelfit_out: OutputPathType
    """Model fit output as a 4d volume"""
    residuals_out: OutputPathType
    """Residuals output as a 4d volume"""
    modelextras_out: OutputPathType
    """Model extras output"""
    mvn_out: OutputPathType
    """Final MVN distributions output"""
    mean_out: OutputPathType
    """Parameter means output"""
    std_out: OutputPathType
    """Parameter standard deviations output"""
    var_out: OutputPathType
    """Parameter variances output"""
    zstat_out: OutputPathType
    """Parameter Z statistics output"""
    noise_mean_out: OutputPathType
    """Noise means output"""
    noise_std_out: OutputPathType
    """Noise standard deviations output"""
    free_energy_out: OutputPathType
    """Free energy output"""


def fabber_cest_params(
) -> FabberCestParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fabber_cest",
    }
    return params


def fabber_cest_cargs(
    params: FabberCestParameters,
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
    cargs.append("fabber_cest")
    cargs.append("[--<option>")
    cargs.append("|")
    cargs.append("--<option>=<value>")
    cargs.append("...]")
    return cargs


def fabber_cest_outputs(
    params: FabberCestParameters,
    execution: Execution,
) -> FabberCestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FabberCestOutputs(
        root=execution.output_file("."),
        logfile=execution.output_file("[OUTPUT]/logfile.log"),
        modelfit_out=execution.output_file("[OUTPUT]/model_fit.nii.gz"),
        residuals_out=execution.output_file("[OUTPUT]/residuals.nii.gz"),
        modelextras_out=execution.output_file("[OUTPUT]/model_extras.nii.gz"),
        mvn_out=execution.output_file("[OUTPUT]/mvn.nii.gz"),
        mean_out=execution.output_file("[OUTPUT]/mean.nii.gz"),
        std_out=execution.output_file("[OUTPUT]/std.nii.gz"),
        var_out=execution.output_file("[OUTPUT]/var.nii.gz"),
        zstat_out=execution.output_file("[OUTPUT]/zstat.nii.gz"),
        noise_mean_out=execution.output_file("[OUTPUT]/noise_mean.nii.gz"),
        noise_std_out=execution.output_file("[OUTPUT]/noise_std.nii.gz"),
        free_energy_out=execution.output_file("[OUTPUT]/free_energy.nii.gz"),
    )
    return ret


def fabber_cest_execute(
    params: FabberCestParameters,
    execution: Execution,
) -> FabberCestOutputs:
    """
    Fabber Model-based Analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FabberCestOutputs`).
    """
    cargs = fabber_cest_cargs(params, execution)
    ret = fabber_cest_outputs(params, execution)
    execution.run(cargs)
    return ret


def fabber_cest(
    runner: Runner | None = None,
) -> FabberCestOutputs:
    """
    Fabber Model-based Analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberCestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_CEST_METADATA)
    params = fabber_cest_params()
    return fabber_cest_execute(params, execution)


__all__ = [
    "FABBER_CEST_METADATA",
    "FabberCestOutputs",
    "FabberCestParameters",
    "fabber_cest",
    "fabber_cest_params",
]

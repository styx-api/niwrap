# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_ENTS_METADATA = Metadata(
    id="f66a5a56bce20baecbbcffc7deaf985412131450.boutiques",
    name="fsl_ents",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslEntsParameters = typing.TypedDict('FslEntsParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_ents"],
    "icadir": str,
    "components": list[str],
    "outfile": typing.NotRequired[InputPathType | None],
    "overwrite": bool,
    "conffile": typing.NotRequired[list[InputPathType] | None],
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
        "fsl_ents": fsl_ents_cargs,
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
        "fsl_ents": fsl_ents_outputs,
    }.get(t)


class FslEntsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_ents(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_time_series: OutputPathType | None
    """File to save time series to"""


def fsl_ents_params(
    icadir: str,
    components: list[str],
    outfile: InputPathType | None = None,
    overwrite: bool = False,
    conffile: list[InputPathType] | None = None,
) -> FslEntsParameters:
    """
    Build parameters.
    
    Args:
        icadir: .ica directory to extract time series from.
        components: Component number or FIX/AROMA file specifying components to\
            extract.
        outfile: File to save time series to.
        overwrite: Overwrite output file if it exists.
        conffile: Extra files to append to output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_ents",
        "icadir": icadir,
        "components": components,
        "overwrite": overwrite,
    }
    if outfile is not None:
        params["outfile"] = outfile
    if conffile is not None:
        params["conffile"] = conffile
    return params


def fsl_ents_cargs(
    params: FslEntsParameters,
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
    cargs.append("fsl_ents")
    cargs.append(params.get("icadir"))
    cargs.extend(params.get("components"))
    if params.get("outfile") is not None:
        cargs.extend([
            "-o",
            execution.input_file(params.get("outfile"))
        ])
    if params.get("overwrite"):
        cargs.append("-ow")
    if params.get("conffile") is not None:
        cargs.extend([
            "-c",
            *[execution.input_file(f) for f in params.get("conffile")]
        ])
    cargs.append("[-h]")
    return cargs


def fsl_ents_outputs(
    params: FslEntsParameters,
    execution: Execution,
) -> FslEntsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslEntsOutputs(
        root=execution.output_file("."),
        out_time_series=execution.output_file(pathlib.Path(params.get("outfile")).name) if (params.get("outfile") is not None) else None,
    )
    return ret


def fsl_ents_execute(
    params: FslEntsParameters,
    execution: Execution,
) -> FslEntsOutputs:
    """
    Extract component time series from a MELODIC .ica directory.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslEntsOutputs`).
    """
    cargs = fsl_ents_cargs(params, execution)
    ret = fsl_ents_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fsl_ents(
    icadir: str,
    components: list[str],
    outfile: InputPathType | None = None,
    overwrite: bool = False,
    conffile: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> FslEntsOutputs:
    """
    Extract component time series from a MELODIC .ica directory.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        icadir: .ica directory to extract time series from.
        components: Component number or FIX/AROMA file specifying components to\
            extract.
        outfile: File to save time series to.
        overwrite: Overwrite output file if it exists.
        conffile: Extra files to append to output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslEntsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_ENTS_METADATA)
    params = fsl_ents_params(icadir=icadir, components=components, outfile=outfile, overwrite=overwrite, conffile=conffile)
    return fsl_ents_execute(params, execution)


__all__ = [
    "FSL_ENTS_METADATA",
    "FslEntsOutputs",
    "FslEntsParameters",
    "fsl_ents",
    "fsl_ents_params",
]

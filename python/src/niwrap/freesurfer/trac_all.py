# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TRAC_ALL_METADATA = Metadata(
    id="73a5f89795c73c559ddd404cdcdd1e92ea957a5a.boutiques",
    name="trac-all",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TracAllParameters = typing.TypedDict('TracAllParameters', {
    "__STYX_TYPE__": typing.Literal["trac-all"],
    "config_file": typing.NotRequired[InputPathType | None],
    "subject_name": typing.NotRequired[str | None],
    "dicom_file": typing.NotRequired[InputPathType | None],
    "assemble_measures": bool,
    "no_pathway_priors": bool,
    "help": bool,
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
        "trac-all": trac_all_cargs,
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
        "trac-all": trac_all_outputs,
    }.get(t)


class TracAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `trac_all(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    default_log: OutputPathType
    """Default log file"""
    default_cmd: OutputPathType
    """Default command file"""


def trac_all_params(
    config_file: InputPathType | None = None,
    subject_name: str | None = None,
    dicom_file: InputPathType | None = None,
    assemble_measures: bool = False,
    no_pathway_priors: bool = False,
    help_: bool = False,
) -> TracAllParameters:
    """
    Build parameters.
    
    Args:
        config_file: Configuration file to set analysis options (dmrirc file).
        subject_name: Subject name (if not defined in dmrirc).
        dicom_file: Input DWI DICOM (if not defined in dmrirc).
        assemble_measures: Assemble pathway measures from multiple subjects\
            (step 4).
        no_pathway_priors: Skip pathway priors (step 1.6).
        help_: Print full contents of help.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "trac-all",
        "assemble_measures": assemble_measures,
        "no_pathway_priors": no_pathway_priors,
        "help": help_,
    }
    if config_file is not None:
        params["config_file"] = config_file
    if subject_name is not None:
        params["subject_name"] = subject_name
    if dicom_file is not None:
        params["dicom_file"] = dicom_file
    return params


def trac_all_cargs(
    params: TracAllParameters,
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
    cargs.append("trac-all")
    if params.get("config_file") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("config_file"))
        ])
    if params.get("subject_name") is not None:
        cargs.extend([
            "-s",
            params.get("subject_name")
        ])
    if params.get("dicom_file") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("dicom_file"))
        ])
    if params.get("assemble_measures"):
        cargs.append("-stat")
    if params.get("no_pathway_priors"):
        cargs.append("-noprior")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def trac_all_outputs(
    params: TracAllParameters,
    execution: Execution,
) -> TracAllOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TracAllOutputs(
        root=execution.output_file("."),
        default_log=execution.output_file("scripts/trac-all.log"),
        default_cmd=execution.output_file("scripts/trac-all.cmd"),
    )
    return ret


def trac_all_execute(
    params: TracAllParameters,
    execution: Execution,
) -> TracAllOutputs:
    """
    Reconstruct white-matter pathways using an atlas of the underlying anatomy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TracAllOutputs`).
    """
    params = execution.params(params)
    cargs = trac_all_cargs(params, execution)
    ret = trac_all_outputs(params, execution)
    execution.run(cargs)
    return ret


def trac_all(
    config_file: InputPathType | None = None,
    subject_name: str | None = None,
    dicom_file: InputPathType | None = None,
    assemble_measures: bool = False,
    no_pathway_priors: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> TracAllOutputs:
    """
    Reconstruct white-matter pathways using an atlas of the underlying anatomy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        config_file: Configuration file to set analysis options (dmrirc file).
        subject_name: Subject name (if not defined in dmrirc).
        dicom_file: Input DWI DICOM (if not defined in dmrirc).
        assemble_measures: Assemble pathway measures from multiple subjects\
            (step 4).
        no_pathway_priors: Skip pathway priors (step 1.6).
        help_: Print full contents of help.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TracAllOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRAC_ALL_METADATA)
    params = trac_all_params(
        config_file=config_file,
        subject_name=subject_name,
        dicom_file=dicom_file,
        assemble_measures=assemble_measures,
        no_pathway_priors=no_pathway_priors,
        help_=help_,
    )
    return trac_all_execute(params, execution)


__all__ = [
    "TRAC_ALL_METADATA",
    "TracAllOutputs",
    "TracAllParameters",
    "trac_all",
    "trac_all_params",
]

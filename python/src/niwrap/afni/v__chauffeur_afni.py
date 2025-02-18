# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CHAUFFEUR_AFNI_METADATA = Metadata(
    id="7bd1968eb762331f9eaee48a7484852a7e447634.boutiques",
    name="@chauffeur_afni",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VChauffeurAfniParameters = typing.TypedDict('VChauffeurAfniParameters', {
    "__STYX_TYPE__": typing.Literal["@chauffeur_afni"],
    "ulay": InputPathType,
    "olay": typing.NotRequired[InputPathType | None],
    "prefix": str,
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
        "@chauffeur_afni": v__chauffeur_afni_cargs,
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
        "@chauffeur_afni": v__chauffeur_afni_outputs,
    }.get(t)


class VChauffeurAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__chauffeur_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Generated montage image"""
    cluster_report: OutputPathType
    """Clusterization report"""
    whereami_report: OutputPathType
    """Whereami report for clusterized data"""


def v__chauffeur_afni_params(
    ulay: InputPathType,
    prefix: str,
    olay: InputPathType | None = None,
) -> VChauffeurAfniParameters:
    """
    Build parameters.
    
    Args:
        ulay: Name of underlay dataset (required); can be 3D or 4D set.
        prefix: Prefix for output files (required).
        olay: Name of overlay dataset (optional).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@chauffeur_afni",
        "ulay": ulay,
        "prefix": prefix,
    }
    if olay is not None:
        params["olay"] = olay
    return params


def v__chauffeur_afni_cargs(
    params: VChauffeurAfniParameters,
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
    cargs.append("@chauffeur_afni")
    cargs.append(execution.input_file(params.get("ulay")))
    if params.get("olay") is not None:
        cargs.append(execution.input_file(params.get("olay")))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.append("[options]")
    return cargs


def v__chauffeur_afni_outputs(
    params: VChauffeurAfniParameters,
    execution: Execution,
) -> VChauffeurAfniOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VChauffeurAfniOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("prefix") + ".png"),
        cluster_report=execution.output_file(params.get("prefix") + "_clust_rep.txt"),
        whereami_report=execution.output_file(params.get("prefix") + "_clust_whereami.txt"),
    )
    return ret


def v__chauffeur_afni_execute(
    params: VChauffeurAfniParameters,
    execution: Execution,
) -> VChauffeurAfniOutputs:
    """
    Automated QC snapshots generator in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VChauffeurAfniOutputs`).
    """
    cargs = v__chauffeur_afni_cargs(params, execution)
    ret = v__chauffeur_afni_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def v__chauffeur_afni(
    ulay: InputPathType,
    prefix: str,
    olay: InputPathType | None = None,
    runner: Runner | None = None,
) -> VChauffeurAfniOutputs:
    """
    Automated QC snapshots generator in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ulay: Name of underlay dataset (required); can be 3D or 4D set.
        prefix: Prefix for output files (required).
        olay: Name of overlay dataset (optional).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VChauffeurAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CHAUFFEUR_AFNI_METADATA)
    params = v__chauffeur_afni_params(ulay=ulay, olay=olay, prefix=prefix)
    return v__chauffeur_afni_execute(params, execution)


__all__ = [
    "VChauffeurAfniOutputs",
    "VChauffeurAfniParameters",
    "V__CHAUFFEUR_AFNI_METADATA",
    "v__chauffeur_afni",
    "v__chauffeur_afni_params",
]

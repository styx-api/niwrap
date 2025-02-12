# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

XHEMIREG_METADATA = Metadata(
    id="f01b4255c8c371fe9d8cf7dac45f58046ba01896.boutiques",
    name="xhemireg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
XhemiregParameters = typing.TypedDict('XhemiregParameters', {
    "__STYX_TYPE__": typing.Literal["xhemireg"],
    "subject": str,
    "output_dir": typing.NotRequired[str | None],
    "map_lh": bool,
    "map_rh": bool,
    "perform_reg": bool,
    "tal_compute": bool,
    "no_tal_compute": bool,
    "tal_estimate": bool,
    "no_tal_estimate": bool,
    "gcaprep": typing.NotRequired[str | None],
    "threads": typing.NotRequired[float | None],
    "version": bool,
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
        "xhemireg": xhemireg_cargs,
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


class XhemiregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xhemireg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def xhemireg_params(
    subject: str,
    output_dir: str | None = None,
    map_lh: bool = False,
    map_rh: bool = False,
    perform_reg: bool = False,
    tal_compute: bool = False,
    no_tal_compute: bool = False,
    tal_estimate: bool = False,
    no_tal_estimate: bool = False,
    gcaprep: str | None = None,
    threads: float | None = None,
    version: bool = False,
    help_: bool = False,
) -> XhemiregParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject ID for the hemisphere registration process.
        output_dir: Output directory for the hemisphere registration.
        map_lh: Map from left hemisphere to right hemisphere.
        map_rh: Map from right hemisphere to left hemisphere.
        perform_reg: Perform registration to create sphere.reg.
        tal_compute: Recompute Talairach registration.
        no_tal_compute: Do not perform Talairach registration.
        tal_estimate: Compute estimate of Talairach registration from unflipped\
            registration.
        no_tal_estimate: Do not perform estimation of Talairach registration.
        gcaprep: Prepare GCA for training symmetrical GCA atlases.
        threads: Number of threads used, applicable with --gcaprep option.
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "xhemireg",
        "subject": subject,
        "map_lh": map_lh,
        "map_rh": map_rh,
        "perform_reg": perform_reg,
        "tal_compute": tal_compute,
        "no_tal_compute": no_tal_compute,
        "tal_estimate": tal_estimate,
        "no_tal_estimate": no_tal_estimate,
        "version": version,
        "help": help_,
    }
    if output_dir is not None:
        params["output_dir"] = output_dir
    if gcaprep is not None:
        params["gcaprep"] = gcaprep
    if threads is not None:
        params["threads"] = threads
    return params


def xhemireg_cargs(
    params: XhemiregParameters,
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
    cargs.append("xhemireg")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("output_dir") is not None:
        cargs.extend([
            "--o",
            params.get("output_dir")
        ])
    if params.get("map_lh"):
        cargs.append("--lh")
    if params.get("map_rh"):
        cargs.append("--rh")
    if params.get("perform_reg"):
        cargs.append("--reg")
    if params.get("tal_compute"):
        cargs.append("--tal-compute")
    if params.get("no_tal_compute"):
        cargs.append("--no-tal-compute")
    if params.get("tal_estimate"):
        cargs.append("--tal-estimate")
    if params.get("no_tal_estimate"):
        cargs.append("--no-tal-estimate")
    if params.get("gcaprep") is not None:
        cargs.extend([
            "--gcaprep",
            params.get("gcaprep")
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def xhemireg_outputs(
    params: XhemiregParameters,
    execution: Execution,
) -> XhemiregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = XhemiregOutputs(
        root=execution.output_file("."),
    )
    return ret


def xhemireg_execute(
    params: XhemiregParameters,
    execution: Execution,
) -> XhemiregOutputs:
    """
    Tool for hemisphere registration in neuroimaging.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `XhemiregOutputs`).
    """
    cargs = xhemireg_cargs(params, execution)
    ret = xhemireg_outputs(params, execution)
    execution.run(cargs)
    return ret


def xhemireg(
    subject: str,
    output_dir: str | None = None,
    map_lh: bool = False,
    map_rh: bool = False,
    perform_reg: bool = False,
    tal_compute: bool = False,
    no_tal_compute: bool = False,
    tal_estimate: bool = False,
    no_tal_estimate: bool = False,
    gcaprep: str | None = None,
    threads: float | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> XhemiregOutputs:
    """
    Tool for hemisphere registration in neuroimaging.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject ID for the hemisphere registration process.
        output_dir: Output directory for the hemisphere registration.
        map_lh: Map from left hemisphere to right hemisphere.
        map_rh: Map from right hemisphere to left hemisphere.
        perform_reg: Perform registration to create sphere.reg.
        tal_compute: Recompute Talairach registration.
        no_tal_compute: Do not perform Talairach registration.
        tal_estimate: Compute estimate of Talairach registration from unflipped\
            registration.
        no_tal_estimate: Do not perform estimation of Talairach registration.
        gcaprep: Prepare GCA for training symmetrical GCA atlases.
        threads: Number of threads used, applicable with --gcaprep option.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XhemiregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XHEMIREG_METADATA)
    params = xhemireg_params(subject=subject, output_dir=output_dir, map_lh=map_lh, map_rh=map_rh, perform_reg=perform_reg, tal_compute=tal_compute, no_tal_compute=no_tal_compute, tal_estimate=tal_estimate, no_tal_estimate=no_tal_estimate, gcaprep=gcaprep, threads=threads, version=version, help_=help_)
    return xhemireg_execute(params, execution)


__all__ = [
    "XHEMIREG_METADATA",
    "XhemiregOutputs",
    "XhemiregParameters",
    "xhemireg",
    "xhemireg_params",
]

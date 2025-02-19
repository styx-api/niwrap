# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PLUGOUT_IJK_METADATA = Metadata(
    id="546af73f34fcb7f296f73da1cc63ae4ec231fec2.boutiques",
    name="plugout_ijk",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


PlugoutIjkParameters = typing.TypedDict('PlugoutIjkParameters', {
    "__STYX_TYPE__": typing.Literal["plugout_ijk"],
    "host": typing.NotRequired[str | None],
    "verbose": bool,
    "port": typing.NotRequired[float | None],
    "name": typing.NotRequired[str | None],
    "port_offset": typing.NotRequired[float | None],
    "port_quiet": typing.NotRequired[float | None],
    "port_bloc_offset": typing.NotRequired[float | None],
    "max_bloc": bool,
    "max_bloc_quiet": bool,
    "num_assigned_ports": bool,
    "num_assigned_ports_quiet": bool,
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
        "plugout_ijk": plugout_ijk_cargs,
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


class PlugoutIjkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `plugout_ijk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def plugout_ijk_params(
    host: str | None = None,
    verbose: bool = False,
    port: float | None = None,
    name: str | None = None,
    port_offset: float | None = None,
    port_quiet: float | None = None,
    port_bloc_offset: float | None = None,
    max_bloc: bool = False,
    max_bloc_quiet: bool = False,
    num_assigned_ports: bool = False,
    num_assigned_ports_quiet: bool = False,
) -> PlugoutIjkParameters:
    """
    Build parameters.
    
    Args:
        host: Connect to AFNI running on the specified computer using TCP/IP.
        verbose: Verbose mode.
        port: Use TCP/IP port number 'pp'.
        name: Use the string 'sss' for the name that AFNI assigns to this\
            plugout.
        port_offset: Provide a port offset to allow multiple instances of\
            communicating programs to operate on the same machine.
        port_quiet: Provide a port offset like -np, but more quiet in the face\
            of adversity.
        port_bloc_offset: Provide a port offset block for easier port\
            management.
        max_bloc: Print the current value of MAX_BLOC and exit.
        max_bloc_quiet: Print MAX_BLOC value only and exit.
        num_assigned_ports: Print the number of assigned ports used by AFNI\
            then quit.
        num_assigned_ports_quiet: Prints the number of assigned ports quietly.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "plugout_ijk",
        "verbose": verbose,
        "max_bloc": max_bloc,
        "max_bloc_quiet": max_bloc_quiet,
        "num_assigned_ports": num_assigned_ports,
        "num_assigned_ports_quiet": num_assigned_ports_quiet,
    }
    if host is not None:
        params["host"] = host
    if port is not None:
        params["port"] = port
    if name is not None:
        params["name"] = name
    if port_offset is not None:
        params["port_offset"] = port_offset
    if port_quiet is not None:
        params["port_quiet"] = port_quiet
    if port_bloc_offset is not None:
        params["port_bloc_offset"] = port_bloc_offset
    return params


def plugout_ijk_cargs(
    params: PlugoutIjkParameters,
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
    cargs.append("plugout_ijk")
    if params.get("host") is not None:
        cargs.extend([
            "-host",
            params.get("host")
        ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("port") is not None:
        cargs.extend([
            "-port",
            str(params.get("port"))
        ])
    if params.get("name") is not None:
        cargs.extend([
            "-name",
            params.get("name")
        ])
    if params.get("port_offset") is not None:
        cargs.extend([
            "-np",
            str(params.get("port_offset"))
        ])
    if params.get("port_quiet") is not None:
        cargs.extend([
            "-npq",
            str(params.get("port_quiet"))
        ])
    if params.get("port_bloc_offset") is not None:
        cargs.extend([
            "-npb",
            str(params.get("port_bloc_offset"))
        ])
    if params.get("max_bloc"):
        cargs.append("-max_port_bloc")
    if params.get("max_bloc_quiet"):
        cargs.append("-max_port_bloc_quiet")
    if params.get("num_assigned_ports"):
        cargs.append("-num_assigned_ports")
    if params.get("num_assigned_ports_quiet"):
        cargs.append("-num_assigned_ports_quiet")
    return cargs


def plugout_ijk_outputs(
    params: PlugoutIjkParameters,
    execution: Execution,
) -> PlugoutIjkOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PlugoutIjkOutputs(
        root=execution.output_file("."),
    )
    return ret


def plugout_ijk_execute(
    params: PlugoutIjkParameters,
    execution: Execution,
) -> PlugoutIjkOutputs:
    """
    Connects to AFNI and sends (i,j,k) dataset indices to control the viewpoint.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PlugoutIjkOutputs`).
    """
    params = execution.params(params)
    cargs = plugout_ijk_cargs(params, execution)
    ret = plugout_ijk_outputs(params, execution)
    execution.run(cargs)
    return ret


def plugout_ijk(
    host: str | None = None,
    verbose: bool = False,
    port: float | None = None,
    name: str | None = None,
    port_offset: float | None = None,
    port_quiet: float | None = None,
    port_bloc_offset: float | None = None,
    max_bloc: bool = False,
    max_bloc_quiet: bool = False,
    num_assigned_ports: bool = False,
    num_assigned_ports_quiet: bool = False,
    runner: Runner | None = None,
) -> PlugoutIjkOutputs:
    """
    Connects to AFNI and sends (i,j,k) dataset indices to control the viewpoint.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        host: Connect to AFNI running on the specified computer using TCP/IP.
        verbose: Verbose mode.
        port: Use TCP/IP port number 'pp'.
        name: Use the string 'sss' for the name that AFNI assigns to this\
            plugout.
        port_offset: Provide a port offset to allow multiple instances of\
            communicating programs to operate on the same machine.
        port_quiet: Provide a port offset like -np, but more quiet in the face\
            of adversity.
        port_bloc_offset: Provide a port offset block for easier port\
            management.
        max_bloc: Print the current value of MAX_BLOC and exit.
        max_bloc_quiet: Print MAX_BLOC value only and exit.
        num_assigned_ports: Print the number of assigned ports used by AFNI\
            then quit.
        num_assigned_ports_quiet: Prints the number of assigned ports quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PlugoutIjkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PLUGOUT_IJK_METADATA)
    params = plugout_ijk_params(
        host=host,
        verbose=verbose,
        port=port,
        name=name,
        port_offset=port_offset,
        port_quiet=port_quiet,
        port_bloc_offset=port_bloc_offset,
        max_bloc=max_bloc,
        max_bloc_quiet=max_bloc_quiet,
        num_assigned_ports=num_assigned_ports,
        num_assigned_ports_quiet=num_assigned_ports_quiet,
    )
    return plugout_ijk_execute(params, execution)


__all__ = [
    "PLUGOUT_IJK_METADATA",
    "PlugoutIjkOutputs",
    "PlugoutIjkParameters",
    "plugout_ijk",
    "plugout_ijk_params",
]

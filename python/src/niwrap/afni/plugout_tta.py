# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PLUGOUT_TTA_METADATA = Metadata(
    id="eed1ec955438438ba757fc77c80cf0639ea64da3.boutiques",
    name="plugout_tta",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class PlugoutTtaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `plugout_tta(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def plugout_tta(
    host: str | None = None,
    port: int | None = None,
    verbose: bool = False,
    port_offset: int | None = None,
    port_offset_quiet: int | None = None,
    port_offset_bloc: int | None = None,
    max_port_bloc: bool = False,
    max_port_bloc_quiet: bool = False,
    num_assigned_ports: bool = False,
    num_assigned_ports_quiet: bool = False,
    runner: Runner | None = None,
) -> PlugoutTtaOutputs:
    """
    Connects to AFNI and receives notification whenever the user changes Talairach
    coordinates, then drives Netscape to display the closest figures from the
    Talairach-Tournoux atlas.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/plugout_tta.html
    
    Args:
        host: Connect to AFNI running on the specified computer using TCP/IP.\
            Use '-host localhost' to connect on current host with TCP/IP.
        port: Use TCP/IP port number 'pp'. Default is 8005.
        verbose: Verbose mode: prints out progress reports.
        port_offset: Provide a port offset to allow multiple instances of\
            programs to communicate on the same machine. All ports are assigned\
            numbers relative to PORT_OFFSET. Range: [1025, 65500].
        port_offset_quiet: Like -np, but more quiet in the face of adversity.
        port_offset_bloc: Provide a port offset block. Easier to use than -np.\
            Range: [0, MAX_BLOC]. Using this reduces chances of port conflicts.
        max_port_bloc: Print the current value of MAX_BLOC and exit.
        max_port_bloc_quiet: Print MAX_BLOC value and exit quietly.
        num_assigned_ports: Print the number of assigned ports used by AFNI\
            then quit.
        num_assigned_ports_quiet: Print the number of assigned ports used by\
            AFNI then quit quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PlugoutTtaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PLUGOUT_TTA_METADATA)
    cargs = []
    cargs.append("plugout_tta")
    if host is not None:
        cargs.extend([
            "-host",
            host
        ])
    if port is not None:
        cargs.extend([
            "-port",
            str(port)
        ])
    if verbose:
        cargs.append("-v")
    if port_offset is not None:
        cargs.extend([
            "-np",
            str(port_offset)
        ])
    if port_offset_quiet is not None:
        cargs.extend([
            "-npq",
            str(port_offset_quiet)
        ])
    if port_offset_bloc is not None:
        cargs.extend([
            "-npb",
            str(port_offset_bloc)
        ])
    if max_port_bloc:
        cargs.append("-max_port_bloc")
    if max_port_bloc_quiet:
        cargs.append("-max_port_bloc_quiet")
    if num_assigned_ports:
        cargs.append("-num_assigned_ports")
    if num_assigned_ports_quiet:
        cargs.append("-num_assigned_ports_quiet")
    ret = PlugoutTtaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PLUGOUT_TTA_METADATA",
    "PlugoutTtaOutputs",
    "plugout_tta",
]

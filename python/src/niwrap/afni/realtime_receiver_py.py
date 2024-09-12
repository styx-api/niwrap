# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REALTIME_RECEIVER_PY_METADATA = Metadata(
    id="9de2be43370c85b484b9455706b62a276bf1580c.boutiques",
    name="realtime_receiver.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class RealtimeReceiverPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `realtime_receiver_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def realtime_receiver_py(
    show_data: typing.Literal["yes", "no"] | None = None,
    write_text_data: str | None = None,
    data_choice: typing.Literal["motion", "motion_norm", "all_extras", "diff_ratio"] | None = None,
    serial_port: str | None = None,
    show_demo_gui: typing.Literal["yes", "no"] | None = None,
    dc_params: list[float] | None = None,
    extras_on_one_line: typing.Literal["yes", "no"] | None = None,
    show_comm_times: bool = False,
    show_demo_data: bool = False,
    swap: bool = False,
    tcp_port: float | None = None,
    verbosity: float | None = None,
    runner: Runner | None = None,
) -> RealtimeReceiverPyOutputs:
    """
    Program to receive and display real-time plugin data from AFNI.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/realtime_receiver.py.html
    
    Args:
        show_data: Display incoming data in terminal window.
        write_text_data: Write data to text file.
        data_choice: Pick which data to send as feedback.
        serial_port: Specify serial port file for feedback data.
        show_demo_gui: Demonstrate a feedback GUI.
        dc_params: Set data_choice parameters, e.g. for diff_ratio, params P1\
            P2.
        extras_on_one_line: Show 'extras' on one line only.
        show_comm_times: Display communication times.
        show_demo_data: Display feedback data in terminal window.
        swap: Swap bytes of incoming data.
        tcp_port: Specify TCP port for incoming connections.
        verbosity: Set the verbosity level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RealtimeReceiverPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REALTIME_RECEIVER_PY_METADATA)
    cargs = []
    cargs.append("realtime_receiver.py")
    if show_data is not None:
        cargs.extend([
            "-show_data",
            show_data
        ])
    if write_text_data is not None:
        cargs.extend([
            "-write_text_data",
            write_text_data
        ])
    if data_choice is not None:
        cargs.extend([
            "-data_choice",
            data_choice
        ])
    if serial_port is not None:
        cargs.extend([
            "-serial_port",
            serial_port
        ])
    if show_demo_gui is not None:
        cargs.extend([
            "-show_demo_gui",
            show_demo_gui
        ])
    if dc_params is not None:
        cargs.extend([
            "-dc_params",
            *map(str, dc_params)
        ])
    if extras_on_one_line is not None:
        cargs.extend([
            "-extras_on_one_line",
            extras_on_one_line
        ])
    if show_comm_times:
        cargs.append("-show_comm_times")
    if show_demo_data:
        cargs.append("-show_demo_data")
    if swap:
        cargs.append("-swap")
    if tcp_port is not None:
        cargs.extend([
            "-tcp_port",
            str(tcp_port)
        ])
    if verbosity is not None:
        cargs.extend([
            "-verb",
            str(verbosity)
        ])
    ret = RealtimeReceiverPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REALTIME_RECEIVER_PY_METADATA",
    "RealtimeReceiverPyOutputs",
    "realtime_receiver_py",
]

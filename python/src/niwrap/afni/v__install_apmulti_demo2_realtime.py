# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_APMULTI_DEMO2_REALTIME_METADATA = Metadata(
    id="35a4473905976e57395c02879ed22abe1b49a7c1.boutiques",
    name="@Install_APMULTI_Demo2_realtime",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstallApmultiDemo2RealtimeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_apmulti_demo2_realtime(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__install_apmulti_demo2_realtime(
    curl: bool = False,
    runner: Runner | None = None,
) -> VInstallApmultiDemo2RealtimeOutputs:
    """
    Fetches the demo data and scripts corresponding to AFNI's Demo #2 for
    experimenting with AFNI's real-time system.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_APMULTI_Demo2_realtime.html
    
    Args:
        curl: Use curl to download the archive. By default, the script prefers\
            curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallApmultiDemo2RealtimeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_APMULTI_DEMO2_REALTIME_METADATA)
    cargs = []
    cargs.append("@Install_APMULTI_Demo2_realtime")
    if curl:
        cargs.append("-curl")
    ret = VInstallApmultiDemo2RealtimeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallApmultiDemo2RealtimeOutputs",
    "V__INSTALL_APMULTI_DEMO2_REALTIME_METADATA",
    "v__install_apmulti_demo2_realtime",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_SURFLAYERS_DEMO1_METADATA = Metadata(
    id="96992a1608117a9aed2d18e498316b838723c21d.boutiques",
    name="@Install_SURFLAYERS_DEMO1",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstallSurflayersDemo1Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_surflayers_demo1(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__install_surflayers_demo1(
    use_wget: bool = False,
    use_curl: bool = False,
    runner: Runner | None = None,
) -> VInstallSurflayersDemo1Outputs:
    """
    Fetches 6 driver scripts for 3 datasets as demonstrated in the 2021 OHBM poster
    and demo video about SurfLayers.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_SURFLAYERS_DEMO1.html
    
    Args:
        use_wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        use_curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallSurflayersDemo1Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_SURFLAYERS_DEMO1_METADATA)
    cargs = []
    cargs.append("@Install_SURFLAYERS_DEMO1")
    if use_wget:
        cargs.append("-wget")
    if use_curl:
        cargs.append("-curl")
    ret = VInstallSurflayersDemo1Outputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallSurflayersDemo1Outputs",
    "V__INSTALL_SURFLAYERS_DEMO1_METADATA",
    "v__install_surflayers_demo1",
]

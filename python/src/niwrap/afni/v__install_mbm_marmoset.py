# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_MBM_MARMOSET_METADATA = Metadata(
    id="f5f69f845ca75bf6764009410dc0384dc0ba5615.boutiques",
    name="@Install_MBM_Marmoset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstallMbmMarmosetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_mbm_marmoset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__install_mbm_marmoset(
    wget: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> VInstallMbmMarmosetOutputs:
    """
    Installs the NIH marmoset template and atlases.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_MBM_Marmoset.html
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallMbmMarmosetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_MBM_MARMOSET_METADATA)
    cargs = []
    cargs.append("@Install_MBM_Marmoset")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    ret = VInstallMbmMarmosetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallMbmMarmosetOutputs",
    "V__INSTALL_MBM_MARMOSET_METADATA",
    "v__install_mbm_marmoset",
]

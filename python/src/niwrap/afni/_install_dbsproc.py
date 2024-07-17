# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

INSTALL_DBSPROC_METADATA = Metadata(
    id="ad9b1c1ff5bdee560b6525d93ce8d8cee3e9b847",
    name="Install_DBSproc",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-dbproc:latest",
)


class InstallDbsprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_dbsproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def install_dbsproc(
    use_wget: bool = False,
    use_curl: bool = False,
    runner: Runner | None = None,
) -> InstallDbsprocOutputs:
    """
    Install_DBSproc by Lauro PM, Vanegas-Arroyave N, Huang L, Taylor PA, Zaghloul
    KA, Lungu C, Saad ZS, Horovitz SG.
    
    Installs the demo archive for DBS processing tools.
    
    More information: https://dx.doi.org/10.1002/hbm.23039
    
    Args:
        use_wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        use_curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallDbsprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_DBSPROC_METADATA)
    cargs = []
    cargs.append("Install_DBSproc")
    if use_wget:
        cargs.append("-wget")
    if use_curl:
        cargs.append("-curl")
    ret = InstallDbsprocOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_DBSPROC_METADATA",
    "InstallDbsprocOutputs",
    "install_dbsproc",
]

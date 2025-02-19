# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CVS_DATA_COPY_METADATA = Metadata(
    id="b73336351ee9c11ffda39c6ee8b2af17a54695d1.boutiques",
    name="mri_cvs_data_copy",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCvsDataCopyParameters = typing.TypedDict('MriCvsDataCopyParameters', {
    "__STYX_TYPE__": typing.Literal["mri_cvs_data_copy"],
    "subjid": str,
    "olddir": str,
    "newdir": str,
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
        "mri_cvs_data_copy": mri_cvs_data_copy_cargs,
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


class MriCvsDataCopyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cvs_data_copy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_cvs_data_copy_params(
    subjid: str,
    olddir: str,
    newdir: str,
    version: bool = False,
    help_: bool = False,
) -> MriCvsDataCopyParameters:
    """
    Build parameters.
    
    Args:
        subjid: Subject ID of the subject to be moved/registered.
        olddir: Directory where data (FS reconned output files for the subject)\
            is currently located. Use full path.
        newdir: Directory where data (FS reconned output files for the subject)\
            should be moved to. Use full path.
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_cvs_data_copy",
        "subjid": subjid,
        "olddir": olddir,
        "newdir": newdir,
        "version": version,
        "help": help_,
    }
    return params


def mri_cvs_data_copy_cargs(
    params: MriCvsDataCopyParameters,
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
    cargs.append("mri_cvs_data_copy")
    cargs.extend([
        "--subjid",
        params.get("subjid")
    ])
    cargs.extend([
        "--olddir",
        params.get("olddir")
    ])
    cargs.extend([
        "--newdir",
        params.get("newdir")
    ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mri_cvs_data_copy_outputs(
    params: MriCvsDataCopyParameters,
    execution: Execution,
) -> MriCvsDataCopyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCvsDataCopyOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_cvs_data_copy_execute(
    params: MriCvsDataCopyParameters,
    execution: Execution,
) -> MriCvsDataCopyOutputs:
    """
    Packs and copies files that are required for mri_cvs_register.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCvsDataCopyOutputs`).
    """
    params = execution.params(params)
    cargs = mri_cvs_data_copy_cargs(params, execution)
    ret = mri_cvs_data_copy_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_cvs_data_copy(
    subjid: str,
    olddir: str,
    newdir: str,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriCvsDataCopyOutputs:
    """
    Packs and copies files that are required for mri_cvs_register.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjid: Subject ID of the subject to be moved/registered.
        olddir: Directory where data (FS reconned output files for the subject)\
            is currently located. Use full path.
        newdir: Directory where data (FS reconned output files for the subject)\
            should be moved to. Use full path.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCvsDataCopyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CVS_DATA_COPY_METADATA)
    params = mri_cvs_data_copy_params(
        subjid=subjid,
        olddir=olddir,
        newdir=newdir,
        version=version,
        help_=help_,
    )
    return mri_cvs_data_copy_execute(params, execution)


__all__ = [
    "MRI_CVS_DATA_COPY_METADATA",
    "MriCvsDataCopyOutputs",
    "MriCvsDataCopyParameters",
    "mri_cvs_data_copy",
    "mri_cvs_data_copy_params",
]

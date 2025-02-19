# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FSLABEL2DSET_METADATA = Metadata(
    id="9fe2630c3f97cdc57615a68de7b89685d793afec.boutiques",
    name="@FSlabel2dset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VFslabel2dsetParameters = typing.TypedDict('VFslabel2dsetParameters', {
    "__STYX_TYPE__": typing.Literal["@FSlabel2dset"],
    "fs_label_file": InputPathType,
    "val": typing.NotRequired[float | None],
    "help": bool,
    "echo": bool,
    "keep_tmp": bool,
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
        "@FSlabel2dset": v__fslabel2dset_cargs,
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


class VFslabel2dsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fslabel2dset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__fslabel2dset_params(
    fs_label_file: InputPathType,
    val: float | None = None,
    help_: bool = False,
    echo: bool = False,
    keep_tmp: bool = False,
) -> VFslabel2dsetParameters:
    """
    Build parameters.
    
    Args:
        fs_label_file: Specify the ASCII label file from FreeSurfer.
        val: Assign integer VAL to the nodes in FS_LABEL_FILE (Default is 1).
        help_: Display help message.
        echo: Turn echo for debugging.
        keep_tmp: Don't cleanup temp files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@FSlabel2dset",
        "fs_label_file": fs_label_file,
        "help": help_,
        "echo": echo,
        "keep_tmp": keep_tmp,
    }
    if val is not None:
        params["val"] = val
    return params


def v__fslabel2dset_cargs(
    params: VFslabel2dsetParameters,
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
    cargs.append("@FSlabel2dset")
    cargs.extend([
        "-fs",
        execution.input_file(params.get("fs_label_file"))
    ])
    if params.get("val") is not None:
        cargs.extend([
            "-val",
            str(params.get("val"))
        ])
    if params.get("help"):
        cargs.append("-help")
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("keep_tmp"):
        cargs.append("-keep_tmp")
    return cargs


def v__fslabel2dset_outputs(
    params: VFslabel2dsetParameters,
    execution: Execution,
) -> VFslabel2dsetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFslabel2dsetOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__fslabel2dset_execute(
    params: VFslabel2dsetParameters,
    execution: Execution,
) -> VFslabel2dsetOutputs:
    """
    A script to convert a FreeSurfer ASCII label file into a SUMA dataset and a SUMA
    ROI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFslabel2dsetOutputs`).
    """
    params = execution.params(params)
    cargs = v__fslabel2dset_cargs(params, execution)
    ret = v__fslabel2dset_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__fslabel2dset(
    fs_label_file: InputPathType,
    val: float | None = None,
    help_: bool = False,
    echo: bool = False,
    keep_tmp: bool = False,
    runner: Runner | None = None,
) -> VFslabel2dsetOutputs:
    """
    A script to convert a FreeSurfer ASCII label file into a SUMA dataset and a SUMA
    ROI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fs_label_file: Specify the ASCII label file from FreeSurfer.
        val: Assign integer VAL to the nodes in FS_LABEL_FILE (Default is 1).
        help_: Display help message.
        echo: Turn echo for debugging.
        keep_tmp: Don't cleanup temp files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFslabel2dsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FSLABEL2DSET_METADATA)
    params = v__fslabel2dset_params(
        fs_label_file=fs_label_file,
        val=val,
        help_=help_,
        echo=echo,
        keep_tmp=keep_tmp,
    )
    return v__fslabel2dset_execute(params, execution)


__all__ = [
    "VFslabel2dsetOutputs",
    "VFslabel2dsetParameters",
    "V__FSLABEL2DSET_METADATA",
    "v__fslabel2dset",
    "v__fslabel2dset_params",
]

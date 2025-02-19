# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_REGISTER_LABEL_MAP_METADATA = Metadata(
    id="da7f5799fccbaa00ae28b92114de5d6ef1a4db4f.boutiques",
    name="mris_register_label_map",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisRegisterLabelMapParameters = typing.TypedDict('MrisRegisterLabelMapParameters', {
    "__STYX_TYPE__": typing.Literal["mris_register_label_map"],
    "subjects_list": str,
    "target_subject": str,
    "prior": str,
    "label": str,
    "template_volume": InputPathType,
    "debug": bool,
    "check_opts": bool,
    "help": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "version": bool,
    "vno": typing.NotRequired[float | None],
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
        "mris_register_label_map": mris_register_label_map_cargs,
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


class MrisRegisterLabelMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_register_label_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_register_label_map_params(
    subjects_list: str,
    target_subject: str,
    prior: str,
    label: str,
    template_volume: InputPathType,
    debug: bool = False,
    check_opts: bool = False,
    help_: bool = False,
    subjects_dir: str | None = None,
    version: bool = False,
    vno: float | None = None,
) -> MrisRegisterLabelMapParameters:
    """
    Build parameters.
    
    Args:
        subjects_list: List of training subjects.
        target_subject: Name of target subject.
        prior: Name of prior surface overlay.
        label: Name of label for each subject.
        template_volume: Template volume file.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        subjects_dir: SUBJECTS_DIR.
        version: Print out version and exit.
        vno: Debug this vertex.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_register_label_map",
        "subjects_list": subjects_list,
        "target_subject": target_subject,
        "prior": prior,
        "label": label,
        "template_volume": template_volume,
        "debug": debug,
        "check_opts": check_opts,
        "help": help_,
        "version": version,
    }
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if vno is not None:
        params["vno"] = vno
    return params


def mris_register_label_map_cargs(
    params: MrisRegisterLabelMapParameters,
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
    cargs.append("mris_register_label_map")
    cargs.extend([
        "--subjects",
        params.get("subjects_list")
    ])
    cargs.extend([
        "--trgsubject",
        params.get("target_subject")
    ])
    cargs.extend([
        "--prior",
        params.get("prior")
    ])
    cargs.extend([
        "--label",
        params.get("label")
    ])
    cargs.extend([
        "--temp-vol",
        execution.input_file(params.get("template_volume"))
    ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("check_opts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sdir",
            params.get("subjects_dir")
        ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("vno") is not None:
        cargs.extend([
            "--v",
            str(params.get("vno"))
        ])
    return cargs


def mris_register_label_map_outputs(
    params: MrisRegisterLabelMapParameters,
    execution: Execution,
) -> MrisRegisterLabelMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRegisterLabelMapOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_register_label_map_execute(
    params: MrisRegisterLabelMapParameters,
    execution: Execution,
) -> MrisRegisterLabelMapOutputs:
    """
    Tool for registering label maps in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRegisterLabelMapOutputs`).
    """
    params = execution.params(params)
    cargs = mris_register_label_map_cargs(params, execution)
    ret = mris_register_label_map_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_register_label_map(
    subjects_list: str,
    target_subject: str,
    prior: str,
    label: str,
    template_volume: InputPathType,
    debug: bool = False,
    check_opts: bool = False,
    help_: bool = False,
    subjects_dir: str | None = None,
    version: bool = False,
    vno: float | None = None,
    runner: Runner | None = None,
) -> MrisRegisterLabelMapOutputs:
    """
    Tool for registering label maps in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_list: List of training subjects.
        target_subject: Name of target subject.
        prior: Name of prior surface overlay.
        label: Name of label for each subject.
        template_volume: Template volume file.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        subjects_dir: SUBJECTS_DIR.
        version: Print out version and exit.
        vno: Debug this vertex.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRegisterLabelMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REGISTER_LABEL_MAP_METADATA)
    params = mris_register_label_map_params(
        subjects_list=subjects_list,
        target_subject=target_subject,
        prior=prior,
        label=label,
        template_volume=template_volume,
        debug=debug,
        check_opts=check_opts,
        help_=help_,
        subjects_dir=subjects_dir,
        version=version,
        vno=vno,
    )
    return mris_register_label_map_execute(params, execution)


__all__ = [
    "MRIS_REGISTER_LABEL_MAP_METADATA",
    "MrisRegisterLabelMapOutputs",
    "MrisRegisterLabelMapParameters",
    "mris_register_label_map",
    "mris_register_label_map_params",
]

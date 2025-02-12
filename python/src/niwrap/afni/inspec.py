# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INSPEC_METADATA = Metadata(
    id="6a13b0f30f764b4a293786927f7b9ec71eacbd6c.boutiques",
    name="inspec",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
InspecParameters = typing.TypedDict('InspecParameters', {
    "__STYX_TYPE__": typing.Literal["inspec"],
    "specfile": InputPathType,
    "newspecname": typing.NotRequired[str | None],
    "detail": typing.NotRequired[float | None],
    "leftspec": typing.NotRequired[InputPathType | None],
    "rightspec": typing.NotRequired[InputPathType | None],
    "state_rm": typing.NotRequired[str | None],
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
        "inspec": inspec_cargs,
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


class InspecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inspec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def inspec_params(
    specfile: InputPathType,
    newspecname: str | None = None,
    detail: float | None = None,
    leftspec: InputPathType | None = None,
    rightspec: InputPathType | None = None,
    state_rm: str | None = None,
    help_: bool = False,
) -> InspecParameters:
    """
    Build parameters.
    
    Args:
        specfile: Spec file to be read.
        newspecname: Rewrite spec file.
        detail: Level of output detail. Default is 1 in general, 0 with\
            -LRmerge. Available levels are 0, 1, 2, and 3.
        leftspec: Merge two spec files in a way that makes sense for viewing in\
            SUMA.
        rightspec: Merge two spec files in a way that makes sense for viewing\
            in SUMA.
        state_rm: Get rid of state STATE_RM from the specfile.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inspec",
        "specfile": specfile,
        "help": help_,
    }
    if newspecname is not None:
        params["newspecname"] = newspecname
    if detail is not None:
        params["detail"] = detail
    if leftspec is not None:
        params["leftspec"] = leftspec
    if rightspec is not None:
        params["rightspec"] = rightspec
    if state_rm is not None:
        params["state_rm"] = state_rm
    return params


def inspec_cargs(
    params: InspecParameters,
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
    cargs.append("inspec")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("specfile"))
    ])
    if params.get("newspecname") is not None:
        cargs.extend([
            "-prefix",
            params.get("newspecname")
        ])
    if params.get("detail") is not None:
        cargs.extend([
            "-detail",
            str(params.get("detail"))
        ])
    if params.get("leftspec") is not None:
        cargs.extend([
            "-LRmerge",
            execution.input_file(params.get("leftspec"))
        ])
    if params.get("rightspec") is not None:
        cargs.extend([
            "-LRmerge",
            execution.input_file(params.get("rightspec"))
        ])
    if params.get("state_rm") is not None:
        cargs.extend([
            "-remove_state",
            params.get("state_rm")
        ])
    if params.get("help"):
        cargs.append("-help")
    return cargs


def inspec_outputs(
    params: InspecParameters,
    execution: Execution,
) -> InspecOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InspecOutputs(
        root=execution.output_file("."),
    )
    return ret


def inspec_execute(
    params: InspecParameters,
    execution: Execution,
) -> InspecOutputs:
    """
    Outputs information found from specfile.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InspecOutputs`).
    """
    cargs = inspec_cargs(params, execution)
    ret = inspec_outputs(params, execution)
    execution.run(cargs)
    return ret


def inspec(
    specfile: InputPathType,
    newspecname: str | None = None,
    detail: float | None = None,
    leftspec: InputPathType | None = None,
    rightspec: InputPathType | None = None,
    state_rm: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> InspecOutputs:
    """
    Outputs information found from specfile.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        specfile: Spec file to be read.
        newspecname: Rewrite spec file.
        detail: Level of output detail. Default is 1 in general, 0 with\
            -LRmerge. Available levels are 0, 1, 2, and 3.
        leftspec: Merge two spec files in a way that makes sense for viewing in\
            SUMA.
        rightspec: Merge two spec files in a way that makes sense for viewing\
            in SUMA.
        state_rm: Get rid of state STATE_RM from the specfile.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InspecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSPEC_METADATA)
    params = inspec_params(specfile=specfile, newspecname=newspecname, detail=detail, leftspec=leftspec, rightspec=rightspec, state_rm=state_rm, help_=help_)
    return inspec_execute(params, execution)


__all__ = [
    "INSPEC_METADATA",
    "InspecOutputs",
    "InspecParameters",
    "inspec",
    "inspec_params",
]

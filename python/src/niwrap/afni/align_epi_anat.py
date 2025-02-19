# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ALIGN_EPI_ANAT_METADATA = Metadata(
    id="8b0229305647603bf69640345954c0975124bb02.boutiques",
    name="align_epi_anat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


AlignEpiAnatParameters = typing.TypedDict('AlignEpiAnatParameters', {
    "__STYX_TYPE__": typing.Literal["align_epi_anat"],
    "epi": InputPathType,
    "anat": InputPathType,
    "epi_base": str,
    "anat2epi": bool,
    "epi2anat": bool,
    "suffix": typing.NotRequired[str | None],
    "AddEdge": bool,
    "big_move": bool,
    "giant_move": bool,
    "ginormous_move": bool,
    "keep_rm_files": bool,
    "prep_only": bool,
    "ana_has_skull": typing.NotRequired[typing.Literal["yes", "no"] | None],
    "epi_strip": typing.NotRequired[typing.Literal["3dSkullStrip", "3dAutomask", "None"] | None],
    "volreg_method": typing.NotRequired[typing.Literal["3dvolreg", "3dWarpDrive", "3dAllineate"] | None],
    "ex_mode": typing.NotRequired[typing.Literal["quiet", "echo", "dry_run", "script"] | None],
    "overwrite": bool,
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
        "align_epi_anat": align_epi_anat_cargs,
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
        "align_epi_anat": align_epi_anat_outputs,
    }.get(t)


class AlignEpiAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `align_epi_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    anat_aligned: OutputPathType
    """A version of the anatomy that is aligned to the EPI"""
    epi_aligned: OutputPathType
    """A version of the EPI dataset aligned to the Anatomy"""


def align_epi_anat_params(
    epi: InputPathType,
    anat: InputPathType,
    epi_base: str,
    anat2epi: bool = False,
    epi2anat: bool = False,
    suffix: str | None = None,
    add_edge: bool = False,
    big_move: bool = False,
    giant_move: bool = False,
    ginormous_move: bool = False,
    keep_rm_files: bool = False,
    prep_only: bool = False,
    ana_has_skull: typing.Literal["yes", "no"] | None = None,
    epi_strip: typing.Literal["3dSkullStrip", "3dAutomask", "None"] | None = None,
    volreg_method: typing.Literal["3dvolreg", "3dWarpDrive", "3dAllineate"] | None = None,
    ex_mode: typing.Literal["quiet", "echo", "dry_run", "script"] | None = None,
    overwrite: bool = False,
) -> AlignEpiAnatParameters:
    """
    Build parameters.
    
    Args:
        epi: EPI dataset to align or to which to align.
        anat: Anatomical dataset to align or to which to align.
        epi_base: Base sub-brick to use for alignment\
            (0/mean/median/max/subbrick#).
        anat2epi: Align anatomical to EPI dataset (default).
        epi2anat: Align EPI to anatomical dataset.
        suffix: Append suffix to the original anat/epi dataset to use in the\
            resulting dataset names.
        add_edge: Run @AddEdge script to create composite edge images.
        big_move: Large displacement is needed to align the two volumes.
        giant_move: Even larger movement required, uses cmass, two passes and\
            very large angles and shifts.
        ginormous_move: Adds align_centers to giant_move.
        keep_rm_files: Don't delete any of the temporary files created.
        prep_only: Do preprocessing steps only without alignment.
        ana_has_skull: Do not skullstrip anat dataset.
        epi_strip: Method to remove skull for EPI data.
        volreg_method: Time series volume registration method.
        ex_mode: Command execution mode.
        overwrite: Overwrite existing files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "align_epi_anat",
        "epi": epi,
        "anat": anat,
        "epi_base": epi_base,
        "anat2epi": anat2epi,
        "epi2anat": epi2anat,
        "AddEdge": add_edge,
        "big_move": big_move,
        "giant_move": giant_move,
        "ginormous_move": ginormous_move,
        "keep_rm_files": keep_rm_files,
        "prep_only": prep_only,
        "overwrite": overwrite,
    }
    if suffix is not None:
        params["suffix"] = suffix
    if ana_has_skull is not None:
        params["ana_has_skull"] = ana_has_skull
    if epi_strip is not None:
        params["epi_strip"] = epi_strip
    if volreg_method is not None:
        params["volreg_method"] = volreg_method
    if ex_mode is not None:
        params["ex_mode"] = ex_mode
    return params


def align_epi_anat_cargs(
    params: AlignEpiAnatParameters,
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
    cargs.append("align_epi_anat.py")
    cargs.extend([
        "-epi",
        execution.input_file(params.get("epi"))
    ])
    cargs.extend([
        "-anat",
        execution.input_file(params.get("anat"))
    ])
    cargs.extend([
        "-epi_base",
        params.get("epi_base")
    ])
    if params.get("anat2epi"):
        cargs.append("-anat2epi")
    if params.get("epi2anat"):
        cargs.append("-epi2anat")
    if params.get("suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("suffix")
        ])
    if params.get("AddEdge"):
        cargs.append("-AddEdge")
    if params.get("big_move"):
        cargs.append("-big_move")
    if params.get("giant_move"):
        cargs.append("-giant_move")
    if params.get("ginormous_move"):
        cargs.append("-ginormous_move")
    if params.get("keep_rm_files"):
        cargs.append("-keep_rm_files")
    if params.get("prep_only"):
        cargs.append("-prep_only")
    if params.get("ana_has_skull") is not None:
        cargs.extend([
            "-anat_has_skull",
            params.get("ana_has_skull")
        ])
    if params.get("epi_strip") is not None:
        cargs.extend([
            "-epi_strip",
            params.get("epi_strip")
        ])
    if params.get("volreg_method") is not None:
        cargs.extend([
            "-volreg_method",
            params.get("volreg_method")
        ])
    if params.get("ex_mode") is not None:
        cargs.extend([
            "-ex_mode",
            params.get("ex_mode")
        ])
    if params.get("overwrite"):
        cargs.append("-overwrite")
    return cargs


def align_epi_anat_outputs(
    params: AlignEpiAnatParameters,
    execution: Execution,
) -> AlignEpiAnatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AlignEpiAnatOutputs(
        root=execution.output_file("."),
        anat_aligned=execution.output_file(pathlib.Path(params.get("anat")).name + "+orig"),
        epi_aligned=execution.output_file(pathlib.Path(params.get("epi")).name + "+orig"),
    )
    return ret


def align_epi_anat_execute(
    params: AlignEpiAnatParameters,
    execution: Execution,
) -> AlignEpiAnatOutputs:
    """
    Align EPI to anatomical datasets or vice versa.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AlignEpiAnatOutputs`).
    """
    params = execution.params(params)
    cargs = align_epi_anat_cargs(params, execution)
    ret = align_epi_anat_outputs(params, execution)
    execution.run(cargs)
    return ret


def align_epi_anat(
    epi: InputPathType,
    anat: InputPathType,
    epi_base: str,
    anat2epi: bool = False,
    epi2anat: bool = False,
    suffix: str | None = None,
    add_edge: bool = False,
    big_move: bool = False,
    giant_move: bool = False,
    ginormous_move: bool = False,
    keep_rm_files: bool = False,
    prep_only: bool = False,
    ana_has_skull: typing.Literal["yes", "no"] | None = None,
    epi_strip: typing.Literal["3dSkullStrip", "3dAutomask", "None"] | None = None,
    volreg_method: typing.Literal["3dvolreg", "3dWarpDrive", "3dAllineate"] | None = None,
    ex_mode: typing.Literal["quiet", "echo", "dry_run", "script"] | None = None,
    overwrite: bool = False,
    runner: Runner | None = None,
) -> AlignEpiAnatOutputs:
    """
    Align EPI to anatomical datasets or vice versa.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        epi: EPI dataset to align or to which to align.
        anat: Anatomical dataset to align or to which to align.
        epi_base: Base sub-brick to use for alignment\
            (0/mean/median/max/subbrick#).
        anat2epi: Align anatomical to EPI dataset (default).
        epi2anat: Align EPI to anatomical dataset.
        suffix: Append suffix to the original anat/epi dataset to use in the\
            resulting dataset names.
        add_edge: Run @AddEdge script to create composite edge images.
        big_move: Large displacement is needed to align the two volumes.
        giant_move: Even larger movement required, uses cmass, two passes and\
            very large angles and shifts.
        ginormous_move: Adds align_centers to giant_move.
        keep_rm_files: Don't delete any of the temporary files created.
        prep_only: Do preprocessing steps only without alignment.
        ana_has_skull: Do not skullstrip anat dataset.
        epi_strip: Method to remove skull for EPI data.
        volreg_method: Time series volume registration method.
        ex_mode: Command execution mode.
        overwrite: Overwrite existing files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AlignEpiAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ALIGN_EPI_ANAT_METADATA)
    params = align_epi_anat_params(
        epi=epi,
        anat=anat,
        epi_base=epi_base,
        anat2epi=anat2epi,
        epi2anat=epi2anat,
        suffix=suffix,
        add_edge=add_edge,
        big_move=big_move,
        giant_move=giant_move,
        ginormous_move=ginormous_move,
        keep_rm_files=keep_rm_files,
        prep_only=prep_only,
        ana_has_skull=ana_has_skull,
        epi_strip=epi_strip,
        volreg_method=volreg_method,
        ex_mode=ex_mode,
        overwrite=overwrite,
    )
    return align_epi_anat_execute(params, execution)


__all__ = [
    "ALIGN_EPI_ANAT_METADATA",
    "AlignEpiAnatOutputs",
    "AlignEpiAnatParameters",
    "align_epi_anat",
    "align_epi_anat_params",
]

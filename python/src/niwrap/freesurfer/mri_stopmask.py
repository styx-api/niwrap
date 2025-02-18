# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_STOPMASK_METADATA = Metadata(
    id="e7f2a3c2cfe3f7fafce248b01fa340177fa54cc2.boutiques",
    name="mri_stopmask",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriStopmaskParameters = typing.TypedDict('MriStopmaskParameters', {
    "__STYX_TYPE__": typing.Literal["mri_stopmask"],
    "output_mask": str,
    "filled": list[InputPathType],
    "aseg_presurf": InputPathType,
    "lateral_ventricles": bool,
    "wmsa": typing.NotRequired[float | None],
    "wm_voxels": typing.NotRequired[InputPathType | None],
    "brain_final_surfs": typing.NotRequired[InputPathType | None],
    "no_filled": bool,
    "no_lv": bool,
    "no_wmsa": bool,
    "no_wm": bool,
    "no_bfs": bool,
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
        "mri_stopmask": mri_stopmask_cargs,
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
        "mri_stopmask": mri_stopmask_outputs,
    }.get(t)


class MriStopmaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_stopmask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    generated_mask: OutputPathType
    """The generated stop mask output file"""


def mri_stopmask_params(
    output_mask: str,
    filled: list[InputPathType],
    aseg_presurf: InputPathType,
    lateral_ventricles: bool = False,
    wmsa: float | None = None,
    wm_voxels: InputPathType | None = None,
    brain_final_surfs: InputPathType | None = None,
    no_filled: bool = False,
    no_lv: bool = False,
    no_wmsa: bool = False,
    no_wm: bool = False,
    no_bfs: bool = False,
) -> MriStopmaskParameters:
    """
    Build parameters.
    
    Args:
        output_mask: Output stop mask in volume format.
        filled: Include voxels edited fill voxels that are set in the\
            filled.mgz.
        aseg_presurf: Used with --lv and/or --wmsa; Note: must be\
            aseg.presurf.mgz, not aseg.mgz.
        lateral_ventricles: Add lateral ventricles and choroid plexus to the\
            mask (needs --aseg).
        wmsa: Add WM hypointensities to the mask (needs --aseg); erode by given\
            distance away from any adjacent cortex.
        wm_voxels: Include voxels that =255 from wm.mgz.
        brain_final_surfs: Include voxels that =255 from brain.finalsurfs.mgz.
        no_filled: Turns off --filled option.
        no_lv: Turns off --lv option.
        no_wmsa: Turns off --wmsa option.
        no_wm: Turns off --wm option.
        no_bfs: Turns off --bfs option.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_stopmask",
        "output_mask": output_mask,
        "filled": filled,
        "aseg_presurf": aseg_presurf,
        "lateral_ventricles": lateral_ventricles,
        "no_filled": no_filled,
        "no_lv": no_lv,
        "no_wmsa": no_wmsa,
        "no_wm": no_wm,
        "no_bfs": no_bfs,
    }
    if wmsa is not None:
        params["wmsa"] = wmsa
    if wm_voxels is not None:
        params["wm_voxels"] = wm_voxels
    if brain_final_surfs is not None:
        params["brain_final_surfs"] = brain_final_surfs
    return params


def mri_stopmask_cargs(
    params: MriStopmaskParameters,
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
    cargs.append("mri_stopmask")
    cargs.extend([
        "--o",
        params.get("output_mask")
    ])
    cargs.extend([
        "--filled",
        *[execution.input_file(f) for f in params.get("filled")]
    ])
    cargs.extend([
        "--aseg",
        execution.input_file(params.get("aseg_presurf"))
    ])
    if params.get("lateral_ventricles"):
        cargs.append("--lv")
    if params.get("wmsa") is not None:
        cargs.extend([
            "--wmsa",
            str(params.get("wmsa"))
        ])
    if params.get("wm_voxels") is not None:
        cargs.extend([
            "--wm",
            execution.input_file(params.get("wm_voxels"))
        ])
    if params.get("brain_final_surfs") is not None:
        cargs.extend([
            "--bfs",
            execution.input_file(params.get("brain_final_surfs"))
        ])
    if params.get("no_filled"):
        cargs.append("--no-filled")
    if params.get("no_lv"):
        cargs.append("--no-lv")
    if params.get("no_wmsa"):
        cargs.append("--no-wmsa")
    if params.get("no_wm"):
        cargs.append("--no-wm")
    if params.get("no_bfs"):
        cargs.append("--no-bfs")
    return cargs


def mri_stopmask_outputs(
    params: MriStopmaskParameters,
    execution: Execution,
) -> MriStopmaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriStopmaskOutputs(
        root=execution.output_file("."),
        generated_mask=execution.output_file(params.get("output_mask")),
    )
    return ret


def mri_stopmask_execute(
    params: MriStopmaskParameters,
    execution: Execution,
) -> MriStopmaskOutputs:
    """
    This program creates a mask used to stop the search for the maximum gradient in
    mris_place_surface, preventing the surface from wandering into areas it should
    not.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriStopmaskOutputs`).
    """
    cargs = mri_stopmask_cargs(params, execution)
    ret = mri_stopmask_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_stopmask(
    output_mask: str,
    filled: list[InputPathType],
    aseg_presurf: InputPathType,
    lateral_ventricles: bool = False,
    wmsa: float | None = None,
    wm_voxels: InputPathType | None = None,
    brain_final_surfs: InputPathType | None = None,
    no_filled: bool = False,
    no_lv: bool = False,
    no_wmsa: bool = False,
    no_wm: bool = False,
    no_bfs: bool = False,
    runner: Runner | None = None,
) -> MriStopmaskOutputs:
    """
    This program creates a mask used to stop the search for the maximum gradient in
    mris_place_surface, preventing the surface from wandering into areas it should
    not.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_mask: Output stop mask in volume format.
        filled: Include voxels edited fill voxels that are set in the\
            filled.mgz.
        aseg_presurf: Used with --lv and/or --wmsa; Note: must be\
            aseg.presurf.mgz, not aseg.mgz.
        lateral_ventricles: Add lateral ventricles and choroid plexus to the\
            mask (needs --aseg).
        wmsa: Add WM hypointensities to the mask (needs --aseg); erode by given\
            distance away from any adjacent cortex.
        wm_voxels: Include voxels that =255 from wm.mgz.
        brain_final_surfs: Include voxels that =255 from brain.finalsurfs.mgz.
        no_filled: Turns off --filled option.
        no_lv: Turns off --lv option.
        no_wmsa: Turns off --wmsa option.
        no_wm: Turns off --wm option.
        no_bfs: Turns off --bfs option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriStopmaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_STOPMASK_METADATA)
    params = mri_stopmask_params(output_mask=output_mask, filled=filled, aseg_presurf=aseg_presurf, lateral_ventricles=lateral_ventricles, wmsa=wmsa, wm_voxels=wm_voxels, brain_final_surfs=brain_final_surfs, no_filled=no_filled, no_lv=no_lv, no_wmsa=no_wmsa, no_wm=no_wm, no_bfs=no_bfs)
    return mri_stopmask_execute(params, execution)


__all__ = [
    "MRI_STOPMASK_METADATA",
    "MriStopmaskOutputs",
    "MriStopmaskParameters",
    "mri_stopmask",
    "mri_stopmask_params",
]

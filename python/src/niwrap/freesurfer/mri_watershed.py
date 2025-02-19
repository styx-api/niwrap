# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_WATERSHED_METADATA = Metadata(
    id="1390c3e2e9ad7d6fa430f8cfd5c3863c2de5ce50.boutiques",
    name="mri_watershed",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriWatershedParameters = typing.TypedDict('MriWatershedParameters', {
    "__STYX_TYPE__": typing.Literal["mri_watershed"],
    "input_volume": InputPathType,
    "output_volume": str,
    "weight": typing.NotRequired[float | None],
    "no_wta_flag": bool,
    "proba_merging": typing.NotRequired[float | None],
    "preflooding_height": typing.NotRequired[float | None],
    "no_seedpt_flag": bool,
    "no_ta_flag": bool,
    "copy_flag": bool,
    "atlas_flag": bool,
    "surf_name": typing.NotRequired[str | None],
    "usesurf_ras_flag": bool,
    "no_t1_analysis_flag": bool,
    "shrink_surface_flag": bool,
    "expand_surface_flag": bool,
    "use_watershed_flag": bool,
    "t1_volume": typing.NotRequired[InputPathType | None],
    "wat_temp_flag": bool,
    "first_temp_flag": bool,
    "surf_debug_flag": bool,
    "brain_surf_name": typing.NotRequired[str | None],
    "shrink_brain_surf": typing.NotRequired[str | None],
    "seed_point": typing.NotRequired[list[float] | None],
    "center_brain": typing.NotRequired[list[float] | None],
    "brain_radius": typing.NotRequired[float | None],
    "watershed_threshold": typing.NotRequired[float | None],
    "no_watershed_analysis_flag": bool,
    "label_flag": bool,
    "manual_params": typing.NotRequired[list[float] | None],
    "xthresh": typing.NotRequired[float | None],
    "mask_flag": bool,
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
        "mri_watershed": mri_watershed_cargs,
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
        "mri_watershed": mri_watershed_outputs,
    }.get(t)


class MriWatershedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_watershed(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brain_vol: OutputPathType
    """Skull stripped brain volume"""
    output_brain_surf: OutputPathType | None
    """Saved brain surface when specified"""


def mri_watershed_params(
    input_volume: InputPathType,
    output_volume: str,
    weight: float | None = None,
    no_wta_flag: bool = False,
    proba_merging: float | None = None,
    preflooding_height: float | None = None,
    no_seedpt_flag: bool = False,
    no_ta_flag: bool = False,
    copy_flag: bool = False,
    atlas_flag: bool = False,
    surf_name: str | None = None,
    usesurf_ras_flag: bool = False,
    no_t1_analysis_flag: bool = False,
    shrink_surface_flag: bool = False,
    expand_surface_flag: bool = False,
    use_watershed_flag: bool = False,
    t1_volume: InputPathType | None = None,
    wat_temp_flag: bool = False,
    first_temp_flag: bool = False,
    surf_debug_flag: bool = False,
    brain_surf_name: str | None = None,
    shrink_brain_surf: str | None = None,
    seed_point: list[float] | None = None,
    center_brain: list[float] | None = None,
    brain_radius: float | None = None,
    watershed_threshold: float | None = None,
    no_watershed_analysis_flag: bool = False,
    label_flag: bool = False,
    manual_params: list[float] | None = None,
    xthresh: float | None = None,
    mask_flag: bool = False,
) -> MriWatershedParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume (e.g., T1 volume).
        output_volume: Output volume (e.g., skull stripped brain volume).
        weight: Preweight the input image using atlas information.
        no_wta_flag: Don't use the preweighting for the template deformation.
        proba_merging: Use the basins merging using atlas information.
        preflooding_height: Pre-size the preflooding height (in percent).
        no_seedpt_flag: Don't use seedpoints using atlas information.
        no_ta_flag: Don't use template deformation using atlas information.
        copy_flag: Just copy input to output, ignore other options.
        atlas_flag: Use the atlas information to correct the segmentation.
        surf_name: Save the BEM surfaces; use consistent coordinates with\
            tkmedit.
        usesurf_ras_flag: Use the surface RAS coordinates for surfaces.
        no_t1_analysis_flag: Don't do T1 analysis, useful when running out of\
            memory.
        shrink_surface_flag: Shrink the surface.
        expand_surface_flag: Expand the surface.
        use_watershed_flag: Use only the watershed algorithm.
        t1_volume: Specify T1 input volume.
        wat_temp_flag: Use watershed algorithm and first template smoothing.
        first_temp_flag: Use only the first template smoothing + local matching.
        surf_debug_flag: Visualize the surfaces onto the output volume.
        brain_surf_name: Save the brain surface.
        shrink_brain_surf: Save the brain surface shrank inward by a specified\
            mm.
        seed_point: Add a seed point as a 3D coordinate.
        center_brain: Specify the center of the brain (voxel coordinates).
        brain_radius: Specify the radius of the brain (voxel units).
        watershed_threshold: Change the threshold in the watershed process.
        no_watershed_analysis_flag: Don't use the watershed analysis process.
        label_flag: Labelize the output volume into scalp, skull, csf, gray,\
            and white matter.
        manual_params: Change parameters csf_max, transition intensity, and\
            GM_intensity.
        xthresh: Remove voxels whose intensity exceeds the specified threshold.
        mask_flag: Mask a volume with the brain mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_watershed",
        "input_volume": input_volume,
        "output_volume": output_volume,
        "no_wta_flag": no_wta_flag,
        "no_seedpt_flag": no_seedpt_flag,
        "no_ta_flag": no_ta_flag,
        "copy_flag": copy_flag,
        "atlas_flag": atlas_flag,
        "usesurf_ras_flag": usesurf_ras_flag,
        "no_t1_analysis_flag": no_t1_analysis_flag,
        "shrink_surface_flag": shrink_surface_flag,
        "expand_surface_flag": expand_surface_flag,
        "use_watershed_flag": use_watershed_flag,
        "wat_temp_flag": wat_temp_flag,
        "first_temp_flag": first_temp_flag,
        "surf_debug_flag": surf_debug_flag,
        "no_watershed_analysis_flag": no_watershed_analysis_flag,
        "label_flag": label_flag,
        "mask_flag": mask_flag,
    }
    if weight is not None:
        params["weight"] = weight
    if proba_merging is not None:
        params["proba_merging"] = proba_merging
    if preflooding_height is not None:
        params["preflooding_height"] = preflooding_height
    if surf_name is not None:
        params["surf_name"] = surf_name
    if t1_volume is not None:
        params["t1_volume"] = t1_volume
    if brain_surf_name is not None:
        params["brain_surf_name"] = brain_surf_name
    if shrink_brain_surf is not None:
        params["shrink_brain_surf"] = shrink_brain_surf
    if seed_point is not None:
        params["seed_point"] = seed_point
    if center_brain is not None:
        params["center_brain"] = center_brain
    if brain_radius is not None:
        params["brain_radius"] = brain_radius
    if watershed_threshold is not None:
        params["watershed_threshold"] = watershed_threshold
    if manual_params is not None:
        params["manual_params"] = manual_params
    if xthresh is not None:
        params["xthresh"] = xthresh
    return params


def mri_watershed_cargs(
    params: MriWatershedParameters,
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
    cargs.append("mri_watershed")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(params.get("output_volume"))
    if params.get("weight") is not None:
        cargs.extend([
            "-w",
            str(params.get("weight"))
        ])
    if params.get("no_wta_flag"):
        cargs.append("-no_wta")
    if params.get("proba_merging") is not None:
        cargs.extend([
            "-b",
            str(params.get("proba_merging"))
        ])
    if params.get("preflooding_height") is not None:
        cargs.extend([
            "-h",
            str(params.get("preflooding_height"))
        ])
    if params.get("no_seedpt_flag"):
        cargs.append("-no_seedpt")
    if params.get("no_ta_flag"):
        cargs.append("-no-ta")
    if params.get("copy_flag"):
        cargs.append("-copy")
    if params.get("atlas_flag"):
        cargs.append("-atlas")
    if params.get("surf_name") is not None:
        cargs.extend([
            "-surf",
            params.get("surf_name")
        ])
    if params.get("usesurf_ras_flag"):
        cargs.append("-useSRAS")
    if params.get("no_t1_analysis_flag"):
        cargs.append("-noT1")
    if params.get("shrink_surface_flag"):
        cargs.append("-less")
    if params.get("expand_surface_flag"):
        cargs.append("-more")
    if params.get("use_watershed_flag"):
        cargs.append("-wat")
    if params.get("t1_volume") is not None:
        cargs.extend([
            "-T1",
            execution.input_file(params.get("t1_volume"))
        ])
    if params.get("wat_temp_flag"):
        cargs.append("-wat+temp")
    if params.get("first_temp_flag"):
        cargs.append("-first_temp")
    if params.get("surf_debug_flag"):
        cargs.append("-surf_debug")
    if params.get("brain_surf_name") is not None:
        cargs.extend([
            "-brainsurf",
            params.get("brain_surf_name")
        ])
    if params.get("shrink_brain_surf") is not None:
        cargs.extend([
            "-shk_br_surf",
            params.get("shrink_brain_surf")
        ])
    if params.get("seed_point") is not None:
        cargs.extend([
            "-s",
            *map(str, params.get("seed_point"))
        ])
    if params.get("center_brain") is not None:
        cargs.extend([
            "-c",
            *map(str, params.get("center_brain"))
        ])
    if params.get("brain_radius") is not None:
        cargs.extend([
            "-r",
            str(params.get("brain_radius"))
        ])
    if params.get("watershed_threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("watershed_threshold"))
        ])
    if params.get("no_watershed_analysis_flag"):
        cargs.append("-n")
    if params.get("label_flag"):
        cargs.append("-LABEL")
    if params.get("manual_params") is not None:
        cargs.extend([
            "-man",
            *map(str, params.get("manual_params"))
        ])
    if params.get("xthresh") is not None:
        cargs.extend([
            "-xthresh",
            str(params.get("xthresh"))
        ])
    if params.get("mask_flag"):
        cargs.append("-mask")
    return cargs


def mri_watershed_outputs(
    params: MriWatershedParameters,
    execution: Execution,
) -> MriWatershedOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriWatershedOutputs(
        root=execution.output_file("."),
        output_brain_vol=execution.output_file(params.get("output_volume")),
        output_brain_surf=execution.output_file(params.get("brain_surf_name")) if (params.get("brain_surf_name") is not None) else None,
    )
    return ret


def mri_watershed_execute(
    params: MriWatershedParameters,
    execution: Execution,
) -> MriWatershedOutputs:
    """
    A tool for stripping skull and other non-brain tissues to produce brain volume
    from T1 volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriWatershedOutputs`).
    """
    params = execution.params(params)
    cargs = mri_watershed_cargs(params, execution)
    ret = mri_watershed_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_watershed(
    input_volume: InputPathType,
    output_volume: str,
    weight: float | None = None,
    no_wta_flag: bool = False,
    proba_merging: float | None = None,
    preflooding_height: float | None = None,
    no_seedpt_flag: bool = False,
    no_ta_flag: bool = False,
    copy_flag: bool = False,
    atlas_flag: bool = False,
    surf_name: str | None = None,
    usesurf_ras_flag: bool = False,
    no_t1_analysis_flag: bool = False,
    shrink_surface_flag: bool = False,
    expand_surface_flag: bool = False,
    use_watershed_flag: bool = False,
    t1_volume: InputPathType | None = None,
    wat_temp_flag: bool = False,
    first_temp_flag: bool = False,
    surf_debug_flag: bool = False,
    brain_surf_name: str | None = None,
    shrink_brain_surf: str | None = None,
    seed_point: list[float] | None = None,
    center_brain: list[float] | None = None,
    brain_radius: float | None = None,
    watershed_threshold: float | None = None,
    no_watershed_analysis_flag: bool = False,
    label_flag: bool = False,
    manual_params: list[float] | None = None,
    xthresh: float | None = None,
    mask_flag: bool = False,
    runner: Runner | None = None,
) -> MriWatershedOutputs:
    """
    A tool for stripping skull and other non-brain tissues to produce brain volume
    from T1 volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume (e.g., T1 volume).
        output_volume: Output volume (e.g., skull stripped brain volume).
        weight: Preweight the input image using atlas information.
        no_wta_flag: Don't use the preweighting for the template deformation.
        proba_merging: Use the basins merging using atlas information.
        preflooding_height: Pre-size the preflooding height (in percent).
        no_seedpt_flag: Don't use seedpoints using atlas information.
        no_ta_flag: Don't use template deformation using atlas information.
        copy_flag: Just copy input to output, ignore other options.
        atlas_flag: Use the atlas information to correct the segmentation.
        surf_name: Save the BEM surfaces; use consistent coordinates with\
            tkmedit.
        usesurf_ras_flag: Use the surface RAS coordinates for surfaces.
        no_t1_analysis_flag: Don't do T1 analysis, useful when running out of\
            memory.
        shrink_surface_flag: Shrink the surface.
        expand_surface_flag: Expand the surface.
        use_watershed_flag: Use only the watershed algorithm.
        t1_volume: Specify T1 input volume.
        wat_temp_flag: Use watershed algorithm and first template smoothing.
        first_temp_flag: Use only the first template smoothing + local matching.
        surf_debug_flag: Visualize the surfaces onto the output volume.
        brain_surf_name: Save the brain surface.
        shrink_brain_surf: Save the brain surface shrank inward by a specified\
            mm.
        seed_point: Add a seed point as a 3D coordinate.
        center_brain: Specify the center of the brain (voxel coordinates).
        brain_radius: Specify the radius of the brain (voxel units).
        watershed_threshold: Change the threshold in the watershed process.
        no_watershed_analysis_flag: Don't use the watershed analysis process.
        label_flag: Labelize the output volume into scalp, skull, csf, gray,\
            and white matter.
        manual_params: Change parameters csf_max, transition intensity, and\
            GM_intensity.
        xthresh: Remove voxels whose intensity exceeds the specified threshold.
        mask_flag: Mask a volume with the brain mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriWatershedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_WATERSHED_METADATA)
    params = mri_watershed_params(
        input_volume=input_volume,
        output_volume=output_volume,
        weight=weight,
        no_wta_flag=no_wta_flag,
        proba_merging=proba_merging,
        preflooding_height=preflooding_height,
        no_seedpt_flag=no_seedpt_flag,
        no_ta_flag=no_ta_flag,
        copy_flag=copy_flag,
        atlas_flag=atlas_flag,
        surf_name=surf_name,
        usesurf_ras_flag=usesurf_ras_flag,
        no_t1_analysis_flag=no_t1_analysis_flag,
        shrink_surface_flag=shrink_surface_flag,
        expand_surface_flag=expand_surface_flag,
        use_watershed_flag=use_watershed_flag,
        t1_volume=t1_volume,
        wat_temp_flag=wat_temp_flag,
        first_temp_flag=first_temp_flag,
        surf_debug_flag=surf_debug_flag,
        brain_surf_name=brain_surf_name,
        shrink_brain_surf=shrink_brain_surf,
        seed_point=seed_point,
        center_brain=center_brain,
        brain_radius=brain_radius,
        watershed_threshold=watershed_threshold,
        no_watershed_analysis_flag=no_watershed_analysis_flag,
        label_flag=label_flag,
        manual_params=manual_params,
        xthresh=xthresh,
        mask_flag=mask_flag,
    )
    return mri_watershed_execute(params, execution)


__all__ = [
    "MRI_WATERSHED_METADATA",
    "MriWatershedOutputs",
    "MriWatershedParameters",
    "mri_watershed",
    "mri_watershed_params",
]

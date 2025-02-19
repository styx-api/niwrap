# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SURF2VOL_METADATA = Metadata(
    id="750ed03dd5a1fd4b3541f1778bd76f62c8dcfbba.boutiques",
    name="mri_surf2vol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriSurf2volParameters = typing.TypedDict('MriSurf2volParameters', {
    "__STYX_TYPE__": typing.Literal["mri_surf2vol"],
    "surface_overlay": typing.NotRequired[list[str] | None],
    "ltafile": typing.NotRequired[InputPathType | None],
    "outfile": str,
    "subject": typing.NotRequired[str | None],
    "ribbonfile": typing.NotRequired[InputPathType | None],
    "merge_volume": typing.NotRequired[InputPathType | None],
    "surface_values": typing.NotRequired[str | None],
    "mkmask": bool,
    "hemi": typing.NotRequired[str | None],
    "surfname": typing.NotRequired[str | None],
    "projfrac": typing.NotRequired[float | None],
    "fill_ribbon": bool,
    "fill_projfrac": typing.NotRequired[str | None],
    "reg_volume": typing.NotRequired[InputPathType | None],
    "identity": typing.NotRequired[str | None],
    "template_volume": typing.NotRequired[InputPathType | None],
    "fstal_res": typing.NotRequired[str | None],
    "vtxvol": typing.NotRequired[InputPathType | None],
    "flat2mri": typing.NotRequired[str | None],
    "sphpvf": typing.NotRequired[str | None],
    "mask_to_cortex": bool,
    "mask_to_label": typing.NotRequired[InputPathType | None],
    "surface_mask": typing.NotRequired[InputPathType | None],
    "add_const": typing.NotRequired[float | None],
    "copy_ctab": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "gdiagno": typing.NotRequired[int | None],
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
        "mri_surf2vol": mri_surf2vol_cargs,
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
        "mri_surf2vol": mri_surf2vol_outputs,
    }.get(t)


class MriSurf2volOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_surf2vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Output volume with resampled surface"""
    vertex_volume: OutputPathType | None
    """Vertex map volume indicating mapped voxels"""


def mri_surf2vol_params(
    outfile: str,
    surface_overlay: list[str] | None = None,
    ltafile: InputPathType | None = None,
    subject: str | None = None,
    ribbonfile: InputPathType | None = None,
    merge_volume: InputPathType | None = None,
    surface_values: str | None = None,
    mkmask: bool = False,
    hemi: str | None = None,
    surfname: str | None = None,
    projfrac: float | None = None,
    fill_ribbon: bool = False,
    fill_projfrac: str | None = None,
    reg_volume: InputPathType | None = None,
    identity: str | None = None,
    template_volume: InputPathType | None = None,
    fstal_res: str | None = None,
    vtxvol: InputPathType | None = None,
    flat2mri: str | None = None,
    sphpvf: str | None = None,
    mask_to_cortex: bool = False,
    mask_to_label: InputPathType | None = None,
    surface_mask: InputPathType | None = None,
    add_const: float | None = None,
    copy_ctab: bool = False,
    subjects_dir: str | None = None,
    gdiagno: int | None = None,
    version: bool = False,
    help_: bool = False,
) -> MriSurf2volParameters:
    """
    Build parameters.
    
    Args:
        outfile: Path to output volume.
        surface_overlay: Specify path to a surface and matching overlay.
        ltafile: Specify registration file.
        subject: Specify subject name.
        ribbonfile: Specify path to ribbon file.
        merge_volume: Merge with this volume, replacing surface values.
        surface_values: Source of surface values, optionally with format.
        mkmask: Create a binary mask instead of loading surfval.
        hemi: Hemisphere for the surface values (lh or rh).
        surfname: Surface name in surf directory (default is white).
        projfrac: Fraction for thickness projection.
        fill_ribbon: Fill the entire ribbon.
        fill_projfrac: Fill ribbon by iterating projfrac.
        reg_volume: Volume registration file.
        identity: Use identity matrix for volume registration (requires subject\
            name).
        template_volume: Template volume for output configuration.
        fstal_res: Use fs Talairach registration with specified resolution.
        vtxvol: Vertex map volume path.
        flat2mri: Options for flat surface to MRI mapping.
        sphpvf: Spherical point to voxel function options.
        mask_to_cortex: Mask to cortex label.
        mask_to_label: Mask to specified label file.
        surface_mask: Mask to specified surface mask.
        add_const: Add constant value to each non-zero output voxel.
        copy_ctab: Copy color table header.
        subjects_dir: FreeSurfer subjects directory.
        gdiagno: Set diagnostic level.
        version: Print version and exit.
        help_: Display help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_surf2vol",
        "outfile": outfile,
        "mkmask": mkmask,
        "fill_ribbon": fill_ribbon,
        "mask_to_cortex": mask_to_cortex,
        "copy_ctab": copy_ctab,
        "version": version,
        "help": help_,
    }
    if surface_overlay is not None:
        params["surface_overlay"] = surface_overlay
    if ltafile is not None:
        params["ltafile"] = ltafile
    if subject is not None:
        params["subject"] = subject
    if ribbonfile is not None:
        params["ribbonfile"] = ribbonfile
    if merge_volume is not None:
        params["merge_volume"] = merge_volume
    if surface_values is not None:
        params["surface_values"] = surface_values
    if hemi is not None:
        params["hemi"] = hemi
    if surfname is not None:
        params["surfname"] = surfname
    if projfrac is not None:
        params["projfrac"] = projfrac
    if fill_projfrac is not None:
        params["fill_projfrac"] = fill_projfrac
    if reg_volume is not None:
        params["reg_volume"] = reg_volume
    if identity is not None:
        params["identity"] = identity
    if template_volume is not None:
        params["template_volume"] = template_volume
    if fstal_res is not None:
        params["fstal_res"] = fstal_res
    if vtxvol is not None:
        params["vtxvol"] = vtxvol
    if flat2mri is not None:
        params["flat2mri"] = flat2mri
    if sphpvf is not None:
        params["sphpvf"] = sphpvf
    if mask_to_label is not None:
        params["mask_to_label"] = mask_to_label
    if surface_mask is not None:
        params["surface_mask"] = surface_mask
    if add_const is not None:
        params["add_const"] = add_const
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if gdiagno is not None:
        params["gdiagno"] = gdiagno
    return params


def mri_surf2vol_cargs(
    params: MriSurf2volParameters,
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
    cargs.append("mri_surf2vol")
    if params.get("surface_overlay") is not None:
        cargs.extend([
            "--so",
            *params.get("surface_overlay")
        ])
    if params.get("ltafile") is not None:
        cargs.extend([
            "--lta",
            execution.input_file(params.get("ltafile"))
        ])
    cargs.extend([
        "--o",
        params.get("outfile")
    ])
    if params.get("subject") is not None:
        cargs.extend([
            "--subject",
            params.get("subject")
        ])
    if params.get("ribbonfile") is not None:
        cargs.extend([
            "--ribbon",
            execution.input_file(params.get("ribbonfile"))
        ])
    if params.get("merge_volume") is not None:
        cargs.extend([
            "--merge",
            execution.input_file(params.get("merge_volume"))
        ])
    if params.get("surface_values") is not None:
        cargs.extend([
            "--surfval",
            params.get("surface_values")
        ])
    if params.get("mkmask"):
        cargs.append("--mkmask")
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("surfname") is not None:
        cargs.extend([
            "--surf",
            params.get("surfname")
        ])
    if params.get("projfrac") is not None:
        cargs.extend([
            "--projfrac",
            str(params.get("projfrac"))
        ])
    if params.get("fill_ribbon"):
        cargs.append("--fillribbon")
    if params.get("fill_projfrac") is not None:
        cargs.extend([
            "--fill-projfrac",
            params.get("fill_projfrac")
        ])
    if params.get("reg_volume") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("reg_volume"))
        ])
    if params.get("identity") is not None:
        cargs.extend([
            "--identity",
            params.get("identity")
        ])
    if params.get("template_volume") is not None:
        cargs.extend([
            "--template",
            execution.input_file(params.get("template_volume"))
        ])
    if params.get("fstal_res") is not None:
        cargs.extend([
            "--fstal",
            params.get("fstal_res")
        ])
    if params.get("vtxvol") is not None:
        cargs.extend([
            "--vtxvol",
            execution.input_file(params.get("vtxvol"))
        ])
    if params.get("flat2mri") is not None:
        cargs.extend([
            "--flat2mri",
            params.get("flat2mri")
        ])
    if params.get("sphpvf") is not None:
        cargs.extend([
            "--sphpvf",
            params.get("sphpvf")
        ])
    if params.get("mask_to_cortex"):
        cargs.append("--mask-to-cortex")
    if params.get("mask_to_label") is not None:
        cargs.extend([
            "--mask-to-label",
            execution.input_file(params.get("mask_to_label"))
        ])
    if params.get("surface_mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("surface_mask"))
        ])
    if params.get("add_const") is not None:
        cargs.extend([
            "--add",
            str(params.get("add_const"))
        ])
    if params.get("copy_ctab"):
        cargs.append("--copy-ctab")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("gdiagno") is not None:
        cargs.extend([
            "--gdiagno",
            str(params.get("gdiagno"))
        ])
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mri_surf2vol_outputs(
    params: MriSurf2volParameters,
    execution: Execution,
) -> MriSurf2volOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSurf2volOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("outfile")),
        vertex_volume=execution.output_file(pathlib.Path(params.get("vtxvol")).name) if (params.get("vtxvol") is not None) else None,
    )
    return ret


def mri_surf2vol_execute(
    params: MriSurf2volParameters,
    execution: Execution,
) -> MriSurf2volOutputs:
    """
    Resamples a surface into a volume using one of two methods.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSurf2volOutputs`).
    """
    params = execution.params(params)
    cargs = mri_surf2vol_cargs(params, execution)
    ret = mri_surf2vol_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_surf2vol(
    outfile: str,
    surface_overlay: list[str] | None = None,
    ltafile: InputPathType | None = None,
    subject: str | None = None,
    ribbonfile: InputPathType | None = None,
    merge_volume: InputPathType | None = None,
    surface_values: str | None = None,
    mkmask: bool = False,
    hemi: str | None = None,
    surfname: str | None = None,
    projfrac: float | None = None,
    fill_ribbon: bool = False,
    fill_projfrac: str | None = None,
    reg_volume: InputPathType | None = None,
    identity: str | None = None,
    template_volume: InputPathType | None = None,
    fstal_res: str | None = None,
    vtxvol: InputPathType | None = None,
    flat2mri: str | None = None,
    sphpvf: str | None = None,
    mask_to_cortex: bool = False,
    mask_to_label: InputPathType | None = None,
    surface_mask: InputPathType | None = None,
    add_const: float | None = None,
    copy_ctab: bool = False,
    subjects_dir: str | None = None,
    gdiagno: int | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriSurf2volOutputs:
    """
    Resamples a surface into a volume using one of two methods.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outfile: Path to output volume.
        surface_overlay: Specify path to a surface and matching overlay.
        ltafile: Specify registration file.
        subject: Specify subject name.
        ribbonfile: Specify path to ribbon file.
        merge_volume: Merge with this volume, replacing surface values.
        surface_values: Source of surface values, optionally with format.
        mkmask: Create a binary mask instead of loading surfval.
        hemi: Hemisphere for the surface values (lh or rh).
        surfname: Surface name in surf directory (default is white).
        projfrac: Fraction for thickness projection.
        fill_ribbon: Fill the entire ribbon.
        fill_projfrac: Fill ribbon by iterating projfrac.
        reg_volume: Volume registration file.
        identity: Use identity matrix for volume registration (requires subject\
            name).
        template_volume: Template volume for output configuration.
        fstal_res: Use fs Talairach registration with specified resolution.
        vtxvol: Vertex map volume path.
        flat2mri: Options for flat surface to MRI mapping.
        sphpvf: Spherical point to voxel function options.
        mask_to_cortex: Mask to cortex label.
        mask_to_label: Mask to specified label file.
        surface_mask: Mask to specified surface mask.
        add_const: Add constant value to each non-zero output voxel.
        copy_ctab: Copy color table header.
        subjects_dir: FreeSurfer subjects directory.
        gdiagno: Set diagnostic level.
        version: Print version and exit.
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSurf2volOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SURF2VOL_METADATA)
    params = mri_surf2vol_params(
        surface_overlay=surface_overlay,
        ltafile=ltafile,
        outfile=outfile,
        subject=subject,
        ribbonfile=ribbonfile,
        merge_volume=merge_volume,
        surface_values=surface_values,
        mkmask=mkmask,
        hemi=hemi,
        surfname=surfname,
        projfrac=projfrac,
        fill_ribbon=fill_ribbon,
        fill_projfrac=fill_projfrac,
        reg_volume=reg_volume,
        identity=identity,
        template_volume=template_volume,
        fstal_res=fstal_res,
        vtxvol=vtxvol,
        flat2mri=flat2mri,
        sphpvf=sphpvf,
        mask_to_cortex=mask_to_cortex,
        mask_to_label=mask_to_label,
        surface_mask=surface_mask,
        add_const=add_const,
        copy_ctab=copy_ctab,
        subjects_dir=subjects_dir,
        gdiagno=gdiagno,
        version=version,
        help_=help_,
    )
    return mri_surf2vol_execute(params, execution)


__all__ = [
    "MRI_SURF2VOL_METADATA",
    "MriSurf2volOutputs",
    "MriSurf2volParameters",
    "mri_surf2vol",
    "mri_surf2vol_params",
]

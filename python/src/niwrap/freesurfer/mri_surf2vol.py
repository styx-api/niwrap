# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SURF2VOL_METADATA = Metadata(
    id="b536f4224339f33b063ca9bc15eb59e4bb464334.boutiques",
    name="mri_surf2vol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


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
    cargs = []
    cargs.append("mri_surf2vol")
    if surface_overlay is not None:
        cargs.extend([
            "--so",
            *surface_overlay
        ])
    if ltafile is not None:
        cargs.extend([
            "--lta",
            execution.input_file(ltafile)
        ])
    cargs.extend([
        "--o",
        outfile
    ])
    if subject is not None:
        cargs.extend([
            "--subject",
            subject
        ])
    if ribbonfile is not None:
        cargs.extend([
            "--ribbon",
            execution.input_file(ribbonfile)
        ])
    if merge_volume is not None:
        cargs.extend([
            "--merge",
            execution.input_file(merge_volume)
        ])
    if surface_values is not None:
        cargs.extend([
            "--surfval",
            surface_values
        ])
    if mkmask:
        cargs.append("--mkmask")
    if hemi is not None:
        cargs.extend([
            "--hemi",
            hemi
        ])
    if surfname is not None:
        cargs.extend([
            "--surf",
            surfname
        ])
    if projfrac is not None:
        cargs.extend([
            "--projfrac",
            str(projfrac)
        ])
    if fill_ribbon:
        cargs.append("--fillribbon")
    if fill_projfrac is not None:
        cargs.extend([
            "--fill-projfrac",
            fill_projfrac
        ])
    if reg_volume is not None:
        cargs.extend([
            "--reg",
            execution.input_file(reg_volume)
        ])
    if identity is not None:
        cargs.extend([
            "--identity",
            identity
        ])
    if template_volume is not None:
        cargs.extend([
            "--template",
            execution.input_file(template_volume)
        ])
    if fstal_res is not None:
        cargs.extend([
            "--fstal",
            fstal_res
        ])
    if vtxvol is not None:
        cargs.extend([
            "--vtxvol",
            execution.input_file(vtxvol)
        ])
    if flat2mri is not None:
        cargs.extend([
            "--flat2mri",
            flat2mri
        ])
    if sphpvf is not None:
        cargs.extend([
            "--sphpvf",
            sphpvf
        ])
    if mask_to_cortex:
        cargs.append("--mask-to-cortex")
    if mask_to_label is not None:
        cargs.extend([
            "--mask-to-label",
            execution.input_file(mask_to_label)
        ])
    if surface_mask is not None:
        cargs.extend([
            "--mask",
            execution.input_file(surface_mask)
        ])
    if add_const is not None:
        cargs.extend([
            "--add",
            str(add_const)
        ])
    if copy_ctab:
        cargs.append("--copy-ctab")
    if subjects_dir is not None:
        cargs.extend([
            "--sd",
            subjects_dir
        ])
    if gdiagno is not None:
        cargs.extend([
            "--gdiagno",
            str(gdiagno)
        ])
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = MriSurf2volOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(outfile),
        vertex_volume=execution.output_file(pathlib.Path(vtxvol).name) if (vtxvol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SURF2VOL_METADATA",
    "MriSurf2volOutputs",
    "mri_surf2vol",
]

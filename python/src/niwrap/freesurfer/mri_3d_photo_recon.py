# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_3D_PHOTO_RECON_METADATA = Metadata(
    id="758a1a093fab9575ca102e598e24939fc9ecf832.boutiques",
    name="mri_3d_photo_recon",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Mri3dPhotoReconOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_3d_photo_recon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reconstructed_volume: OutputPathType
    """Reconstructed photo volume output file"""
    reference_data: OutputPathType
    """Output reference data"""


def mri_3d_photo_recon(
    input_photo_dir: list[InputPathType],
    input_segmentation_dir: list[InputPathType],
    slice_thickness: float,
    photo_resolution: float,
    output_directory: str,
    ref_mask: InputPathType | None = None,
    ref_surface: InputPathType | None = None,
    ref_soft_mask: InputPathType | None = None,
    mesh_reorient_with_indices: str | None = None,
    photos_posterior_side: bool = False,
    order_posterior_to_anterior: bool = False,
    allow_z_stretch: bool = False,
    rigid_only_for_photos: bool = False,
    gpu_index: float | None = None,
    runner: Runner | None = None,
) -> Mri3dPhotoReconOutputs:
    """
    Code for 3D photo reconstruction (Tregidgo, et al., MICCAI 2020).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_photo_dir: Directory with input photos (required).
        input_segmentation_dir: Directory with input slab masks / segmentations\
            (required).
        slice_thickness: Slice thickness in mm.
        photo_resolution: Resolution of the photos in mm.
        output_directory: Output directory with reconstructed photo volume and\
            reference.
        ref_mask: Reference binary mask.
        ref_surface: Reference surface file.
        ref_soft_mask: Reference soft mask.
        mesh_reorient_with_indices: Vertex indices of frontal pole, occipital\
            pole, and top of central sulcus, separated with commas, for mesh\
            alignment.
        photos_posterior_side: Use when photos are taken of posterior side of\
            slabs (default is anterior side).
        order_posterior_to_anterior: Use when photos are ordered from posterior\
            to anterior (default is anterior to posterior).
        allow_z_stretch: Use to adjust the slice thickness to best match the\
            reference. You should probably *never* use this with soft references\
            (ref_soft_mask).
        rigid_only_for_photos: Switch on if you want photos to deform only\
            rigidly (not affine).
        gpu_index: Index of GPU to use.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Mri3dPhotoReconOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_3D_PHOTO_RECON_METADATA)
    cargs = []
    cargs.append("mri_3d_photo_recon")
    cargs.extend([
        "--input_photo_dir",
        *[execution.input_file(f) for f in input_photo_dir]
    ])
    cargs.extend([
        "--input_segmentation_dir",
        *[execution.input_file(f) for f in input_segmentation_dir]
    ])
    cargs.extend([
        "--slice_thickness",
        str(slice_thickness)
    ])
    cargs.extend([
        "--photo_resolution",
        str(photo_resolution)
    ])
    cargs.extend([
        "--output_directory",
        output_directory
    ])
    if ref_mask is not None:
        cargs.extend([
            "--ref_mask",
            execution.input_file(ref_mask)
        ])
    if ref_surface is not None:
        cargs.extend([
            "--ref_surface",
            execution.input_file(ref_surface)
        ])
    if ref_soft_mask is not None:
        cargs.extend([
            "--ref_soft_mask",
            execution.input_file(ref_soft_mask)
        ])
    if mesh_reorient_with_indices is not None:
        cargs.extend([
            "--mesh_reorient_with_indices",
            mesh_reorient_with_indices
        ])
    if photos_posterior_side:
        cargs.append("--photos_of_posterior_side")
    if order_posterior_to_anterior:
        cargs.append("--order_posterior_to_anterior")
    if allow_z_stretch:
        cargs.append("--allow_z_stretch")
    if rigid_only_for_photos:
        cargs.append("--rigid_only_for_photos")
    if gpu_index is not None:
        cargs.extend([
            "--gpu",
            str(gpu_index)
        ])
    ret = Mri3dPhotoReconOutputs(
        root=execution.output_file("."),
        reconstructed_volume=execution.output_file(output_directory + "/reconstructed_volume.nii.gz"),
        reference_data=execution.output_file(output_directory + "/reference_data.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_3D_PHOTO_RECON_METADATA",
    "Mri3dPhotoReconOutputs",
    "mri_3d_photo_recon",
]

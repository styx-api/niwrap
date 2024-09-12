# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__MEASURE_EROSION_THICK_METADATA = Metadata(
    id="b6a8c4aa07127613bf960024c046b21cc74c0f1f.boutiques",
    name="@measure_erosion_thick",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VMeasureErosionThickOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__measure_erosion_thick(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    erosion_depth: OutputPathType
    """Depth dataset."""
    erosion_thick: OutputPathType
    """Volumetric thickness dataset."""
    erosion_thick_smooth: OutputPathType
    """Smoothed volumetric thickness dataset."""
    erosion_thick_niml: OutputPathType
    """Unsmoothed thickness mapped to surface nodes."""
    erosion_thick_smooth_niml: OutputPathType
    """Smoothed thickness mapped to surface nodes."""
    maskset_output: OutputPathType
    """Mask dataset."""
    resampled_maskset: OutputPathType
    """Resampled mask dataset."""
    anat_gii: OutputPathType
    """Surface representation of mask volume."""
    quick_spec: OutputPathType
    """Simple specification file for surface to use with suma commands."""


def v__measure_erosion_thick(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
    resample: str | None = None,
    surfsmooth: float | None = None,
    smoothmm: float | None = None,
    maxthick: float | None = None,
    depthsearch: float | None = None,
    keep_temp_files: bool = False,
    surfsmooth_method: str | None = None,
    runner: Runner | None = None,
) -> VMeasureErosionThickOutputs:
    """
    Compute thickness of mask using erosion method.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@measure_erosion_thick.html
    
    Args:
        maskset: Mask dataset for input.
        surfset: Surface dataset onto which to map thickness (probably a\
            pial/gray matter surface).
        outdir: Output directory. If not specified, erosion_thickdir is used.
        resample: Resample input to mm in millimeters (put a number here).\
            Recommended for most 1mm data.
        surfsmooth: Smooth surface map of thickness by mm millimeters. Default\
            is 8 mm.
        smoothmm: Smooth volume by mm FWHM in mask. Default is 2*voxelsize of\
            mask or resampled mask.
        maxthick: Search for maximum thickness value of mm millimeters. Default\
            is 6 mm.
        depthsearch: Map to surface by looking for max along mm millimeter\
            normal vectors. Default is 3 mm.
        keep_temp_files: Do not delete the intermediate files (for testing).
        surfsmooth_method: Heat method used for smoothing surfaces. Default is\
            HEAT_07 but HEAT_05 is also useful for models.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMeasureErosionThickOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MEASURE_EROSION_THICK_METADATA)
    cargs = []
    cargs.append("@measure_erosion_thick")
    cargs.append("-maskset")
    cargs.append(execution.input_file(maskset))
    cargs.append("-surfset")
    cargs.append(execution.input_file(surfset))
    cargs.append("-outdir")
    if outdir is not None:
        cargs.append(outdir)
    if resample is not None:
        cargs.extend([
            "-resample",
            resample
        ])
    if surfsmooth is not None:
        cargs.extend([
            "-surfsmooth",
            str(surfsmooth)
        ])
    if smoothmm is not None:
        cargs.extend([
            "-smoothmm",
            str(smoothmm)
        ])
    if maxthick is not None:
        cargs.extend([
            "-maxthick",
            str(maxthick)
        ])
    if depthsearch is not None:
        cargs.extend([
            "-depthsearch",
            str(depthsearch)
        ])
    if keep_temp_files:
        cargs.append("-keep_temp_files")
    if surfsmooth_method is not None:
        cargs.extend([
            "-surfsmooth_method",
            surfsmooth_method
        ])
    ret = VMeasureErosionThickOutputs(
        root=execution.output_file("."),
        erosion_depth=execution.output_file("erosion_depth.nii.gz"),
        erosion_thick=execution.output_file("erosion_thick.nii.gz"),
        erosion_thick_smooth=execution.output_file("erosion_thick_smooth.nii.gz"),
        erosion_thick_niml=execution.output_file("erosion_thick.niml.dset"),
        erosion_thick_smooth_niml=execution.output_file("erosion_thick_smooth_nn_mm.niml.dset"),
        maskset_output=execution.output_file("maskset.nii.gz"),
        resampled_maskset=execution.output_file("maskset_rs.nii.gz"),
        anat_gii=execution.output_file("anat.gii"),
        quick_spec=execution.output_file("quick.spec"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VMeasureErosionThickOutputs",
    "V__MEASURE_EROSION_THICK_METADATA",
    "v__measure_erosion_thick",
]

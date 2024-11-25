# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BIANCA_METADATA = Metadata(
    id="faece12893f9764ba2ed673c9b5a6791f2ed9a43.boutiques",
    name="bianca",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class BiancaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bianca(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    base_output: OutputPathType | None
    """Base output file generated by BIANCA"""


def bianca(
    master_file: InputPathType,
    label_feature_num: float,
    brain_mask_feature_num: float,
    query_subject_num: float,
    feature_subset: str | None = None,
    mat_feature_num: float | None = None,
    spatial_weight: float | None = 1,
    patch_sizes: str | None = None,
    patch_3d: bool = False,
    select_pts: str | None = "any",
    training_pts: str | None = None,
    non_les_pts: str | None = None,
    save_classifier_data: str | None = None,
    verbose_flag: bool = False,
    out_name: str | None = "output_bianca",
    runner: Runner | None = None,
) -> BiancaOutputs:
    """
    BIANCA: Brain Intensity AbNormality Classification Algorithm.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        master_file: Name of the master file.
        label_feature_num: Column number (in the master file) of the manual\
            masks (or any placeholder name for query subjects).
        brain_mask_feature_num: Column number (in the master file) of images to\
            derive non-zero mask from.
        query_subject_num: Row number of query subject (in masterlistfile).
        feature_subset: Set of column numbers (comma separated and no spaces)\
            for features/images to use (default: use all available modalities as\
            intensity features). The image used to derive non-zero mask from must\
            be part of the features subset.
        mat_feature_num: Column number of matrix files (in masterlistfile).\
            Needed to extract spatial features (MNI coordinates).
        spatial_weight: Weighting for spatial coordinates (default = 1, i.e.,\
            variance-normalized MNI coordinates). Requires --matfeaturenum to be\
            specified.
        patch_sizes: List of patch sizes for local averaging.
        patch_3d: Use 3D patches (default is 2D).
        select_pts: "any" (default) or "surround" or "noborder".
        training_pts: Number (max) of (lesion) points to use (per training\
            subject) or "equalpoints" to select all lesion points and equal number\
            of non-lesion points.
        non_les_pts: Number (max) of non-lesion points to use. If not specified\
            will be set to the same amount of lesion points.
        save_classifier_data: Save training data to file.
        verbose_flag: Use verbose mode.
        out_name: Specify (base) output name of files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BiancaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BIANCA_METADATA)
    cargs = []
    cargs.append("bianca")
    cargs.append("--singlefile=" + execution.input_file(master_file))
    cargs.append("--labelfeaturenum=" + str(label_feature_num))
    cargs.append("--brainmaskfeaturenum=" + str(brain_mask_feature_num))
    cargs.append("--querysubjectnum=" + str(query_subject_num))
    if feature_subset is not None:
        cargs.extend([
            "--featuresubset",
            feature_subset
        ])
    if mat_feature_num is not None:
        cargs.extend([
            "--matfeaturenum",
            str(mat_feature_num)
        ])
    if spatial_weight is not None:
        cargs.extend([
            "--spatialweight",
            str(spatial_weight)
        ])
    if patch_sizes is not None:
        cargs.extend([
            "--patchsizes",
            patch_sizes
        ])
    if patch_3d:
        cargs.append("--patch3D")
    if select_pts is not None:
        cargs.extend([
            "--selectpts",
            select_pts
        ])
    if training_pts is not None:
        cargs.extend([
            "--trainingpts",
            training_pts
        ])
    if non_les_pts is not None:
        cargs.extend([
            "--nonlespts",
            non_les_pts
        ])
    if save_classifier_data is not None:
        cargs.extend([
            "--saveclassifierdata",
            save_classifier_data
        ])
    if verbose_flag:
        cargs.append("-v")
    if out_name is not None:
        cargs.extend([
            "-o",
            out_name
        ])
    ret = BiancaOutputs(
        root=execution.output_file("."),
        base_output=execution.output_file(out_name + "_bianca") if (out_name is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BIANCA_METADATA",
    "BiancaOutputs",
    "bianca",
]

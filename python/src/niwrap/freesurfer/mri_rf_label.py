# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RF_LABEL_METADATA = Metadata(
    id="99758d7616ca4f61f65200c8a30bd05f887b17bb.boutiques",
    name="mri_rf_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRfLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rf_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outvol: OutputPathType
    """Output volume from mri_ca_label"""


def mri_rf_label(
    input_volumes: list[InputPathType],
    transform_file: InputPathType,
    gcafile: InputPathType,
    output_volume: str,
    cross_sequence_flag: bool = False,
    nogibbs_flag: bool = False,
    wm_path: InputPathType | None = None,
    conform_flag: bool = False,
    normpd_flag: bool = False,
    debug_voxel: list[float] | None = None,
    debug_node: list[float] | None = None,
    debug_label: float | None = None,
    tr: float | None = None,
    te: float | None = None,
    alpha: float | None = None,
    example: list[InputPathType] | None = None,
    pthresh: float | None = 0.7,
    niter: float | None = 2,
    novar_flag: bool = False,
    regularize: float | None = None,
    nohippo_flag: bool = False,
    fwm: InputPathType | None = None,
    mri_vol: InputPathType | None = None,
    heq: InputPathType | None = None,
    renorm: InputPathType | None = None,
    flash_flag: bool = False,
    flash_params: InputPathType | None = None,
    renormalize: list[float] | None = None,
    set_input: InputPathType | None = None,
    histogram_flag: bool = False,
    cond_density_mean: float | None = None,
    snapshots: list[str] | None = None,
    mask: InputPathType | None = None,
    expand: float | None = None,
    max_iter: float | None = 200,
    filter_mode: list[float] | None = [0, 0.5],
    longitudinal_vol: InputPathType | None = None,
    longitudinal_lta: InputPathType | None = None,
    relabel_unlikely_flag: list[float] | None = None,
    runner: Runner | None = None,
) -> MriRfLabelOutputs:
    """
    MRI automatic tissue labeling using a Gaussian Classifier Atlas (GCA).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volumes: Input volume(s).
        transform_file: Transform file.
        gcafile: GCA file.
        output_volume: Output volume.
        cross_sequence_flag: Label a volume acquired with a sequence different\
            than atlas.
        nogibbs_flag: Disable gibbs priors.
        wm_path: Use WM segmentation from provided file.
        conform_flag: Interpolate volume to be isotropic 1mm^3.
        normpd_flag: Normalize PD image to GCA means.
        debug_voxel: Debug voxel at specified coordinates.
        debug_node: Debug node at specified coordinates.
        debug_label: Debug label at specified index.
        tr: Set TR in msec.
        te: Set TE in msec.
        alpha: Set alpha in radians.
        example: Use T1 (mri_vol) and segmentation as example.
        pthresh: Use p threshold for adaptive renormalization.
        niter: Apply max likelihood for n iterations.
        novar_flag: Do not use variance in classification.
        regularize: Regularize variance to be sigma+nC(noise).
        nohippo_flag: Do not auto-edit hippocampus.
        fwm: Use fixed white matter segmentation from wm.
        mri_vol: Write most likely MR volume to specified file.
        heq: Use histogram equalization from specified volume.
        renorm: Renormalize using predicted intensity values.
        flash_flag: Use FLASH forward model to predict intensity values.
        flash_params: Use FLASH forward model and tissue params from file.
        renormalize: Renorm class means iter times after initial label with\
            window of wsize.
        set_input: Set input volume.
        histogram_flag: Use GCA to histogram normalize input image.
        cond_density_mean: Mean filter n times to conditional densities.
        snapshots: Write snapshots of gibbs process every n times to filename.
        mask: Use mri_vol to mask final labeling.
        expand: Expand.
        max_iter: Set max iterations.
        filter_mode: Filter labeled volume with threshold t mode filter f times.
        longitudinal_vol: Longitudinal processing: mri_vol is label from tp1,\
            LTA is registration from tp1 to current data.
        longitudinal_lta: Longitudinal LTA registration.
        relabel_unlikely_flag: Reclassify voxels using a Gaussian window to\
            recomute priors and likelihoods.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRfLabelOutputs`).
    """
    if snapshots is not None and (len(snapshots) != 2): 
        raise ValueError(f"Length of 'snapshots' must be 2 but was {len(snapshots)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RF_LABEL_METADATA)
    cargs = []
    cargs.append("mri_ca_label")
    cargs.extend([execution.input_file(f) for f in input_volumes])
    cargs.append(execution.input_file(transform_file))
    cargs.append(execution.input_file(gcafile))
    cargs.append(output_volume)
    if cross_sequence_flag:
        cargs.append("-cross-sequence")
    if nogibbs_flag:
        cargs.append("-nogibbs")
    if wm_path is not None:
        cargs.extend([
            "-wm",
            execution.input_file(wm_path)
        ])
    if conform_flag:
        cargs.append("-conform")
    if normpd_flag:
        cargs.append("-normpd")
    cargs.append("[GLA_TL]")
    if debug_voxel is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, debug_voxel)
        ])
    if debug_node is not None:
        cargs.extend([
            "-debug_node",
            *map(str, debug_node)
        ])
    if debug_label is not None:
        cargs.extend([
            "-debug_label",
            str(debug_label)
        ])
    if tr is not None:
        cargs.extend([
            "-tr",
            str(tr)
        ])
    if te is not None:
        cargs.extend([
            "-te",
            str(te)
        ])
    if alpha is not None:
        cargs.extend([
            "-alpha",
            str(alpha)
        ])
    if example is not None:
        cargs.extend([
            "-example",
            *[execution.input_file(f) for f in example]
        ])
    if pthresh is not None:
        cargs.extend([
            "-pthresh",
            str(pthresh)
        ])
    if niter is not None:
        cargs.extend([
            "-niter",
            str(niter)
        ])
    if novar_flag:
        cargs.append("-novar")
    if regularize is not None:
        cargs.extend([
            "-regularize",
            str(regularize)
        ])
    if nohippo_flag:
        cargs.append("-nohippo")
    if fwm is not None:
        cargs.extend([
            "-fwm",
            execution.input_file(fwm)
        ])
    if mri_vol is not None:
        cargs.extend([
            "-mri",
            execution.input_file(mri_vol)
        ])
    if heq is not None:
        cargs.extend([
            "-heq",
            execution.input_file(heq)
        ])
    if renorm is not None:
        cargs.extend([
            "-renorm",
            execution.input_file(renorm)
        ])
    if flash_flag:
        cargs.append("-flash")
    if flash_params is not None:
        cargs.extend([
            "-flash_params",
            execution.input_file(flash_params)
        ])
    if renormalize is not None:
        cargs.extend([
            "-renormalize",
            *map(str, renormalize)
        ])
    if set_input is not None:
        cargs.extend([
            "-r",
            execution.input_file(set_input)
        ])
    if histogram_flag:
        cargs.append("-h")
    if cond_density_mean is not None:
        cargs.extend([
            "-a",
            str(cond_density_mean)
        ])
    if snapshots is not None:
        cargs.extend([
            "-w",
            *snapshots
        ])
    if mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask)
        ])
    if expand is not None:
        cargs.extend([
            "-e",
            str(expand)
        ])
    if max_iter is not None:
        cargs.extend([
            "-n",
            str(max_iter)
        ])
    if filter_mode is not None:
        cargs.extend([
            "-f",
            *map(str, filter_mode)
        ])
    if longitudinal_vol is not None:
        cargs.extend([
            "-L",
            execution.input_file(longitudinal_vol)
        ])
    if longitudinal_lta is not None:
        cargs.append(execution.input_file(longitudinal_lta))
    if relabel_unlikely_flag is not None:
        cargs.extend([
            "-RELABEL_UNLIKELY",
            *map(str, relabel_unlikely_flag)
        ])
    ret = MriRfLabelOutputs(
        root=execution.output_file("."),
        outvol=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_RF_LABEL_METADATA",
    "MriRfLabelOutputs",
    "mri_rf_label",
]

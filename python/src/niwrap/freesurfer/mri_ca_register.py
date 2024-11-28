# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CA_REGISTER_METADATA = Metadata(
    id="b27982b2cf32c82b5c162a9c2f5e298b284040cc.boutiques",
    name="mri_ca_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriCaRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_ca_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Multidimensional transform in m3d format"""


def mri_ca_register(
    input_volume: InputPathType,
    template: InputPathType,
    output_volume: str,
    tolerance: float | None = None,
    mask: InputPathType | None = None,
    transform_lta: InputPathType | None = None,
    level: float | None = None,
    read_intensity: bool = False,
    align: bool = False,
    invert_save_file: str | None = None,
    distance: float | None = None,
    regularize: float | None = None,
    regularize_mean: float | None = None,
    scale_smoothness: float | None = None,
    nobright: bool = False,
    renormalize_map: bool = False,
    renormalize: InputPathType | None = None,
    read_lta: bool = False,
    smoothness: float | None = None,
    samples: float | None = None,
    nsmall: float | None = None,
    fixed: bool = False,
    optimal: bool = False,
    noneg: bool = False,
    wm: bool = False,
    min_avgs: float | None = None,
    transform_limit: float | None = None,
    relabel: float | None = None,
    relabel_avgs: float | None = None,
    reset_avgs: float | None = None,
    vf_file: str | None = None,
    diag_file: str | None = None,
    tr: float | None = None,
    te: float | None = None,
    example: str | None = None,
    bigventricles: bool = False,
    uncompress: bool = False,
    second_pass_renorm: bool = False,
    threads: float | None = None,
    runner: Runner | None = None,
) -> MriCaRegisterOutputs:
    """
    Generates a multi-dimensional talairach transform from a gca file and
    talairach.lta file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        template: Template in GCA format.
        output_volume: Output volume in M3D format.
        tolerance: Defines convergence of registration.
        mask: Specifies volume to use as a mask.
        transform_lta: Transform in LTA format.
        level: Defines how many surrounding voxels will be used in\
            interpolations, default is 6.
        read_intensity: Allows reading of multiple intensity normalization.
        align: Enable alignment.
        invert_save_file: Invert and save as GCAM file.
        distance: Distance for registration.
        regularize: Regularization parameter.
        regularize_mean: Mean regularization.
        scale_smoothness: Smoothness scaling factor.
        nobright: Disable brightness adjustment.
        renormalize_map: Renormalize using map.
        renormalize: Renormalize with intensity file.
        read_lta: Use LTA file for registration.
        smoothness: Smoothness parameter.
        samples: Sample points for registration.
        nsmall: Number of small features.
        fixed: Fixed mode for registration.
        optimal: Optimal registration settings.
        noneg: Disallow negative values.
        wm: White matter flag.
        min_avgs: Minimum number of averages.
        transform_limit: Transform limit.
        relabel: Relabel options.
        relabel_avgs: Relabel averages.
        reset_avgs: Reset averages.
        vf_file: VF file name.
        diag_file: Diagnostic file name.
        tr: TR parameter.
        te: TE parameter.
        example: Example file.
        bigventricles: Handle big ventricles.
        uncompress: Uncompress files.
        second_pass_renorm: Second pass renormalization.
        threads: Number of threads.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCaRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CA_REGISTER_METADATA)
    cargs = []
    cargs.append("mri_ca_register")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(template))
    cargs.append(output_volume)
    if tolerance is not None:
        cargs.extend([
            "-tol",
            str(tolerance)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if transform_lta is not None:
        cargs.extend([
            "-T",
            execution.input_file(transform_lta)
        ])
    if level is not None:
        cargs.extend([
            "-level",
            str(level)
        ])
    if read_intensity:
        cargs.append("-ri")
    if align:
        cargs.append("-align")
    if invert_save_file is not None:
        cargs.extend([
            "-invert-and-save",
            invert_save_file
        ])
    if distance is not None:
        cargs.extend([
            "-dist",
            str(distance)
        ])
    if regularize is not None:
        cargs.extend([
            "-regularize",
            str(regularize)
        ])
    if regularize_mean is not None:
        cargs.extend([
            "-regularize-mean",
            str(regularize_mean)
        ])
    if scale_smoothness is not None:
        cargs.extend([
            "-scale_smoothness",
            str(scale_smoothness)
        ])
    if nobright:
        cargs.append("-nobright")
    if renormalize_map:
        cargs.append("-renormalize_map")
    if renormalize is not None:
        cargs.extend([
            "-renormalize",
            execution.input_file(renormalize)
        ])
    if read_lta:
        cargs.append("-read_lta")
    if smoothness is not None:
        cargs.extend([
            "-smoothness",
            str(smoothness)
        ])
    if samples is not None:
        cargs.extend([
            "-samples",
            str(samples)
        ])
    if nsmall is not None:
        cargs.extend([
            "-nsmall",
            str(nsmall)
        ])
    if fixed:
        cargs.append("-fixed")
    if optimal:
        cargs.append("-optimal")
    if noneg:
        cargs.append("-noneg")
    if wm:
        cargs.append("-wm")
    if min_avgs is not None:
        cargs.extend([
            "-min_avgs",
            str(min_avgs)
        ])
    if transform_limit is not None:
        cargs.extend([
            "-tl",
            str(transform_limit)
        ])
    if relabel is not None:
        cargs.extend([
            "-relabel",
            str(relabel)
        ])
    if relabel_avgs is not None:
        cargs.extend([
            "-relabel_avgs",
            str(relabel_avgs)
        ])
    if reset_avgs is not None:
        cargs.extend([
            "-reset_avgs",
            str(reset_avgs)
        ])
    if vf_file is not None:
        cargs.extend([
            "-vf",
            vf_file
        ])
    if diag_file is not None:
        cargs.extend([
            "-diag",
            diag_file
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
    if example is not None:
        cargs.extend([
            "-example",
            example
        ])
    if bigventricles:
        cargs.append("-<no>bigventricles")
    if uncompress:
        cargs.append("-uncompress")
    if second_pass_renorm:
        cargs.append("-secondpassrenorm")
    if threads is not None:
        cargs.extend([
            "-threads",
            str(threads)
        ])
    ret = MriCaRegisterOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_volume + ".m3d"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CA_REGISTER_METADATA",
    "MriCaRegisterOutputs",
    "mri_ca_register",
]

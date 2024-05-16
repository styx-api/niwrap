# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.751269

import typing

from ..styxdefs import *


CIFTI_CORRELATION_GRADIENT_METADATA = Metadata(
    id="0dc80c97f9d3bafaf90e5e7e1d86156b2154774a",
    name="cifti-correlation-gradient",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiCorrelationGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_correlation_gradient(...)`.
    """
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_correlation_gradient(
    runner: Runner,
    cifti: InputPathType,
    cifti_out: InputPathType,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    opt_surface_presmooth_surface_kernel: float | int | None = None,
    opt_volume_presmooth_volume_kernel: float | int | None = None,
    opt_presmooth_fwhm: bool = False,
    opt_undo_fisher_z: bool = False,
    opt_fisher_z: bool = False,
    opt_surface_exclude_distance: float | int | None = None,
    opt_volume_exclude_distance: float | int | None = None,
    opt_covariance: bool = False,
    opt_mem_limit_limit_gb: float | int | None = None,
    opt_double_correlation: bool = False,
) -> CiftiCorrelationGradientOutputs:
    """
    CORRELATE CIFTI ROWS AND TAKE GRADIENT.
    
    For each structure, compute the correlation of the rows in the structure,
    and take the gradients of the resulting rows, then average them. Memory
    limit does not need to be an integer, you may also specify 0 to use as
    little memory as possible (this may be very slow).
    
    Args:
        runner: Command runner
        cifti: the input cifti
        cifti_out: the output cifti
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
        opt_surface_presmooth_surface_kernel: smooth on the surface before
            computing the gradient: the size of the gaussian surface smoothing
            kernel in mm, as sigma by default
        opt_volume_presmooth_volume_kernel: smooth the volume before computing
            the gradient: the size of the gaussian volume smoothing kernel in mm, as
            sigma by default
        opt_presmooth_fwhm: smoothing kernel sizes are FWHM, not sigma
        opt_undo_fisher_z: apply the inverse fisher small z transform to the
            input
        opt_fisher_z: apply the fisher small z transform to the correlations
            before taking the gradient
        opt_surface_exclude_distance: exclude vertices near each seed vertex
            from computation: geodesic distance from seed vertex for the exclusion
            zone, in mm
        opt_volume_exclude_distance: exclude voxels near each seed voxel from
            computation: distance from seed voxel for the exclusion zone, in mm
        opt_covariance: compute covariance instead of correlation
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in gigabytes
        opt_double_correlation: do two correlations before taking the gradient
    Returns:
        NamedTuple of outputs (described in `CiftiCorrelationGradientOutputs`).
    """
    execution = runner.start_execution(CIFTI_CORRELATION_GRADIENT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-correlation-gradient")
    cargs.append(execution.input_file(cifti))
    cargs.append(execution.input_file(cifti_out))
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    if opt_surface_presmooth_surface_kernel is not None:
        cargs.extend(["-surface-presmooth", str(opt_surface_presmooth_surface_kernel)])
    if opt_volume_presmooth_volume_kernel is not None:
        cargs.extend(["-volume-presmooth", str(opt_volume_presmooth_volume_kernel)])
    if opt_presmooth_fwhm:
        cargs.append("-presmooth-fwhm")
    if opt_undo_fisher_z:
        cargs.append("-undo-fisher-z")
    if opt_fisher_z:
        cargs.append("-fisher-z")
    if opt_surface_exclude_distance is not None:
        cargs.extend(["-surface-exclude", str(opt_surface_exclude_distance)])
    if opt_volume_exclude_distance is not None:
        cargs.extend(["-volume-exclude", str(opt_volume_exclude_distance)])
    if opt_covariance:
        cargs.append("-covariance")
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    if opt_double_correlation:
        cargs.append("-double-correlation")
    ret = CiftiCorrelationGradientOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret

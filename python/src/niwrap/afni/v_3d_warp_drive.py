# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_WARP_DRIVE_METADATA = Metadata(
    id="8f83d827a638274ca724256cf87b99333ecd5bfb",
    name="3dWarpDrive",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="your-docker-image:latest",
)


class V3dWarpDriveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_warp_drive(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Warped dataset output"""
    output_summary: OutputPathType | None
    """Summary of calculations"""
    oned_output_file: OutputPathType | None
    """File with warping parameters"""
    matrix_output_file: OutputPathType | None
    """File with transformation matrices"""


def v_3d_warp_drive(
    dataset: InputPathType,
    base_dataset: InputPathType,
    prefix: str,
    shift_only: bool = False,
    shift_rotate: bool = False,
    shift_rotate_scale: bool = False,
    affine_general: bool = False,
    bilinear_general: bool = False,
    linear: bool = False,
    cubic: bool = False,
    nn: bool = False,
    quintic: bool = False,
    input_dataset: InputPathType | None = None,
    verbosity_flag: bool = False,
    summary_file: str | None = None,
    max_iterations: int | None = None,
    delta: float | int | None = None,
    weight: str | None = None,
    convergence_thresh: float | int | None = None,
    twopass: bool = False,
    final_mode: str | None = None,
    parfix: list[str] | None = None,
    oned_file: InputPathType | None = None,
    float_format: bool = False,
    coarserot_init: bool = False,
    oned_matrix_save: InputPathType | None = None,
    sdu_order: bool = False,
    sud_order: bool = False,
    dsu_order: bool = False,
    dus_order: bool = False,
    usd_order: bool = False,
    uds_order: bool = False,
    supper_s_matrix: bool = False,
    slower_s_matrix: bool = False,
    ashift: bool = False,
    bshift: bool = False,
    runner: Runner | None = None,
) -> V3dWarpDriveOutputs:
    """
    3dWarpDrive by RWCox.
    
    Warp a dataset to match another one (the base) using an affine
    transformation.
    
    Args:
        dataset: Input dataset.
        base_dataset: Load dataset as the base to which the input dataset will\
            be matched. This is a mandatory option.
        prefix: Sets the prefix of the output dataset. If 'NULL', no output\
            dataset is written.
        shift_only: 3 parameters (shifts).
        shift_rotate: 6 parameters (shifts + angles).
        shift_rotate_scale: 9 parameters (shifts + angles + scale factors).
        affine_general: 12 parameters (3 shifts + 3x3 matrix).
        bilinear_general: 39 parameters (3 + 3x3 + 3x3x3). Not implemented and\
            will never be.
        linear: Linear interpolation method.
        cubic: Cubic interpolation method.
        nn: Nearest neighbor interpolation method [default].
        quintic: Quintic interpolation method.
        input_dataset: Specify the input dataset anywhere in the command line\
            option list.
        verbosity_flag: Print out lots of information along the way.
        summary_file: Save summary of calculations into text file. If value is\
            '-', summary goes to stdout.
        max_iterations: Allow up to 'm' iterations for convergence.
        delta: Distance, in voxel size, used to compute image derivatives using\
            finite differences. [Default=1.0].
        weight: Set the weighting applied to each voxel proportional to the\
            brick specified here. [Default=computed by program from base].
        convergence_thresh: Set the convergence parameter to be RMS 't' voxels\
            movement between iterations. [Default=0.03].
        twopass: Do the parameter estimation in two passes, coarse-but-fast\
            first, then fine-but-slow second.
        final_mode: Set the final warp to be interpolated using 'mode'.
        parfix: Fix the n'th parameter of the warp model to the value 'v'. More\
            than one -parfix option can be used.
        oned_file: Write out the warping parameters to this file.
        float_format: Write output dataset in float format, even if input\
            dataset is short or byte.
        coarserot_init: Initialize shift+rotation parameters by a brute force\
            coarse search.
        oned_matrix_save: Save base-to-input transformation matrices in\
            specified file. If the file does not end in '.1D', the program will\
            append '.aff12.1D'.
        sdu_order: Set the order of the matrix multiplication for the affine\
            transformations (S=triangular shear, D=diagonal scaling matrix,\
            U=rotation matrix).
        sud_order: Set the order of the matrix multiplication for the affine\
            transformations (S=triangular shear, U=rotation matrix, D=diagonal\
            scaling matrix).
        dsu_order: Set the order of the matrix multiplication for the affine\
            transformations (D=diagonal scaling matrix, S=triangular shear,\
            U=rotation matrix).
        dus_order: Set the order of the matrix multiplication for the affine\
            transformations (D=diagonal scaling matrix, U=rotation matrix,\
            S=triangular shear).
        usd_order: Set the order of the matrix multiplication for the affine\
            transformations (U=rotation matrix, S=triangular shear, D=diagonal\
            scaling matrix).
        uds_order: Set the order of the matrix multiplication for the affine\
            transformations (U=rotation matrix, D=diagonal scaling matrix,\
            S=triangular shear).
        supper_s_matrix: Set the S matrix to be upper triangular.
        slower_s_matrix: Set the S matrix to be lower triangular.
        ashift: Apply the shift parameters after the matrix transformation.
        bshift: Apply the shift parameters before the matrix transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dWarpDriveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_WARP_DRIVE_METADATA)
    cargs = []
    cargs.append("3dWarpDrive")
    if bilinear_general:
        cargs.append("-bilinear_general")
    if quintic:
        cargs.append("-quintic")
    cargs.append("-base")
    cargs.extend(["-base", execution.input_file(base_dataset)])
    cargs.append("-prefix")
    cargs.extend(["-prefix", prefix])
    cargs.append("[TECHNICAL_OPTIONS]")
    cargs.append(execution.input_file(dataset))
    ret = V3dWarpDriveOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(f"{prefix}+orig", optional=True),
        output_summary=execution.output_file(f"{summary_file}", optional=True) if summary_file is not None else None,
        oned_output_file=execution.output_file(f"{pathlib.Path(oned_file).name}", optional=True) if oned_file is not None else None,
        matrix_output_file=execution.output_file(f"{pathlib.Path(oned_matrix_save).name}", optional=True) if oned_matrix_save is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dWarpDriveOutputs",
    "V_3D_WARP_DRIVE_METADATA",
    "v_3d_warp_drive",
]

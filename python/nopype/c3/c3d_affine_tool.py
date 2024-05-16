# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.676335

import typing

from ..styxdefs import *


C3D_AFFINE_TOOL_METADATA = Metadata(
    id="614ba2ea5b01463cd238b679d9b58701b20958ca",
    name="C3dAffineTool",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class C3dAffineToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `c3d_affine_tool(...)`.
    """
    itk_transform_outfile: OutputPathType
    """Output ITK transform file."""
    irtk_transform_outfile: OutputPathType
    """Output IRTK transform file."""
    matrix_transform_outfile: OutputPathType
    """Write output matrix."""


def c3d_affine_tool(
    runner: Runner,
    transform_file: InputPathType,
    reference_file: InputPathType | None = None,
    source_file: InputPathType | None = None,
    fsl2ras: bool = False,
    ras2fsl: bool = False,
    determinant: bool = False,
    invert: bool = False,
    multiply: bool = False,
    sqrt: bool = False,
    out_matfile: str | None = None,
    sform_file: InputPathType | None = None,
    itk_transform: InputPathType | None = None,
    out_itk_transform: str | None = None,
    irtk_transform: InputPathType | None = None,
    out_irtk_transform: str | None = None,
    info: bool = False,
    info_full: bool = False,
) -> C3dAffineToolOutputs:
    """
    C3dAffineTool, as implemented in Nipype (module: nipype.interfaces.c3,
    interface: C3dAffineTool).
    Converts fsl-style Affine registration into ANTS compatible itk format.'
    
    Args:
        runner: Command runner
        transform_file: file or string representing the transform.
        reference_file: Set reference (fixed) image - only for -fsl2ras and
            -ras2fsl.
        source_file: Set source (moving) image - only for -fsl2ras and -ras2fsl.
        fsl2ras: Convert FSL to RAS.
        ras2fsl: Convert RAS to FSL.
        determinant: Print the determinant.
        invert: Invert matrix.
        multiply: Multiply matrices.
        sqrt: Matrix square root (i.e., Q s.t. A = Q * Q).
        out_matfile: Write output matrix.
        sform_file: Read matrix from NifTI sform.
        itk_transform: Import ITK transform.
        out_itk_transform: Export ITK transform.
        irtk_transform: Import IRTK .dof format transform.
        out_irtk_transform: Export IRTK .dof format transform.
        info: Print matrix.
        info_full: Print matrix and more detail about the transform.
    Returns:
        NamedTuple of outputs (described in `C3dAffineToolOutputs`).
    """
    execution = runner.start_execution(C3D_AFFINE_TOOL_METADATA)
    cargs = []
    cargs.append("c3d_affine_tool")
    if reference_file is not None:
        cargs.extend(["-ref", execution.input_file(reference_file)])
    if source_file is not None:
        cargs.extend(["-src", execution.input_file(source_file)])
    cargs.append(execution.input_file(transform_file))
    if sform_file is not None:
        cargs.extend(["-sform", execution.input_file(sform_file)])
    if out_matfile is not None:
        cargs.extend(["-o", out_matfile])
    if fsl2ras:
        cargs.append("-fsl2ras")
    if ras2fsl:
        cargs.append("-ras2fsl")
    if invert:
        cargs.append("-inv")
    if determinant:
        cargs.append("-det")
    if multiply:
        cargs.append("-mult")
    if sqrt:
        cargs.append("-sqrt")
    if itk_transform is not None:
        cargs.extend(["-itk", execution.input_file(itk_transform)])
    if out_itk_transform is not None:
        cargs.extend(["-oitk", out_itk_transform])
    if irtk_transform is not None:
        cargs.extend(["-irtk", execution.input_file(irtk_transform)])
    if out_irtk_transform is not None:
        cargs.extend(["-oirtk", out_irtk_transform])
    if info:
        cargs.append("-info")
    if info_full:
        cargs.append("-info-full")
    ret = C3dAffineToolOutputs(
        itk_transform_outfile=execution.output_file(f"{out_itk_transform}.txt", optional=True),
        irtk_transform_outfile=execution.output_file(f"{out_irtk_transform}.dof", optional=True),
        matrix_transform_outfile=execution.output_file(f"{out_matfile}.mat", optional=True),
    )
    execution.run(cargs)
    return ret

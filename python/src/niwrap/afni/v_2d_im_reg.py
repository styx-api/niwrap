# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_2D_IM_REG_METADATA = Metadata(
    id="fba9dc129622c45cef523765c1de161c8a41a790",
    name="2dImReg",
)


class V2dImRegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_2d_im_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output 3d+time dataset"""
    dx_file: OutputPathType | None
    """File containing dx registration parameters in pixels/mm"""
    dy_file: OutputPathType | None
    """File containing dy registration parameters in pixels/mm"""
    psi_file: OutputPathType | None
    """File containing psi registration parameters in degrees"""
    oldrms_file: OutputPathType | None
    """File containing the volume RMS error for the original dataset"""
    newrms_file: OutputPathType | None
    """File containing the volume RMS error for the registered dataset"""


def v_2d_im_reg(
    input_file: InputPathType,
    prefix: str,
    base_file: InputPathType | None = None,
    base: float | int | None = None,
    nofine: bool = False,
    fine_blur: float | int | None = None,
    fine_dxy: float | int | None = None,
    fine_dphi: float | int | None = None,
    dprefix: str | None = None,
    dmm: bool = False,
    rprefix: str | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> V2dImRegOutputs:
    """
    2dImReg by Author Unknown.
    
    2D image registration tool for 3D+time datasets, aligning images on a
    slice-by-slice basis to a specified base image.
    
    More information: http://example.url/2dImReg
    
    Args:
        input_file: Filename of input 3d+time dataset to process.
        prefix: Prefix name for output 3d+time dataset.
        base_file: Filename of 3d+time dataset for base image (default =\
            current input dataset).
        base: Time index for base image (0 <= num) (default: num = 3).
        nofine: Deactivate fine fit phase of image registration (default: fine\
            fit is active).
        fine_blur: FWHM of blurring prior to registration (in pixels) (default:\
            blur = 1.0).
        fine_dxy: Convergence tolerance for translations (in pixels) (default:\
            dxy = 0.07).
        fine_dphi: Convergence tolerance for rotations (in degrees) (default:\
            dphi = 0.21).
        dprefix: Write files containing the registration parameters for each\
            slice in chronological order.
        dmm: Change dx and dy output format from pixels to mm.
        rprefix: Write files containing the volume RMS error for the original\
            and the registered datasets.
        debug: Lots of additional output to screen.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2dImRegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_2D_IM_REG_METADATA)
    cargs = []
    cargs.append("2dImReg")
    cargs.append(execution.input_file(input_file))
    if base_file is not None:
        cargs.append(execution.input_file(base_file))
    if base is not None:
        cargs.append(str(base))
    if nofine:
        cargs.append("-nofine")
    if fine_blur is not None:
        cargs.append(str(fine_blur))
    if fine_dxy is not None:
        cargs.append(str(fine_dxy))
    if fine_dphi is not None:
        cargs.append(str(fine_dphi))
    cargs.append(prefix)
    if dprefix is not None:
        cargs.append(dprefix)
    if dmm:
        cargs.append("-dmm")
    if rprefix is not None:
        cargs.append(rprefix)
    if debug:
        cargs.append("-debug")
    ret = V2dImRegOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(f"{prefix}.nii"),
        dx_file=execution.output_file(f"{dprefix}.dx", optional=True) if dprefix is not None else None,
        dy_file=execution.output_file(f"{dprefix}.dy", optional=True) if dprefix is not None else None,
        psi_file=execution.output_file(f"{dprefix}.psi", optional=True) if dprefix is not None else None,
        oldrms_file=execution.output_file(f"{rprefix}.oldrms", optional=True) if rprefix is not None else None,
        newrms_file=execution.output_file(f"{rprefix}.newrms", optional=True) if rprefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V2dImRegOutputs",
    "V_2D_IM_REG_METADATA",
    "v_2d_im_reg",
]

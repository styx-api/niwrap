# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CONVERTWARP_METADATA = Metadata(
    id="575e0d71c10f27c1e159f9ac1206e9cf51085161",
    name="convertwarp",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ConvertwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convertwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Name of output file, containing warps that are the combination of all those given as arguments. the format of this will be a field-file (rather than spline coefficients) with any affine components included."""
    out_file_: OutputPathType
    """Name of output file, containing the warp as field or coefficients."""


def convertwarp(
    runner: Runner,
    reference: InputPathType,
    abswarp: bool = False,
    cons_jacobian: bool = False,
    jacobian_max: float | int | None = None,
    jacobian_min: float | int | None = None,
    midmat: InputPathType | None = None,
    out_abswarp: bool = False,
    out_relwarp: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    postmat: InputPathType | None = None,
    premat: InputPathType | None = None,
    relwarp: bool = False,
    shift_direction: typing.Literal["y-", "y", "x", "x-", "z", "z-"] | None = None,
    shift_in_file: InputPathType | None = None,
    warp1: InputPathType | None = None,
    warp2: InputPathType | None = None,
) -> ConvertwarpOutputs:
    """
    convertwarp by Nipype (interface).
    
    Use FSL convertwarp for combining multiple transforms into one.
    
    More information:
    http://fsl.fmrib.ox.ac.uk/fsl/fsl-4.1.9/fnirt/warp_utils.html
    
    Args:
        runner: Command runner
        reference: Name of a file in target space of the full transform.
        abswarp: If set it indicates that the warps in --warp1 and --warp2
            should be interpreted as absolute. i.e. the values in --warp1/2 are the
            coordinates in the next space, rather than displacements. this flag is
            ignored if --warp1/2 was created by fnirt, which always creates relative
            displacements.
        cons_jacobian: Constrain the jacobian of the warpfield to lie within
            specified min/max limits.
        jacobian_max: Maximum acceptable jacobian value for constraint (default
            100.0).
        jacobian_min: Minimum acceptable jacobian value for constraint (default
            0.01).
        midmat: Name of file containing mid-warp-affine transform.
        out_abswarp: If set it indicates that the warps in --out should be
            absolute, i.e. the values in --out are displacements from the
            coordinates in --ref.
        out_relwarp: If set it indicates that the warps in --out should be
            relative, i.e. the values in --out are displacements from the
            coordinates in --ref.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.
            Fsl output type.
        postmat: Name of file containing an affine transform (applied last). it
            could e.g. be an affine transform that maps the mni152-space into a
            better approximation to the talairach-space (if indeed there is one).
        premat: Filename for pre-transform (affine matrix).
        relwarp: If set it indicates that the warps in --warp1/2 should be
            interpreted as relative. i.e. the values in --warp1/2 are displacements
            from the coordinates in the next space.
        shift_direction: 'y-' or 'y' or 'x' or 'x-' or 'z' or 'z-'. Indicates
            the direction that the distortions from --shiftmap goes. it depends on
            the direction and polarity of the phase-encoding in the epi sequence.
        shift_in_file: Name of file containing a "shiftmap", a non-linear
            transform with displacements only in one direction (applied first,
            before premat). this would typically be a fieldmap that has been
            pre-processed using fugue that maps a subjects functional (epi) data
            onto an undistorted space (i.e. a space that corresponds to his/her true
            anatomy).
        warp1: Name of file containing initial warp-fields/coefficients (follows
            premat). this could e.g. be a fnirt-transform from a subjects structural
            scan to an average of a group of subjects.
        warp2: Name of file containing secondary warp-fields/coefficients (after
            warp1/midmat but before postmat). this could e.g. be a fnirt-transform
            from the average of a group of subjects to some standard space (e.g.
            mni152).
    Returns:
        NamedTuple of outputs (described in `ConvertwarpOutputs`).
    """
    if (
        relwarp +
        abswarp
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "relwarp,\n"
            "abswarp"
        )
    if (
        out_abswarp +
        out_relwarp
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_abswarp,\n"
            "out_relwarp"
        )
    execution = runner.start_execution(CONVERTWARP_METADATA)
    cargs = []
    cargs.append("convertwarp")
    cargs.append(("--ref=" + execution.input_file(reference)))
    cargs.append("[OUT_FILE]")
    if abswarp:
        cargs.append("--abs")
    if cons_jacobian:
        cargs.append("--constrainj")
    if jacobian_max is not None:
        cargs.append(("--jmax=" + str(jacobian_max)))
    if jacobian_min is not None:
        cargs.append(("--jmin=" + str(jacobian_min)))
    if midmat is not None:
        cargs.append(("--midmat=" + execution.input_file(midmat)))
    if out_abswarp:
        cargs.append("--absout")
    if out_relwarp:
        cargs.append("--relout")
    if output_type is not None:
        cargs.append(output_type)
    if postmat is not None:
        cargs.append(("--postmat=" + execution.input_file(postmat)))
    if premat is not None:
        cargs.append(("--premat=" + execution.input_file(premat)))
    if relwarp:
        cargs.append("--rel")
    if shift_direction is not None:
        cargs.append(("--shiftdir=" + shift_direction))
    if shift_in_file is not None:
        cargs.append(("--shiftmap=" + execution.input_file(shift_in_file)))
    if warp1 is not None:
        cargs.append(("--warp1=" + execution.input_file(warp1)))
    if warp2 is not None:
        cargs.append(("--warp2=" + execution.input_file(warp2)))
    ret = ConvertwarpOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(reference).stem}_concatwarp", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret

# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:56.043820

import typing

from ..styxdefs import *


FNIRT_METADATA = Metadata(
    id="86fa56260abb70199c45df4f7b2c704a62deccad",
    name="fnirt",
    container_image_type="docker",
    container_image_tag="container/image",
)


class FnirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fnirt(...)`.
    """
    field_file_outfile: OutputPathType
    """File with warp field."""
    fieldcoeff_file_outfile: OutputPathType
    """File with field coefficients."""
    jacobian_file_outfile: OutputPathType
    """File containing jacobian of the field."""
    log_file_outfile: OutputPathType
    """Name of log-file."""
    modulatedref_file_outfile: OutputPathType
    """File containing intensity modulated --ref."""
    out_intensitymap_file_outfile: OutputPathType
    """Files containing info pertaining to intensity mapping."""
    warped_file_outfile: OutputPathType
    """Warped image."""


def fnirt(
    runner: Runner,
    in_file: InputPathType,
    ref_file: InputPathType,
    affine_file: InputPathType | None = None,
    config_file: typing.Literal["T1_2_MNI152_2mm", "FA_2_FMRIB58_1mm"] | None = None,
    field_file: InputPathType | None = None,
    fieldcoeff_file: InputPathType | None = None,
    jacobian_file: bool = False,
    log_file: InputPathType | None = None,
    modulatedref_file: bool = False,
    refmask_file: InputPathType | None = None,
    warped_file: InputPathType | None = None,
) -> FnirtOutputs:
    """
    FNIRT, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    FNIRT).
    FSL FNIRT wrapper for non-linear registration
    For complete details, see the `FNIRT Documentation.
    <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT>`_
    
    Args:
        runner: Command runner
        in_file: Name of input image.
        ref_file: Name of reference image.
        affine_file: Name of file containing affine transform.
        config_file: 't1_2_mni152_2mm' or 'fa_2_fmrib58_1mm' or file or string.
            Name of config file specifying command line arguments.
        field_file: file. Name of output file with field.
        fieldcoeff_file: string representing a file. Name of output file with
            field coefficients.
        jacobian_file: A boolean or file. Name of file for writing out the
            jacobian of the field (for diagnostic or vbm purposes).
        log_file: Name of log-file.
        modulatedref_file: string representing a file. Name of file for writing
            out intensity modulated --ref (for diagnostic purposes).
        refmask_file: Name of file with mask in reference space.
        warped_file: Name of output-file containing the --in image after it has
            been warped to the --ref image
    Returns:
        NamedTuple of outputs (described in `FnirtOutputs`).
    """
    execution = runner.start_execution(FNIRT_METADATA)
    cargs = []
    cargs.append("fnirt")
    if affine_file is not None:
        cargs.append(("--aff=" + execution.input_file(affine_file)))
    if config_file is not None:
        cargs.append(("--config=" + config_file))
    if field_file is not None:
        cargs.append(("--fout=" + execution.input_file(field_file)))
    if fieldcoeff_file is not None:
        cargs.append(("--cout=" + execution.input_file(fieldcoeff_file)))
    cargs.append(("--in=" + execution.input_file(in_file)))
    if jacobian_file:
        cargs.append("--jout")
    if log_file is not None:
        cargs.append(("--logout=" + execution.input_file(log_file)))
    if modulatedref_file:
        cargs.append("--refout")
    cargs.append(("--ref=" + execution.input_file(ref_file)))
    if refmask_file is not None:
        cargs.append(("--refmask=" + execution.input_file(refmask_file)))
    if warped_file is not None:
        cargs.append(("--iout=" + execution.input_file(warped_file)))
    ret = FnirtOutputs(
        field_file_outfile=execution.output_file(f"{field_file}.nii.gz", optional=True),
        fieldcoeff_file_outfile=execution.output_file(f"{fieldcoeff_file}.nii.gz", optional=True),
        jacobian_file_outfile=execution.output_file(f"{jacobian_file}.mat", optional=True),
        log_file_outfile=execution.output_file(f"{log_file}.txt", optional=True),
        modulatedref_file_outfile=execution.output_file(f"{modulatedref_file}.nii.gz", optional=True),
        out_intensitymap_file_outfile=execution.output_file(f"[OUT_INTENSITYMAP_FILE]", optional=True),
        warped_file_outfile=execution.output_file(f"{warped_file}.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret

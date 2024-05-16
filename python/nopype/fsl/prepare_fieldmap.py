# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


PREPARE_FIELDMAP_METADATA = Metadata(
    id="2231a5d83adb417b7d33f74216049429d0a1a84b",
    name="PrepareFieldmap",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class PrepareFieldmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prepare_fieldmap(...)`.
    """
    out_fieldmap_outfile: OutputPathType
    """Output name for prepared fieldmap."""


def prepare_fieldmap(
    runner: Runner,
    in_magnitude: InputPathType,
    in_phase: InputPathType,
    delta_te: float | int = 2.46,
    nocheck: bool = False,
    out_fieldmap: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    scanner: str | None = "SIEMENS",
) -> PrepareFieldmapOutputs:
    """
    PrepareFieldmap, as implemented in Nipype (module: nipype.interfaces.fsl.epi,
    interface: PrepareFieldmap).
    
    Interface for the fsl_prepare_fieldmap script (FSL 5.0)
    Prepares a fieldmap suitable for FEAT from SIEMENS data - saves output in
    rad/s format (e.g. ```fsl_prepare_fieldmap SIEMENS
    images_3_gre_field_mapping images_4_gre_field_mapping fmap_rads 2.65```).
    
    Args:
        runner: Command runner
        in_magnitude: Magnitude difference map, brain extracted.
        in_phase: Phase difference map, in siemens format range from 0-4096 or
            0-8192).
        delta_te: Echo time difference of the fieldmap sequence in ms. (usually
            2.46ms in siemens).
        nocheck: Do not perform sanity checks for image size/range/dimensions.
        out_fieldmap: Output name for prepared fieldmap.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.
            Fsl output type.
        scanner: Must be siemens.
    Returns:
        NamedTuple of outputs (described in `PrepareFieldmapOutputs`).
    """
    execution = runner.start_execution(PREPARE_FIELDMAP_METADATA)
    cargs = []
    cargs.append("PrepareFieldmap")
    cargs.append(str(delta_te))
    if scanner is not None:
        cargs.append(scanner)
    cargs.append(execution.input_file(in_phase))
    cargs.append(execution.input_file(in_magnitude))
    if out_fieldmap is not None:
        cargs.append(execution.input_file(out_fieldmap))
    if nocheck:
        cargs.append("--nocheck")
    cargs.append("[ARGS]")
    cargs.append("[ENVIRON]")
    if output_type is not None:
        cargs.append(output_type)
    ret = PrepareFieldmapOutputs(
        out_fieldmap_outfile=execution.output_file(f"{out_fieldmap}", optional=True),
    )
    execution.run(cargs)
    return ret

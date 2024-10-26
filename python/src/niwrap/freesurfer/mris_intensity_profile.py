# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_INTENSITY_PROFILE_METADATA = Metadata(
    id="4503435a83a78998ccb884fce0c0c30ed9f78d3b.boutiques",
    name="mris_intensity_profile",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisIntensityProfileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_intensity_profile(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_curvature_file: OutputPathType
    """Curvature file with the intensity profile measurement."""
    output_mean_profile_integral: OutputPathType | None
    """File with the mean profile-integral."""


def mris_intensity_profile(
    subject_name: str,
    hemi: str,
    volume: InputPathType,
    output_file: str,
    write_surf: str | None = None,
    sdir: str | None = None,
    white: str | None = None,
    pial: str | None = None,
    normalize_flag: bool = False,
    mean: str | None = None,
    xform: InputPathType | None = None,
    src: InputPathType | None = None,
    dst: InputPathType | None = None,
    invert_flag: bool = False,
    runner: Runner | None = None,
) -> MrisIntensityProfileOutputs:
    """
    This program computes the intensity profile of the cortical ribbon and writes
    the resulting measurement into a 'curvature' file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemi: Hemisphere (e.g. lh or rh).
        volume: Volume file to be processed.
        output_file: Output file where the measurement is saved.
        write_surf: Write the variational pial surface target locations.
        sdir: Specifies the SUBJECTS_DIR.
        white: Specifies the WHITE surface filename.
        pial: Specifies the PIAL surface filename.
        normalize_flag: Normalized sampling with respect to thickness.
        mean: Outputs the mean profile-integral to the specified file (output\
            is in curv format).
        xform: Specify the registration transformation that maps the T1 volume\
            to the input volume to be sampled.
        src: Source volume used when computing the registration transformation.
        dst: Destination volume used when computing the registration\
            transformation.
        invert_flag: Apply the registration transformation inversely.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisIntensityProfileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_INTENSITY_PROFILE_METADATA)
    cargs = []
    cargs.append("mris_intensity_profile")
    cargs.append(subject_name)
    cargs.append(hemi)
    cargs.append(execution.input_file(volume))
    cargs.append(output_file)
    if write_surf is not None:
        cargs.extend([
            "-write_surf",
            write_surf
        ])
    if sdir is not None:
        cargs.extend([
            "-sdir",
            sdir
        ])
    if white is not None:
        cargs.extend([
            "-white",
            white
        ])
    if pial is not None:
        cargs.extend([
            "-pial",
            pial
        ])
    if normalize_flag:
        cargs.append("-normalize")
    if mean is not None:
        cargs.extend([
            "-mean",
            mean
        ])
    if xform is not None:
        cargs.extend([
            "-xform",
            execution.input_file(xform)
        ])
    if src is not None:
        cargs.extend([
            "-src",
            execution.input_file(src)
        ])
    if dst is not None:
        cargs.extend([
            "-dst",
            execution.input_file(dst)
        ])
    if invert_flag:
        cargs.append("-invert")
    ret = MrisIntensityProfileOutputs(
        root=execution.output_file("."),
        output_curvature_file=execution.output_file(output_file),
        output_mean_profile_integral=execution.output_file(mean) if (mean is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_INTENSITY_PROFILE_METADATA",
    "MrisIntensityProfileOutputs",
    "mris_intensity_profile",
]

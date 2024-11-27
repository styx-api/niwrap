# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_AVERAGE_SUBJECT_METADATA = Metadata(
    id="d75a24ae99cd3258e4c0323f2c5c4fba80dcea8b.boutiques",
    name="make_average_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MakeAverageSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_average_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def make_average_subject(
    subjects: list[str],
    average_subject_name: str,
    fsgd_file: InputPathType | None = None,
    subject_list_file: InputPathType | None = None,
    sd_out: str | None = None,
    no_link: bool = False,
    sdir: str | None = None,
    ico_order: float | None = 7,
    transform_file: InputPathType | None = None,
    surface_registration: str | None = "sphere.reg",
    no_surfaces: bool = False,
    no_volumes: bool = False,
    force: bool = False,
    keep_all_orig: bool = False,
    no_symlink: bool = False,
    no_ribbon: bool = False,
    no_surf2surf: bool = False,
    rca_threads: float | None = None,
    help_: bool = False,
    version: bool = False,
    echo: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> MakeAverageSubjectOutputs:
    """
    Creates an average subject by averaging surfaces, curvatures, and volumes from a
    set of subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subject names.
        average_subject_name: Name of the average subject.
        fsgd_file: Get subject list from a FreeSurfer Group Descriptor file.
        subject_list_file: Text file containing all subject names.
        sd_out: Directory to put output under instead of SUBJECTS_DIR.
        no_link: Do not link back to the original SUBJECTS_DIR with --sd-out.
        sdir: Use an alternative SUBJECTS_DIR instead of the default one in the\
            environment.
        ico_order: Change order of icosahedron.
        transform_file: Filename of transform file.
        surface_registration: Alternative registration surface name.
        no_surfaces: Do not make average surfaces.
        no_volumes: Do not make average volumes.
        force: Overwrite existing average subject data.
        keep_all_orig: Concatenate all original volumes into mri/orig.all.mgz.
        no_symlink: Do not use symbolic links with surfaces, copy files instead.
        no_ribbon: Do not create ribbon.mgz and aparc+aseg.mgz files.
        no_surf2surf: Use old parametric surface mapping method.
        rca_threads: Number of threads to pass to recon-all.
        help_: Show short descriptive help.
        version: Show script version info.
        echo: Enable command echo for debugging.
        debug: Enable debug mode, same as --echo.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeAverageSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_AVERAGE_SUBJECT_METADATA)
    cargs = []
    cargs.append("make_average_subject")
    cargs.extend([
        "--subjects",
        *subjects
    ])
    if fsgd_file is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(fsgd_file)
        ])
    if subject_list_file is not None:
        cargs.extend([
            "--f",
            execution.input_file(subject_list_file)
        ])
    cargs.extend([
        "--out",
        average_subject_name
    ])
    if sd_out is not None:
        cargs.extend([
            "--sd-out",
            sd_out
        ])
    if no_link:
        cargs.append("--no-link")
    if sdir is not None:
        cargs.extend([
            "--sdir",
            sdir
        ])
    if ico_order is not None:
        cargs.extend([
            "--ico",
            str(ico_order)
        ])
    if transform_file is not None:
        cargs.extend([
            "--xform",
            execution.input_file(transform_file)
        ])
    if surface_registration is not None:
        cargs.extend([
            "--surf-reg",
            surface_registration
        ])
    if no_surfaces:
        cargs.append("--no-surf")
    if no_volumes:
        cargs.append("--no-vol")
    if force:
        cargs.append("--force")
    if keep_all_orig:
        cargs.append("--keep-all-orig")
    if no_symlink:
        cargs.append("--no-symlink")
    if no_ribbon:
        cargs.append("--no-ribbon")
    if no_surf2surf:
        cargs.append("--no-surf2surf")
    if rca_threads is not None:
        cargs.extend([
            "--rca-threads",
            str(rca_threads)
        ])
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    if echo:
        cargs.append("--echo")
    if debug:
        cargs.append("--debug")
    ret = MakeAverageSubjectOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_AVERAGE_SUBJECT_METADATA",
    "MakeAverageSubjectOutputs",
    "make_average_subject",
]

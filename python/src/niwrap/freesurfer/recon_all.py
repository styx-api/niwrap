# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RECON_ALL_METADATA_ = Metadata(
    id="773eade9a7d8dbfdc4fded9fef5895e8cf103d2f.boutiques",
    name="ReconAll",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ReconAllOutputs_(typing.NamedTuple):
    """
    Output object returned when calling `recon_all_(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    subjects_dir_outfile: OutputPathType
    """file or string representing an existing directory. Freesurfer subjects
    directory."""


def recon_all_(
    subjects_dir: InputPathType,
    directive: typing.Literal["all", "autorecon1", "autorecon2", "autorecon2-volonly", "autorecon2-perhemi", "autorecon2-inflate1", "autorecon2-cp", "autorecon2-wm", "autorecon3", "autorecon3-T2pial", "autorecon-pial", "autorecon-hemi", "localGI", "qcache"] | None = "all",
    flair_file: InputPathType | None = None,
    t1_files: list[InputPathType] | None = None,
    t2_file: InputPathType | None = None,
    big_ventricles: bool = False,
    brainstem: bool = False,
    expert: InputPathType | None = None,
    flags: list[InputPathType] | None = None,
    hemi: typing.Literal["lh", "rh"] | None = None,
    hippocampal_subfields_t1: bool = False,
    hippocampal_subfields_t2: list[str] | None = None,
    hires: bool = False,
    mprage: bool = False,
    openmp: int | None = None,
    parallel: bool = False,
    subject_id: str | None = "recon_all",
    talairach: str | None = None,
    use_flair: bool = False,
    use_t2: bool = False,
    xopts: typing.Literal["use", "clean", "overwrite"] | None = None,
    runner: Runner | None = None,
) -> ReconAllOutputs_:
    """
    Performs all, or any part of, the FreeSurfer cortical reconstruction process.
    
    Author: Members of the Laboratories for Computational Neuroimaging (LCN) at
    the Athinoula A. Martinos Center for Biomedical Imaging
    
    URL: https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all
    
    Args:
        subjects_dir: file or string representing an existing directory. Path\
            to subjects directory.
        directive: 'all' or 'autorecon1' or 'autorecon2' or\
            'autorecon2-volonly' or 'autorecon2-perhemi' or 'autorecon2-inflate1'\
            or 'autorecon2-cp' or 'autorecon2-wm' or 'autorecon3' or\
            'autorecon3-t2pial' or 'autorecon-pial' or 'autorecon-hemi' or\
            'localgi' or 'qcache'. Process directive.
        flair_file: Convert flair image to orig directory.
        t1_files: Name of t1 file to process.
        t2_file: Convert t2 image to orig directory.
        big_ventricles: For use in subjects with enlarged ventricles.
        brainstem: Segment brainstem structures.
        expert: Set parameters using expert file.
        flags: A list of items which are a string. Additional parameters.
        hemi: 'lh' or 'rh'. Hemisphere to process.
        hippocampal_subfields_t1: Segment hippocampal subfields using input t1\
            scan.
        hippocampal_subfields_t2: (file or string, a string). Segment\
            hippocampal subfields using t2 scan, identified by id (may be combined\
            with hippocampal_subfields_t1).
        hires: Conform to minimum voxel size (for voxels < 1mm).
        mprage: Assume scan parameters are mgh mp-rage protocol, which produces\
            darker gray matter.
        openmp: Number of processors to use in parallel.
        parallel: Enable parallel execution.
        subject_id: Subject name.
        talairach: Flags to pass to talairach commands.
        use_flair: Use flair image to refine the pial surface.
        use_t2: Use t2 image to refine the pial surface.
        xopts: 'use' or 'clean' or 'overwrite'. Use, delete or overwrite\
            existing expert options file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconAllOutputs_`).
    """
    if hippocampal_subfields_t2 is not None and (len(hippocampal_subfields_t2) != 2): 
        raise ValueError(f"Length of 'hippocampal_subfields_t2' must be 2 but was {len(hippocampal_subfields_t2)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECON_ALL_METADATA_)
    cargs = []
    cargs.append("ReconAll")
    if directive is not None:
        cargs.extend([
            "-",
            directive
        ])
    if flair_file is not None:
        cargs.extend([
            "-FLAIR",
            execution.input_file(flair_file)
        ])
    if t1_files is not None:
        cargs.extend([
            "-i",
            *[execution.input_file(f) for f in t1_files]
        ])
    if t2_file is not None:
        cargs.extend([
            "-T2",
            execution.input_file(t2_file)
        ])
    if big_ventricles:
        cargs.append("-bigventricles")
    if brainstem:
        cargs.append("-brainstem-structures")
    if expert is not None:
        cargs.extend([
            "-expert",
            execution.input_file(expert)
        ])
    if flags is not None:
        cargs.extend([execution.input_file(f) for f in flags])
    if hemi is not None:
        cargs.extend([
            "-hemi",
            hemi
        ])
    if hippocampal_subfields_t1:
        cargs.append("-hippocampal-subfields-T1")
    if hippocampal_subfields_t2 is not None:
        cargs.extend([
            "-hippocampal-subfields-T2",
            *hippocampal_subfields_t2
        ])
    if hires:
        cargs.append("-hires")
    if mprage:
        cargs.append("-mprage")
    if openmp is not None:
        cargs.extend([
            "-openmp",
            str(openmp)
        ])
    if parallel:
        cargs.append("-parallel")
    if subject_id is not None:
        cargs.extend([
            "-subjid",
            subject_id
        ])
    cargs.extend([
        "-sd",
        execution.input_file(subjects_dir)
    ])
    if talairach is not None:
        cargs.append(talairach)
    if use_flair:
        cargs.append("-FLAIRpial")
    if use_t2:
        cargs.append("-T2pial")
    if xopts is not None:
        cargs.extend([
            "-xopts-",
            xopts
        ])
    ret = ReconAllOutputs_(
        root=execution.output_file("."),
        subjects_dir_outfile=execution.output_file("file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RECON_ALL_METADATA_",
    "ReconAllOutputs_",
    "recon_all_",
]

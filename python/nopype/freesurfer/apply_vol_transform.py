# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


APPLY_VOL_TRANSFORM_METADATA = Metadata(
    id="465660307dcc5a6670714a363e3aaad86063aa04",
    name="ApplyVolTransform",
    container_image_type="docker",
    container_image_tag="container/image",
)


class ApplyVolTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apply_vol_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_file_outfile: OutputPathType | None
    """Path to output file if used normally."""


def apply_vol_transform(
    runner: Runner,
    fs_target: bool = False,
    fsl_reg_file: InputPathType | None = None,
    interp: typing.Literal["trilin", "nearest", "cubic"] | None = None,
    inverse: bool = False,
    invert_morph: bool = False,
    lta_file: InputPathType | None = None,
    lta_inv_file: InputPathType | None = None,
    m3z_file: InputPathType | None = None,
    mni_152_reg: bool = False,
    no_def_m3z_path: bool = False,
    no_resample: bool = False,
    reg_file: InputPathType | None = None,
    reg_header: bool = False,
    source_file: InputPathType | None = None,
    subject: str | None = None,
    subjects_dir: InputPathType | None = None,
    tal: bool = False,
    tal_resolution: float | int | None = None,
    target_file: InputPathType | None = None,
    transformed_file: InputPathType | None = None,
    xfm_reg_file: InputPathType | None = None,
) -> ApplyVolTransformOutputs:
    """
    ApplyVolTransform by Members of the Laboratories for Computational Neuroimaging
    (LCN) at the Athinoula A. Martinos Center for Biomedical Imaging.
    
    Resamples a volume into another field-of-view using varous types of matrices
    (FreeSurfer, FSL, SPM, and MNI).
    
    More information: https://surfer.nmr.mgh.harvard.edu/fswiki/mri_vol2vol
    
    Args:
        runner: Command runner
        fs_target: Use orig.mgz from subject in regfile as target.
        fsl_reg_file: Fslras-to-fslras matrix (fsl format).
        interp: 'trilin' or 'nearest' or 'cubic'. Interpolation method (<trilin>
            or nearest).
        inverse: Sample from target to source.
        invert_morph: Compute and use the inverse of the non-linear morph to
            resample the input volume. to be used by --m3z.
        lta_file: Linear transform array file.
        lta_inv_file: Lta, invert.
        m3z_file: This is the morph to be applied to the volume. unless the
            morph is in mri/transforms (eg.: for talairach.m3z computed by
            reconall), you will need to specify the full path to this morph and use
            the --nodefm3zpath flag.
        mni_152_reg: Target mni152 space.
        no_def_m3z_path: To be used with the m3z flag. Instructs the code not to
            look for the non-linear m3z morph in the default location
            (subjects_dir/subj/mri/transforms), but instead just use the path
            indicated in --m3z.
        no_resample: Do not resample; just change vox2ras matrix.
        reg_file: Tkras-to-tkras matrix (tkregister2 format).
        reg_header: Scannerras-to-scannerras matrix = identity.
        source_file: Input volume you wish to transform.
        subject: Set matrix = identity and use subject for any templates.
        subjects_dir: file or string representing an existing directory.
            Subjects directory.
        tal: Map to a sub fov of mni305 (with --reg only).
        tal_resolution: Resolution to sample when using tal.
        target_file: Output template volume.
        transformed_file: Output volume.
        xfm_reg_file: Scannerras-to-scannerras matrix (mni format).
    Returns:
        NamedTuple of outputs (described in `ApplyVolTransformOutputs`).
    """
    if (
        tal +
        fs_target +
        (target_file is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "tal,\n"
            "fs_target,\n"
            "target_file"
        )
    if (
        (subject is not None) +
        (lta_file is not None) +
        (xfm_reg_file is not None) +
        mni_152_reg +
        (reg_file is not None) +
        (lta_inv_file is not None) +
        reg_header +
        (fsl_reg_file is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "subject,\n"
            "lta_file,\n"
            "xfm_reg_file,\n"
            "mni_152_reg,\n"
            "reg_file,\n"
            "lta_inv_file,\n"
            "reg_header,\n"
            "fsl_reg_file"
        )
    if not (
        tal or
        fs_target or
        (target_file is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- tal\n"
            "- fs_target\n"
            "- target_file"
        )
    if not (
        (subject is not None) or
        (lta_file is not None) or
        (xfm_reg_file is not None) or
        mni_152_reg or
        (reg_file is not None) or
        (lta_inv_file is not None) or
        reg_header or
        (fsl_reg_file is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- subject\n"
            "- lta_file\n"
            "- xfm_reg_file\n"
            "- mni_152_reg\n"
            "- reg_file\n"
            "- lta_inv_file\n"
            "- reg_header\n"
            "- fsl_reg_file"
        )
    execution = runner.start_execution(APPLY_VOL_TRANSFORM_METADATA)
    cargs = []
    cargs.append("mri_vol2vol")
    if fs_target:
        cargs.append("--fstarg")
    if fsl_reg_file is not None:
        cargs.extend(["--fsl", execution.input_file(fsl_reg_file)])
    if interp is not None:
        cargs.extend(["--interp", interp])
    if inverse:
        cargs.append("--inv")
    if invert_morph:
        cargs.append("--inv-morph")
    if lta_file is not None:
        cargs.extend(["--lta", execution.input_file(lta_file)])
    if lta_inv_file is not None:
        cargs.extend(["--lta-inv", execution.input_file(lta_inv_file)])
    if m3z_file is not None:
        cargs.extend(["--m3z", execution.input_file(m3z_file)])
    if mni_152_reg:
        cargs.append("--regheader")
    if no_def_m3z_path:
        cargs.append("--noDefM3zPath")
    if no_resample:
        cargs.append("--no-resample")
    if reg_file is not None:
        cargs.extend(["--reg", execution.input_file(reg_file)])
    if reg_header:
        cargs.append("--regheader")
    if source_file is not None:
        cargs.extend(["--mov", execution.input_file(source_file)])
    if subject is not None:
        cargs.extend(["--s", subject])
    if subjects_dir is not None:
        cargs.append(execution.input_file(subjects_dir))
    if tal:
        cargs.append("--tal")
    if tal_resolution is not None:
        cargs.extend(["--talres", str(tal_resolution)])
    if target_file is not None:
        cargs.extend(["--targ", execution.input_file(target_file)])
    if transformed_file is not None:
        cargs.extend(["--o", execution.input_file(transformed_file)])
    if xfm_reg_file is not None:
        cargs.extend(["--xfm", execution.input_file(xfm_reg_file)])
    ret = ApplyVolTransformOutputs(
        root=execution.output_file("."),
        transformed_file_outfile=execution.output_file(f"{pathlib.Path(transformed_file).stem}.nii.gz", optional=True) if transformed_file is not None else None,
    )
    execution.run(cargs)
    return ret

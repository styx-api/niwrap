# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_ANNOTATION2LABEL_METADATA = Metadata(
    id="90b6d8bcd55a8d08f2bccdf11454197b855e2864.boutiques",
    name="mri_annotation2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriAnnotation2labelParameters = typing.TypedDict('MriAnnotation2labelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_annotation2label"],
    "subject": str,
    "hemi": str,
    "lobes": typing.NotRequired[InputPathType | None],
    "lobes_strict": typing.NotRequired[InputPathType | None],
    "lobes_strict_phcg": typing.NotRequired[InputPathType | None],
    "label": typing.NotRequired[float | None],
    "labelbase": typing.NotRequired[str | None],
    "outdir": typing.NotRequired[str | None],
    "seg": typing.NotRequired[InputPathType | None],
    "segbase": typing.NotRequired[float | None],
    "ctab": typing.NotRequired[InputPathType | None],
    "border": typing.NotRequired[InputPathType | None],
    "border_annot": typing.NotRequired[str | None],
    "annotation": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "surface": typing.NotRequired[str | None],
    "stat": typing.NotRequired[InputPathType | None],
    "help": bool,
    "version": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_annotation2label": mri_annotation2label_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class MriAnnotation2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_annotation2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_annotation2label_params(
    subject: str,
    hemi: str,
    lobes: InputPathType | None = None,
    lobes_strict: InputPathType | None = None,
    lobes_strict_phcg: InputPathType | None = None,
    label: float | None = None,
    labelbase: str | None = None,
    outdir: str | None = None,
    seg: InputPathType | None = None,
    segbase: float | None = None,
    ctab: InputPathType | None = None,
    border: InputPathType | None = None,
    border_annot: str | None = None,
    annotation: str | None = None,
    subjects_dir: str | None = None,
    surface: str | None = None,
    stat_: InputPathType | None = None,
    help_: bool = False,
    version: bool = False,
) -> MriAnnotation2labelParameters:
    """
    Build parameters.
    
    Args:
        subject: Source subject.
        hemi: Hemisphere (lh or rh) with surface.
        lobes: Create an annotation based on cortical lobes, saved to\
            <LobesFile>.
        lobes_strict: Use a stricter lobe definition with precentral added to\
            'frontal' and postcentral with 'parietal', saved to <LobesFile>.
        lobes_strict_phcg: Use a stricter lobe definition with an additional\
            lobe 'parahippocampalgyrus', saved to <LobesFile>.
        label: Extract only single label.
        labelbase: Output will be base-XXX.label.
        outdir: Output will be in dir/hemi.name.label.
        seg: Output will be a segmentation volume.
        segbase: Add base to the annotation number to get segmentation value.
        ctab: Color table, like FreeSurferColorLUT.txt.
        border: Output will be a binary overlay of the parc borders.
        border_annot: Default goes in subject/label.
        annotation: As found in SUBJDIR/labels <aparc>.
        subjects_dir: Specify SUBJECTS_DIR on the command line.
        surface: Name of surface <white>. Only affect xyz in label.
        stat_: Surface overlay file (curv or volume format).
        help_: Display help.
        version: Display version.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_annotation2label",
        "subject": subject,
        "hemi": hemi,
        "help": help_,
        "version": version,
    }
    if lobes is not None:
        params["lobes"] = lobes
    if lobes_strict is not None:
        params["lobes_strict"] = lobes_strict
    if lobes_strict_phcg is not None:
        params["lobes_strict_phcg"] = lobes_strict_phcg
    if label is not None:
        params["label"] = label
    if labelbase is not None:
        params["labelbase"] = labelbase
    if outdir is not None:
        params["outdir"] = outdir
    if seg is not None:
        params["seg"] = seg
    if segbase is not None:
        params["segbase"] = segbase
    if ctab is not None:
        params["ctab"] = ctab
    if border is not None:
        params["border"] = border
    if border_annot is not None:
        params["border_annot"] = border_annot
    if annotation is not None:
        params["annotation"] = annotation
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if surface is not None:
        params["surface"] = surface
    if stat_ is not None:
        params["stat"] = stat_
    return params


def mri_annotation2label_cargs(
    params: MriAnnotation2labelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_annotation2label")
    cargs.extend([
        "--subject",
        params.get("subject")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemi")
    ])
    if params.get("lobes") is not None:
        cargs.extend([
            "--lobes",
            execution.input_file(params.get("lobes"))
        ])
    if params.get("lobes_strict") is not None:
        cargs.extend([
            "--lobesStrict",
            execution.input_file(params.get("lobes_strict"))
        ])
    if params.get("lobes_strict_phcg") is not None:
        cargs.extend([
            "--lobesStrictPHCG",
            execution.input_file(params.get("lobes_strict_phcg"))
        ])
    if params.get("label") is not None:
        cargs.extend([
            "--label",
            str(params.get("label"))
        ])
    if params.get("labelbase") is not None:
        cargs.extend([
            "--labelbase",
            params.get("labelbase")
        ])
    if params.get("outdir") is not None:
        cargs.extend([
            "--outdir",
            params.get("outdir")
        ])
    if params.get("seg") is not None:
        cargs.extend([
            "--seg",
            execution.input_file(params.get("seg"))
        ])
    if params.get("segbase") is not None:
        cargs.extend([
            "--segbase",
            str(params.get("segbase"))
        ])
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab"))
        ])
    if params.get("border") is not None:
        cargs.extend([
            "--border",
            execution.input_file(params.get("border"))
        ])
    if params.get("border_annot") is not None:
        cargs.extend([
            "--border-annot",
            params.get("border_annot")
        ])
    if params.get("annotation") is not None:
        cargs.extend([
            "--annotation",
            params.get("annotation")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("surface") is not None:
        cargs.extend([
            "--surface",
            params.get("surface")
        ])
    if params.get("stat") is not None:
        cargs.extend([
            "--stat",
            execution.input_file(params.get("stat"))
        ])
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_annotation2label_outputs(
    params: MriAnnotation2labelParameters,
    execution: Execution,
) -> MriAnnotation2labelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriAnnotation2labelOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_annotation2label_execute(
    params: MriAnnotation2labelParameters,
    execution: Execution,
) -> MriAnnotation2labelOutputs:
    """
    Convert an annotation into multiple label files or into a segmentation volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriAnnotation2labelOutputs`).
    """
    cargs = mri_annotation2label_cargs(params, execution)
    ret = mri_annotation2label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_annotation2label(
    subject: str,
    hemi: str,
    lobes: InputPathType | None = None,
    lobes_strict: InputPathType | None = None,
    lobes_strict_phcg: InputPathType | None = None,
    label: float | None = None,
    labelbase: str | None = None,
    outdir: str | None = None,
    seg: InputPathType | None = None,
    segbase: float | None = None,
    ctab: InputPathType | None = None,
    border: InputPathType | None = None,
    border_annot: str | None = None,
    annotation: str | None = None,
    subjects_dir: str | None = None,
    surface: str | None = None,
    stat_: InputPathType | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriAnnotation2labelOutputs:
    """
    Convert an annotation into multiple label files or into a segmentation volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Source subject.
        hemi: Hemisphere (lh or rh) with surface.
        lobes: Create an annotation based on cortical lobes, saved to\
            <LobesFile>.
        lobes_strict: Use a stricter lobe definition with precentral added to\
            'frontal' and postcentral with 'parietal', saved to <LobesFile>.
        lobes_strict_phcg: Use a stricter lobe definition with an additional\
            lobe 'parahippocampalgyrus', saved to <LobesFile>.
        label: Extract only single label.
        labelbase: Output will be base-XXX.label.
        outdir: Output will be in dir/hemi.name.label.
        seg: Output will be a segmentation volume.
        segbase: Add base to the annotation number to get segmentation value.
        ctab: Color table, like FreeSurferColorLUT.txt.
        border: Output will be a binary overlay of the parc borders.
        border_annot: Default goes in subject/label.
        annotation: As found in SUBJDIR/labels <aparc>.
        subjects_dir: Specify SUBJECTS_DIR on the command line.
        surface: Name of surface <white>. Only affect xyz in label.
        stat_: Surface overlay file (curv or volume format).
        help_: Display help.
        version: Display version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAnnotation2labelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ANNOTATION2LABEL_METADATA)
    params = mri_annotation2label_params(subject=subject, hemi=hemi, lobes=lobes, lobes_strict=lobes_strict, lobes_strict_phcg=lobes_strict_phcg, label=label, labelbase=labelbase, outdir=outdir, seg=seg, segbase=segbase, ctab=ctab, border=border, border_annot=border_annot, annotation=annotation, subjects_dir=subjects_dir, surface=surface, stat_=stat_, help_=help_, version=version)
    return mri_annotation2label_execute(params, execution)


__all__ = [
    "MRI_ANNOTATION2LABEL_METADATA",
    "MriAnnotation2labelOutputs",
    "MriAnnotation2labelParameters",
    "mri_annotation2label",
    "mri_annotation2label_params",
]

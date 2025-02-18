# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_CA_TRAIN_METADATA = Metadata(
    id="8e70a6159e0a5ec42aaae4b7bcd8282432b8dd18.boutiques",
    name="mris_ca_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisCaTrainParameters = typing.TypedDict('MrisCaTrainParameters', {
    "__STYX_TYPE__": typing.Literal["mris_ca_train"],
    "hemi": str,
    "canonsurf": InputPathType,
    "annot_file": InputPathType,
    "subjects": list[str],
    "output_file": str,
    "sdir": typing.NotRequired[str | None],
    "nbrs": typing.NotRequired[float | None],
    "orig": typing.NotRequired[InputPathType | None],
    "norm1": bool,
    "norm2": bool,
    "norm3": bool,
    "ic": typing.NotRequired[str | None],
    "sulc": bool,
    "sulconly": bool,
    "a": typing.NotRequired[float | None],
    "parcellation_table": typing.NotRequired[InputPathType | None],
    "n": typing.NotRequired[float | None],
    "verbose": typing.NotRequired[float | None],
    "debug_vertex": typing.NotRequired[float | None],
    "gcs_means": typing.NotRequired[str | None],
    "gcs_priors": typing.NotRequired[str | None],
    "gcs_diff": typing.NotRequired[str | None],
    "nfill": typing.NotRequired[float | None],
    "no_fill": bool,
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
        "mris_ca_train": mris_ca_train_cargs,
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
        "mris_ca_train": mris_ca_train_outputs,
    }.get(t)


class MrisCaTrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_ca_train(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Classifier array output file generated by mris_ca_train"""


def mris_ca_train_params(
    hemi: str,
    canonsurf: InputPathType,
    annot_file: InputPathType,
    subjects: list[str],
    output_file: str,
    sdir: str | None = None,
    nbrs: float | None = None,
    orig: InputPathType | None = None,
    norm1: bool = False,
    norm2: bool = False,
    norm3: bool = False,
    ic: str | None = None,
    sulc: bool = False,
    sulconly: bool = False,
    a: float | None = None,
    parcellation_table: InputPathType | None = None,
    n: float | None = None,
    verbose: float | None = None,
    debug_vertex: float | None = None,
    gcs_means: str | None = None,
    gcs_priors: str | None = None,
    gcs_diff: str | None = None,
    nfill: float | None = None,
    no_fill: bool = False,
    help_: bool = False,
    version: bool = False,
) -> MrisCaTrainParameters:
    """
    Build parameters.
    
    Args:
        hemi: Hemisphere: rh or lh.
        canonsurf: Canonical surface filename.
        annot_file: Annotation filename.
        subjects: List of subject ids.
        output_file: Classifier array output file.
        sdir: Directory as subjects directory (default: $SUBJECTS_DIR).
        nbrs: Neighborhood size (default=2).
        orig: Filename of original surface (default=smoothwm).
        norm1: GCSA normalize input #1 after reading (default: disabled).
        norm2: GCSA normalize input #2 after reading (default: disabled).
        norm3: GCSA normalize input #3 after reading (default: disabled).
        ic: Parameters passed to the classifier routine (default: -ic 7 4).
        sulc: Specify sulc as only input (default: sulcus and curvature).
        sulconly: Same as -sulc.
        a: Number of nearest neighbor smoothing iterations to apply to input 1\
            (default=5).
        parcellation_table: Parcellation table input file (default: none).
        n: Number of inputs (default=1,max=3).
        verbose: Diagnostic level (default=0).
        debug_vertex: Debug diagnostic level for a specific vertex (default=0).
        gcs_means: Extract likelihood means for all classes for given input.
        gcs_priors: Extract priors for all classes for given input.
        gcs_diff: Determine whether GCSAs are different.
        nfill: Set the max number of iterations for filling empty vertices.
        no_fill: Do not fill at all.
        help_: Print help info.
        version: Print version info.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_ca_train",
        "hemi": hemi,
        "canonsurf": canonsurf,
        "annot_file": annot_file,
        "subjects": subjects,
        "output_file": output_file,
        "norm1": norm1,
        "norm2": norm2,
        "norm3": norm3,
        "sulc": sulc,
        "sulconly": sulconly,
        "no_fill": no_fill,
        "help": help_,
        "version": version,
    }
    if sdir is not None:
        params["sdir"] = sdir
    if nbrs is not None:
        params["nbrs"] = nbrs
    if orig is not None:
        params["orig"] = orig
    if ic is not None:
        params["ic"] = ic
    if a is not None:
        params["a"] = a
    if parcellation_table is not None:
        params["parcellation_table"] = parcellation_table
    if n is not None:
        params["n"] = n
    if verbose is not None:
        params["verbose"] = verbose
    if debug_vertex is not None:
        params["debug_vertex"] = debug_vertex
    if gcs_means is not None:
        params["gcs_means"] = gcs_means
    if gcs_priors is not None:
        params["gcs_priors"] = gcs_priors
    if gcs_diff is not None:
        params["gcs_diff"] = gcs_diff
    if nfill is not None:
        params["nfill"] = nfill
    return params


def mris_ca_train_cargs(
    params: MrisCaTrainParameters,
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
    cargs.append("mris_ca_train")
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("canonsurf")))
    cargs.append(execution.input_file(params.get("annot_file")))
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_file"))
    if params.get("sdir") is not None:
        cargs.extend([
            "-sdir",
            params.get("sdir")
        ])
    if params.get("nbrs") is not None:
        cargs.extend([
            "-nbrs",
            str(params.get("nbrs"))
        ])
    if params.get("orig") is not None:
        cargs.extend([
            "-orig",
            execution.input_file(params.get("orig"))
        ])
    if params.get("norm1"):
        cargs.append("-norm1")
    if params.get("norm2"):
        cargs.append("-norm2")
    if params.get("norm3"):
        cargs.append("-norm3")
    if params.get("ic") is not None:
        cargs.extend([
            "-ic",
            params.get("ic")
        ])
    if params.get("sulc"):
        cargs.append("-sulc")
    if params.get("sulconly"):
        cargs.append("-sulconly")
    if params.get("a") is not None:
        cargs.extend([
            "-a",
            str(params.get("a"))
        ])
    if params.get("parcellation_table") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("parcellation_table"))
        ])
    if params.get("n") is not None:
        cargs.extend([
            "-n",
            str(params.get("n"))
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "-v",
            str(params.get("verbose"))
        ])
    if params.get("debug_vertex") is not None:
        cargs.extend([
            "-debug-vertex",
            str(params.get("debug_vertex"))
        ])
    if params.get("gcs_means") is not None:
        cargs.extend([
            "-gcs-means",
            params.get("gcs_means")
        ])
    if params.get("gcs_priors") is not None:
        cargs.extend([
            "-gcs-priors",
            params.get("gcs_priors")
        ])
    if params.get("gcs_diff") is not None:
        cargs.extend([
            "-gcs-diff",
            params.get("gcs_diff")
        ])
    if params.get("nfill") is not None:
        cargs.extend([
            "-nfill",
            str(params.get("nfill"))
        ])
    if params.get("no_fill"):
        cargs.append("-no-fill")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mris_ca_train_outputs(
    params: MrisCaTrainParameters,
    execution: Execution,
) -> MrisCaTrainOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisCaTrainOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def mris_ca_train_execute(
    params: MrisCaTrainParameters,
    execution: Execution,
) -> MrisCaTrainOutputs:
    """
    Creates a cortical parcellation atlas file based on one or more annotated
    subjects using probabilistic information.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisCaTrainOutputs`).
    """
    cargs = mris_ca_train_cargs(params, execution)
    ret = mris_ca_train_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mris_ca_train(
    hemi: str,
    canonsurf: InputPathType,
    annot_file: InputPathType,
    subjects: list[str],
    output_file: str,
    sdir: str | None = None,
    nbrs: float | None = None,
    orig: InputPathType | None = None,
    norm1: bool = False,
    norm2: bool = False,
    norm3: bool = False,
    ic: str | None = None,
    sulc: bool = False,
    sulconly: bool = False,
    a: float | None = None,
    parcellation_table: InputPathType | None = None,
    n: float | None = None,
    verbose: float | None = None,
    debug_vertex: float | None = None,
    gcs_means: str | None = None,
    gcs_priors: str | None = None,
    gcs_diff: str | None = None,
    nfill: float | None = None,
    no_fill: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrisCaTrainOutputs:
    """
    Creates a cortical parcellation atlas file based on one or more annotated
    subjects using probabilistic information.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere: rh or lh.
        canonsurf: Canonical surface filename.
        annot_file: Annotation filename.
        subjects: List of subject ids.
        output_file: Classifier array output file.
        sdir: Directory as subjects directory (default: $SUBJECTS_DIR).
        nbrs: Neighborhood size (default=2).
        orig: Filename of original surface (default=smoothwm).
        norm1: GCSA normalize input #1 after reading (default: disabled).
        norm2: GCSA normalize input #2 after reading (default: disabled).
        norm3: GCSA normalize input #3 after reading (default: disabled).
        ic: Parameters passed to the classifier routine (default: -ic 7 4).
        sulc: Specify sulc as only input (default: sulcus and curvature).
        sulconly: Same as -sulc.
        a: Number of nearest neighbor smoothing iterations to apply to input 1\
            (default=5).
        parcellation_table: Parcellation table input file (default: none).
        n: Number of inputs (default=1,max=3).
        verbose: Diagnostic level (default=0).
        debug_vertex: Debug diagnostic level for a specific vertex (default=0).
        gcs_means: Extract likelihood means for all classes for given input.
        gcs_priors: Extract priors for all classes for given input.
        gcs_diff: Determine whether GCSAs are different.
        nfill: Set the max number of iterations for filling empty vertices.
        no_fill: Do not fill at all.
        help_: Print help info.
        version: Print version info.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCaTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CA_TRAIN_METADATA)
    params = mris_ca_train_params(hemi=hemi, canonsurf=canonsurf, annot_file=annot_file, subjects=subjects, output_file=output_file, sdir=sdir, nbrs=nbrs, orig=orig, norm1=norm1, norm2=norm2, norm3=norm3, ic=ic, sulc=sulc, sulconly=sulconly, a=a, parcellation_table=parcellation_table, n=n, verbose=verbose, debug_vertex=debug_vertex, gcs_means=gcs_means, gcs_priors=gcs_priors, gcs_diff=gcs_diff, nfill=nfill, no_fill=no_fill, help_=help_, version=version)
    return mris_ca_train_execute(params, execution)


__all__ = [
    "MRIS_CA_TRAIN_METADATA",
    "MrisCaTrainOutputs",
    "MrisCaTrainParameters",
    "mris_ca_train",
    "mris_ca_train_params",
]

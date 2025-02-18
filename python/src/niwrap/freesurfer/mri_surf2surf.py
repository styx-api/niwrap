# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SURF2SURF_METADATA = Metadata(
    id="d67a0abaca8f23d784a32410fdaa560c5667746c.boutiques",
    name="mri_surf2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSurf2surfParameters = typing.TypedDict('MriSurf2surfParameters', {
    "__STYX_TYPE__": typing.Literal["mri_surf2surf"],
    "src_subject": str,
    "sval_path": typing.NotRequired[InputPathType | None],
    "sval_xyz": typing.NotRequired[str | None],
    "projfrac": typing.NotRequired[list[str] | None],
    "projabs": typing.NotRequired[list[str] | None],
    "sval_tal_xyz": typing.NotRequired[str | None],
    "sval_area": typing.NotRequired[str | None],
    "sval_annot": typing.NotRequired[InputPathType | None],
    "sval_nxyz": typing.NotRequired[str | None],
    "patch": typing.NotRequired[list[str] | None],
    "sfmt": typing.NotRequired[str | None],
    "reg": typing.NotRequired[list[str] | None],
    "reg_inv": typing.NotRequired[list[str] | None],
    "srcicoorder": typing.NotRequired[int | None],
    "trg_subject": str,
    "trgicoorder": typing.NotRequired[int | None],
    "tval_path": typing.NotRequired[str | None],
    "tval_xyz": typing.NotRequired[str | None],
    "tfmt": typing.NotRequired[str | None],
    "trg_dist": typing.NotRequired[str | None],
    "s": typing.NotRequired[str | None],
    "hemi": typing.NotRequired[str | None],
    "src_hemi": typing.NotRequired[str | None],
    "trg_hemi": typing.NotRequired[str | None],
    "dual_hemi": bool,
    "jac": bool,
    "surfreg": typing.NotRequired[str | None],
    "src_surfreg": typing.NotRequired[str | None],
    "trg_surfreg": typing.NotRequired[str | None],
    "mapmethod": typing.NotRequired[str | None],
    "frame": typing.NotRequired[int | None],
    "fwhm_src": typing.NotRequired[float | None],
    "fwhm_trg": typing.NotRequired[float | None],
    "nsmooth_in": typing.NotRequired[int | None],
    "nsmooth_out": typing.NotRequired[int | None],
    "cortex": bool,
    "no_cortex": bool,
    "label_src": typing.NotRequired[InputPathType | None],
    "label_trg": typing.NotRequired[InputPathType | None],
    "mul": typing.NotRequired[float | None],
    "div": typing.NotRequired[float | None],
    "reshape": bool,
    "reshape_factor": typing.NotRequired[int | None],
    "reshape3d": bool,
    "split": bool,
    "synth": bool,
    "ones": bool,
    "normvar": bool,
    "seed": typing.NotRequired[int | None],
    "prune": bool,
    "no_prune": bool,
    "proj_surf": typing.NotRequired[list[str] | None],
    "proj_norm": typing.NotRequired[list[str] | None],
    "reg_diff": typing.NotRequired[str | None],
    "rms": typing.NotRequired[InputPathType | None],
    "rms_mask": typing.NotRequired[InputPathType | None],
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
        "mri_surf2surf": mri_surf2surf_cargs,
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
        "mri_surf2surf": mri_surf2surf_outputs,
    }.get(t)


class MriSurf2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_surf2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_values: OutputPathType | None
    """File in which to store output values."""
    trg_distances: OutputPathType | None
    """File containing distances from source to target vertices."""


def mri_surf2surf_params(
    src_subject: str,
    trg_subject: str,
    sval_path: InputPathType | None = None,
    sval_xyz: str | None = None,
    projfrac: list[str] | None = None,
    projabs: list[str] | None = None,
    sval_tal_xyz: str | None = None,
    sval_area: str | None = None,
    sval_annot: InputPathType | None = None,
    sval_nxyz: str | None = None,
    patch: list[str] | None = None,
    sfmt: str | None = None,
    reg: list[str] | None = None,
    reg_inv: list[str] | None = None,
    srcicoorder: int | None = None,
    trgicoorder: int | None = None,
    tval_path: str | None = None,
    tval_xyz: str | None = None,
    tfmt: str | None = None,
    trg_dist: str | None = None,
    s: str | None = None,
    hemi: str | None = None,
    src_hemi: str | None = None,
    trg_hemi: str | None = None,
    dual_hemi: bool = False,
    jac: bool = False,
    surfreg: str | None = None,
    src_surfreg: str | None = None,
    trg_surfreg: str | None = None,
    mapmethod: str | None = None,
    frame: int | None = None,
    fwhm_src: float | None = None,
    fwhm_trg: float | None = None,
    nsmooth_in: int | None = None,
    nsmooth_out: int | None = None,
    cortex: bool = False,
    no_cortex: bool = False,
    label_src: InputPathType | None = None,
    label_trg: InputPathType | None = None,
    mul: float | None = None,
    div: float | None = None,
    reshape: bool = False,
    reshape_factor: int | None = None,
    reshape3d: bool = False,
    split: bool = False,
    synth: bool = False,
    ones: bool = False,
    normvar: bool = False,
    seed: int | None = None,
    prune: bool = False,
    no_prune: bool = False,
    proj_surf: list[str] | None = None,
    proj_norm: list[str] | None = None,
    reg_diff: str | None = None,
    rms: InputPathType | None = None,
    rms_mask: InputPathType | None = None,
) -> MriSurf2surfParameters:
    """
    Build parameters.
    
    Args:
        src_subject: Name of source subject as found in $SUBJECTS_DIR or ico\
            for icosahedron.
        trg_subject: Name of target subject as found in $SUBJECTS_DIR or ico\
            for icosahedron.
        sval_path: Path of the file with input values.
        sval_xyz: Use xyz of a surface as input.
        projfrac: Use projected xyz of a surface as input.
        projabs: Use projected xyz absolute of a surface as input.
        sval_tal_xyz: Use tal xyz of a surface as input.
        sval_area: Use vertex area of a surface as input.
        sval_annot: Map annotation file.
        sval_nxyz: Use surface normals of a surface as input.
        patch: Specify source patch file, target surface and number of\
            dilations.
        sfmt: Source format type string.
        reg: Apply registration file to sval-xyz.
        reg_inv: Apply inverse registration file to sval-xyz.
        srcicoorder: Icosahedron order for the source.
        trgicoorder: Icosahedron order for the target.
        tval_path: Path of the file in which to store output values.
        tval_xyz: Save target value as a surface file with source xyz.
        tfmt: Target format type string.
        trg_dist: Save distance from source to target vertices.
        s: Use the same subject for both source and target.
        hemi: Hemisphere for both source and target (lh or rh).
        src_hemi: Hemisphere for source (lh or rh).
        trg_hemi: Hemisphere for target (lh or rh).
        dual_hemi: Assume source ?h.?h.surfreg file name.
        jac: Turn on jacobian correction, needed when applying to area or\
            volume.
        surfreg: Surface registration for source and target (sphere.reg).
        src_surfreg: Source surface registration (sphere.reg).
        trg_surfreg: Target surface registration (sphere.reg).
        mapmethod: Method used to map from the vertices in one subject to\
            another (nnfr or nnf).
        frame: Save only nth frame (when using paint output format).
        fwhm_src: Smooth the source to given FWHM.
        fwhm_trg: Smooth the target to given FWHM.
        nsmooth_in: Number of smoothing iterations for input.
        nsmooth_out: Number of smoothing iterations for output.
        cortex: Use ?h.cortex.label as a smoothing mask.
        no_cortex: Do NOT use ?h.cortex.label as a smoothing mask (default).
        label_src: Source smoothing mask.
        label_trg: Target smoothing mask.
        mul: Multiply the input by the given value.
        div: Divide the input by the given value.
        reshape: Reshape output to multiple 'slices'.
        reshape_factor: Reshape to Nfactor 'slices'.
        reshape3d: Reshape fsaverage (ico7) into 42 x 47 x 83.
        split: Output each frame separately.
        synth: Replace input with white Gaussian noise.
        ones: Replace input with 1s.
        normvar: Rescale so that stddev=1 (good with --synth).
        seed: Seed for synth (default is auto).
        prune: Remove any voxel that is zero in any time point (for smoothing).
        no_prune: Do not prune (default).
        proj_surf: Project vertices by mag*scale at each vertex.
        proj_norm: Project vertices by distmm at each vertex.
        reg_diff: Subtract reg2 from --reg (primarily for testing).
        rms: Save RMS of reg1-reg2 (primarily for testing).
        rms_mask: Compute RMS in mask (primarily for testing).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_surf2surf",
        "src_subject": src_subject,
        "trg_subject": trg_subject,
        "dual_hemi": dual_hemi,
        "jac": jac,
        "cortex": cortex,
        "no_cortex": no_cortex,
        "reshape": reshape,
        "reshape3d": reshape3d,
        "split": split,
        "synth": synth,
        "ones": ones,
        "normvar": normvar,
        "prune": prune,
        "no_prune": no_prune,
    }
    if sval_path is not None:
        params["sval_path"] = sval_path
    if sval_xyz is not None:
        params["sval_xyz"] = sval_xyz
    if projfrac is not None:
        params["projfrac"] = projfrac
    if projabs is not None:
        params["projabs"] = projabs
    if sval_tal_xyz is not None:
        params["sval_tal_xyz"] = sval_tal_xyz
    if sval_area is not None:
        params["sval_area"] = sval_area
    if sval_annot is not None:
        params["sval_annot"] = sval_annot
    if sval_nxyz is not None:
        params["sval_nxyz"] = sval_nxyz
    if patch is not None:
        params["patch"] = patch
    if sfmt is not None:
        params["sfmt"] = sfmt
    if reg is not None:
        params["reg"] = reg
    if reg_inv is not None:
        params["reg_inv"] = reg_inv
    if srcicoorder is not None:
        params["srcicoorder"] = srcicoorder
    if trgicoorder is not None:
        params["trgicoorder"] = trgicoorder
    if tval_path is not None:
        params["tval_path"] = tval_path
    if tval_xyz is not None:
        params["tval_xyz"] = tval_xyz
    if tfmt is not None:
        params["tfmt"] = tfmt
    if trg_dist is not None:
        params["trg_dist"] = trg_dist
    if s is not None:
        params["s"] = s
    if hemi is not None:
        params["hemi"] = hemi
    if src_hemi is not None:
        params["src_hemi"] = src_hemi
    if trg_hemi is not None:
        params["trg_hemi"] = trg_hemi
    if surfreg is not None:
        params["surfreg"] = surfreg
    if src_surfreg is not None:
        params["src_surfreg"] = src_surfreg
    if trg_surfreg is not None:
        params["trg_surfreg"] = trg_surfreg
    if mapmethod is not None:
        params["mapmethod"] = mapmethod
    if frame is not None:
        params["frame"] = frame
    if fwhm_src is not None:
        params["fwhm_src"] = fwhm_src
    if fwhm_trg is not None:
        params["fwhm_trg"] = fwhm_trg
    if nsmooth_in is not None:
        params["nsmooth_in"] = nsmooth_in
    if nsmooth_out is not None:
        params["nsmooth_out"] = nsmooth_out
    if label_src is not None:
        params["label_src"] = label_src
    if label_trg is not None:
        params["label_trg"] = label_trg
    if mul is not None:
        params["mul"] = mul
    if div is not None:
        params["div"] = div
    if reshape_factor is not None:
        params["reshape_factor"] = reshape_factor
    if seed is not None:
        params["seed"] = seed
    if proj_surf is not None:
        params["proj_surf"] = proj_surf
    if proj_norm is not None:
        params["proj_norm"] = proj_norm
    if reg_diff is not None:
        params["reg_diff"] = reg_diff
    if rms is not None:
        params["rms"] = rms
    if rms_mask is not None:
        params["rms_mask"] = rms_mask
    return params


def mri_surf2surf_cargs(
    params: MriSurf2surfParameters,
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
    cargs.append("mri_surf2surf")
    cargs.extend([
        "--srcsubject",
        params.get("src_subject")
    ])
    if params.get("sval_path") is not None:
        cargs.extend([
            "--sval",
            execution.input_file(params.get("sval_path"))
        ])
    if params.get("sval_xyz") is not None:
        cargs.extend([
            "--sval-xyz",
            params.get("sval_xyz")
        ])
    if params.get("projfrac") is not None:
        cargs.extend([
            "--projfrac",
            *params.get("projfrac")
        ])
    if params.get("projabs") is not None:
        cargs.extend([
            "--projabs",
            *params.get("projabs")
        ])
    if params.get("sval_tal_xyz") is not None:
        cargs.extend([
            "--sval-tal-xyz",
            params.get("sval_tal_xyz")
        ])
    if params.get("sval_area") is not None:
        cargs.extend([
            "--sval-area",
            params.get("sval_area")
        ])
    if params.get("sval_annot") is not None:
        cargs.extend([
            "--sval-annot",
            execution.input_file(params.get("sval_annot"))
        ])
    if params.get("sval_nxyz") is not None:
        cargs.extend([
            "--sval-nxyz",
            params.get("sval_nxyz")
        ])
    if params.get("patch") is not None:
        cargs.extend([
            "--patch",
            *params.get("patch")
        ])
    if params.get("sfmt") is not None:
        cargs.extend([
            "--sfmt",
            params.get("sfmt")
        ])
    if params.get("reg") is not None:
        cargs.extend([
            "--reg",
            *params.get("reg")
        ])
    if params.get("reg_inv") is not None:
        cargs.extend([
            "--reg-inv",
            *params.get("reg_inv")
        ])
    if params.get("srcicoorder") is not None:
        cargs.extend([
            "--srcicoorder",
            str(params.get("srcicoorder"))
        ])
    cargs.extend([
        "--trgsubject",
        params.get("trg_subject")
    ])
    if params.get("trgicoorder") is not None:
        cargs.extend([
            "--trgicoorder",
            str(params.get("trgicoorder"))
        ])
    if params.get("tval_path") is not None:
        cargs.extend([
            "--tval",
            params.get("tval_path")
        ])
    if params.get("tval_xyz") is not None:
        cargs.extend([
            "--tval-xyz",
            params.get("tval_xyz")
        ])
    if params.get("tfmt") is not None:
        cargs.extend([
            "--tfmt",
            params.get("tfmt")
        ])
    if params.get("trg_dist") is not None:
        cargs.extend([
            "--trgdist",
            params.get("trg_dist")
        ])
    if params.get("s") is not None:
        cargs.extend([
            "--s",
            params.get("s")
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("src_hemi") is not None:
        cargs.extend([
            "--srchemi",
            params.get("src_hemi")
        ])
    if params.get("trg_hemi") is not None:
        cargs.extend([
            "--trghemi",
            params.get("trg_hemi")
        ])
    if params.get("dual_hemi"):
        cargs.append("--dual-hemi")
    if params.get("jac"):
        cargs.append("--jac")
    if params.get("surfreg") is not None:
        cargs.extend([
            "--surfreg",
            params.get("surfreg")
        ])
    if params.get("src_surfreg") is not None:
        cargs.extend([
            "--srcsurfreg",
            params.get("src_surfreg")
        ])
    if params.get("trg_surfreg") is not None:
        cargs.extend([
            "--trgsurfreg",
            params.get("trg_surfreg")
        ])
    if params.get("mapmethod") is not None:
        cargs.extend([
            "--mapmethod",
            params.get("mapmethod")
        ])
    if params.get("frame") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame"))
        ])
    if params.get("fwhm_src") is not None:
        cargs.extend([
            "--fwhm-src",
            str(params.get("fwhm_src"))
        ])
    if params.get("fwhm_trg") is not None:
        cargs.extend([
            "--fwhm-trg",
            str(params.get("fwhm_trg"))
        ])
    if params.get("nsmooth_in") is not None:
        cargs.extend([
            "--nsmooth-in",
            str(params.get("nsmooth_in"))
        ])
    if params.get("nsmooth_out") is not None:
        cargs.extend([
            "--nsmooth-out",
            str(params.get("nsmooth_out"))
        ])
    if params.get("cortex"):
        cargs.append("--cortex")
    if params.get("no_cortex"):
        cargs.append("--no-cortex")
    if params.get("label_src") is not None:
        cargs.extend([
            "--label-src",
            execution.input_file(params.get("label_src"))
        ])
    if params.get("label_trg") is not None:
        cargs.extend([
            "--label-trg",
            execution.input_file(params.get("label_trg"))
        ])
    if params.get("mul") is not None:
        cargs.extend([
            "--mul",
            str(params.get("mul"))
        ])
    if params.get("div") is not None:
        cargs.extend([
            "--div",
            str(params.get("div"))
        ])
    if params.get("reshape"):
        cargs.append("--reshape")
    if params.get("reshape_factor") is not None:
        cargs.extend([
            "--reshape-factor",
            str(params.get("reshape_factor"))
        ])
    if params.get("reshape3d"):
        cargs.append("--reshape3d")
    if params.get("split"):
        cargs.append("--split")
    if params.get("synth"):
        cargs.append("--synth")
    if params.get("ones"):
        cargs.append("--ones")
    if params.get("normvar"):
        cargs.append("--normvar")
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("prune"):
        cargs.append("--prune")
    if params.get("no_prune"):
        cargs.append("--no-prune")
    if params.get("proj_surf") is not None:
        cargs.extend([
            "--proj-surf",
            *params.get("proj_surf")
        ])
    if params.get("proj_norm") is not None:
        cargs.extend([
            "--proj-norm",
            *params.get("proj_norm")
        ])
    if params.get("reg_diff") is not None:
        cargs.extend([
            "--reg-diff",
            params.get("reg_diff")
        ])
    if params.get("rms") is not None:
        cargs.extend([
            "--rms",
            execution.input_file(params.get("rms"))
        ])
    if params.get("rms_mask") is not None:
        cargs.extend([
            "--rms-mask",
            execution.input_file(params.get("rms_mask"))
        ])
    return cargs


def mri_surf2surf_outputs(
    params: MriSurf2surfParameters,
    execution: Execution,
) -> MriSurf2surfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSurf2surfOutputs(
        root=execution.output_file("."),
        output_values=execution.output_file(params.get("tval_path")) if (params.get("tval_path") is not None) else None,
        trg_distances=execution.output_file(params.get("trg_dist")) if (params.get("trg_dist") is not None) else None,
    )
    return ret


def mri_surf2surf_execute(
    params: MriSurf2surfParameters,
    execution: Execution,
) -> MriSurf2surfOutputs:
    """
    Resample one surface onto another using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSurf2surfOutputs`).
    """
    cargs = mri_surf2surf_cargs(params, execution)
    ret = mri_surf2surf_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mri_surf2surf(
    src_subject: str,
    trg_subject: str,
    sval_path: InputPathType | None = None,
    sval_xyz: str | None = None,
    projfrac: list[str] | None = None,
    projabs: list[str] | None = None,
    sval_tal_xyz: str | None = None,
    sval_area: str | None = None,
    sval_annot: InputPathType | None = None,
    sval_nxyz: str | None = None,
    patch: list[str] | None = None,
    sfmt: str | None = None,
    reg: list[str] | None = None,
    reg_inv: list[str] | None = None,
    srcicoorder: int | None = None,
    trgicoorder: int | None = None,
    tval_path: str | None = None,
    tval_xyz: str | None = None,
    tfmt: str | None = None,
    trg_dist: str | None = None,
    s: str | None = None,
    hemi: str | None = None,
    src_hemi: str | None = None,
    trg_hemi: str | None = None,
    dual_hemi: bool = False,
    jac: bool = False,
    surfreg: str | None = None,
    src_surfreg: str | None = None,
    trg_surfreg: str | None = None,
    mapmethod: str | None = None,
    frame: int | None = None,
    fwhm_src: float | None = None,
    fwhm_trg: float | None = None,
    nsmooth_in: int | None = None,
    nsmooth_out: int | None = None,
    cortex: bool = False,
    no_cortex: bool = False,
    label_src: InputPathType | None = None,
    label_trg: InputPathType | None = None,
    mul: float | None = None,
    div: float | None = None,
    reshape: bool = False,
    reshape_factor: int | None = None,
    reshape3d: bool = False,
    split: bool = False,
    synth: bool = False,
    ones: bool = False,
    normvar: bool = False,
    seed: int | None = None,
    prune: bool = False,
    no_prune: bool = False,
    proj_surf: list[str] | None = None,
    proj_norm: list[str] | None = None,
    reg_diff: str | None = None,
    rms: InputPathType | None = None,
    rms_mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriSurf2surfOutputs:
    """
    Resample one surface onto another using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_subject: Name of source subject as found in $SUBJECTS_DIR or ico\
            for icosahedron.
        trg_subject: Name of target subject as found in $SUBJECTS_DIR or ico\
            for icosahedron.
        sval_path: Path of the file with input values.
        sval_xyz: Use xyz of a surface as input.
        projfrac: Use projected xyz of a surface as input.
        projabs: Use projected xyz absolute of a surface as input.
        sval_tal_xyz: Use tal xyz of a surface as input.
        sval_area: Use vertex area of a surface as input.
        sval_annot: Map annotation file.
        sval_nxyz: Use surface normals of a surface as input.
        patch: Specify source patch file, target surface and number of\
            dilations.
        sfmt: Source format type string.
        reg: Apply registration file to sval-xyz.
        reg_inv: Apply inverse registration file to sval-xyz.
        srcicoorder: Icosahedron order for the source.
        trgicoorder: Icosahedron order for the target.
        tval_path: Path of the file in which to store output values.
        tval_xyz: Save target value as a surface file with source xyz.
        tfmt: Target format type string.
        trg_dist: Save distance from source to target vertices.
        s: Use the same subject for both source and target.
        hemi: Hemisphere for both source and target (lh or rh).
        src_hemi: Hemisphere for source (lh or rh).
        trg_hemi: Hemisphere for target (lh or rh).
        dual_hemi: Assume source ?h.?h.surfreg file name.
        jac: Turn on jacobian correction, needed when applying to area or\
            volume.
        surfreg: Surface registration for source and target (sphere.reg).
        src_surfreg: Source surface registration (sphere.reg).
        trg_surfreg: Target surface registration (sphere.reg).
        mapmethod: Method used to map from the vertices in one subject to\
            another (nnfr or nnf).
        frame: Save only nth frame (when using paint output format).
        fwhm_src: Smooth the source to given FWHM.
        fwhm_trg: Smooth the target to given FWHM.
        nsmooth_in: Number of smoothing iterations for input.
        nsmooth_out: Number of smoothing iterations for output.
        cortex: Use ?h.cortex.label as a smoothing mask.
        no_cortex: Do NOT use ?h.cortex.label as a smoothing mask (default).
        label_src: Source smoothing mask.
        label_trg: Target smoothing mask.
        mul: Multiply the input by the given value.
        div: Divide the input by the given value.
        reshape: Reshape output to multiple 'slices'.
        reshape_factor: Reshape to Nfactor 'slices'.
        reshape3d: Reshape fsaverage (ico7) into 42 x 47 x 83.
        split: Output each frame separately.
        synth: Replace input with white Gaussian noise.
        ones: Replace input with 1s.
        normvar: Rescale so that stddev=1 (good with --synth).
        seed: Seed for synth (default is auto).
        prune: Remove any voxel that is zero in any time point (for smoothing).
        no_prune: Do not prune (default).
        proj_surf: Project vertices by mag*scale at each vertex.
        proj_norm: Project vertices by distmm at each vertex.
        reg_diff: Subtract reg2 from --reg (primarily for testing).
        rms: Save RMS of reg1-reg2 (primarily for testing).
        rms_mask: Compute RMS in mask (primarily for testing).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSurf2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SURF2SURF_METADATA)
    params = mri_surf2surf_params(src_subject=src_subject, sval_path=sval_path, sval_xyz=sval_xyz, projfrac=projfrac, projabs=projabs, sval_tal_xyz=sval_tal_xyz, sval_area=sval_area, sval_annot=sval_annot, sval_nxyz=sval_nxyz, patch=patch, sfmt=sfmt, reg=reg, reg_inv=reg_inv, srcicoorder=srcicoorder, trg_subject=trg_subject, trgicoorder=trgicoorder, tval_path=tval_path, tval_xyz=tval_xyz, tfmt=tfmt, trg_dist=trg_dist, s=s, hemi=hemi, src_hemi=src_hemi, trg_hemi=trg_hemi, dual_hemi=dual_hemi, jac=jac, surfreg=surfreg, src_surfreg=src_surfreg, trg_surfreg=trg_surfreg, mapmethod=mapmethod, frame=frame, fwhm_src=fwhm_src, fwhm_trg=fwhm_trg, nsmooth_in=nsmooth_in, nsmooth_out=nsmooth_out, cortex=cortex, no_cortex=no_cortex, label_src=label_src, label_trg=label_trg, mul=mul, div=div, reshape=reshape, reshape_factor=reshape_factor, reshape3d=reshape3d, split=split, synth=synth, ones=ones, normvar=normvar, seed=seed, prune=prune, no_prune=no_prune, proj_surf=proj_surf, proj_norm=proj_norm, reg_diff=reg_diff, rms=rms, rms_mask=rms_mask)
    return mri_surf2surf_execute(params, execution)


__all__ = [
    "MRI_SURF2SURF_METADATA",
    "MriSurf2surfOutputs",
    "MriSurf2surfParameters",
    "mri_surf2surf",
    "mri_surf2surf_params",
]

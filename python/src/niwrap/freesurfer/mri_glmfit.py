# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_GLMFIT_METADATA = Metadata(
    id="79f830582903b4c568e10c98abbe12709997f2f4.boutiques",
    name="mri_glmfit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriGlmfitParameters = typing.TypedDict('MriGlmfitParameters', {
    "__STYX_TYPE__": typing.Literal["mri_glmfit"],
    "glmdir": typing.NotRequired[str | None],
    "y_input": InputPathType,
    "table_input": typing.NotRequired[InputPathType | None],
    "fsgd": typing.NotRequired[InputPathType | None],
    "design_matrix": typing.NotRequired[InputPathType | None],
    "contrast_matrix": typing.NotRequired[list[InputPathType] | None],
    "osgm_flag": bool,
    "no_contrasts_ok_flag": bool,
    "dti_params": typing.NotRequired[list[str] | None],
    "dti_matrix": typing.NotRequired[InputPathType | None],
    "pvr": typing.NotRequired[list[InputPathType] | None],
    "selfreg": typing.NotRequired[list[float] | None],
    "wls": typing.NotRequired[str | None],
    "yffxvar": typing.NotRequired[InputPathType | None],
    "ffxdof": typing.NotRequired[float | None],
    "ffxdofdat": typing.NotRequired[InputPathType | None],
    "weight": typing.NotRequired[InputPathType | None],
    "weight_inv_flag": bool,
    "weight_sqrt_flag": bool,
    "fwhm": typing.NotRequired[float | None],
    "var_fwhm": typing.NotRequired[float | None],
    "no_mask_smooth_flag": bool,
    "no_est_fwhm_flag": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "label": typing.NotRequired[InputPathType | None],
    "no_mask_flag": bool,
    "no_cortex_flag": bool,
    "mask_inv_flag": bool,
    "prune_flag": bool,
    "no_prune_flag": bool,
    "logy_flag": bool,
    "no_logy_flag": bool,
    "rm_spatial_mean_flag": bool,
    "yhat_save_flag": bool,
    "eres_save_flag": bool,
    "eres_scm_flag": bool,
    "save_fwhm_map_flag": bool,
    "y_out": typing.NotRequired[InputPathType | None],
    "surface": typing.NotRequired[str | None],
    "skew_flag": bool,
    "kurtosis_flag": bool,
    "sim_params": typing.NotRequired[list[str] | None],
    "sim_sign": typing.NotRequired[str | None],
    "uniform_params": typing.NotRequired[list[str] | None],
    "permute_input_flag": bool,
    "pca_flag": bool,
    "tar1_flag": bool,
    "save_yhat_flag": bool,
    "save_cond_flag": bool,
    "voxdump": typing.NotRequired[list[float] | None],
    "seed": typing.NotRequired[float | None],
    "synth_flag": bool,
    "resynthtest_it": typing.NotRequired[float | None],
    "profile_it": typing.NotRequired[float | None],
    "mrtm1_params": typing.NotRequired[list[str] | None],
    "mrtm2_params": typing.NotRequired[list[str] | None],
    "logan_params": typing.NotRequired[list[str] | None],
    "bp_clip_neg_flag": bool,
    "bp_clip_max": typing.NotRequired[float | None],
    "perm_force_flag": bool,
    "diag_level": typing.NotRequired[float | None],
    "diag_cluster_flag": bool,
    "debug_flag": bool,
    "checkopts_flag": bool,
    "help_flag": bool,
    "version_flag": bool,
    "no_fix_vertex_area_flag": bool,
    "allowsubjrep_flag": bool,
    "allow_zero_dof_flag": bool,
    "illcond_flag": bool,
    "sim_done_file": typing.NotRequired[InputPathType | None],
    "no_sig_double_flag": bool,
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
        "mri_glmfit": mri_glmfit_cargs,
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
        "mri_glmfit": mri_glmfit_outputs,
    }.get(t)


class MriGlmfitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_glmfit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    regression_coefs: OutputPathType
    """All regression coefficients (B)."""
    residual_error: OutputPathType
    """Residual error."""
    residual_variance: OutputPathType
    """Residual error variance."""
    residual_stddev: OutputPathType
    """Residual error standard deviation."""
    fsgd_output: OutputPathType
    """FSGD file if one was input."""
    normalized_weights: OutputPathType
    """Normalized weights with --w or --wls."""
    signal_estimate: OutputPathType
    """Signal estimate with --save-yhat."""
    final_mask: OutputPathType
    """Final mask when a mask is used."""
    design_condition: OutputPathType
    """Design matrix condition at each voxel with --save-cond."""
    contrast_output_dir: OutputPathType
    """Directory for each contrast output files."""


def mri_glmfit_params(
    y_input: InputPathType,
    glmdir: str | None = None,
    table_input: InputPathType | None = None,
    fsgd: InputPathType | None = None,
    design_matrix: InputPathType | None = None,
    contrast_matrix: list[InputPathType] | None = None,
    osgm_flag: bool = False,
    no_contrasts_ok_flag: bool = False,
    dti_params: list[str] | None = None,
    dti_matrix: InputPathType | None = None,
    pvr: list[InputPathType] | None = None,
    selfreg: list[float] | None = None,
    wls: str | None = None,
    yffxvar: InputPathType | None = None,
    ffxdof: float | None = None,
    ffxdofdat: InputPathType | None = None,
    weight: InputPathType | None = None,
    weight_inv_flag: bool = False,
    weight_sqrt_flag: bool = False,
    fwhm: float | None = None,
    var_fwhm: float | None = None,
    no_mask_smooth_flag: bool = False,
    no_est_fwhm_flag: bool = False,
    mask: InputPathType | None = None,
    label: InputPathType | None = None,
    no_mask_flag: bool = False,
    no_cortex_flag: bool = False,
    mask_inv_flag: bool = False,
    prune_flag: bool = False,
    no_prune_flag: bool = False,
    logy_flag: bool = False,
    no_logy_flag: bool = False,
    rm_spatial_mean_flag: bool = False,
    yhat_save_flag: bool = False,
    eres_save_flag: bool = False,
    eres_scm_flag: bool = False,
    save_fwhm_map_flag: bool = False,
    y_out: InputPathType | None = None,
    surface: str | None = None,
    skew_flag: bool = False,
    kurtosis_flag: bool = False,
    sim_params: list[str] | None = None,
    sim_sign: str | None = None,
    uniform_params: list[str] | None = None,
    permute_input_flag: bool = False,
    pca_flag: bool = False,
    tar1_flag: bool = False,
    save_yhat_flag: bool = False,
    save_cond_flag: bool = False,
    voxdump: list[float] | None = None,
    seed: float | None = None,
    synth_flag: bool = False,
    resynthtest_it: float | None = None,
    profile_it: float | None = None,
    mrtm1_params: list[str] | None = None,
    mrtm2_params: list[str] | None = None,
    logan_params: list[str] | None = None,
    bp_clip_neg_flag: bool = False,
    bp_clip_max: float | None = None,
    perm_force_flag: bool = False,
    diag_level: float | None = None,
    diag_cluster_flag: bool = False,
    debug_flag: bool = False,
    checkopts_flag: bool = False,
    help_flag: bool = False,
    version_flag: bool = False,
    no_fix_vertex_area_flag: bool = False,
    allowsubjrep_flag: bool = False,
    allow_zero_dof_flag: bool = False,
    illcond_flag: bool = False,
    sim_done_file: InputPathType | None = None,
    no_sig_double_flag: bool = False,
) -> MriGlmfitParameters:
    """
    Build parameters.
    
    Args:
        y_input: Path to input file where each frame is a separate input.\
            Accepts volume or surface-based formats.
        glmdir: Directory where output will be saved.
        table_input: Use text table as input instead of --y. Table should be of\
            form produced by asegstats2table or aparcstats2table.
        fsgd: Specify the global design matrix with a FreeSurfer Group\
            Descriptor File (FSGDF).
        design_matrix: Explicitly specify the design matrix. Can be in simple\
            text or in matlab4 format.
        contrast_matrix: Specify one or more contrasts to test. File should be\
            ASCII text with the contrast matrix.
        osgm_flag: Construct X and C as a one-sample group mean.
        no_contrasts_ok_flag: Do not fail if no contrasts are specified.
        dti_params: Do DTI analysis using bvals and bvecs.
        dti_matrix: Do DTI analysis using provided matrix.
        pvr: Per-voxel (or vertex) regressors.
        selfreg: Create a 'self-regressor' from the input data based on the\
            waveform at index col row slice.
        wls: Perform weighted least squares (WLS) random effects analysis\
            instead of ordinary least squares (OLS) using yffxvar.
        yffxvar: For fixed effects analysis.
        ffxdof: Degrees of Freedom (DOF) for fixed effects analysis.
        ffxdofdat: Text file with DOF for fixed effects analysis.
        weight: Perform weighted LMS using per-voxel weights from the\
            weightfile.
        weight_inv_flag: Invert weights.
        weight_sqrt_flag: Square root of (inverted) weights.
        fwhm: Smooth input with a Gaussian kernel, specified in mm.
        var_fwhm: Smooth residual variance map with a Gaussian kernel,\
            specified in mm.
        no_mask_smooth_flag: Do not mask when smoothing.
        no_est_fwhm_flag: Turn off FWHM output estimation.
        mask: Binary mask file for analysis.
        label: Use label as mask for surface data.
        no_mask_flag: Do NOT use a mask, same as --no-cortex.
        no_cortex_flag: Do NOT use subjects ?h.cortex.label as --label.
        mask_inv_flag: Invert mask for analysis.
        prune_flag: Remove voxels that do not have a non-zero value at each\
            frame.
        no_prune_flag: Do not prune zero-value voxels.
        logy_flag: Compute natural log of y prior to analysis.
        no_logy_flag: Do not compute natural log of y prior to analysis.
        rm_spatial_mean_flag: Subtract the (masked) mean from each frame.
        yhat_save_flag: Save signal estimate (yhat).
        eres_save_flag: Save residual error (eres).
        eres_scm_flag: Save residual error spatial correlation matrix\
            (eres.scm).
        save_fwhm_map_flag: Save voxel-wise map of FWHM estimates.
        y_out: Save input after any pre-processing.
        surface: Specify that the input has a surface geometry from the\
            hemisphere of the given FreeSurfer subject. Required for surface data\
            operations.
        skew_flag: Compute skew and p-value for skew.
        kurtosis_flag: Compute kurtosis and p-value for kurtosis.
        sim_params: Simulate data for statistical testing. Specify nulltype,\
            number of simulations, threshold and csd basename.
        sim_sign: Specify sign for simulation: abs, pos, or neg.
        uniform_params: Use uniform distribution for mc-full, specify min and\
            max.
        permute_input_flag: Permute input for testing purposes (not related to\
            simulation).
        pca_flag: Perform PCA/SVD analysis on the residual.
        tar1_flag: Compute and save temporal AR1 of residual.
        save_yhat_flag: Flag to save the signal estimate.
        save_cond_flag: Flag to save design matrix condition at each voxel.
        voxdump: Save GLM data for a single voxel at the specified col, row,\
            slice.
        seed: Use seed for random number generation.
        synth_flag: Replace input data with Gaussian noise for testing.
        resynthtest_it: Test GLM by resynthsis with the number of iterations\
            specified.
        profile_it: Test speed with specified number of iterations.
        mrtm1_params: Perform MRTM1 kinetic modeling with specified reference\
            tissue activity and time in seconds.
        mrtm2_params: Perform MRTM2 kinetic modeling with specified parameters.
        logan_params: Perform Logan kinetic modeling with specified parameters.
        bp_clip_neg_flag: Set negative BP voxels to 0.
        bp_clip_max: Set BP voxels above max to max.
        perm_force_flag: Force permutation test, even when design matrix is not\
            orthogonal.
        diag_level: Set diagnostic level.
        diag_cluster_flag: Save significant volume and exit from first\
            simulation loop.
        debug_flag: Turn on debugging mode.
        checkopts_flag: Check options and exit without executing.
        help_flag: Display help information.
        version_flag: Print out version and exit.
        no_fix_vertex_area_flag: Turn off fixing of vertex area (backward\
            compatibility).
        allowsubjrep_flag: Allow subject names to repeat in the fsgd file.
        allow_zero_dof_flag: Allow analyses with zero degrees of freedom.
        illcond_flag: Allow ill-conditioned design matrices.
        sim_done_file: Create done file when simulation finishes.
        no_sig_double_flag: Compute sig = -log10(p) from float p value, not\
            double.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_glmfit",
        "y_input": y_input,
        "osgm_flag": osgm_flag,
        "no_contrasts_ok_flag": no_contrasts_ok_flag,
        "weight_inv_flag": weight_inv_flag,
        "weight_sqrt_flag": weight_sqrt_flag,
        "no_mask_smooth_flag": no_mask_smooth_flag,
        "no_est_fwhm_flag": no_est_fwhm_flag,
        "no_mask_flag": no_mask_flag,
        "no_cortex_flag": no_cortex_flag,
        "mask_inv_flag": mask_inv_flag,
        "prune_flag": prune_flag,
        "no_prune_flag": no_prune_flag,
        "logy_flag": logy_flag,
        "no_logy_flag": no_logy_flag,
        "rm_spatial_mean_flag": rm_spatial_mean_flag,
        "yhat_save_flag": yhat_save_flag,
        "eres_save_flag": eres_save_flag,
        "eres_scm_flag": eres_scm_flag,
        "save_fwhm_map_flag": save_fwhm_map_flag,
        "skew_flag": skew_flag,
        "kurtosis_flag": kurtosis_flag,
        "permute_input_flag": permute_input_flag,
        "pca_flag": pca_flag,
        "tar1_flag": tar1_flag,
        "save_yhat_flag": save_yhat_flag,
        "save_cond_flag": save_cond_flag,
        "synth_flag": synth_flag,
        "bp_clip_neg_flag": bp_clip_neg_flag,
        "perm_force_flag": perm_force_flag,
        "diag_cluster_flag": diag_cluster_flag,
        "debug_flag": debug_flag,
        "checkopts_flag": checkopts_flag,
        "help_flag": help_flag,
        "version_flag": version_flag,
        "no_fix_vertex_area_flag": no_fix_vertex_area_flag,
        "allowsubjrep_flag": allowsubjrep_flag,
        "allow_zero_dof_flag": allow_zero_dof_flag,
        "illcond_flag": illcond_flag,
        "no_sig_double_flag": no_sig_double_flag,
    }
    if glmdir is not None:
        params["glmdir"] = glmdir
    if table_input is not None:
        params["table_input"] = table_input
    if fsgd is not None:
        params["fsgd"] = fsgd
    if design_matrix is not None:
        params["design_matrix"] = design_matrix
    if contrast_matrix is not None:
        params["contrast_matrix"] = contrast_matrix
    if dti_params is not None:
        params["dti_params"] = dti_params
    if dti_matrix is not None:
        params["dti_matrix"] = dti_matrix
    if pvr is not None:
        params["pvr"] = pvr
    if selfreg is not None:
        params["selfreg"] = selfreg
    if wls is not None:
        params["wls"] = wls
    if yffxvar is not None:
        params["yffxvar"] = yffxvar
    if ffxdof is not None:
        params["ffxdof"] = ffxdof
    if ffxdofdat is not None:
        params["ffxdofdat"] = ffxdofdat
    if weight is not None:
        params["weight"] = weight
    if fwhm is not None:
        params["fwhm"] = fwhm
    if var_fwhm is not None:
        params["var_fwhm"] = var_fwhm
    if mask is not None:
        params["mask"] = mask
    if label is not None:
        params["label"] = label
    if y_out is not None:
        params["y_out"] = y_out
    if surface is not None:
        params["surface"] = surface
    if sim_params is not None:
        params["sim_params"] = sim_params
    if sim_sign is not None:
        params["sim_sign"] = sim_sign
    if uniform_params is not None:
        params["uniform_params"] = uniform_params
    if voxdump is not None:
        params["voxdump"] = voxdump
    if seed is not None:
        params["seed"] = seed
    if resynthtest_it is not None:
        params["resynthtest_it"] = resynthtest_it
    if profile_it is not None:
        params["profile_it"] = profile_it
    if mrtm1_params is not None:
        params["mrtm1_params"] = mrtm1_params
    if mrtm2_params is not None:
        params["mrtm2_params"] = mrtm2_params
    if logan_params is not None:
        params["logan_params"] = logan_params
    if bp_clip_max is not None:
        params["bp_clip_max"] = bp_clip_max
    if diag_level is not None:
        params["diag_level"] = diag_level
    if sim_done_file is not None:
        params["sim_done_file"] = sim_done_file
    return params


def mri_glmfit_cargs(
    params: MriGlmfitParameters,
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
    cargs.append("mri_glmfit")
    if params.get("glmdir") is not None:
        cargs.extend([
            "--glmdir",
            params.get("glmdir")
        ])
    cargs.extend([
        "--y",
        execution.input_file(params.get("y_input"))
    ])
    if params.get("table_input") is not None:
        cargs.extend([
            "--table",
            execution.input_file(params.get("table_input"))
        ])
    if params.get("fsgd") is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(params.get("fsgd"))
        ])
    if params.get("design_matrix") is not None:
        cargs.extend([
            "--X",
            execution.input_file(params.get("design_matrix"))
        ])
    if params.get("contrast_matrix") is not None:
        cargs.extend([
            "--C",
            *[execution.input_file(f) for f in params.get("contrast_matrix")]
        ])
    if params.get("osgm_flag"):
        cargs.append("--osgm")
    if params.get("no_contrasts_ok_flag"):
        cargs.append("--no-contrasts-ok")
    if params.get("dti_params") is not None:
        cargs.extend([
            "--dti",
            *params.get("dti_params")
        ])
    if params.get("dti_matrix") is not None:
        cargs.extend([
            "--dti-X",
            execution.input_file(params.get("dti_matrix"))
        ])
    if params.get("pvr") is not None:
        cargs.extend([
            "--pvr",
            *[execution.input_file(f) for f in params.get("pvr")]
        ])
    if params.get("selfreg") is not None:
        cargs.extend([
            "--selfreg",
            *map(str, params.get("selfreg"))
        ])
    if params.get("wls") is not None:
        cargs.extend([
            "--wls",
            params.get("wls")
        ])
    if params.get("yffxvar") is not None:
        cargs.extend([
            "--yffxvar",
            execution.input_file(params.get("yffxvar"))
        ])
    if params.get("ffxdof") is not None:
        cargs.extend([
            "--ffxdof",
            str(params.get("ffxdof"))
        ])
    if params.get("ffxdofdat") is not None:
        cargs.extend([
            "--ffxdofdat",
            execution.input_file(params.get("ffxdofdat"))
        ])
    if params.get("weight") is not None:
        cargs.extend([
            "--w",
            execution.input_file(params.get("weight"))
        ])
    if params.get("weight_inv_flag"):
        cargs.append("--w-inv")
    if params.get("weight_sqrt_flag"):
        cargs.append("--w-sqrt")
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("var_fwhm") is not None:
        cargs.extend([
            "--var-fwhm",
            str(params.get("var_fwhm"))
        ])
    if params.get("no_mask_smooth_flag"):
        cargs.append("--no-mask-smooth")
    if params.get("no_est_fwhm_flag"):
        cargs.append("--no-est-fwhm")
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("label") is not None:
        cargs.extend([
            "--label",
            execution.input_file(params.get("label"))
        ])
    if params.get("no_mask_flag"):
        cargs.append("--no-mask")
    if params.get("no_cortex_flag"):
        cargs.append("--no-cortex")
    if params.get("mask_inv_flag"):
        cargs.append("--mask-inv")
    if params.get("prune_flag"):
        cargs.append("--prune")
    if params.get("no_prune_flag"):
        cargs.append("--no-prune")
    if params.get("logy_flag"):
        cargs.append("--logy")
    if params.get("no_logy_flag"):
        cargs.append("--no-logy")
    if params.get("rm_spatial_mean_flag"):
        cargs.append("--rm-spatial-mean")
    if params.get("yhat_save_flag"):
        cargs.append("--yhat-save")
    if params.get("eres_save_flag"):
        cargs.append("--eres-save")
    if params.get("eres_scm_flag"):
        cargs.append("--eres-scm")
    if params.get("save_fwhm_map_flag"):
        cargs.append("--save-fwhm-map")
    if params.get("y_out") is not None:
        cargs.extend([
            "--y-out",
            execution.input_file(params.get("y_out"))
        ])
    if params.get("surface") is not None:
        cargs.extend([
            "--surf",
            params.get("surface")
        ])
    if params.get("skew_flag"):
        cargs.append("--skew")
    if params.get("kurtosis_flag"):
        cargs.append("--kurtosis")
    if params.get("sim_params") is not None:
        cargs.extend([
            "--sim",
            *params.get("sim_params")
        ])
    if params.get("sim_sign") is not None:
        cargs.extend([
            "--sim-sign",
            params.get("sim_sign")
        ])
    if params.get("uniform_params") is not None:
        cargs.extend([
            "--uniform",
            *params.get("uniform_params")
        ])
    if params.get("permute_input_flag"):
        cargs.append("--permute-input")
    if params.get("pca_flag"):
        cargs.append("--pca")
    if params.get("tar1_flag"):
        cargs.append("--tar1")
    if params.get("save_yhat_flag"):
        cargs.append("--save-yhat")
    if params.get("save_cond_flag"):
        cargs.append("--save-cond")
    if params.get("voxdump") is not None:
        cargs.extend([
            "--voxdump",
            *map(str, params.get("voxdump"))
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("synth_flag"):
        cargs.append("--synth")
    if params.get("resynthtest_it") is not None:
        cargs.extend([
            "--resynthtest",
            str(params.get("resynthtest_it"))
        ])
    if params.get("profile_it") is not None:
        cargs.extend([
            "--profile",
            str(params.get("profile_it"))
        ])
    if params.get("mrtm1_params") is not None:
        cargs.extend([
            "--mrtm1",
            *params.get("mrtm1_params")
        ])
    if params.get("mrtm2_params") is not None:
        cargs.extend([
            "--mrtm2",
            *params.get("mrtm2_params")
        ])
    if params.get("logan_params") is not None:
        cargs.extend([
            "--logan",
            *params.get("logan_params")
        ])
    if params.get("bp_clip_neg_flag"):
        cargs.append("--bp-clip-neg")
    if params.get("bp_clip_max") is not None:
        cargs.extend([
            "--bp-clip-max",
            str(params.get("bp_clip_max"))
        ])
    if params.get("perm_force_flag"):
        cargs.append("--perm-force")
    if params.get("diag_level") is not None:
        cargs.extend([
            "--diag",
            str(params.get("diag_level"))
        ])
    if params.get("diag_cluster_flag"):
        cargs.append("--diag-cluster")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("checkopts_flag"):
        cargs.append("--checkopts")
    if params.get("help_flag"):
        cargs.append("--help")
    if params.get("version_flag"):
        cargs.append("--version")
    if params.get("no_fix_vertex_area_flag"):
        cargs.append("--no-fix-vertex-area")
    if params.get("allowsubjrep_flag"):
        cargs.append("--allowsubjrep")
    if params.get("allow_zero_dof_flag"):
        cargs.append("--allow-zero-dof")
    if params.get("illcond_flag"):
        cargs.append("--illcond")
    if params.get("sim_done_file") is not None:
        cargs.extend([
            "--sim-done",
            execution.input_file(params.get("sim_done_file"))
        ])
    if params.get("no_sig_double_flag"):
        cargs.append("--no-sig-double")
    return cargs


def mri_glmfit_outputs(
    params: MriGlmfitParameters,
    execution: Execution,
) -> MriGlmfitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGlmfitOutputs(
        root=execution.output_file("."),
        regression_coefs=execution.output_file("beta.mgh"),
        residual_error=execution.output_file("eres.mgh"),
        residual_variance=execution.output_file("rvar.mgh"),
        residual_stddev=execution.output_file("rstd.mgh"),
        fsgd_output=execution.output_file("y.fsgd"),
        normalized_weights=execution.output_file("wn.mgh"),
        signal_estimate=execution.output_file("yhat.mgh"),
        final_mask=execution.output_file("mask.mgh"),
        design_condition=execution.output_file("cond.mgh"),
        contrast_output_dir=execution.output_file("contrast1name"),
    )
    return ret


def mri_glmfit_execute(
    params: MriGlmfitParameters,
    execution: Execution,
) -> MriGlmfitOutputs:
    """
    Performs general linear model (GLM) analysis in the volume or the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGlmfitOutputs`).
    """
    params = execution.params(params)
    cargs = mri_glmfit_cargs(params, execution)
    ret = mri_glmfit_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_glmfit(
    y_input: InputPathType,
    glmdir: str | None = None,
    table_input: InputPathType | None = None,
    fsgd: InputPathType | None = None,
    design_matrix: InputPathType | None = None,
    contrast_matrix: list[InputPathType] | None = None,
    osgm_flag: bool = False,
    no_contrasts_ok_flag: bool = False,
    dti_params: list[str] | None = None,
    dti_matrix: InputPathType | None = None,
    pvr: list[InputPathType] | None = None,
    selfreg: list[float] | None = None,
    wls: str | None = None,
    yffxvar: InputPathType | None = None,
    ffxdof: float | None = None,
    ffxdofdat: InputPathType | None = None,
    weight: InputPathType | None = None,
    weight_inv_flag: bool = False,
    weight_sqrt_flag: bool = False,
    fwhm: float | None = None,
    var_fwhm: float | None = None,
    no_mask_smooth_flag: bool = False,
    no_est_fwhm_flag: bool = False,
    mask: InputPathType | None = None,
    label: InputPathType | None = None,
    no_mask_flag: bool = False,
    no_cortex_flag: bool = False,
    mask_inv_flag: bool = False,
    prune_flag: bool = False,
    no_prune_flag: bool = False,
    logy_flag: bool = False,
    no_logy_flag: bool = False,
    rm_spatial_mean_flag: bool = False,
    yhat_save_flag: bool = False,
    eres_save_flag: bool = False,
    eres_scm_flag: bool = False,
    save_fwhm_map_flag: bool = False,
    y_out: InputPathType | None = None,
    surface: str | None = None,
    skew_flag: bool = False,
    kurtosis_flag: bool = False,
    sim_params: list[str] | None = None,
    sim_sign: str | None = None,
    uniform_params: list[str] | None = None,
    permute_input_flag: bool = False,
    pca_flag: bool = False,
    tar1_flag: bool = False,
    save_yhat_flag: bool = False,
    save_cond_flag: bool = False,
    voxdump: list[float] | None = None,
    seed: float | None = None,
    synth_flag: bool = False,
    resynthtest_it: float | None = None,
    profile_it: float | None = None,
    mrtm1_params: list[str] | None = None,
    mrtm2_params: list[str] | None = None,
    logan_params: list[str] | None = None,
    bp_clip_neg_flag: bool = False,
    bp_clip_max: float | None = None,
    perm_force_flag: bool = False,
    diag_level: float | None = None,
    diag_cluster_flag: bool = False,
    debug_flag: bool = False,
    checkopts_flag: bool = False,
    help_flag: bool = False,
    version_flag: bool = False,
    no_fix_vertex_area_flag: bool = False,
    allowsubjrep_flag: bool = False,
    allow_zero_dof_flag: bool = False,
    illcond_flag: bool = False,
    sim_done_file: InputPathType | None = None,
    no_sig_double_flag: bool = False,
    runner: Runner | None = None,
) -> MriGlmfitOutputs:
    """
    Performs general linear model (GLM) analysis in the volume or the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        y_input: Path to input file where each frame is a separate input.\
            Accepts volume or surface-based formats.
        glmdir: Directory where output will be saved.
        table_input: Use text table as input instead of --y. Table should be of\
            form produced by asegstats2table or aparcstats2table.
        fsgd: Specify the global design matrix with a FreeSurfer Group\
            Descriptor File (FSGDF).
        design_matrix: Explicitly specify the design matrix. Can be in simple\
            text or in matlab4 format.
        contrast_matrix: Specify one or more contrasts to test. File should be\
            ASCII text with the contrast matrix.
        osgm_flag: Construct X and C as a one-sample group mean.
        no_contrasts_ok_flag: Do not fail if no contrasts are specified.
        dti_params: Do DTI analysis using bvals and bvecs.
        dti_matrix: Do DTI analysis using provided matrix.
        pvr: Per-voxel (or vertex) regressors.
        selfreg: Create a 'self-regressor' from the input data based on the\
            waveform at index col row slice.
        wls: Perform weighted least squares (WLS) random effects analysis\
            instead of ordinary least squares (OLS) using yffxvar.
        yffxvar: For fixed effects analysis.
        ffxdof: Degrees of Freedom (DOF) for fixed effects analysis.
        ffxdofdat: Text file with DOF for fixed effects analysis.
        weight: Perform weighted LMS using per-voxel weights from the\
            weightfile.
        weight_inv_flag: Invert weights.
        weight_sqrt_flag: Square root of (inverted) weights.
        fwhm: Smooth input with a Gaussian kernel, specified in mm.
        var_fwhm: Smooth residual variance map with a Gaussian kernel,\
            specified in mm.
        no_mask_smooth_flag: Do not mask when smoothing.
        no_est_fwhm_flag: Turn off FWHM output estimation.
        mask: Binary mask file for analysis.
        label: Use label as mask for surface data.
        no_mask_flag: Do NOT use a mask, same as --no-cortex.
        no_cortex_flag: Do NOT use subjects ?h.cortex.label as --label.
        mask_inv_flag: Invert mask for analysis.
        prune_flag: Remove voxels that do not have a non-zero value at each\
            frame.
        no_prune_flag: Do not prune zero-value voxels.
        logy_flag: Compute natural log of y prior to analysis.
        no_logy_flag: Do not compute natural log of y prior to analysis.
        rm_spatial_mean_flag: Subtract the (masked) mean from each frame.
        yhat_save_flag: Save signal estimate (yhat).
        eres_save_flag: Save residual error (eres).
        eres_scm_flag: Save residual error spatial correlation matrix\
            (eres.scm).
        save_fwhm_map_flag: Save voxel-wise map of FWHM estimates.
        y_out: Save input after any pre-processing.
        surface: Specify that the input has a surface geometry from the\
            hemisphere of the given FreeSurfer subject. Required for surface data\
            operations.
        skew_flag: Compute skew and p-value for skew.
        kurtosis_flag: Compute kurtosis and p-value for kurtosis.
        sim_params: Simulate data for statistical testing. Specify nulltype,\
            number of simulations, threshold and csd basename.
        sim_sign: Specify sign for simulation: abs, pos, or neg.
        uniform_params: Use uniform distribution for mc-full, specify min and\
            max.
        permute_input_flag: Permute input for testing purposes (not related to\
            simulation).
        pca_flag: Perform PCA/SVD analysis on the residual.
        tar1_flag: Compute and save temporal AR1 of residual.
        save_yhat_flag: Flag to save the signal estimate.
        save_cond_flag: Flag to save design matrix condition at each voxel.
        voxdump: Save GLM data for a single voxel at the specified col, row,\
            slice.
        seed: Use seed for random number generation.
        synth_flag: Replace input data with Gaussian noise for testing.
        resynthtest_it: Test GLM by resynthsis with the number of iterations\
            specified.
        profile_it: Test speed with specified number of iterations.
        mrtm1_params: Perform MRTM1 kinetic modeling with specified reference\
            tissue activity and time in seconds.
        mrtm2_params: Perform MRTM2 kinetic modeling with specified parameters.
        logan_params: Perform Logan kinetic modeling with specified parameters.
        bp_clip_neg_flag: Set negative BP voxels to 0.
        bp_clip_max: Set BP voxels above max to max.
        perm_force_flag: Force permutation test, even when design matrix is not\
            orthogonal.
        diag_level: Set diagnostic level.
        diag_cluster_flag: Save significant volume and exit from first\
            simulation loop.
        debug_flag: Turn on debugging mode.
        checkopts_flag: Check options and exit without executing.
        help_flag: Display help information.
        version_flag: Print out version and exit.
        no_fix_vertex_area_flag: Turn off fixing of vertex area (backward\
            compatibility).
        allowsubjrep_flag: Allow subject names to repeat in the fsgd file.
        allow_zero_dof_flag: Allow analyses with zero degrees of freedom.
        illcond_flag: Allow ill-conditioned design matrices.
        sim_done_file: Create done file when simulation finishes.
        no_sig_double_flag: Compute sig = -log10(p) from float p value, not\
            double.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGlmfitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GLMFIT_METADATA)
    params = mri_glmfit_params(
        glmdir=glmdir,
        y_input=y_input,
        table_input=table_input,
        fsgd=fsgd,
        design_matrix=design_matrix,
        contrast_matrix=contrast_matrix,
        osgm_flag=osgm_flag,
        no_contrasts_ok_flag=no_contrasts_ok_flag,
        dti_params=dti_params,
        dti_matrix=dti_matrix,
        pvr=pvr,
        selfreg=selfreg,
        wls=wls,
        yffxvar=yffxvar,
        ffxdof=ffxdof,
        ffxdofdat=ffxdofdat,
        weight=weight,
        weight_inv_flag=weight_inv_flag,
        weight_sqrt_flag=weight_sqrt_flag,
        fwhm=fwhm,
        var_fwhm=var_fwhm,
        no_mask_smooth_flag=no_mask_smooth_flag,
        no_est_fwhm_flag=no_est_fwhm_flag,
        mask=mask,
        label=label,
        no_mask_flag=no_mask_flag,
        no_cortex_flag=no_cortex_flag,
        mask_inv_flag=mask_inv_flag,
        prune_flag=prune_flag,
        no_prune_flag=no_prune_flag,
        logy_flag=logy_flag,
        no_logy_flag=no_logy_flag,
        rm_spatial_mean_flag=rm_spatial_mean_flag,
        yhat_save_flag=yhat_save_flag,
        eres_save_flag=eres_save_flag,
        eres_scm_flag=eres_scm_flag,
        save_fwhm_map_flag=save_fwhm_map_flag,
        y_out=y_out,
        surface=surface,
        skew_flag=skew_flag,
        kurtosis_flag=kurtosis_flag,
        sim_params=sim_params,
        sim_sign=sim_sign,
        uniform_params=uniform_params,
        permute_input_flag=permute_input_flag,
        pca_flag=pca_flag,
        tar1_flag=tar1_flag,
        save_yhat_flag=save_yhat_flag,
        save_cond_flag=save_cond_flag,
        voxdump=voxdump,
        seed=seed,
        synth_flag=synth_flag,
        resynthtest_it=resynthtest_it,
        profile_it=profile_it,
        mrtm1_params=mrtm1_params,
        mrtm2_params=mrtm2_params,
        logan_params=logan_params,
        bp_clip_neg_flag=bp_clip_neg_flag,
        bp_clip_max=bp_clip_max,
        perm_force_flag=perm_force_flag,
        diag_level=diag_level,
        diag_cluster_flag=diag_cluster_flag,
        debug_flag=debug_flag,
        checkopts_flag=checkopts_flag,
        help_flag=help_flag,
        version_flag=version_flag,
        no_fix_vertex_area_flag=no_fix_vertex_area_flag,
        allowsubjrep_flag=allowsubjrep_flag,
        allow_zero_dof_flag=allow_zero_dof_flag,
        illcond_flag=illcond_flag,
        sim_done_file=sim_done_file,
        no_sig_double_flag=no_sig_double_flag,
    )
    return mri_glmfit_execute(params, execution)


__all__ = [
    "MRI_GLMFIT_METADATA",
    "MriGlmfitOutputs",
    "MriGlmfitParameters",
    "mri_glmfit",
    "mri_glmfit_params",
]

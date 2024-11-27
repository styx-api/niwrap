# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_GLMFIT_METADATA = Metadata(
    id="79f830582903b4c568e10c98abbe12709997f2f4.boutiques",
    name="mri_glmfit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


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
    cargs = []
    cargs.append("mri_glmfit")
    if glmdir is not None:
        cargs.extend([
            "--glmdir",
            glmdir
        ])
    cargs.extend([
        "--y",
        execution.input_file(y_input)
    ])
    if table_input is not None:
        cargs.extend([
            "--table",
            execution.input_file(table_input)
        ])
    if fsgd is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(fsgd)
        ])
    if design_matrix is not None:
        cargs.extend([
            "--X",
            execution.input_file(design_matrix)
        ])
    if contrast_matrix is not None:
        cargs.extend([
            "--C",
            *[execution.input_file(f) for f in contrast_matrix]
        ])
    if osgm_flag:
        cargs.append("--osgm")
    if no_contrasts_ok_flag:
        cargs.append("--no-contrasts-ok")
    if dti_params is not None:
        cargs.extend([
            "--dti",
            *dti_params
        ])
    if dti_matrix is not None:
        cargs.extend([
            "--dti-X",
            execution.input_file(dti_matrix)
        ])
    if pvr is not None:
        cargs.extend([
            "--pvr",
            *[execution.input_file(f) for f in pvr]
        ])
    if selfreg is not None:
        cargs.extend([
            "--selfreg",
            *map(str, selfreg)
        ])
    if wls is not None:
        cargs.extend([
            "--wls",
            wls
        ])
    if yffxvar is not None:
        cargs.extend([
            "--yffxvar",
            execution.input_file(yffxvar)
        ])
    if ffxdof is not None:
        cargs.extend([
            "--ffxdof",
            str(ffxdof)
        ])
    if ffxdofdat is not None:
        cargs.extend([
            "--ffxdofdat",
            execution.input_file(ffxdofdat)
        ])
    if weight is not None:
        cargs.extend([
            "--w",
            execution.input_file(weight)
        ])
    if weight_inv_flag:
        cargs.append("--w-inv")
    if weight_sqrt_flag:
        cargs.append("--w-sqrt")
    if fwhm is not None:
        cargs.extend([
            "--fwhm",
            str(fwhm)
        ])
    if var_fwhm is not None:
        cargs.extend([
            "--var-fwhm",
            str(var_fwhm)
        ])
    if no_mask_smooth_flag:
        cargs.append("--no-mask-smooth")
    if no_est_fwhm_flag:
        cargs.append("--no-est-fwhm")
    if mask is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask)
        ])
    if label is not None:
        cargs.extend([
            "--label",
            execution.input_file(label)
        ])
    if no_mask_flag:
        cargs.append("--no-mask")
    if no_cortex_flag:
        cargs.append("--no-cortex")
    if mask_inv_flag:
        cargs.append("--mask-inv")
    if prune_flag:
        cargs.append("--prune")
    if no_prune_flag:
        cargs.append("--no-prune")
    if logy_flag:
        cargs.append("--logy")
    if no_logy_flag:
        cargs.append("--no-logy")
    if rm_spatial_mean_flag:
        cargs.append("--rm-spatial-mean")
    if yhat_save_flag:
        cargs.append("--yhat-save")
    if eres_save_flag:
        cargs.append("--eres-save")
    if eres_scm_flag:
        cargs.append("--eres-scm")
    if save_fwhm_map_flag:
        cargs.append("--save-fwhm-map")
    if y_out is not None:
        cargs.extend([
            "--y-out",
            execution.input_file(y_out)
        ])
    if surface is not None:
        cargs.extend([
            "--surf",
            surface
        ])
    if skew_flag:
        cargs.append("--skew")
    if kurtosis_flag:
        cargs.append("--kurtosis")
    if sim_params is not None:
        cargs.extend([
            "--sim",
            *sim_params
        ])
    if sim_sign is not None:
        cargs.extend([
            "--sim-sign",
            sim_sign
        ])
    if uniform_params is not None:
        cargs.extend([
            "--uniform",
            *uniform_params
        ])
    if permute_input_flag:
        cargs.append("--permute-input")
    if pca_flag:
        cargs.append("--pca")
    if tar1_flag:
        cargs.append("--tar1")
    if save_yhat_flag:
        cargs.append("--save-yhat")
    if save_cond_flag:
        cargs.append("--save-cond")
    if voxdump is not None:
        cargs.extend([
            "--voxdump",
            *map(str, voxdump)
        ])
    if seed is not None:
        cargs.extend([
            "--seed",
            str(seed)
        ])
    if synth_flag:
        cargs.append("--synth")
    if resynthtest_it is not None:
        cargs.extend([
            "--resynthtest",
            str(resynthtest_it)
        ])
    if profile_it is not None:
        cargs.extend([
            "--profile",
            str(profile_it)
        ])
    if mrtm1_params is not None:
        cargs.extend([
            "--mrtm1",
            *mrtm1_params
        ])
    if mrtm2_params is not None:
        cargs.extend([
            "--mrtm2",
            *mrtm2_params
        ])
    if logan_params is not None:
        cargs.extend([
            "--logan",
            *logan_params
        ])
    if bp_clip_neg_flag:
        cargs.append("--bp-clip-neg")
    if bp_clip_max is not None:
        cargs.extend([
            "--bp-clip-max",
            str(bp_clip_max)
        ])
    if perm_force_flag:
        cargs.append("--perm-force")
    if diag_level is not None:
        cargs.extend([
            "--diag",
            str(diag_level)
        ])
    if diag_cluster_flag:
        cargs.append("--diag-cluster")
    if debug_flag:
        cargs.append("--debug")
    if checkopts_flag:
        cargs.append("--checkopts")
    if help_flag:
        cargs.append("--help")
    if version_flag:
        cargs.append("--version")
    if no_fix_vertex_area_flag:
        cargs.append("--no-fix-vertex-area")
    if allowsubjrep_flag:
        cargs.append("--allowsubjrep")
    if allow_zero_dof_flag:
        cargs.append("--allow-zero-dof")
    if illcond_flag:
        cargs.append("--illcond")
    if sim_done_file is not None:
        cargs.extend([
            "--sim-done",
            execution.input_file(sim_done_file)
        ])
    if no_sig_double_flag:
        cargs.append("--no-sig-double")
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
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_GLMFIT_METADATA",
    "MriGlmfitOutputs",
    "mri_glmfit",
]

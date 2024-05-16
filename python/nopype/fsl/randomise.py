# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.909832

import typing

from ..styxdefs import *


RANDOMISE_METADATA = Metadata(
    id="e178f3d3dafd5dfc1945cc679a26ca2b956a0973",
    name="Randomise",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class RandomiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `randomise(...)`.
    """
    f_corrected_p_files: OutputPathType
    """F contrast fwe (family-wise error) corrected p values files."""
    f_p_files: OutputPathType
    """F contrast uncorrected p values files."""
    fstat_files: OutputPathType
    """F contrast raw statistic."""
    t_corrected_p_files: OutputPathType
    """T contrast fwe (family-wise error) corrected p values files."""
    t_p_files: OutputPathType
    """F contrast uncorrected p values files."""
    tstat_files: OutputPathType
    """T contrast raw statistic."""


def randomise(
    runner: Runner,
    in_file: InputPathType,
    base_name: str | None = "randomise",
    c_thresh: float | int | None = None,
    cm_thresh: float | int | None = None,
    demean: bool = False,
    design_mat: InputPathType | None = None,
    f_c_thresh: float | int | None = None,
    f_cm_thresh: float | int | None = None,
    f_only: bool = False,
    fcon: InputPathType | None = None,
    mask: InputPathType | None = None,
    num_perm: int | None = None,
    one_sample_group_mean: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    p_vec_n_dist_files: bool = False,
    raw_stats_imgs: bool = False,
    seed: int | None = None,
    show_info_parallel_mode: bool = False,
    show_total_perms: bool = False,
    tcon: InputPathType | None = None,
    tfce: bool = False,
    tfce2_d: bool = False,
    tfce_c: float | int | None = None,
    tfce_e: float | int | None = None,
    tfce_h: float | int | None = None,
    var_smooth: int | None = None,
    vox_p_values: bool = False,
    x_block_labels: InputPathType | None = None,
) -> RandomiseOutputs:
    """
    Randomise, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    Randomise).
    FSL Randomise: feeds the 4D projected FA data into GLM modelling and
    thresholding in order to find voxels which correlate with your model
    Example ------- >>> import nipype.interfaces.fsl as fsl >>> rand =
    fsl.Randomise(in_file='allFA.nii', mask = 'mask.nii', tcon='design.con',
    design_mat='design.mat') >>> rand.cmdline 'randomise -i allFA.nii -o
    "randomise" -d design.mat -t design.con -m mask.nii'
    
    Args:
        runner: Command runner
        in_file: 4d input file.
        base_name: The rootname that all generated files will have.
        c_thresh: Carry out cluster-based thresholding.
        cm_thresh: Carry out cluster-mass-based thresholding.
        demean: Demean data temporally before model fitting.
        design_mat: Design matrix file.
        f_c_thresh: Carry out f cluster thresholding.
        f_cm_thresh: Carry out f cluster-mass thresholding.
        f_only: Calculate f-statistics only.
        fcon: F contrasts file.
        mask: Mask image.
        num_perm: Number of permutations (default 5000, set to 0 for
            exhaustive).
        one_sample_group_mean: Perform 1-sample group-mean test instead of
            generic permutation test.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.
            Fsl output type.
        p_vec_n_dist_files: Output permutation vector and null distribution text
            files.
        raw_stats_imgs: Output raw ( unpermuted ) statistic images.
        seed: Specific integer seed for random number generator.
        show_info_parallel_mode: Print out information required for parallel
            mode and exit.
        show_total_perms: Print out how many unique permutations would be
            generated and exit.
        tcon: T contrasts file.
        tfce: Carry out threshold-free cluster enhancement.
        tfce2_d: Carry out threshold-free cluster enhancement with 2d
            optimisation.
        tfce_c: Tfce connectivity (6 or 26; default=6).
        tfce_e: Tfce extent parameter (default=0.5).
        tfce_h: Tfce height parameter (default=2).
        var_smooth: Use variance smoothing (std is in mm).
        vox_p_values: Output voxelwise (corrected and uncorrected) p-value
            images.
        x_block_labels: Exchangeability block labels file.
    Returns:
        NamedTuple of outputs (described in `RandomiseOutputs`).
    """
    execution = runner.start_execution(RANDOMISE_METADATA)
    cargs = []
    cargs.append("Randomise")
    cargs.extend(["-i", execution.input_file(in_file)])
    if base_name is not None:
        cargs.extend(["-o", base_name])
    if design_mat is not None:
        cargs.extend(["-d", execution.input_file(design_mat)])
    if tcon is not None:
        cargs.extend(["-t", execution.input_file(tcon)])
    cargs.append("[ARGS]")
    if c_thresh is not None:
        cargs.extend(["-c", str(c_thresh)])
    if cm_thresh is not None:
        cargs.extend(["-C", str(cm_thresh)])
    if demean:
        cargs.append("-D")
    cargs.append("[ENVIRON]")
    if f_c_thresh is not None:
        cargs.extend(["-F", str(f_c_thresh)])
    if f_cm_thresh is not None:
        cargs.extend(["-S", str(f_cm_thresh)])
    if f_only:
        cargs.append("--fonly")
    if fcon is not None:
        cargs.extend(["-f", execution.input_file(fcon)])
    if mask is not None:
        cargs.extend(["-m", execution.input_file(mask)])
    if num_perm is not None:
        cargs.extend(["-n", str(num_perm)])
    if one_sample_group_mean:
        cargs.append("-1")
    if output_type is not None:
        cargs.append(output_type)
    if p_vec_n_dist_files:
        cargs.append("-P")
    if raw_stats_imgs:
        cargs.append("-R")
    if seed is not None:
        cargs.append(("--seed=" + str(seed)))
    if show_info_parallel_mode:
        cargs.append("-Q")
    if show_total_perms:
        cargs.append("-q")
    if tfce:
        cargs.append("-T")
    if tfce2_d:
        cargs.append("--T2")
    if tfce_c is not None:
        cargs.append(("--tfce_C=" + str(tfce_c)))
    if tfce_e is not None:
        cargs.append(("--tfce_E=" + str(tfce_e)))
    if tfce_h is not None:
        cargs.append(("--tfce_H=" + str(tfce_h)))
    if var_smooth is not None:
        cargs.extend(["-v", str(var_smooth)])
    if vox_p_values:
        cargs.append("-x")
    if x_block_labels is not None:
        cargs.extend(["-e", execution.input_file(x_block_labels)])
    ret = RandomiseOutputs(
        f_corrected_p_files=execution.output_file(f"f_corrected_p_files", optional=True),
        f_p_files=execution.output_file(f"f_p_files", optional=True),
        fstat_files=execution.output_file(f"fstat_files", optional=True),
        t_corrected_p_files=execution.output_file(f"t_corrected_p_files", optional=True),
        t_p_files=execution.output_file(f"t_p_files", optional=True),
        tstat_files=execution.output_file(f"tstat_files", optional=True),
    )
    execution.run(cargs)
    return ret

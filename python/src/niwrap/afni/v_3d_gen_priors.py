# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_GEN_PRIORS_METADATA = Metadata(
    id="845d9172d4ae6f1eca3fec82fab483b9e0b7907b.boutiques",
    name="3dGenPriors",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dGenPriorsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_gen_priors(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_cprefix: OutputPathType
    """Main classification output"""
    out_pprefix: OutputPathType
    """Main probability output"""


def v_3d_gen_priors(
    sigs: InputPathType,
    tdist: InputPathType,
    cprefix: str,
    pprefix: str,
    labeltable: InputPathType,
    do: str,
    prefix: str | None = None,
    cmask: str | None = None,
    mask: str | None = None,
    mrange: list[float] | None = None,
    debug: float | None = None,
    vox_debug: str | None = None,
    vox_debug_file: str | None = None,
    uid: str | None = None,
    use_tmp: bool = False,
    no_tmp: bool = False,
    pset: str | None = None,
    cset: str | None = None,
    regroup_classes: str | None = None,
    classes: str | None = None,
    features: str | None = None,
    strict_feature_match: bool = False,
    featgroups: str | None = None,
    show_this_dist: str | None = None,
    fast: bool = False,
    slow: bool = False,
    runner: Runner | None = None,
) -> V3dGenPriorsOutputs:
    """
    Produces classification priors based on voxel signatures.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        sigs: Signatures dataset. A dataset with F features per voxel.
        tdist: Training results. This file is generated by 3dSignatures.
        cprefix: Prefix for class dataset.
        pprefix: Prefix for probability dataset.
        labeltable: Labeltable to attach to output dataset.
        do: Specify the output that this program should create.
        prefix: Specify root prefix for output volumes.
        cmask: Provide cmask expression. Voxels where expression is 0 are\
            excluded from computations.
        mask: Provide mask dataset.
        mrange: Consider MASK only for values between M0 and M1, inclusive.
        debug: Set debug level.
        vox_debug: 1D index or 3D indices (I J K) of voxel to debug.
        vox_debug_file: File in which debug information is output.
        uid: User identifier string. Used to generate names for temporary\
            files.
        use_tmp: Use temporary storage to speed up the program.
        no_tmp: Do not use temporary storage.
        pset: Reuse probability output from an earlier run.
        cset: Reuse classification output from an earlier run.
        regroup_classes: Regroup classes into parent classes. Requires naming\
            the original classes as C1.*, C2.*, etc.
        classes: Classify into these classes only.
        features: Use these features only. Otherwise, all features in the\
            signature file will be used.
        strict_feature_match: Use strict feature name matching.
        featgroups: Feature groups.
        show_this_dist: Show information obtained from the training data about\
            the distribution of DIST. Set DIST to ALL to see all distributions.
        fast: Use OpenMPized routines for faster performance.
        slow: Do not use OpenMPized routines.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGenPriorsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GEN_PRIORS_METADATA)
    cargs = []
    cargs.append("3dGenPriors")
    cargs.extend([
        "-sig",
        execution.input_file(sigs)
    ])
    cargs.extend([
        "-tdist",
        execution.input_file(tdist)
    ])
    cargs.extend([
        "-cprefix",
        cprefix
    ])
    cargs.extend([
        "-pprefix",
        pprefix
    ])
    cargs.extend([
        "-labeltable",
        execution.input_file(labeltable)
    ])
    cargs.extend([
        "-do",
        do
    ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if cmask is not None:
        cargs.extend([
            "-cmask",
            cmask
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            mask
        ])
    if mrange is not None:
        cargs.extend([
            "-mrange",
            *map(str, mrange)
        ])
    if debug is not None:
        cargs.extend([
            "-debug",
            str(debug)
        ])
    if vox_debug is not None:
        cargs.extend([
            "-vox_debug",
            vox_debug
        ])
    if vox_debug_file is not None:
        cargs.extend([
            "-vox_debug_file",
            vox_debug_file
        ])
    if uid is not None:
        cargs.extend([
            "-uid",
            uid
        ])
    if use_tmp:
        cargs.append("-use_tmp")
    if no_tmp:
        cargs.append("-no_tmp")
    if pset is not None:
        cargs.extend([
            "-pset",
            pset
        ])
    if cset is not None:
        cargs.extend([
            "-cset",
            cset
        ])
    if regroup_classes is not None:
        cargs.extend([
            "-regroup_classes",
            regroup_classes
        ])
    if classes is not None:
        cargs.extend([
            "-classes",
            classes
        ])
    if features is not None:
        cargs.extend([
            "-features",
            features
        ])
    if strict_feature_match:
        cargs.append("-strict_feature_match")
    if featgroups is not None:
        cargs.extend([
            "-featgroups",
            featgroups
        ])
    if show_this_dist is not None:
        cargs.extend([
            "-ShowThisDist",
            show_this_dist
        ])
    if fast:
        cargs.append("-fast")
    if slow:
        cargs.append("-slow")
    ret = V3dGenPriorsOutputs(
        root=execution.output_file("."),
        out_cprefix=execution.output_file(cprefix + ".nii.gz"),
        out_pprefix=execution.output_file(pprefix + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dGenPriorsOutputs",
    "V_3D_GEN_PRIORS_METADATA",
    "v_3d_gen_priors",
]

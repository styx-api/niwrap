# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_SEG_METADATA = Metadata(
    id="f6e7c61caa09a93af688039024093f43ff4f67a3.boutiques",
    name="3dSeg",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dSegParameters = typing.TypedDict('V3dSegParameters', {
    "__STYX_TYPE__": typing.Literal["3dSeg"],
    "anat": InputPathType,
    "mask": typing.NotRequired[str | None],
    "blur_meth": typing.NotRequired[str | None],
    "bias_fwhm": typing.NotRequired[float | None],
    "classes": typing.NotRequired[str | None],
    "Bmrf": typing.NotRequired[float | None],
    "bias_classes": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "overwrite": bool,
    "debug": typing.NotRequired[float | None],
    "mixfrac": typing.NotRequired[str | None],
    "mixfloor": typing.NotRequired[float | None],
    "gold": typing.NotRequired[InputPathType | None],
    "gold_bias": typing.NotRequired[InputPathType | None],
    "main_N": typing.NotRequired[float | None],
    "cset": typing.NotRequired[InputPathType | None],
    "labeltable": typing.NotRequired[InputPathType | None],
    "vox_debug": typing.NotRequired[str | None],
    "vox_debug_file": typing.NotRequired[str | None],
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
        "3dSeg": v_3d_seg_cargs,
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
        "3dSeg": v_3d_seg_outputs,
    }.get(t)


class V3dSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_volume: OutputPathType | None
    """Segmented brain volume output"""
    bias_field: OutputPathType | None
    """Bias field estimate output"""
    classified_volume: OutputPathType | None
    """Classified volume output"""


def v_3d_seg_params(
    anat: InputPathType,
    mask: str | None = None,
    blur_meth: str | None = None,
    bias_fwhm: float | None = None,
    classes: str | None = None,
    bmrf: float | None = None,
    bias_classes: str | None = None,
    prefix: str | None = None,
    overwrite: bool = False,
    debug: float | None = None,
    mixfrac: str | None = None,
    mixfloor: float | None = None,
    gold: InputPathType | None = None,
    gold_bias: InputPathType | None = None,
    main_n: float | None = None,
    cset: InputPathType | None = None,
    labeltable: InputPathType | None = None,
    vox_debug: str | None = None,
    vox_debug_file: str | None = None,
) -> V3dSegParameters:
    """
    Build parameters.
    
    Args:
        anat: Volume to segment.
        mask: Mask of the volume to be segmented. Can be a dataset or 'AUTO' to\
            use AFNI's automask function.
        blur_meth: Blurring method for bias field estimation. Options: BFT,\
            BIM, BNN, LSB. Default: BFT.
        bias_fwhm: The amount of blurring used when estimating the field bias.\
            Default: 25.0.
        classes: String of class labels separated by semicolons. Default: 'CSF;\
            GM; WM'.
        bmrf: Weighting factor controlling spatial homogeneity of\
            classifications. Default: 0.0.
        bias_classes: Classes that contribute to the estimation of the bias\
            field. Default: 'GM; WM'.
        prefix: Prefix for all output volume.
        overwrite: Automatically overwrite existing files with the same prefix.
        debug: Set debug level (0, 1, or 2).
        mixfrac: Volume-wide mixing fractions for initialization. Options: '0.1\
            0.45 0.45', 'UNI', 'AVG152_BRAIN_MASK', 'IGNORE'. Default: UNI.
        mixfloor: Set the minimum value for any class's mixing fraction.\
            Default: 0.0001.
        gold: Goldstandard segmentation volume for comparison.
        gold_bias: Goldstandard bias volume for comparison.
        main_n: Number of iterations to perform. Default: 5.
        cset: Initial classification. Uses 3dkmean's engine if not provided.
        labeltable: Label table containing integer keys and corresponding\
            labels.
        vox_debug: 1D index of voxel to debug or 3D voxel indices.
        vox_debug_file: File in which debug information is output, use '-' for\
            stdout, '+' for stderr.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dSeg",
        "anat": anat,
        "overwrite": overwrite,
    }
    if mask is not None:
        params["mask"] = mask
    if blur_meth is not None:
        params["blur_meth"] = blur_meth
    if bias_fwhm is not None:
        params["bias_fwhm"] = bias_fwhm
    if classes is not None:
        params["classes"] = classes
    if bmrf is not None:
        params["Bmrf"] = bmrf
    if bias_classes is not None:
        params["bias_classes"] = bias_classes
    if prefix is not None:
        params["prefix"] = prefix
    if debug is not None:
        params["debug"] = debug
    if mixfrac is not None:
        params["mixfrac"] = mixfrac
    if mixfloor is not None:
        params["mixfloor"] = mixfloor
    if gold is not None:
        params["gold"] = gold
    if gold_bias is not None:
        params["gold_bias"] = gold_bias
    if main_n is not None:
        params["main_N"] = main_n
    if cset is not None:
        params["cset"] = cset
    if labeltable is not None:
        params["labeltable"] = labeltable
    if vox_debug is not None:
        params["vox_debug"] = vox_debug
    if vox_debug_file is not None:
        params["vox_debug_file"] = vox_debug_file
    return params


def v_3d_seg_cargs(
    params: V3dSegParameters,
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
    cargs.append("3dSeg")
    cargs.extend([
        "-anat",
        execution.input_file(params.get("anat"))
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            params.get("mask")
        ])
    if params.get("blur_meth") is not None:
        cargs.extend([
            "-blur_meth",
            params.get("blur_meth")
        ])
    if params.get("bias_fwhm") is not None:
        cargs.extend([
            "-bias_fwhm",
            str(params.get("bias_fwhm"))
        ])
    if params.get("classes") is not None:
        cargs.extend([
            "-classes",
            params.get("classes")
        ])
    if params.get("Bmrf") is not None:
        cargs.extend([
            "-Bmrf",
            str(params.get("Bmrf"))
        ])
    if params.get("bias_classes") is not None:
        cargs.extend([
            "-bias_classes",
            params.get("bias_classes")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("overwrite"):
        cargs.append("-overwrite")
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug"))
        ])
    if params.get("mixfrac") is not None:
        cargs.extend([
            "-mixfrac",
            params.get("mixfrac")
        ])
    if params.get("mixfloor") is not None:
        cargs.extend([
            "-mixfloor",
            str(params.get("mixfloor"))
        ])
    if params.get("gold") is not None:
        cargs.extend([
            "-gold",
            execution.input_file(params.get("gold"))
        ])
    if params.get("gold_bias") is not None:
        cargs.extend([
            "-gold_bias",
            execution.input_file(params.get("gold_bias"))
        ])
    if params.get("main_N") is not None:
        cargs.extend([
            "-main_N",
            str(params.get("main_N"))
        ])
    if params.get("cset") is not None:
        cargs.extend([
            "-cset",
            execution.input_file(params.get("cset"))
        ])
    if params.get("labeltable") is not None:
        cargs.extend([
            "-labeltable",
            execution.input_file(params.get("labeltable"))
        ])
    if params.get("vox_debug") is not None:
        cargs.extend([
            "-vox_debug",
            params.get("vox_debug")
        ])
    if params.get("vox_debug_file") is not None:
        cargs.extend([
            "-vox_debug_file",
            params.get("vox_debug_file")
        ])
    return cargs


def v_3d_seg_outputs(
    params: V3dSegParameters,
    execution: Execution,
) -> V3dSegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dSegOutputs(
        root=execution.output_file("."),
        segmented_volume=execution.output_file(params.get("prefix") + "_Segsy+orig.HEAD") if (params.get("prefix") is not None) else None,
        bias_field=execution.output_file(params.get("prefix") + "_BiasField+orig.HEAD") if (params.get("prefix") is not None) else None,
        classified_volume=execution.output_file(params.get("prefix") + "_Classes+orig.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_seg_execute(
    params: V3dSegParameters,
    execution: Execution,
) -> V3dSegOutputs:
    """
    Segments brain volumes into tissue classes with optional global and voxelwise
    priors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dSegOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_seg_cargs(params, execution)
    ret = v_3d_seg_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_seg(
    anat: InputPathType,
    mask: str | None = None,
    blur_meth: str | None = None,
    bias_fwhm: float | None = None,
    classes: str | None = None,
    bmrf: float | None = None,
    bias_classes: str | None = None,
    prefix: str | None = None,
    overwrite: bool = False,
    debug: float | None = None,
    mixfrac: str | None = None,
    mixfloor: float | None = None,
    gold: InputPathType | None = None,
    gold_bias: InputPathType | None = None,
    main_n: float | None = None,
    cset: InputPathType | None = None,
    labeltable: InputPathType | None = None,
    vox_debug: str | None = None,
    vox_debug_file: str | None = None,
    runner: Runner | None = None,
) -> V3dSegOutputs:
    """
    Segments brain volumes into tissue classes with optional global and voxelwise
    priors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        anat: Volume to segment.
        mask: Mask of the volume to be segmented. Can be a dataset or 'AUTO' to\
            use AFNI's automask function.
        blur_meth: Blurring method for bias field estimation. Options: BFT,\
            BIM, BNN, LSB. Default: BFT.
        bias_fwhm: The amount of blurring used when estimating the field bias.\
            Default: 25.0.
        classes: String of class labels separated by semicolons. Default: 'CSF;\
            GM; WM'.
        bmrf: Weighting factor controlling spatial homogeneity of\
            classifications. Default: 0.0.
        bias_classes: Classes that contribute to the estimation of the bias\
            field. Default: 'GM; WM'.
        prefix: Prefix for all output volume.
        overwrite: Automatically overwrite existing files with the same prefix.
        debug: Set debug level (0, 1, or 2).
        mixfrac: Volume-wide mixing fractions for initialization. Options: '0.1\
            0.45 0.45', 'UNI', 'AVG152_BRAIN_MASK', 'IGNORE'. Default: UNI.
        mixfloor: Set the minimum value for any class's mixing fraction.\
            Default: 0.0001.
        gold: Goldstandard segmentation volume for comparison.
        gold_bias: Goldstandard bias volume for comparison.
        main_n: Number of iterations to perform. Default: 5.
        cset: Initial classification. Uses 3dkmean's engine if not provided.
        labeltable: Label table containing integer keys and corresponding\
            labels.
        vox_debug: 1D index of voxel to debug or 3D voxel indices.
        vox_debug_file: File in which debug information is output, use '-' for\
            stdout, '+' for stderr.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SEG_METADATA)
    params = v_3d_seg_params(
        anat=anat,
        mask=mask,
        blur_meth=blur_meth,
        bias_fwhm=bias_fwhm,
        classes=classes,
        bmrf=bmrf,
        bias_classes=bias_classes,
        prefix=prefix,
        overwrite=overwrite,
        debug=debug,
        mixfrac=mixfrac,
        mixfloor=mixfloor,
        gold=gold,
        gold_bias=gold_bias,
        main_n=main_n,
        cset=cset,
        labeltable=labeltable,
        vox_debug=vox_debug,
        vox_debug_file=vox_debug_file,
    )
    return v_3d_seg_execute(params, execution)


__all__ = [
    "V3dSegOutputs",
    "V3dSegParameters",
    "V_3D_SEG_METADATA",
    "v_3d_seg",
    "v_3d_seg_params",
]

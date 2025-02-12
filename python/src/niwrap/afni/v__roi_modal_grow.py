# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__ROI_MODAL_GROW_METADATA = Metadata(
    id="d33815ad6bfc8ff7ac694bacf23eb5bed10577bf.boutiques",
    name="@ROI_modal_grow",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VRoiModalGrowParameters = typing.TypedDict('VRoiModalGrowParameters', {
    "__STYX_TYPE__": typing.Literal["@ROI_modal_grow"],
    "input_dset": InputPathType,
    "niters": float,
    "outdir": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "neighborhood_type": typing.NotRequired[int | None],
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
        "@ROI_modal_grow": v__roi_modal_grow_cargs,
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
        "@ROI_modal_grow": v__roi_modal_grow_outputs,
    }.get(t)


class VRoiModalGrowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__roi_modal_grow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Final output dataset"""


def v__roi_modal_grow_params(
    input_dset: InputPathType,
    niters: float,
    outdir: str | None = None,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    neighborhood_type: int | None = None,
) -> VRoiModalGrowParameters:
    """
    Build parameters.
    
    Args:
        input_dset: Required input dataset. This dataset should be a set of\
            integer values, assuming approximate isotropic voxels.
        niters: Number of iterations for modal growth, generally making sense\
            for values from about 1-10.
        outdir: Directory name for output. All output goes to this directory.\
            Default is rmgrow.
        mask: Mask dataset at the same grid as the input dataset. Could be a\
            dilated version of the original mask or a larger region like a cortical\
            ribbon mask. Not required but often desirable.
        prefix: Base name of the final output dataset, i.e., baseprefix.nii.gz.\
            Default is rmg, so output would be rmg.nii.gz.
        neighborhood_type: Neighborhood type used in finding mode. 1 - facing\
            neighbors, 2 - edges, 3 - corners.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ROI_modal_grow",
        "input_dset": input_dset,
        "niters": niters,
    }
    if outdir is not None:
        params["outdir"] = outdir
    if mask is not None:
        params["mask"] = mask
    if prefix is not None:
        params["prefix"] = prefix
    if neighborhood_type is not None:
        params["neighborhood_type"] = neighborhood_type
    return params


def v__roi_modal_grow_cargs(
    params: VRoiModalGrowParameters,
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
    cargs.append("@ROI_modal_grow")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dset"))
    ])
    cargs.extend([
        "-niters",
        str(params.get("niters"))
    ])
    if params.get("outdir") is not None:
        cargs.extend([
            "-outdir",
            params.get("outdir")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("neighborhood_type") is not None:
        cargs.extend([
            "-NN",
            str(params.get("neighborhood_type"))
        ])
    return cargs


def v__roi_modal_grow_outputs(
    params: VRoiModalGrowParameters,
    execution: Execution,
) -> VRoiModalGrowOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VRoiModalGrowOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("outdir") + "/" + params.get("prefix") + ".nii.gz") if (params.get("outdir") is not None and params.get("prefix") is not None) else None,
    )
    return ret


def v__roi_modal_grow_execute(
    params: VRoiModalGrowParameters,
    execution: Execution,
) -> VRoiModalGrowOutputs:
    """
    Script to grow a set of regions in a volumetric dataset using modal smoothing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VRoiModalGrowOutputs`).
    """
    cargs = v__roi_modal_grow_cargs(params, execution)
    ret = v__roi_modal_grow_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__roi_modal_grow(
    input_dset: InputPathType,
    niters: float,
    outdir: str | None = None,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    neighborhood_type: int | None = None,
    runner: Runner | None = None,
) -> VRoiModalGrowOutputs:
    """
    Script to grow a set of regions in a volumetric dataset using modal smoothing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dset: Required input dataset. This dataset should be a set of\
            integer values, assuming approximate isotropic voxels.
        niters: Number of iterations for modal growth, generally making sense\
            for values from about 1-10.
        outdir: Directory name for output. All output goes to this directory.\
            Default is rmgrow.
        mask: Mask dataset at the same grid as the input dataset. Could be a\
            dilated version of the original mask or a larger region like a cortical\
            ribbon mask. Not required but often desirable.
        prefix: Base name of the final output dataset, i.e., baseprefix.nii.gz.\
            Default is rmg, so output would be rmg.nii.gz.
        neighborhood_type: Neighborhood type used in finding mode. 1 - facing\
            neighbors, 2 - edges, 3 - corners.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRoiModalGrowOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ROI_MODAL_GROW_METADATA)
    params = v__roi_modal_grow_params(input_dset=input_dset, niters=niters, outdir=outdir, mask=mask, prefix=prefix, neighborhood_type=neighborhood_type)
    return v__roi_modal_grow_execute(params, execution)


__all__ = [
    "VRoiModalGrowOutputs",
    "VRoiModalGrowParameters",
    "V__ROI_MODAL_GROW_METADATA",
    "v__roi_modal_grow",
    "v__roi_modal_grow_params",
]

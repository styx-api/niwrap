# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BET_METADATA = Metadata(
    id="cb7a81b5f775bbef34ecb7d03d21d482a296338c.boutiques",
    name="bet",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
BetParameters = typing.TypedDict('BetParameters', {
    "__STYX_TYPE__": typing.Literal["bet"],
    "infile": InputPathType,
    "maskfile": str,
    "fractional_intensity": typing.NotRequired[float | None],
    "vg_fractional_intensity": typing.NotRequired[float | None],
    "center_of_gravity": typing.NotRequired[list[float] | None],
    "overlay": bool,
    "binary_mask": bool,
    "approx_skull": bool,
    "no_seg_output": bool,
    "vtk_mesh": bool,
    "head_radius": typing.NotRequired[float | None],
    "thresholding": bool,
    "robust_iters": bool,
    "residual_optic_cleanup": bool,
    "reduce_bias": bool,
    "slice_padding": bool,
    "whole_set_mask": bool,
    "additional_surfaces": bool,
    "additional_surfaces_t2": typing.NotRequired[InputPathType | None],
    "verbose": bool,
    "debug": bool,
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
        "bet": bet_cargs,
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
        "bet": bet_outputs,
    }.get(t)


class BetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bet(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Main default mask output of BET"""
    binary_mask: OutputPathType
    """Binary mask file (from -m option)"""
    overlay_file: OutputPathType
    """Overlaid brain surface onto original image"""
    approx_skull_img: OutputPathType
    """Approximate skull image file"""
    output_vtk_mesh: OutputPathType
    """Mesh in VTK format"""
    skull_mask: OutputPathType
    """Output mask for skull image"""
    out_inskull_mask: OutputPathType
    """The in-skull mask file from betsurf (from -A or -A2)"""
    out_inskull_mesh: OutputPathType
    """The in-skull mesh file from betsurf (from -A or -A2)"""
    out_inskull_off: OutputPathType
    """The in-skull mesh .off file from betsurf (from -A or -A2)"""
    out_outskin_mask: OutputPathType
    """The out-skin mask file from betsurf (from -A or -A2)"""
    out_outskin_mesh: OutputPathType
    """The out-skin mesh file from betsurf (from -A or -A2)"""
    out_outskin_off: OutputPathType
    """The out-skin mesh .off file from betsurf (from -A or -A2)"""
    out_outskull_mask: OutputPathType
    """The out-skull mask file from betsurf (from -A or -A2)"""
    out_outskull_mesh: OutputPathType
    """The out-skull mesh file from betsurf (from -A or -A2)"""
    out_outskull_off: OutputPathType
    """The out-skull mesh .off file from betsurf (from -A or -A2)"""


def bet_params(
    infile: InputPathType,
    maskfile: str = "img_bet",
    fractional_intensity: float | None = None,
    vg_fractional_intensity: float | None = None,
    center_of_gravity: list[float] | None = None,
    overlay: bool = False,
    binary_mask: bool = False,
    approx_skull: bool = False,
    no_seg_output: bool = False,
    vtk_mesh: bool = False,
    head_radius: float | None = None,
    thresholding: bool = False,
    robust_iters: bool = False,
    residual_optic_cleanup: bool = False,
    reduce_bias: bool = False,
    slice_padding: bool = False,
    whole_set_mask: bool = False,
    additional_surfaces: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose: bool = False,
    debug: bool = False,
) -> BetParameters:
    """
    Build parameters.
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        maskfile: Output brain mask (e.g. img_bet.nii.gz).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        overlay: Generate brain surface outline overlaid onto original image.
        binary_mask: Generate binary brain mask.
        approx_skull: Generate rough skull image (not as clean as betsurf).
        no_seg_output: Don't generate segmented brain image output.
        vtk_mesh: Generate brain surface as mesh in .vtk format.
        head_radius: head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        thresholding: Apply thresholding to segmented brain image and mask.
        robust_iters: More robust brain center estimation, by iterating BET\
            with a changing center-of-gravity.
        residual_optic_cleanup: This attempts to cleanup residual eye and optic\
            nerve voxels which bet2 can sometimes leave behind. This can be useful\
            when running SIENA or SIENAX, for example. Various stages involving\
            standard-space masking, morphpological operations and thresholdings are\
            combined to produce a result which can often give better results than\
            just running bet2.
        reduce_bias: This attempts to reduce image bias, and residual neck\
            voxels. This can be useful when running SIENA or SIENAX, for example.\
            Various stages involving FAST segmentation-based bias field removal and\
            standard-space masking are combined to produce a result which can often\
            give better results than just running bet2.
        slice_padding: This can improve the brain extraction if only a few\
            slices are present in the data (i.e., a small field of view in the Z\
            direction). This is achieved by padding the end slices in both\
            directions, copying the end slices several times, running bet2 and then\
            removing the added slices.
        whole_set_mask: This option uses bet2 to determine a brain mask on the\
            basis of the first volume in a 4D data set, and applies this to the\
            whole data set. This is principally intended for use on FMRI data, for\
            example to remove eyeballs. Because it is normally important (in this\
            application) that masking be liberal (ie that there be little risk of\
            cutting out valid brain voxels) the -f threshold is reduced to 0.3, and\
            also the brain mask is "dilated" slightly before being used.
        additional_surfaces: This runs both bet2 and betsurf programs in order\
            to get the additional skull and scalp surfaces created by betsurf. This\
            involves registering to standard space in order to allow betsurf to\
            find the standard space masks it needs.
        additional_surfaces_t2: This is the same as -A except that a T2 image\
            is also input, to further improve the estimated skull and scalp\
            surfaces. As well as carrying out the standard space registration this\
            also registers the T2 to the T1 input image.
        verbose: Switch on diagnostic messages.
        debug: Don't delete temporary intermediate images.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bet",
        "infile": infile,
        "maskfile": maskfile,
        "overlay": overlay,
        "binary_mask": binary_mask,
        "approx_skull": approx_skull,
        "no_seg_output": no_seg_output,
        "vtk_mesh": vtk_mesh,
        "thresholding": thresholding,
        "robust_iters": robust_iters,
        "residual_optic_cleanup": residual_optic_cleanup,
        "reduce_bias": reduce_bias,
        "slice_padding": slice_padding,
        "whole_set_mask": whole_set_mask,
        "additional_surfaces": additional_surfaces,
        "verbose": verbose,
        "debug": debug,
    }
    if fractional_intensity is not None:
        params["fractional_intensity"] = fractional_intensity
    if vg_fractional_intensity is not None:
        params["vg_fractional_intensity"] = vg_fractional_intensity
    if center_of_gravity is not None:
        params["center_of_gravity"] = center_of_gravity
    if head_radius is not None:
        params["head_radius"] = head_radius
    if additional_surfaces_t2 is not None:
        params["additional_surfaces_t2"] = additional_surfaces_t2
    return params


def bet_cargs(
    params: BetParameters,
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
    cargs.append("bet")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(params.get("maskfile"))
    if params.get("fractional_intensity") is not None:
        cargs.extend([
            "-f",
            str(params.get("fractional_intensity"))
        ])
    if params.get("vg_fractional_intensity") is not None:
        cargs.extend([
            "-g",
            str(params.get("vg_fractional_intensity"))
        ])
    if params.get("center_of_gravity") is not None:
        cargs.extend([
            "-c",
            *map(str, params.get("center_of_gravity"))
        ])
    if params.get("overlay"):
        cargs.append("-o")
    if params.get("binary_mask"):
        cargs.append("-m")
    if params.get("approx_skull"):
        cargs.append("-s")
    if params.get("no_seg_output"):
        cargs.append("-n")
    if params.get("vtk_mesh"):
        cargs.append("-e")
    if params.get("head_radius") is not None:
        cargs.extend([
            "-r",
            str(params.get("head_radius"))
        ])
    if params.get("thresholding"):
        cargs.append("-t")
    if params.get("robust_iters"):
        cargs.append("-R")
    if params.get("residual_optic_cleanup"):
        cargs.append("-S")
    if params.get("reduce_bias"):
        cargs.append("-B")
    if params.get("slice_padding"):
        cargs.append("-Z")
    if params.get("whole_set_mask"):
        cargs.append("-F")
    if params.get("additional_surfaces"):
        cargs.append("-A")
    if params.get("additional_surfaces_t2") is not None:
        cargs.extend([
            "-A2",
            execution.input_file(params.get("additional_surfaces_t2"))
        ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("debug"):
        cargs.append("-d")
    return cargs


def bet_outputs(
    params: BetParameters,
    execution: Execution,
) -> BetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BetOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("maskfile") + ".nii.gz"),
        binary_mask=execution.output_file(params.get("maskfile") + "_mask.nii.gz"),
        overlay_file=execution.output_file(params.get("maskfile") + "_overlay.nii.gz"),
        approx_skull_img=execution.output_file(params.get("maskfile") + "_skull.nii.gz"),
        output_vtk_mesh=execution.output_file(params.get("maskfile") + "_mesh.vtk"),
        skull_mask=execution.output_file(params.get("maskfile") + "_skull_mask.nii.gz"),
        out_inskull_mask=execution.output_file(params.get("maskfile") + "_inskull_mask.nii.gz"),
        out_inskull_mesh=execution.output_file(params.get("maskfile") + "_inskull_mesh.nii.gz"),
        out_inskull_off=execution.output_file(params.get("maskfile") + "_inskull_mesh.off"),
        out_outskin_mask=execution.output_file(params.get("maskfile") + "_outskin_mask.nii.gz"),
        out_outskin_mesh=execution.output_file(params.get("maskfile") + "_outskin_mesh.nii.gz"),
        out_outskin_off=execution.output_file(params.get("maskfile") + "_outskin_mesh.off"),
        out_outskull_mask=execution.output_file(params.get("maskfile") + "_outskull_mask.nii.gz"),
        out_outskull_mesh=execution.output_file(params.get("maskfile") + "_outskull_mesh.nii.gz"),
        out_outskull_off=execution.output_file(params.get("maskfile") + "_outskull_mesh.off"),
    )
    return ret


def bet_execute(
    params: BetParameters,
    execution: Execution,
) -> BetOutputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BetOutputs`).
    """
    cargs = bet_cargs(params, execution)
    ret = bet_outputs(params, execution)
    execution.run(cargs)
    return ret


def bet(
    infile: InputPathType,
    maskfile: str = "img_bet",
    fractional_intensity: float | None = None,
    vg_fractional_intensity: float | None = None,
    center_of_gravity: list[float] | None = None,
    overlay: bool = False,
    binary_mask: bool = False,
    approx_skull: bool = False,
    no_seg_output: bool = False,
    vtk_mesh: bool = False,
    head_radius: float | None = None,
    thresholding: bool = False,
    robust_iters: bool = False,
    residual_optic_cleanup: bool = False,
    reduce_bias: bool = False,
    slice_padding: bool = False,
    whole_set_mask: bool = False,
    additional_surfaces: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> BetOutputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        maskfile: Output brain mask (e.g. img_bet.nii.gz).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        overlay: Generate brain surface outline overlaid onto original image.
        binary_mask: Generate binary brain mask.
        approx_skull: Generate rough skull image (not as clean as betsurf).
        no_seg_output: Don't generate segmented brain image output.
        vtk_mesh: Generate brain surface as mesh in .vtk format.
        head_radius: head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        thresholding: Apply thresholding to segmented brain image and mask.
        robust_iters: More robust brain center estimation, by iterating BET\
            with a changing center-of-gravity.
        residual_optic_cleanup: This attempts to cleanup residual eye and optic\
            nerve voxels which bet2 can sometimes leave behind. This can be useful\
            when running SIENA or SIENAX, for example. Various stages involving\
            standard-space masking, morphpological operations and thresholdings are\
            combined to produce a result which can often give better results than\
            just running bet2.
        reduce_bias: This attempts to reduce image bias, and residual neck\
            voxels. This can be useful when running SIENA or SIENAX, for example.\
            Various stages involving FAST segmentation-based bias field removal and\
            standard-space masking are combined to produce a result which can often\
            give better results than just running bet2.
        slice_padding: This can improve the brain extraction if only a few\
            slices are present in the data (i.e., a small field of view in the Z\
            direction). This is achieved by padding the end slices in both\
            directions, copying the end slices several times, running bet2 and then\
            removing the added slices.
        whole_set_mask: This option uses bet2 to determine a brain mask on the\
            basis of the first volume in a 4D data set, and applies this to the\
            whole data set. This is principally intended for use on FMRI data, for\
            example to remove eyeballs. Because it is normally important (in this\
            application) that masking be liberal (ie that there be little risk of\
            cutting out valid brain voxels) the -f threshold is reduced to 0.3, and\
            also the brain mask is "dilated" slightly before being used.
        additional_surfaces: This runs both bet2 and betsurf programs in order\
            to get the additional skull and scalp surfaces created by betsurf. This\
            involves registering to standard space in order to allow betsurf to\
            find the standard space masks it needs.
        additional_surfaces_t2: This is the same as -A except that a T2 image\
            is also input, to further improve the estimated skull and scalp\
            surfaces. As well as carrying out the standard space registration this\
            also registers the T2 to the T1 input image.
        verbose: Switch on diagnostic messages.
        debug: Don't delete temporary intermediate images.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BET_METADATA)
    params = bet_params(infile=infile, maskfile=maskfile, fractional_intensity=fractional_intensity, vg_fractional_intensity=vg_fractional_intensity, center_of_gravity=center_of_gravity, overlay=overlay, binary_mask=binary_mask, approx_skull=approx_skull, no_seg_output=no_seg_output, vtk_mesh=vtk_mesh, head_radius=head_radius, thresholding=thresholding, robust_iters=robust_iters, residual_optic_cleanup=residual_optic_cleanup, reduce_bias=reduce_bias, slice_padding=slice_padding, whole_set_mask=whole_set_mask, additional_surfaces=additional_surfaces, additional_surfaces_t2=additional_surfaces_t2, verbose=verbose, debug=debug)
    return bet_execute(params, execution)


__all__ = [
    "BET_METADATA",
    "BetOutputs",
    "BetParameters",
    "bet",
    "bet_params",
]

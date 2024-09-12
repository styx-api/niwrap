# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_UNIFIZE_METADATA = Metadata(
    id="259ba307ec72b60b5a71967c5fecb810a7081943.boutiques",
    name="3dUnifize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dUnifizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_unifize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Unifized file."""
    scale_file_outfile: OutputPathType | None
    """Scale factor file."""


def v_3d_unifize(
    in_file: InputPathType,
    cl_frac: float | None = None,
    epi: bool = False,
    gm: bool = False,
    no_duplo: bool = False,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    quiet: bool = False,
    rbt: list[float] | None = None,
    scale_file: InputPathType | None = None,
    t2: bool = False,
    t2_up: float | None = None,
    urad: float | None = None,
    runner: Runner | None = None,
) -> V3dUnifizeOutputs:
    """
    3dUnifize - for uniformizing image intensity
    * The input dataset is supposed to be a T1-weighted volume, possibly already
    skull-stripped (e.g., via 3dSkullStrip). However, this program can be a
    useful step to take BEFORE 3dSkullStrip, since the latter program can fail
    if the input volume is strongly shaded -- 3dUnifize will (mostly) remove
    such shading artifacts.
    * The output dataset has the white matter (WM) intensity approximately
    uniformized across space, and scaled to peak at about 1000.
    * The output dataset is always stored in float format!
    * If the input dataset has more than 1 sub-brick, only sub-brick #0 will be
    processed!
    * Want to correct EPI datasets for nonuniformity? You can try the new and
    experimental [Mar 2017] '-EPI' option.
    * The principal motive for this program is for use in an image registration
    script, and it may or may not be useful otherwise.
    * This program replaces the older (and very different) 3dUniformize, which
    is no longer maintained and may sublimate at any moment. (In other words, we
    do not recommend the use of 3dUniformize.).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dUnifize.html
    
    Args:
        in_file: Input file to 3dunifize.
        cl_frac: Option for afni experts only.set the automask 'clip level\
            fraction'. must be between 0.1 and 0.9. a small fraction means to make\
            the initial threshold for clipping (a la 3dcliplevel) smaller, which\
            will tend to make the mask larger. [default=0.1].
        epi: Assume the input dataset is a t2 (or t2\*) weighted epi time\
            series. after computing the scaling, apply it to all volumes (trs) in\
            the input dataset. that is, a given voxel will be scaled by the same\
            factor at each tr. this option also implies '-noduplo' and '-t2'.this\
            option turns off '-gm' if you turned it on.
        gm: Also scale to unifize 'gray matter' = lower intensity voxels (to\
            aid in registering images from different scanners).
        no_duplo: Do not use the 'duplo down' step; this can be useful for\
            lower resolution datasets.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        quiet: Don't print the progress messages.
        rbt: (a float, a float, a float). Option for afni experts only.specify\
            the 3 parameters for the algorithm:r = radius; same as given by option\
            '-urad', [default=18.3]b = bottom percentile of normalizing data range,\
            [default=70.0]r = top percentile of normalizing data range,\
            [default=80.0].
        scale_file: Output file name to save the scale factor used at each\
            voxel .
        t2: Treat the input as if it were t2-weighted, rather than t1-weighted.\
            this processing is done simply by inverting the image contrast,\
            processing it as if that result were t1-weighted, and then re-inverting\
            the results counts of voxel overlap, i.e., each voxel will contain the\
            number of masks that it is set in.
        t2_up: Option for afni experts only.set the upper percentile point used\
            for t2-t1 inversion. allowed to be anything between 90 and 100\
            (inclusive), with default to 98.5 (for no good reason).
        urad: Sets the radius (in voxels) of the ball used for the sneaky\
            trick. default value is 18.3, and should be changed proportionally if\
            the dataset voxel size differs significantly from 1 mm.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dUnifizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_UNIFIZE_METADATA)
    cargs = []
    cargs.append("3dUnifize")
    cargs.extend([
        "-input",
        execution.input_file(in_file)
    ])
    if cl_frac is not None:
        cargs.extend([
            "-clfrac",
            str(cl_frac)
        ])
    if epi:
        cargs.append("-EPI")
    if gm:
        cargs.append("-GM")
    if no_duplo:
        cargs.append("-noduplo")
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if quiet:
        cargs.append("-quiet")
    if rbt is not None:
        cargs.extend([
            "-rbt",
            *map(str, rbt)
        ])
    if scale_file is not None:
        cargs.extend([
            "-ssave",
            execution.input_file(scale_file)
        ])
    if t2:
        cargs.append("-T2")
    if t2_up is not None:
        cargs.extend([
            "-T2up",
            str(t2_up)
        ])
    if urad is not None:
        cargs.extend([
            "-Urad",
            str(urad)
        ])
    ret = V3dUnifizeOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(in_file).name + "_unifized"),
        out_file_=execution.output_file("out_file"),
        scale_file_outfile=execution.output_file(pathlib.Path(scale_file).name) if (scale_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dUnifizeOutputs",
    "V_3D_UNIFIZE_METADATA",
    "v_3d_unifize",
]

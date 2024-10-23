# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EPI_REG_METADATA = Metadata(
    id="7481c2d9b1035205edb4364331a1b543505879dd.boutiques",
    name="epi_reg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class EpiRegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `epi_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    epi2str_inv: OutputPathType
    """Rigid structural-to-epi transform."""
    epi2str_mat: OutputPathType
    """Rigid epi-to-structural transform."""
    fmap2epi_mat: OutputPathType
    """Rigid fieldmap-to-epi transform."""
    fmap2str_mat: OutputPathType
    """Rigid fieldmap-to-structural transform."""
    fmap_epi: OutputPathType
    """Fieldmap in epi space."""
    fmap_str: OutputPathType
    """Fieldmap in structural space."""
    fmapmag_str: OutputPathType
    """Fieldmap magnitude image in structural space."""
    fullwarp: OutputPathType
    """Warpfield to unwarp epi and transform into structural space."""
    out_1vol: OutputPathType
    """Unwarped and coregistered single volume."""
    out_file: OutputPathType
    """Unwarped and coregistered epi input."""
    seg: OutputPathType
    """White matter, gray matter, csf segmentation."""
    shiftmap: OutputPathType
    """Shiftmap in epi space."""
    wmedge: OutputPathType
    """White matter edges for visualization."""
    wmseg_outfile: OutputPathType
    """White matter segmentation used in flirt bbr."""


def epi_reg(
    epi: InputPathType,
    t1_head: InputPathType,
    t1_brain: InputPathType,
    out_base_name: str,
    echospacing: float | None = None,
    fmap: InputPathType | None = None,
    fmapmag: InputPathType | None = None,
    fmapmagbrain: InputPathType | None = None,
    no_clean: bool = False,
    no_fmapreg: bool = False,
    pedir: typing.Literal["x", "y", "z", "-x", "-y", "-z"] | None = None,
    weight_image: InputPathType | None = None,
    wmseg: InputPathType | None = None,
    runner: Runner | None = None,
) -> EpiRegOutputs:
    """
    Runs FSL epi_reg script for simultaneous coregistration and fieldmap unwarping.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        epi: EPI Nifti image.
        t1_head: Wholehead T1 image.
        t1_brain: Brain-extracted T1 image.
        out_base_name: Output base name.
        echospacing: Effective epi echo spacing (sometimes called dwell time) -\
            in seconds.
        fmap: Fieldmap image (in rad/s).
        fmapmag: Fieldmap magnitude image - wholehead.
        fmapmagbrain: Fieldmap magnitude image - brain extracted.
        no_clean: Do not clean up intermediate files.
        no_fmapreg: Do not perform registration of fmap to t1 (use if fmap\
            already registered).
        pedir: 'x' or 'y' or 'z' or '-x' or '-y' or '-z'. Phase encoding\
            direction, dir = x/y/z/-x/-y/-z.
        weight_image: Weighting image (in t1 space).
        wmseg: White matter segmentation of t1 image, has to be named like the\
            t1brain and end on _wmseg.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EpiRegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EPI_REG_METADATA)
    cargs = []
    cargs.append("epi_reg")
    cargs.append("--epi=" + execution.input_file(epi))
    cargs.append("--t1=" + execution.input_file(t1_head))
    cargs.append("--t1brain=" + execution.input_file(t1_brain))
    cargs.append("--out=" + out_base_name)
    if echospacing is not None:
        cargs.append("--echospacing=" + str(echospacing))
    if fmap is not None:
        cargs.append("--fmap=" + execution.input_file(fmap))
    if fmapmag is not None:
        cargs.append("--fmapmag=" + execution.input_file(fmapmag))
    if fmapmagbrain is not None:
        cargs.append("--fmapmagbrain=" + execution.input_file(fmapmagbrain))
    if no_clean:
        cargs.append("--noclean")
    if no_fmapreg:
        cargs.append("--nofmapreg")
    if pedir is not None:
        cargs.append("--pedir=" + pedir)
    if weight_image is not None:
        cargs.append("--weight=" + execution.input_file(weight_image))
    if wmseg is not None:
        cargs.append("--wmseg=" + execution.input_file(wmseg))
    ret = EpiRegOutputs(
        root=execution.output_file("."),
        epi2str_inv=execution.output_file("epi2str_inv.mat"),
        epi2str_mat=execution.output_file("epi2struct.mat"),
        fmap2epi_mat=execution.output_file("fmap2epi.mat"),
        fmap2str_mat=execution.output_file("fmap2str.mat"),
        fmap_epi=execution.output_file("fmap_epi.nii.gz"),
        fmap_str=execution.output_file("fmap_str.nii.gz"),
        fmapmag_str=execution.output_file("fmapmag_str.nii.gz"),
        fullwarp=execution.output_file("fullwarp.nii.gz"),
        out_1vol=execution.output_file("out_1vol.nii.gz"),
        out_file=execution.output_file(out_base_name + ".nii.gz"),
        seg=execution.output_file(out_base_name + "_fast_seg.nii.gz"),
        shiftmap=execution.output_file("shiftmap.nii.gz"),
        wmedge=execution.output_file(out_base_name + "_fast_wmedge.nii.gz"),
        wmseg_outfile=execution.output_file(out_base_name + "_fast_wmseg.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EPI_REG_METADATA",
    "EpiRegOutputs",
    "epi_reg",
]

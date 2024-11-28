# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFREG_METADATA = Metadata(
    id="68e84766e8130637a36f745fc7308f0bf775b2d7.boutiques",
    name="surfreg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SurfregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surfreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface registration file"""


def surfreg(
    subject: str,
    target: str,
    cross_hemi: bool = False,
    reg_lh: bool = False,
    reg_rh: bool = False,
    reg_both: bool = False,
    no_annot: bool = False,
    annot: str | None = None,
    aparc: bool = False,
    noneg: bool = False,
    init_reg: str | None = None,
    lta: str | None = None,
    init_from_tal: bool = False,
    outsurf: str | None = None,
    no_set_vol_geom: bool = False,
    threads: float | None = None,
    runner: Runner | None = None,
) -> SurfregOutputs:
    """
    Performs surface registration (mris_register) between a subject and a target
    average subject based on the hemi.reg.template.tif atlas in the average subject.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject to register.
        target: Target average subject to use as a registration target.
        cross_hemi: Perform cross-hemi registration.
        reg_lh: Register left hemisphere only.
        reg_rh: Register right hemisphere only.
        reg_both: Register both left and right hemispheres.
        no_annot: Do not use annot to rip.
        annot: Use specified annotation name.
        aparc: Set annotation name to aparc.annot.
        noneg: Option flag with unspecified behavior in the provided help text.
        init_reg: Initial registration name, default is sphere.
        lta: Apply rotational components of affine registration.
        init_from_tal: Use talaiach.xfm.lta for initial spherical registration.
        outsurf: Output surface name, default depends on the target.
        no_set_vol_geom: Do not set volume geometry and center the sphere.
        threads: Number of threads to run in parallel.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFREG_METADATA)
    cargs = []
    cargs.append("surfreg")
    cargs.extend([
        "--s",
        subject
    ])
    cargs.extend([
        "--t",
        target
    ])
    if cross_hemi:
        cargs.append("--xhemi")
    if reg_lh:
        cargs.append("--lh")
    if reg_rh:
        cargs.append("--rh")
    if reg_both:
        cargs.append("--lhrh")
    if no_annot:
        cargs.append("--no-annot")
    if annot is not None:
        cargs.extend([
            "--annot",
            annot
        ])
    if aparc:
        cargs.append("--aparc")
    if noneg:
        cargs.append("--noneg")
    if init_reg is not None:
        cargs.extend([
            "--init-reg",
            init_reg
        ])
    if lta is not None:
        cargs.extend([
            "--lta",
            lta
        ])
    if init_from_tal:
        cargs.append("--init-from-tal")
    if outsurf is not None:
        cargs.extend([
            "--o",
            outsurf
        ])
    if no_set_vol_geom:
        cargs.append("--no-set-vol-geom")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    ret = SurfregOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file("subject/surf/hemi.target.sphere.reg"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFREG_METADATA",
    "SurfregOutputs",
    "surfreg",
]

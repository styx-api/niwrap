# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_REG_ANA_METADATA = Metadata(
    id="1631118904756d1061212c150565890bf979dbc0.boutiques",
    name="3dRegAna",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dRegAnaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_reg_ana(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_fift: OutputPathType
    """Output fift dataset"""
    output_fith: OutputPathType
    """Output fith dataset"""
    output_fitt: OutputPathType
    """Output fitt dataset"""
    output_bucket: OutputPathType
    """Output bucket dataset"""
    output_bucket_brik: OutputPathType
    """Output bucket BRIK file"""


def v_3d_reg_ana(
    rows: float,
    cols: float,
    xydata: list[str],
    model: str,
    diskspace: bool = False,
    workmem: float | None = None,
    rmsmin: float | None = None,
    fdisp: float | None = None,
    flof: float | None = None,
    fcoef: list[str] | None = None,
    rcoef: list[str] | None = None,
    tcoef: list[str] | None = None,
    bucket: str | None = None,
    brick: list[str] | None = None,
    datum: str | None = None,
    runner: Runner | None = None,
) -> V3dRegAnaOutputs:
    """
    Multiple linear regression analysis for AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        rows: Number of input datasets.
        cols: Number of X variables.
        xydata: X variables and Y observations.
        model: Definition of linear regression model: reduced model (Y =\
            f(Xj1,...,Xjr)) and full model (Y = f(Xj1,...,Xjr,Xi1,...,Xiq)).
        diskspace: Print out disk space required for program execution.
        workmem: Number of megabytes of RAM to use for statistical workspace\
            (default = 750).
        rmsmin: Minimum rms error to reject constant model.
        fdisp: Display results for voxels whose F-statistic is > fval.
        flof: Minimum p value for F due to lack of fit.
        fcoef: Estimate of kth regression coefficient along with F-test for the\
            regression is written to AFNI `fift` dataset.
        rcoef: Estimate of kth regression coefficient along with coef. of mult.\
            deter. R^2 is written to AFNI `fith` dataset.
        tcoef: Estimate of kth regression coefficient along with t-test for the\
            coefficient is written to AFNI `fitt` dataset.
        bucket: Create one AFNI 'bucket' dataset having n sub-bricks; n=0\
            creates default output.
        brick: Specify the contents of the mth sub-brick in the bucket dataset.
        datum: Write the output in DATUM format. Choose from short (default) or\
            float.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRegAnaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_REG_ANA_METADATA)
    cargs = []
    cargs.append("3dRegAna")
    cargs.extend([
        "-rows",
        str(rows)
    ])
    cargs.extend([
        "-cols",
        str(cols)
    ])
    cargs.extend([
        "-xydata",
        *xydata
    ])
    cargs.extend([
        "-model",
        model
    ])
    if diskspace:
        cargs.append("-diskspace")
    if workmem is not None:
        cargs.extend([
            "-workmem",
            str(workmem)
        ])
    if rmsmin is not None:
        cargs.extend([
            "-rmsmin",
            str(rmsmin)
        ])
    if fdisp is not None:
        cargs.extend([
            "-fdisp",
            str(fdisp)
        ])
    if flof is not None:
        cargs.extend([
            "-flof",
            str(flof)
        ])
    if fcoef is not None:
        cargs.extend([
            "-fcoef",
            *fcoef
        ])
    if rcoef is not None:
        cargs.extend([
            "-rcoef",
            *rcoef
        ])
    if tcoef is not None:
        cargs.extend([
            "-tcoef",
            *tcoef
        ])
    if bucket is not None:
        cargs.extend([
            "-bucket",
            bucket
        ])
    if brick is not None:
        cargs.extend([
            "-brick",
            *brick
        ])
    if datum is not None:
        cargs.extend([
            "-datum",
            datum
        ])
    ret = V3dRegAnaOutputs(
        root=execution.output_file("."),
        output_fift=execution.output_file("[PREFIX].fift+orig.HEAD"),
        output_fith=execution.output_file("[PREFIX].fith+orig.HEAD"),
        output_fitt=execution.output_file("[PREFIX].fitt+orig.HEAD"),
        output_bucket=execution.output_file("[PREFIX].bucket+orig.HEAD"),
        output_bucket_brik=execution.output_file("[PREFIX].bucket+orig.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dRegAnaOutputs",
    "V_3D_REG_ANA_METADATA",
    "v_3d_reg_ana",
]

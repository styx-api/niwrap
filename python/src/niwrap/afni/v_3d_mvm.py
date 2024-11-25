# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_MVM_METADATA = Metadata(
    id="2612be5737b405f93347f59a146e22ee9c08162b.boutiques",
    name="3dMVM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dMvmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mvm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_head: OutputPathType
    """Output HEAD file in AFNI format"""
    outfile_brik: OutputPathType
    """Output BRIK file in AFNI format"""


def v_3d_mvm(
    prefix: str,
    bs_vars: str,
    data_table: str,
    dbg_args: str | None = None,
    jobs: int | None = None,
    mask: InputPathType | None = None,
    ws_vars: str | None = None,
    q_vars: str | None = None,
    q_var_centers: str | None = None,
    num_glt: int | None = None,
    glt_label: str | None = None,
    glt_code: str | None = None,
    num_glf: int | None = None,
    glf_label: str | None = None,
    glf_code: str | None = None,
    runner: Runner | None = None,
) -> V3dMvmOutputs:
    """
    AFNI Group Analysis Program with Multi-Variate Modeling Approach.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file name prefix.
        bs_vars: Formula for between-subjects variables.
        data_table: Data table for analysis.
        dbg_args: Enable R to save parameters in a file for debugging.
        jobs: Number of jobs for parallel processing.
        mask: Only process voxels inside this mask.
        ws_vars: Formula for within-subjects variables.
        q_vars: Comma-separated list of quantitative variables (covariates).
        q_var_centers: Comma-separated centering values for quantitative\
            variables.
        num_glt: Number of general linear t-tests (GLTs).
        glt_label: Label for each general linear t-test (GLT).
        glt_code: Coding for each general linear t-test (GLT).
        num_glf: Number of general linear F-tests (GLFs).
        glf_label: Label for each general linear F-test (GLF).
        glf_code: Coding for each general linear F-test (GLF).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMvmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MVM_METADATA)
    cargs = []
    cargs.append("3dMVM")
    if dbg_args is not None:
        cargs.append(dbg_args)
    cargs.extend([
        "-prefix",
        prefix
    ])
    if jobs is not None:
        cargs.extend([
            "-jobs",
            str(jobs)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    cargs.extend([
        "-bsVars",
        bs_vars
    ])
    if ws_vars is not None:
        cargs.extend([
            "-wsVars",
            ws_vars
        ])
    if q_vars is not None:
        cargs.extend([
            "-qVars",
            q_vars
        ])
    if q_var_centers is not None:
        cargs.extend([
            "-qVarCenters",
            q_var_centers
        ])
    if num_glt is not None:
        cargs.extend([
            "-num_glt",
            str(num_glt)
        ])
    if glt_label is not None:
        cargs.extend([
            "-gltLabel",
            glt_label
        ])
    if glt_code is not None:
        cargs.extend([
            "-gltCode",
            glt_code
        ])
    if num_glf is not None:
        cargs.extend([
            "-num_glf",
            str(num_glf)
        ])
    if glf_label is not None:
        cargs.extend([
            "-glfLabel",
            glf_label
        ])
    if glf_code is not None:
        cargs.extend([
            "-glfCode",
            glf_code
        ])
    cargs.extend([
        "-dataTable",
        data_table
    ])
    ret = V3dMvmOutputs(
        root=execution.output_file("."),
        outfile_head=execution.output_file(prefix + "+tlrc.HEAD"),
        outfile_brik=execution.output_file(prefix + "+tlrc.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dMvmOutputs",
    "V_3D_MVM_METADATA",
    "v_3d_mvm",
]

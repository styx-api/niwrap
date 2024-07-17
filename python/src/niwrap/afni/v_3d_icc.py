# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ICC_METADATA = Metadata(
    id="8ff7f742055734d6ec1c36afde9bdd4a6e8c531c",
    name="3dICC",
)


class V3dIccOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_icc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Name of the output file"""


def v_3d_icc(
    prefix: str,
    model: str,
    data_table: str,
    mask: InputPathType | None = None,
    bounds: list[float | int] | None = None,
    jobs: float | int | None = None,
    q_vars: str | None = None,
    q_var_centers: str | None = None,
    subj: str | None = None,
    input_file_column: str | None = None,
    t_stat: str | None = None,
    dbg_args: bool = False,
    cio: bool = False,
    rio: bool = False,
    runner: Runner | None = None,
) -> V3dIccOutputs:
    """
    3dICC by Gang Chen.
    
    AFNI Program for IntraClass Correlatin (ICC) Analysis.
    
    Args:
        prefix: Name of output file. For AFNI format, provide prefix only, with\
            no view+suffix needed. Filename for NIfTI format should have .nii\
            attached, while file name for surface data is expected to end with\
            .niml.dset.
        model: Model structure for all the variables. The expression FORMULA\
            with more than one variable has to be surrounded within quotes.\
            Variable names should be consistent with the ones used in the header of\
            -dataTable.
        data_table: List the data structure with a header as the first line.\
            The first column is reserved with label 'Subj', and the last is\
            reserved for 'InputFile'.
        mask: Path to mask file. Only process voxels inside this mask.
        bounds: Bounds for outlier removal. Provide two numbers: the lower\
            bound (lb) and the upper bound (ub). Input data will be confined within\
            [lb, ub]. Any values beyond the bounds will be treated as missing.
        jobs: Number of jobs for parallel computing. Choose 1 for a\
            single-processor computer.
        q_vars: Identify quantitative variables with this option. List should\
            be separated with comma and surrounded within quotes.
        q_var_centers: Specify centering values for quantitative variables\
            identified under -qVars. Multiple centers are separated by commas and\
            should be surrounded within quotes.
        subj: Specify the column name that is designated as the measuring\
            entity variable (usually subject).
        input_file_column: Specify the last column name that is designated for\
            input files of effect estimate.
        t_stat: Specify the column name that is designated as the t-statistic.
        dbg_args: Enable R to save the parameters in a file called\
            .3dICC.dbg.AFNI.args in the current directory for debugging.
        cio: Use AFNI's C io functions. Default is -cio.
        rio: Use R's io functions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dIccOutputs`).
    """
    runner = runner or get_global_runner()
    if bounds is not None and (len(bounds) != 2): 
        raise ValueError(f"Length of 'bounds' must be 2 but was {len(bounds)}")
    execution = runner.start_execution(V_3D_ICC_METADATA)
    cargs = []
    cargs.append("3dICC")
    cargs.append(model)
    cargs.append("-prefix")
    cargs.append(prefix)
    cargs.append("-mask")
    if mask is not None:
        cargs.append(execution.input_file(mask))
    cargs.append("-dataTable")
    cargs.append(data_table)
    cargs.append("[OPTIONS]")
    ret = V3dIccOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{prefix}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dIccOutputs",
    "V_3D_ICC_METADATA",
    "v_3d_icc",
]

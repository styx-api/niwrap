# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_CORRELATION_METADATA = Metadata(
    id="ea40c5ad544d70e0863556307f65b16367de6a39",
    name="cifti-correlation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiCorrelationRoiOverride:
    """
    perform correlation from a subset of rows to all rows
    """
    opt_left_roi_roi_metric: InputPathType | None = None
    """use an roi for left hempsphere: the left roi as a metric file"""
    opt_right_roi_roi_metric: InputPathType | None = None
    """use an roi for right hempsphere: the right roi as a metric file"""
    opt_cerebellum_roi_roi_metric: InputPathType | None = None
    """use an roi for cerebellum: the cerebellum roi as a metric file"""
    opt_vol_roi_roi_vol: InputPathType | None = None
    """use an roi for volume: the volume roi file"""
    opt_cifti_roi_roi_cifti: InputPathType | None = None
    """use a cifti file for combined rois: the cifti roi file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-roi-override")
        if self.opt_left_roi_roi_metric is not None:
            cargs.extend(["-left-roi", execution.input_file(self.opt_left_roi_roi_metric)])
        if self.opt_right_roi_roi_metric is not None:
            cargs.extend(["-right-roi", execution.input_file(self.opt_right_roi_roi_metric)])
        if self.opt_cerebellum_roi_roi_metric is not None:
            cargs.extend(["-cerebellum-roi", execution.input_file(self.opt_cerebellum_roi_roi_metric)])
        if self.opt_vol_roi_roi_vol is not None:
            cargs.extend(["-vol-roi", execution.input_file(self.opt_vol_roi_roi_vol)])
        if self.opt_cifti_roi_roi_cifti is not None:
            cargs.extend(["-cifti-roi", execution.input_file(self.opt_cifti_roi_roi_cifti)])
        return cargs


class CiftiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_correlation(
    cifti: InputPathType,
    cifti_out: str,
    roi_override: CiftiCorrelationRoiOverride | None = None,
    opt_weights_weight_file: str | None = None,
    opt_fisher_z: bool = False,
    opt_no_demean: bool = False,
    opt_covariance: bool = False,
    opt_mem_limit_limit_gb: float | int | None = None,
    runner: Runner = None,
) -> CiftiCorrelationOutputs:
    """
    cifti-correlation by Washington University School of Medicin.
    
    Generate correlation of rows in a cifti file.
    
    For each row (or each row inside an roi if -roi-override is specified),
    correlate to all other rows. The -cifti-roi suboption to -roi-override may
    not be specified with any other -*-roi suboption, but you may specify the
    other -*-roi suboptions together.
    
    When using the -fisher-z option, the output is NOT a Z-score, it is
    artanh(r), to do further math on this output, consider using -cifti-math.
    
    Restricting the memory usage will make it calculate the output in chunks,
    and if the input file size is more than 70% of the memory limit, it will
    also read through the input file as rows are required, resulting in several
    passes through the input file (once per chunk). Memory limit does not need
    to be an integer, you may also specify 0 to calculate a single output row at
    a time (this may be very slow).
    
    Args:
        cifti: input cifti file.
        cifti_out: output cifti file.
        roi_override: perform correlation from a subset of rows to all rows.
        opt_weights_weight_file: specify column weights: text file containing\
            one weight per column.
        opt_fisher_z: apply fisher small z transform (ie, artanh) to\
            correlation.
        opt_no_demean: instead of correlation, do dot product of rows, then\
            normalize by diagonal.
        opt_covariance: compute covariance instead of correlation.
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in\
            gigabytes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-correlation")
    cargs.append(execution.input_file(cifti))
    cargs.append(cifti_out)
    if roi_override is not None:
        cargs.extend(roi_override.run(execution))
    if opt_weights_weight_file is not None:
        cargs.extend(["-weights", opt_weights_weight_file])
    if opt_fisher_z:
        cargs.append("-fisher-z")
    if opt_no_demean:
        cargs.append("-no-demean")
    if opt_covariance:
        cargs.append("-covariance")
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    ret = CiftiCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CORRELATION_METADATA",
    "CiftiCorrelationOutputs",
    "CiftiCorrelationRoiOverride",
    "cifti_correlation",
]

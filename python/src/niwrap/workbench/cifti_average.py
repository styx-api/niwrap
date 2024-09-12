# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_AVERAGE_METADATA = Metadata(
    id="3551f2ac0e86b0fb9c94b69c40047dfc5baa6806.boutiques",
    name="cifti-average",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiAverageExcludeOutliers:
    """
    exclude outliers by standard deviation of each element across files.
    """
    sigma_below: float
    """number of standard deviations below the mean to include"""
    sigma_above: float
    """number of standard deviations above the mean to include"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-exclude-outliers")
        cargs.append(str(self.sigma_below))
        cargs.append(str(self.sigma_above))
        return cargs


@dataclasses.dataclass
class CiftiAverageCifti:
    """
    specify an input file.
    """
    cifti_in: InputPathType
    """the input cifti file"""
    opt_weight_weight: float | None = None
    """give a weight for this file: the weight to use"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-cifti")
        cargs.append(execution.input_file(self.cifti_in))
        if self.opt_weight_weight is not None:
            cargs.extend([
                "-weight",
                str(self.opt_weight_weight)
            ])
        return cargs


class CiftiAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_average(
    cifti_out: str,
    exclude_outliers: CiftiAverageExcludeOutliers | None = None,
    opt_mem_limit_limit_gb: float | None = None,
    cifti: list[CiftiAverageCifti] | None = None,
    runner: Runner | None = None,
) -> CiftiAverageOutputs:
    """
    Average cifti files.
    
    Averages cifti files together. Files without -weight specified are given a
    weight of 1. If -exclude-outliers is specified, at each element, the data
    across all files is taken as a set, its unweighted mean and sample standard
    deviation are found, and values outside the specified number of standard
    deviations are excluded from the (potentially weighted) average at that
    element.
    
    Author: Washington University School of Medicin
    
    Args:
        cifti_out: output cifti file.
        exclude_outliers: exclude outliers by standard deviation of each\
            element across files.
        opt_mem_limit_limit_gb: restrict memory used for file reading\
            efficiency: memory limit in gigabytes.
        cifti: specify an input file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_AVERAGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average")
    cargs.append(cifti_out)
    if exclude_outliers is not None:
        cargs.extend(exclude_outliers.run(execution))
    if opt_mem_limit_limit_gb is not None:
        cargs.extend([
            "-mem-limit",
            str(opt_mem_limit_limit_gb)
        ])
    if cifti is not None:
        cargs.extend([a for c in [s.run(execution) for s in cifti] for a in c])
    ret = CiftiAverageOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_AVERAGE_METADATA",
    "CiftiAverageCifti",
    "CiftiAverageExcludeOutliers",
    "CiftiAverageOutputs",
    "cifti_average",
]

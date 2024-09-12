# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_CONVERT_METADATA = Metadata(
    id="1e779534088fcd161aaabcf0b181dd8df7dea118.boutiques",
    name="metric-convert",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class MetricConvertToNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MetricConvertToNifti | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    nifti_out: OutputPathType
    """the output nifti file"""


@dataclasses.dataclass
class MetricConvertToNifti:
    """
    convert metric to nifti.
    """
    metric_in: InputPathType
    """the metric to convert"""
    nifti_out: str
    """the output nifti file"""
    
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
        cargs.append("-to-nifti")
        cargs.append(execution.input_file(self.metric_in))
        cargs.append(self.nifti_out)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MetricConvertToNiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MetricConvertToNiftiOutputs`).
        """
        ret = MetricConvertToNiftiOutputs(
            root=execution.output_file("."),
            nifti_out=execution.output_file(self.nifti_out),
        )
        return ret


class MetricConvertFromNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MetricConvertFromNifti | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


@dataclasses.dataclass
class MetricConvertFromNifti:
    """
    convert nifti to metric.
    """
    nifti_in: InputPathType
    """the nifti file to convert"""
    surface_in: InputPathType
    """surface file to use number of vertices and structure from"""
    metric_out: str
    """the output metric file"""
    
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
        cargs.append("-from-nifti")
        cargs.append(execution.input_file(self.nifti_in))
        cargs.append(execution.input_file(self.surface_in))
        cargs.append(self.metric_out)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MetricConvertFromNiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MetricConvertFromNiftiOutputs`).
        """
        ret = MetricConvertFromNiftiOutputs(
            root=execution.output_file("."),
            metric_out=execution.output_file(self.metric_out),
        )
        return ret


class MetricConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    to_nifti: MetricConvertToNiftiOutputs | None
    """Outputs from `MetricConvertToNifti`."""
    from_nifti: MetricConvertFromNiftiOutputs | None
    """Outputs from `MetricConvertFromNifti`."""


def metric_convert(
    to_nifti: MetricConvertToNifti | None = None,
    from_nifti: MetricConvertFromNifti | None = None,
    runner: Runner | None = None,
) -> MetricConvertOutputs:
    """
    Convert metric file to fake nifti.
    
    The purpose of this command is to convert between metric files and nifti1 so
    that gifti-unaware programs can operate on the data. You must specify
    exactly one of the options.
    
    Author: Washington University School of Medicin
    
    Args:
        to_nifti: convert metric to nifti.
        from_nifti: convert nifti to metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-convert")
    if to_nifti is not None:
        cargs.extend(to_nifti.run(execution))
    if from_nifti is not None:
        cargs.extend(from_nifti.run(execution))
    ret = MetricConvertOutputs(
        root=execution.output_file("."),
        to_nifti=to_nifti.outputs(execution) if to_nifti else None,
        from_nifti=from_nifti.outputs(execution) if from_nifti else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_CONVERT_METADATA",
    "MetricConvertFromNifti",
    "MetricConvertFromNiftiOutputs",
    "MetricConvertOutputs",
    "MetricConvertToNifti",
    "MetricConvertToNiftiOutputs",
    "metric_convert",
]

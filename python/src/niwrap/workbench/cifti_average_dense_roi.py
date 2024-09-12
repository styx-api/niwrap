# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_AVERAGE_DENSE_ROI_METADATA = Metadata(
    id="c4e840874826cfe093198a63d8044f319d7c2e7e.boutiques",
    name="cifti-average-dense-roi",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiAverageDenseRoiCiftiRoi:
    """
    cifti file containing combined weights.
    """
    roi_cifti: InputPathType
    """the roi cifti file"""
    opt_in_memory: bool = False
    """cache the roi in memory so that it isn't re-read for each input cifti"""
    
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
        cargs.append("-cifti-roi")
        cargs.append(execution.input_file(self.roi_cifti))
        if self.opt_in_memory:
            cargs.append("-in-memory")
        return cargs


@dataclasses.dataclass
class CiftiAverageDenseRoiCifti:
    """
    specify an input cifti file.
    """
    cifti_in: InputPathType
    """a cifti file to average across"""
    
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
        return cargs


class CiftiAverageDenseRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average_dense_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti dscalar file"""


def cifti_average_dense_roi(
    cifti_out: str,
    cifti_roi: CiftiAverageDenseRoiCiftiRoi | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    cifti: list[CiftiAverageDenseRoiCifti] | None = None,
    runner: Runner | None = None,
) -> CiftiAverageDenseRoiOutputs:
    """
    Average cifti rows across subjects by roi.
    
    Averages rows for each map of the ROI(s), across all files. ROI maps are
    treated as weighting functions, including negative values. For efficiency,
    ensure that everything that is not intended to be used is zero in the ROI
    map. If -cifti-roi is specified, -left-roi, -right-roi, -cerebellum-roi, and
    -vol-roi must not be specified. If multiple non-cifti ROI files are
    specified, they must have the same number of columns.
    
    Author: Washington University School of Medicin
    
    Args:
        cifti_out: output cifti dscalar file.
        cifti_roi: cifti file containing combined weights.
        opt_left_roi_roi_metric: weights to use for left hempsphere: the left\
            roi as a metric file.
        opt_right_roi_roi_metric: weights to use for right hempsphere: the\
            right roi as a metric file.
        opt_cerebellum_roi_roi_metric: weights to use for cerebellum surface:\
            the cerebellum roi as a metric file.
        opt_vol_roi_roi_vol: voxel weights to use: the roi volume file.
        opt_left_area_surf_left_surf: specify the left surface for vertex area\
            correction: the left surface file.
        opt_right_area_surf_right_surf: specify the right surface for vertex\
            area correction: the right surface file.
        opt_cerebellum_area_surf_cerebellum_surf: specify the cerebellum\
            surface for vertex area correction: the cerebellum surface file.
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiAverageDenseRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_AVERAGE_DENSE_ROI_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average-dense-roi")
    cargs.append(cifti_out)
    if cifti_roi is not None:
        cargs.extend(cifti_roi.run(execution))
    if opt_left_roi_roi_metric is not None:
        cargs.extend([
            "-left-roi",
            execution.input_file(opt_left_roi_roi_metric)
        ])
    if opt_right_roi_roi_metric is not None:
        cargs.extend([
            "-right-roi",
            execution.input_file(opt_right_roi_roi_metric)
        ])
    if opt_cerebellum_roi_roi_metric is not None:
        cargs.extend([
            "-cerebellum-roi",
            execution.input_file(opt_cerebellum_roi_roi_metric)
        ])
    if opt_vol_roi_roi_vol is not None:
        cargs.extend([
            "-vol-roi",
            execution.input_file(opt_vol_roi_roi_vol)
        ])
    if opt_left_area_surf_left_surf is not None:
        cargs.extend([
            "-left-area-surf",
            execution.input_file(opt_left_area_surf_left_surf)
        ])
    if opt_right_area_surf_right_surf is not None:
        cargs.extend([
            "-right-area-surf",
            execution.input_file(opt_right_area_surf_right_surf)
        ])
    if opt_cerebellum_area_surf_cerebellum_surf is not None:
        cargs.extend([
            "-cerebellum-area-surf",
            execution.input_file(opt_cerebellum_area_surf_cerebellum_surf)
        ])
    if cifti is not None:
        cargs.extend([a for c in [s.run(execution) for s in cifti] for a in c])
    ret = CiftiAverageDenseRoiOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_AVERAGE_DENSE_ROI_METADATA",
    "CiftiAverageDenseRoiCifti",
    "CiftiAverageDenseRoiCiftiRoi",
    "CiftiAverageDenseRoiOutputs",
    "cifti_average_dense_roi",
]

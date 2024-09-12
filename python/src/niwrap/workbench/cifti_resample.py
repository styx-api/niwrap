# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_RESAMPLE_METADATA = Metadata(
    id="839457011a551747f0c4b7746c3af5e6f7e81680.boutiques",
    name="cifti-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiResampleWeighted:
    """
    use weighted dilation (default).
    """
    opt_exponent_exponent: float | None = None
    """specify exponent in weighting function: exponent 'n' to use in (1 /
    (distance ^ n)) as the weighting function (default 7)"""
    opt_legacy_cutoff: bool = False
    """use v1.3.2 logic for the kernel cutoff"""
    
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
        cargs.append("-weighted")
        if self.opt_exponent_exponent is not None:
            cargs.extend([
                "-exponent",
                str(self.opt_exponent_exponent)
            ])
        if self.opt_legacy_cutoff:
            cargs.append("-legacy-cutoff")
        return cargs


@dataclasses.dataclass
class CiftiResampleVolumePredilate:
    """
    dilate the volume components before resampling.
    """
    dilate_mm: float
    """distance, in mm, to dilate"""
    opt_nearest: bool = False
    """use nearest value dilation"""
    weighted: CiftiResampleWeighted | None = None
    """use weighted dilation (default)"""
    
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
        cargs.append("-volume-predilate")
        cargs.append(str(self.dilate_mm))
        if self.opt_nearest:
            cargs.append("-nearest")
        if self.weighted is not None:
            cargs.extend(self.weighted.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleWeighted_:
    """
    use weighted dilation (default for non-label data).
    """
    opt_exponent_exponent: float | None = None
    """specify exponent in weighting function: exponent 'n' to use in (area /
    (distance ^ n)) as the weighting function (default 6)"""
    opt_legacy_cutoff: bool = False
    """use v1.3.2 logic for the kernel cutoff"""
    
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
        cargs.append("-weighted")
        if self.opt_exponent_exponent is not None:
            cargs.extend([
                "-exponent",
                str(self.opt_exponent_exponent)
            ])
        if self.opt_legacy_cutoff:
            cargs.append("-legacy-cutoff")
        return cargs


@dataclasses.dataclass
class CiftiResampleSurfacePostdilate:
    """
    dilate the surface components after resampling.
    """
    dilate_mm: float
    """distance, in mm, to dilate"""
    opt_nearest: bool = False
    """use nearest value dilation"""
    opt_linear: bool = False
    """use linear dilation"""
    weighted: CiftiResampleWeighted_ | None = None
    """use weighted dilation (default for non-label data)"""
    
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
        cargs.append("-surface-postdilate")
        cargs.append(str(self.dilate_mm))
        if self.opt_nearest:
            cargs.append("-nearest")
        if self.opt_linear:
            cargs.append("-linear")
        if self.weighted is not None:
            cargs.extend(self.weighted.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleFlirt:
    """
    MUST be used if affine is a flirt affine.
    """
    source_volume: str
    """the source volume used when generating the affine"""
    target_volume: str
    """the target volume used when generating the affine"""
    
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
        cargs.append("-flirt")
        cargs.append(self.source_volume)
        cargs.append(self.target_volume)
        return cargs


@dataclasses.dataclass
class CiftiResampleAffine:
    """
    use an affine transformation on the volume components.
    """
    affine_file: str
    """the affine file to use"""
    flirt: CiftiResampleFlirt | None = None
    """MUST be used if affine is a flirt affine"""
    
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
        cargs.append("-affine")
        cargs.append(self.affine_file)
        if self.flirt is not None:
            cargs.extend(self.flirt.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleWarpfield:
    """
    use a warpfield on the volume components.
    """
    warpfield: str
    """the warpfield to use"""
    opt_fnirt_source_volume: str | None = None
    """MUST be used if using a fnirt warpfield: the source volume used when
    generating the warpfield"""
    
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
        cargs.append("-warpfield")
        cargs.append(self.warpfield)
        if self.opt_fnirt_source_volume is not None:
            cargs.extend([
                "-fnirt",
                self.opt_fnirt_source_volume
            ])
        return cargs


@dataclasses.dataclass
class CiftiResampleLeftAreaSurfs:
    """
    specify left surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant left anatomical surface with current mesh"""
    new_area: InputPathType
    """a relevant left anatomical surface with new mesh"""
    
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
        cargs.append("-left-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleLeftAreaMetrics:
    """
    specify left vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for the current mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for the new mesh"""
    
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
        cargs.append("-left-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleLeftSpheres:
    """
    specify spheres for left surface resampling.
    """
    current_sphere: InputPathType
    """a sphere with the same mesh as the current left surface"""
    new_sphere: InputPathType
    """a sphere with the new left mesh that is in register with the current
    sphere"""
    left_area_surfs: CiftiResampleLeftAreaSurfs | None = None
    """specify left surfaces to do vertex area correction based on"""
    left_area_metrics: CiftiResampleLeftAreaMetrics | None = None
    """specify left vertex area metrics to do area correction based on"""
    
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
        cargs.append("-left-spheres")
        cargs.append(execution.input_file(self.current_sphere))
        cargs.append(execution.input_file(self.new_sphere))
        if self.left_area_surfs is not None:
            cargs.extend(self.left_area_surfs.run(execution))
        if self.left_area_metrics is not None:
            cargs.extend(self.left_area_metrics.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleRightAreaSurfs:
    """
    specify right surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant right anatomical surface with current mesh"""
    new_area: InputPathType
    """a relevant right anatomical surface with new mesh"""
    
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
        cargs.append("-right-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleRightAreaMetrics:
    """
    specify right vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for the current mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for the new mesh"""
    
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
        cargs.append("-right-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleRightSpheres:
    """
    specify spheres for right surface resampling.
    """
    current_sphere: InputPathType
    """a sphere with the same mesh as the current right surface"""
    new_sphere: InputPathType
    """a sphere with the new right mesh that is in register with the current
    sphere"""
    right_area_surfs: CiftiResampleRightAreaSurfs | None = None
    """specify right surfaces to do vertex area correction based on"""
    right_area_metrics: CiftiResampleRightAreaMetrics | None = None
    """specify right vertex area metrics to do area correction based on"""
    
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
        cargs.append("-right-spheres")
        cargs.append(execution.input_file(self.current_sphere))
        cargs.append(execution.input_file(self.new_sphere))
        if self.right_area_surfs is not None:
            cargs.extend(self.right_area_surfs.run(execution))
        if self.right_area_metrics is not None:
            cargs.extend(self.right_area_metrics.run(execution))
        return cargs


@dataclasses.dataclass
class CiftiResampleCerebellumAreaSurfs:
    """
    specify cerebellum surfaces to do vertex area correction based on.
    """
    current_area: InputPathType
    """a relevant cerebellum anatomical surface with current mesh"""
    new_area: InputPathType
    """a relevant cerebellum anatomical surface with new mesh"""
    
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
        cargs.append("-cerebellum-area-surfs")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleCerebellumAreaMetrics:
    """
    specify cerebellum vertex area metrics to do area correction based on.
    """
    current_area: InputPathType
    """a metric file with vertex areas for the current mesh"""
    new_area: InputPathType
    """a metric file with vertex areas for the new mesh"""
    
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
        cargs.append("-cerebellum-area-metrics")
        cargs.append(execution.input_file(self.current_area))
        cargs.append(execution.input_file(self.new_area))
        return cargs


@dataclasses.dataclass
class CiftiResampleCerebellumSpheres:
    """
    specify spheres for cerebellum surface resampling.
    """
    current_sphere: InputPathType
    """a sphere with the same mesh as the current cerebellum surface"""
    new_sphere: InputPathType
    """a sphere with the new cerebellum mesh that is in register with the
    current sphere"""
    cerebellum_area_surfs: CiftiResampleCerebellumAreaSurfs | None = None
    """specify cerebellum surfaces to do vertex area correction based on"""
    cerebellum_area_metrics: CiftiResampleCerebellumAreaMetrics | None = None
    """specify cerebellum vertex area metrics to do area correction based on"""
    
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
        cargs.append("-cerebellum-spheres")
        cargs.append(execution.input_file(self.current_sphere))
        cargs.append(execution.input_file(self.new_sphere))
        if self.cerebellum_area_surfs is not None:
            cargs.extend(self.cerebellum_area_surfs.run(execution))
        if self.cerebellum_area_metrics is not None:
            cargs.extend(self.cerebellum_area_metrics.run(execution))
        return cargs


class CiftiResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_resample(
    cifti_in: InputPathType,
    direction: str,
    cifti_template: InputPathType,
    template_direction: str,
    surface_method: str,
    volume_method: str,
    cifti_out: str,
    opt_surface_largest: bool = False,
    volume_predilate: CiftiResampleVolumePredilate | None = None,
    surface_postdilate: CiftiResampleSurfacePostdilate | None = None,
    affine: CiftiResampleAffine | None = None,
    warpfield: CiftiResampleWarpfield | None = None,
    left_spheres: CiftiResampleLeftSpheres | None = None,
    right_spheres: CiftiResampleRightSpheres | None = None,
    cerebellum_spheres: CiftiResampleCerebellumSpheres | None = None,
    runner: Runner | None = None,
) -> CiftiResampleOutputs:
    """
    Resample a cifti file to a new cifti space.
    
    Resample cifti data to a different brainordinate space. Use COLUMN for the
    direction to resample dscalar, dlabel, or dtseries. Resampling both
    dimensions of a dconn requires running this command twice, once with COLUMN
    and once with ROW. If you are resampling a dconn and your machine has a
    large amount of memory, you might consider using
    -cifti-resample-dconn-memory to avoid writing and rereading an intermediate
    file. The <template-direction> argument should usually be COLUMN, as
    dtseries, dscalar, and dlabel all have brainordinates on that direction. If
    spheres are not specified for a surface structure which exists in the cifti
    files, its data is copied without resampling or dilation. Dilation is done
    with the 'nearest' method, and is done on <new-sphere> for surface data.
    Volume components are padded before dilation so that dilation doesn't run
    into the edge of the component bounding box. If neither -affine nor
    -warpfield are specified, the identity transform is assumed for the volume
    data.
    
    The recommended resampling methods are ADAP_BARY_AREA and CUBIC (cubic
    spline), except for label data which should use ADAP_BARY_AREA and
    ENCLOSING_VOXEL. Using ADAP_BARY_AREA requires specifying an area option to
    each used -*-spheres option.
    
    The <volume-method> argument must be one of the following:
    
    CUBIC
    ENCLOSING_VOXEL
    TRILINEAR
    
    The <surface-method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Author: Washington University School of Medicin
    
    Args:
        cifti_in: the cifti file to resample.
        direction: the direction of the input that should be resampled, ROW or\
            COLUMN.
        cifti_template: a cifti file containing the cifti space to resample to.
        template_direction: the direction of the template to use as the\
            resampling space, ROW or COLUMN.
        surface_method: specify a surface resampling method.
        volume_method: specify a volume interpolation method.
        cifti_out: the output cifti file.
        opt_surface_largest: use largest weight instead of weighted average or\
            popularity when doing surface resampling.
        volume_predilate: dilate the volume components before resampling.
        surface_postdilate: dilate the surface components after resampling.
        affine: use an affine transformation on the volume components.
        warpfield: use a warpfield on the volume components.
        left_spheres: specify spheres for left surface resampling.
        right_spheres: specify spheres for right surface resampling.
        cerebellum_spheres: specify spheres for cerebellum surface resampling.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-resample")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_template))
    cargs.append(template_direction)
    cargs.append(surface_method)
    cargs.append(volume_method)
    cargs.append(cifti_out)
    if opt_surface_largest:
        cargs.append("-surface-largest")
    if volume_predilate is not None:
        cargs.extend(volume_predilate.run(execution))
    if surface_postdilate is not None:
        cargs.extend(surface_postdilate.run(execution))
    if affine is not None:
        cargs.extend(affine.run(execution))
    if warpfield is not None:
        cargs.extend(warpfield.run(execution))
    if left_spheres is not None:
        cargs.extend(left_spheres.run(execution))
    if right_spheres is not None:
        cargs.extend(right_spheres.run(execution))
    if cerebellum_spheres is not None:
        cargs.extend(cerebellum_spheres.run(execution))
    ret = CiftiResampleOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_RESAMPLE_METADATA",
    "CiftiResampleAffine",
    "CiftiResampleCerebellumAreaMetrics",
    "CiftiResampleCerebellumAreaSurfs",
    "CiftiResampleCerebellumSpheres",
    "CiftiResampleFlirt",
    "CiftiResampleLeftAreaMetrics",
    "CiftiResampleLeftAreaSurfs",
    "CiftiResampleLeftSpheres",
    "CiftiResampleOutputs",
    "CiftiResampleRightAreaMetrics",
    "CiftiResampleRightAreaSurfs",
    "CiftiResampleRightSpheres",
    "CiftiResampleSurfacePostdilate",
    "CiftiResampleVolumePredilate",
    "CiftiResampleWarpfield",
    "CiftiResampleWeighted",
    "CiftiResampleWeighted_",
    "cifti_resample",
]

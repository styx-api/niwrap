# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_ATROPOS_N4_SH_METADATA = Metadata(
    id="26f6c01fef89c147f9f9fc215073f4d86231d70b.boutiques",
    name="antsAtroposN4.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


@dataclasses.dataclass
class AntsAtroposN4ShSegmentationPriors:
    """
    Prior probability images initializing the segmentation. Specified using
    c-style formatting, e.g. -p labelsPriors%02d.nii.gz. If this is not
    specified, k-means initialization is used instead.
    """
    segmentation_priors_pattern: str | None = None
    """Prior probability images initializing the segmentation. Specified using
    c-style formatting, e.g. -p labelsPriors%02d.nii.gz. If this is not
    specified, k-means initialization is used instead."""
    segmentation_priors_folder: InputPathType | None = None
    """Included so."""
    
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
        if self.segmentation_priors_pattern is not None or self.segmentation_priors_folder is not None:
            cargs.append((self.segmentation_priors_pattern if self.segmentation_priors_pattern is not None else "") + "/" + (execution.input_file(self.segmentation_priors_folder) if self.segmentation_priors_folder is not None else ""))
        return cargs


class AntsAtroposN4ShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_atropos_n4_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    n4_corrected: OutputPathType
    """N4 corrected image."""
    segmentation: OutputPathType
    """Segmentation image."""
    segmentation_posteriors: OutputPathType
    """Segmentation posteriors image."""


def ants_atropos_n4_sh(
    image_dimension: typing.Literal[2, 3],
    input_image: InputPathType,
    mask_image: InputPathType,
    number_of_classes: int,
    output_prefix: str,
    segmentation_priors: AntsAtroposN4ShSegmentationPriors,
    max_n4_atropos_iterations: int | None = None,
    max_atropos_iterations: int | None = None,
    mrf: str | None = None,
    denoise_anatomical_images: typing.Literal[0, 1] | None = None,
    posterior_formulation: typing.Literal["Socrates[ 1 ]", "Aristotle[ 1 ]"] | None = None,
    label_propagation: str | None = None,
    posterior_label_for_n4_weight_mask: str | None = None,
    image_file_suffix: str | None = None,
    keep_temporary_files: typing.Literal[0, 1] | None = None,
    use_random_seeding: typing.Literal[0, 1] | None = None,
    atropos_segmentation_prior_weight: float | None = None,
    n4_convergence: str | None = None,
    n4_shrink_factor: int | None = None,
    n4_bspline_params: str | None = None,
    atropos_segmentation_icm: str | None = None,
    atropos_segmentation_use_euclidean_distance: typing.Literal[0, 1] | None = None,
    test_debug_mode: int | None = None,
    runner: Runner | None = None,
) -> AntsAtroposN4ShOutputs:
    """
    antsAtroposN4.sh iterates between N4 <-> Atropos to improve segmentation
    results.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: 2 or 3, for 2- or 3-dimensional image.
        input_image: Anatomical image, typically T1. If more than one\
            anatomical image is specified, subsequent images are also used during\
            the segmentation process.
        mask_image: Binary mask defining the region of interest.
        number_of_classes: Number of classes defining the segmentation.
        output_prefix: The following images are created:\
            {output_prefix}N4Corrected.{output_suffix},\
            {output_prefix}Segmentation.{output_suffix},\
            {output_prefix}SegmentationPosteriors.{output_suffix}.
        segmentation_priors: Prior probability images initializing the\
            segmentation. Specified using c-style formatting, e.g. -p\
            labelsPriors%02d.nii.gz. If this is not specified, k-means\
            initialization is used instead.
        max_n4_atropos_iterations: Maximum number of (outer loop) iterations\
            between N4 <-> Atropos (default = 15).
        max_atropos_iterations: Maximum number of (inner loop) iterations in\
            Atropos (default = 3).
        mrf: Specifies MRF prior (of the form '[ weight,neighborhood ]', e.g.\
            '[ 0.1,1x1x1 ]' which is default).
        denoise_anatomical_images: Denoise anatomical images (1) or not (0)\
            (default = 1).
        posterior_formulation: Posterior formulation and whether or not to use\
            mixture model proportions. e.g 'Socrates[ 1 ]' (default) or 'Aristotle[\
            1 ]'. Choose the latter if you want to use the distance priors, see\
            also the -l option for label propagation control (default = 'Socrates[\
            1 ]').
        label_propagation: Incorporate a distance prior into the 'Aristotle'\
            posterior formulation. Should be of the form 'label[\
            lambda,boundaryProbability ]' where label is a value of 1,2,3,...\
            denoting label ID. The label probability for anything outside the\
            current label\
            \
            = boundaryProbability * exp( -lambda * distanceFromBoundary )\
            \
            Intuitively, smaller lambda values will increase the spatial\
            capture range of the distance prior. To apply to all label values,\
            simply omit specifying the label, i.e. -l '[\
            lambda,boundaryProbability ]'.
        posterior_label_for_n4_weight_mask: Which posterior probability image\
            should be used to define the N4 weight mask. Can also specify multiple\
            posteriors in which case the chosen posteriors are combined.
        image_file_suffix: Any of the standard ITK IO formats e.g. nrrd, nii.gz\
            (default), mhd.
        keep_temporary_files: Keep temporary files on disk (1) or delete them\
            (0) (default = 0).
        use_random_seeding: Use random number generated from system clock in\
            Atropos (default = 1).
        atropos_segmentation_prior_weight: Atropos spatial prior probability\
            weight for the segmentation (default = 0.25).
        n4_convergence: Convergence parameters for N4, see '-c' option in\
            N4BiasFieldCorrection (default = [50x50x50x50,0.0000001]).
        n4_shrink_factor: Shrink factor for N4 (default = 4).
        n4_bspline_params: N4 b-spline specification, see '-b' option in\
            N4BiasFieldCorrection (default = [200,0,0,0]).
        atropos_segmentation_icm: ICM parameters for segmentation, see '-g'\
            option in Atropos (default = [1,1]).
        atropos_segmentation_use_euclidean_distance: Use euclidean distances in\
            distance prior formulation (1) or not (0), see Atropos usage for\
            details (default = 1).
        test_debug_mode: If > 0, attempts to continue after errors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsAtroposN4ShOutputs`).
    """
    if max_n4_atropos_iterations is not None and not (1 <= max_n4_atropos_iterations): 
        raise ValueError(f"'max_n4_atropos_iterations' must be greater than 1 <= x but was {max_n4_atropos_iterations}")
    if max_atropos_iterations is not None and not (1 <= max_atropos_iterations): 
        raise ValueError(f"'max_atropos_iterations' must be greater than 1 <= x but was {max_atropos_iterations}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_ATROPOS_N4_SH_METADATA)
    cargs = []
    cargs.append("antsAtroposN4.sh")
    cargs.extend([
        "-d",
        str(image_dimension)
    ])
    cargs.extend([
        "-a",
        execution.input_file(input_image)
    ])
    cargs.extend([
        "-x",
        execution.input_file(mask_image)
    ])
    cargs.extend([
        "-c",
        str(number_of_classes)
    ])
    cargs.extend([
        "-o",
        output_prefix
    ])
    if max_n4_atropos_iterations is not None:
        cargs.extend([
            "-m",
            str(max_n4_atropos_iterations)
        ])
    if max_atropos_iterations is not None:
        cargs.extend([
            "-n",
            str(max_atropos_iterations)
        ])
    cargs.extend([
        "-p",
        *segmentation_priors.run(execution)
    ])
    if mrf is not None:
        cargs.extend([
            "-r",
            mrf
        ])
    if denoise_anatomical_images is not None:
        cargs.extend([
            "-g",
            str(denoise_anatomical_images)
        ])
    if posterior_formulation is not None:
        cargs.extend([
            "-b",
            posterior_formulation
        ])
    if label_propagation is not None:
        cargs.extend([
            "-l",
            label_propagation
        ])
    if posterior_label_for_n4_weight_mask is not None:
        cargs.extend([
            "-y",
            posterior_label_for_n4_weight_mask
        ])
    if image_file_suffix is not None:
        cargs.extend([
            "-s",
            image_file_suffix
        ])
    if keep_temporary_files is not None:
        cargs.extend([
            "-k",
            str(keep_temporary_files)
        ])
    if use_random_seeding is not None:
        cargs.extend([
            "-u",
            str(use_random_seeding)
        ])
    if atropos_segmentation_prior_weight is not None:
        cargs.extend([
            "-w",
            str(atropos_segmentation_prior_weight)
        ])
    if n4_convergence is not None:
        cargs.extend([
            "-e",
            n4_convergence
        ])
    if n4_shrink_factor is not None:
        cargs.extend([
            "-f",
            str(n4_shrink_factor)
        ])
    if n4_bspline_params is not None:
        cargs.extend([
            "-q",
            n4_bspline_params
        ])
    if atropos_segmentation_icm is not None:
        cargs.extend([
            "-i",
            atropos_segmentation_icm
        ])
    if atropos_segmentation_use_euclidean_distance is not None:
        cargs.extend([
            "-j",
            str(atropos_segmentation_use_euclidean_distance)
        ])
    if test_debug_mode is not None:
        cargs.extend([
            "-z",
            str(test_debug_mode)
        ])
    ret = AntsAtroposN4ShOutputs(
        root=execution.output_file("."),
        n4_corrected=execution.output_file(output_prefix + "N4Corrected.[OUTPUT_SUFFIX]"),
        segmentation=execution.output_file(output_prefix + "Segmentation.[OUTPUT_SUFFIX]"),
        segmentation_posteriors=execution.output_file(output_prefix + "SegmentationPosteriors.[OUTPUT_SUFFIX]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_ATROPOS_N4_SH_METADATA",
    "AntsAtroposN4ShOutputs",
    "AntsAtroposN4ShSegmentationPriors",
    "ants_atropos_n4_sh",
]

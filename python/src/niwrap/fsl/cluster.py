# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CLUSTER_METADATA = Metadata(
    id="f9c277296bff6829746b7b450932118c7250ea4d.boutiques",
    name="cluster",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class ClusterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cluster(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    index_file: OutputPathType
    """Output of cluster index (in size order)."""
    localmax_txt_file: OutputPathType
    """Local maxima text file."""
    localmax_vol_file: OutputPathType
    """Output of local maxima volume."""
    max_file: OutputPathType
    """Filename for output of max image."""
    mean_file: OutputPathType
    """Filename for output of mean image."""
    pval_file: OutputPathType
    """Filename for image output of log pvals."""
    size_file: OutputPathType
    """Filename for output of size image."""
    threshold_file: OutputPathType
    """Thresholded image."""


def cluster(
    in_file: InputPathType,
    threshold: float,
    connectivity: int | None = None,
    cope_file: InputPathType | None = None,
    dlh: float | None = None,
    find_min: bool = False,
    fractional: bool = False,
    minclustersize: bool = False,
    no_table: bool = False,
    num_maxima: int | None = None,
    out_index_file_2: InputPathType | None = None,
    out_localmax_txt_file_2: InputPathType | None = None,
    out_localmax_vol_file_2: InputPathType | None = None,
    out_max_file_2: InputPathType | None = None,
    out_mean_file_2: InputPathType | None = None,
    out_pval_file_2: InputPathType | None = None,
    out_size_file_2: InputPathType | None = None,
    out_threshold_file_2: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    peak_distance: float | None = None,
    pthreshold: float | None = None,
    std_space_file: InputPathType | None = None,
    use_mm: bool = False,
    volume: int | None = None,
    warpfield_file: InputPathType | None = None,
    xfm_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> ClusterOutputs:
    """
    Uses FSL cluster to perform clustering on statistical output.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input volume.
        threshold: Threshold for input volume.
        connectivity: The connectivity of voxels (default 26).
        cope_file: Cope volume.
        dlh: Smoothness estimate = sqrt(det(lambda)).
        find_min: Find minima instead of maxima.
        fractional: Interprets the threshold as a fraction of the robust range.
        minclustersize: Prints out minimum significant cluster size.
        no_table: Suppresses printing of the table info.
        num_maxima: No of local maxima to report.
        out_index_file_2: A boolean or file. Output of cluster index (in size\
            order).
        out_localmax_txt_file_2: A boolean or file. Local maxima text file.
        out_localmax_vol_file_2: A boolean or file. Output of local maxima\
            volume.
        out_max_file_2: A boolean or file. Filename for output of max image.
        out_mean_file_2: A boolean or file. Filename for output of mean image.
        out_pval_file_2: A boolean or file. Filename for image output of log\
            pvals.
        out_size_file_2: A boolean or file. Filename for output of size image.
        out_threshold_file_2: A boolean or file. Thresholded image.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        peak_distance: Minimum distance between local maxima/minima, in mm\
            (default 0).
        pthreshold: P-threshold for clusters.
        std_space_file: Filename for standard-space volume.
        use_mm: Use mm, not voxel, coordinates.
        volume: Number of voxels in the mask.
        warpfield_file: File containing warpfield.
        xfm_file: Filename for linear: input->standard-space transform.\
            non-linear: input->highres transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ClusterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CLUSTER_METADATA)
    cargs = []
    cargs.append("cluster")
    if connectivity is not None:
        cargs.append("--connectivity=" + str(connectivity))
    if cope_file is not None:
        cargs.append("--cope=" + execution.input_file(cope_file))
    if dlh is not None:
        cargs.append("--dlh=" + str(dlh))
    if find_min:
        cargs.append("--min")
    if fractional:
        cargs.append("--fractional")
    cargs.append("--in=" + execution.input_file(in_file))
    if minclustersize:
        cargs.append("--minclustersize")
    if no_table:
        cargs.append("--no_table")
    if num_maxima is not None:
        cargs.append("--num=" + str(num_maxima))
    if out_index_file_2 is not None:
        cargs.append("--oindex=" + execution.input_file(out_index_file_2))
    if out_localmax_txt_file_2 is not None:
        cargs.append("--olmax=" + execution.input_file(out_localmax_txt_file_2))
    if out_localmax_vol_file_2 is not None:
        cargs.append("--olmaxim=" + execution.input_file(out_localmax_vol_file_2))
    if out_max_file_2 is not None:
        cargs.append("--omax=" + execution.input_file(out_max_file_2))
    if out_mean_file_2 is not None:
        cargs.append("--omean=" + execution.input_file(out_mean_file_2))
    if out_pval_file_2 is not None:
        cargs.append("--opvals=" + execution.input_file(out_pval_file_2))
    if out_size_file_2 is not None:
        cargs.append("--osize=" + execution.input_file(out_size_file_2))
    if out_threshold_file_2 is not None:
        cargs.append("--othresh=" + execution.input_file(out_threshold_file_2))
    if output_type is not None:
        cargs.append(output_type)
    if peak_distance is not None:
        cargs.append("--peakdist=" + str(peak_distance))
    if pthreshold is not None:
        cargs.append("--pthresh=" + str(pthreshold))
    if std_space_file is not None:
        cargs.append("--stdvol=" + execution.input_file(std_space_file))
    cargs.append("--thresh=" + str(threshold))
    if use_mm:
        cargs.append("--mm")
    if volume is not None:
        cargs.append("--volume=" + str(volume))
    if warpfield_file is not None:
        cargs.append("--warpvol=" + execution.input_file(warpfield_file))
    if xfm_file is not None:
        cargs.append("--xfm=" + execution.input_file(xfm_file))
    ret = ClusterOutputs(
        root=execution.output_file("."),
        index_file=execution.output_file("index_file"),
        localmax_txt_file=execution.output_file("localmax_txt_file"),
        localmax_vol_file=execution.output_file("localmax_vol_file"),
        max_file=execution.output_file("max_file"),
        mean_file=execution.output_file("mean_file"),
        pval_file=execution.output_file("pval_file"),
        size_file=execution.output_file("size_file"),
        threshold_file=execution.output_file("threshold_file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CLUSTER_METADATA",
    "ClusterOutputs",
    "cluster",
]

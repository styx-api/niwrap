# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_ENTOWM_SEG_METADATA = Metadata(
    id="40109605e55188f3737d75a9e36af58709374335.boutiques",
    name="mri_entowm_seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriEntowmSegParameters = typing.TypedDict('MriEntowmSegParameters', {
    "__STYX_TYPE__": typing.Literal["mri_entowm_seg"],
    "input_image": typing.NotRequired[InputPathType | None],
    "output_segmentation": typing.NotRequired[str | None],
    "recon_subjects": typing.NotRequired[list[str] | None],
    "subjects_directory": typing.NotRequired[str | None],
    "conform": bool,
    "etiv": bool,
    "tal": typing.NotRequired[str | None],
    "write_posteriors": bool,
    "write_volumes": bool,
    "write_qa_stats": bool,
    "exclude_labels": typing.NotRequired[list[str] | None],
    "keep_ac": bool,
    "vox_count_volumes": bool,
    "model_weights": typing.NotRequired[str | None],
    "color_table": typing.NotRequired[str | None],
    "population_stats": typing.NotRequired[str | None],
    "debug": bool,
    "vmp": bool,
    "threads": typing.NotRequired[float | None],
    "seven_tesla": bool,
    "percentile": typing.NotRequired[float | None],
    "cuda_device": typing.NotRequired[str | None],
    "output_base": typing.NotRequired[str | None],
    "no_cite_sclimbic": bool,
    "nchannels": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_entowm_seg": mri_entowm_seg_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_entowm_seg": mri_entowm_seg_outputs,
    }.get(t)


class MriEntowmSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_entowm_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Segmentation output file"""
    label_posteriors: OutputPathType | None
    """Label posterior probabilities"""
    volume_stats: OutputPathType | None
    """Volume statistics"""
    qa_stats: OutputPathType | None
    """Quality assurance statistics"""


def mri_entowm_seg_params(
    input_image: InputPathType | None = None,
    output_segmentation: str | None = None,
    recon_subjects: list[str] | None = None,
    subjects_directory: str | None = None,
    conform: bool = False,
    etiv: bool = False,
    tal: str | None = None,
    write_posteriors: bool = False,
    write_volumes: bool = False,
    write_qa_stats: bool = False,
    exclude_labels: list[str] | None = None,
    keep_ac: bool = False,
    vox_count_volumes: bool = False,
    model_weights: str | None = None,
    color_table: str | None = None,
    population_stats: str | None = None,
    debug: bool = False,
    vmp: bool = False,
    threads: float | None = None,
    seven_tesla: bool = False,
    percentile: float | None = None,
    cuda_device: str | None = None,
    output_base: str | None = None,
    no_cite_sclimbic: bool = False,
    nchannels: float | None = None,
) -> MriEntowmSegParameters:
    """
    Build parameters.
    
    Args:
        input_image: T1-weighted image(s) to segment. Can be a path to a single\
            image or a directory of images.
        output_segmentation: Segmentation output file or directory (required if\
            --i is provided).
        recon_subjects: Process a series of FreeSurfer recon-all subjects,\
            enables subject-mode.
        subjects_directory: Set the subjects directory, overrides the\
            SUBJECTS_DIR env variable.
        conform: Resample input to 1mm-iso; results will be put back in native\
            resolution.
        etiv: Include eTIV in volume stats (enabled by default in subject-mode\
            and with --tal).
        tal: Alternative talairach xfm transform for estimating TIV, can be\
            file or suffix (for multiple inputs).
        write_posteriors: Save the label posteriors.
        write_volumes: Save label volume stats (enabled by default in\
            subject-mode).
        write_qa_stats: Save QA stats (z and confidence).
        exclude_labels: List of label IDs to exclude in any output stats files.
        keep_ac: Explicitly keep anterior commissure in the volume/QA files.
        vox_count_volumes: Use discrete voxel count for label volumes.
        model_weights: Alternative model weights to load.
        color_table: Alternative color lookup table to embed in segmentation.\
            Must be minimal, including 0, and sorted.
        population_stats: Alternative population volume stats for QA output.
        debug: Enable debug logging.
        vmp: Enable printing of vmpeak at the end.
        threads: Number of threads to use. Default is 1.
        seven_tesla: Preprocess 7T images (just sets percentile to 99.9).
        percentile: Use intensity percentile threshold for normalization.
        cuda_device: CUDA device for GPU support.
        output_base: String to use in output file name; default is sclimbic.
        no_cite_sclimbic: Do not cite sclimbic paper at the end.
        nchannels: Number of channels.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_entowm_seg",
        "conform": conform,
        "etiv": etiv,
        "write_posteriors": write_posteriors,
        "write_volumes": write_volumes,
        "write_qa_stats": write_qa_stats,
        "keep_ac": keep_ac,
        "vox_count_volumes": vox_count_volumes,
        "debug": debug,
        "vmp": vmp,
        "seven_tesla": seven_tesla,
        "no_cite_sclimbic": no_cite_sclimbic,
    }
    if input_image is not None:
        params["input_image"] = input_image
    if output_segmentation is not None:
        params["output_segmentation"] = output_segmentation
    if recon_subjects is not None:
        params["recon_subjects"] = recon_subjects
    if subjects_directory is not None:
        params["subjects_directory"] = subjects_directory
    if tal is not None:
        params["tal"] = tal
    if exclude_labels is not None:
        params["exclude_labels"] = exclude_labels
    if model_weights is not None:
        params["model_weights"] = model_weights
    if color_table is not None:
        params["color_table"] = color_table
    if population_stats is not None:
        params["population_stats"] = population_stats
    if threads is not None:
        params["threads"] = threads
    if percentile is not None:
        params["percentile"] = percentile
    if cuda_device is not None:
        params["cuda_device"] = cuda_device
    if output_base is not None:
        params["output_base"] = output_base
    if nchannels is not None:
        params["nchannels"] = nchannels
    return params


def mri_entowm_seg_cargs(
    params: MriEntowmSegParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_entowm_seg")
    if params.get("input_image") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("input_image"))
        ])
    if params.get("output_segmentation") is not None:
        cargs.extend([
            "-o",
            params.get("output_segmentation")
        ])
    if params.get("recon_subjects") is not None:
        cargs.extend([
            "-s",
            *params.get("recon_subjects")
        ])
    if params.get("subjects_directory") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_directory")
        ])
    if params.get("conform"):
        cargs.append("--conform")
    if params.get("etiv"):
        cargs.append("--etiv")
    if params.get("tal") is not None:
        cargs.extend([
            "--tal",
            params.get("tal")
        ])
    if params.get("write_posteriors"):
        cargs.append("--write_posteriors")
    if params.get("write_volumes"):
        cargs.append("--write_volumes")
    if params.get("write_qa_stats"):
        cargs.append("--write_qa_stats")
    if params.get("exclude_labels") is not None:
        cargs.extend([
            "--exclude",
            *params.get("exclude_labels")
        ])
    if params.get("keep_ac"):
        cargs.append("--keep_ac")
    if params.get("vox_count_volumes"):
        cargs.append("--vox-count-volumes")
    if params.get("model_weights") is not None:
        cargs.extend([
            "--model",
            params.get("model_weights")
        ])
    if params.get("color_table") is not None:
        cargs.extend([
            "--ctab",
            params.get("color_table")
        ])
    if params.get("population_stats") is not None:
        cargs.extend([
            "--population-stats",
            params.get("population_stats")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("vmp"):
        cargs.append("--vmp")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("seven_tesla"):
        cargs.append("--7T")
    if params.get("percentile") is not None:
        cargs.extend([
            "--percentile",
            str(params.get("percentile"))
        ])
    if params.get("cuda_device") is not None:
        cargs.extend([
            "--cuda-device",
            params.get("cuda_device")
        ])
    if params.get("output_base") is not None:
        cargs.extend([
            "--output-base",
            params.get("output_base")
        ])
    if params.get("no_cite_sclimbic"):
        cargs.append("--no-cite-sclimbic")
    if params.get("nchannels") is not None:
        cargs.extend([
            "--nchannels",
            str(params.get("nchannels"))
        ])
    return cargs


def mri_entowm_seg_outputs(
    params: MriEntowmSegParameters,
    execution: Execution,
) -> MriEntowmSegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriEntowmSegOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_segmentation")) if (params.get("output_segmentation") is not None) else None,
        label_posteriors=execution.output_file(params.get("output_base") + "_posterior.mgz") if (params.get("output_base") is not None) else None,
        volume_stats=execution.output_file(params.get("output_base") + "_volumes.txt") if (params.get("output_base") is not None) else None,
        qa_stats=execution.output_file(params.get("output_base") + "_qa_stats.txt") if (params.get("output_base") is not None) else None,
    )
    return ret


def mri_entowm_seg_execute(
    params: MriEntowmSegParameters,
    execution: Execution,
) -> MriEntowmSegOutputs:
    """
    Segment white matter near gyrus ambiens entorhinal cortex using a deep learning
    model.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriEntowmSegOutputs`).
    """
    params = execution.params(params)
    cargs = mri_entowm_seg_cargs(params, execution)
    ret = mri_entowm_seg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_entowm_seg(
    input_image: InputPathType | None = None,
    output_segmentation: str | None = None,
    recon_subjects: list[str] | None = None,
    subjects_directory: str | None = None,
    conform: bool = False,
    etiv: bool = False,
    tal: str | None = None,
    write_posteriors: bool = False,
    write_volumes: bool = False,
    write_qa_stats: bool = False,
    exclude_labels: list[str] | None = None,
    keep_ac: bool = False,
    vox_count_volumes: bool = False,
    model_weights: str | None = None,
    color_table: str | None = None,
    population_stats: str | None = None,
    debug: bool = False,
    vmp: bool = False,
    threads: float | None = None,
    seven_tesla: bool = False,
    percentile: float | None = None,
    cuda_device: str | None = None,
    output_base: str | None = None,
    no_cite_sclimbic: bool = False,
    nchannels: float | None = None,
    runner: Runner | None = None,
) -> MriEntowmSegOutputs:
    """
    Segment white matter near gyrus ambiens entorhinal cortex using a deep learning
    model.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: T1-weighted image(s) to segment. Can be a path to a single\
            image or a directory of images.
        output_segmentation: Segmentation output file or directory (required if\
            --i is provided).
        recon_subjects: Process a series of FreeSurfer recon-all subjects,\
            enables subject-mode.
        subjects_directory: Set the subjects directory, overrides the\
            SUBJECTS_DIR env variable.
        conform: Resample input to 1mm-iso; results will be put back in native\
            resolution.
        etiv: Include eTIV in volume stats (enabled by default in subject-mode\
            and with --tal).
        tal: Alternative talairach xfm transform for estimating TIV, can be\
            file or suffix (for multiple inputs).
        write_posteriors: Save the label posteriors.
        write_volumes: Save label volume stats (enabled by default in\
            subject-mode).
        write_qa_stats: Save QA stats (z and confidence).
        exclude_labels: List of label IDs to exclude in any output stats files.
        keep_ac: Explicitly keep anterior commissure in the volume/QA files.
        vox_count_volumes: Use discrete voxel count for label volumes.
        model_weights: Alternative model weights to load.
        color_table: Alternative color lookup table to embed in segmentation.\
            Must be minimal, including 0, and sorted.
        population_stats: Alternative population volume stats for QA output.
        debug: Enable debug logging.
        vmp: Enable printing of vmpeak at the end.
        threads: Number of threads to use. Default is 1.
        seven_tesla: Preprocess 7T images (just sets percentile to 99.9).
        percentile: Use intensity percentile threshold for normalization.
        cuda_device: CUDA device for GPU support.
        output_base: String to use in output file name; default is sclimbic.
        no_cite_sclimbic: Do not cite sclimbic paper at the end.
        nchannels: Number of channels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEntowmSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ENTOWM_SEG_METADATA)
    params = mri_entowm_seg_params(
        input_image=input_image,
        output_segmentation=output_segmentation,
        recon_subjects=recon_subjects,
        subjects_directory=subjects_directory,
        conform=conform,
        etiv=etiv,
        tal=tal,
        write_posteriors=write_posteriors,
        write_volumes=write_volumes,
        write_qa_stats=write_qa_stats,
        exclude_labels=exclude_labels,
        keep_ac=keep_ac,
        vox_count_volumes=vox_count_volumes,
        model_weights=model_weights,
        color_table=color_table,
        population_stats=population_stats,
        debug=debug,
        vmp=vmp,
        threads=threads,
        seven_tesla=seven_tesla,
        percentile=percentile,
        cuda_device=cuda_device,
        output_base=output_base,
        no_cite_sclimbic=no_cite_sclimbic,
        nchannels=nchannels,
    )
    return mri_entowm_seg_execute(params, execution)


__all__ = [
    "MRI_ENTOWM_SEG_METADATA",
    "MriEntowmSegOutputs",
    "MriEntowmSegParameters",
    "mri_entowm_seg",
    "mri_entowm_seg_params",
]

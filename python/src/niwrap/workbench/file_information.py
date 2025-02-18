# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FILE_INFORMATION_METADATA = Metadata(
    id="12389474c2f36cd256667daa74a103d07ac49064.boutiques",
    name="file-information",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
FileInformationOnlyMetadataParameters = typing.TypedDict('FileInformationOnlyMetadataParameters', {
    "__STYX_TYPE__": typing.Literal["only_metadata"],
    "opt_key_key": typing.NotRequired[str | None],
})
FileInformationParameters = typing.TypedDict('FileInformationParameters', {
    "__STYX_TYPE__": typing.Literal["file-information"],
    "data_file": str,
    "opt_no_map_info": bool,
    "opt_only_step_interval": bool,
    "opt_only_number_of_maps": bool,
    "opt_only_map_names": bool,
    "only_metadata": typing.NotRequired[FileInformationOnlyMetadataParameters | None],
    "opt_only_cifti_xml": bool,
    "opt_czi": bool,
    "opt_czi_all_sub_blocks": bool,
    "opt_czi_xml": bool,
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
        "file-information": file_information_cargs,
        "only_metadata": file_information_only_metadata_cargs,
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
    }.get(t)


def file_information_only_metadata_params(
    opt_key_key: str | None = None,
) -> FileInformationOnlyMetadataParameters:
    """
    Build parameters.
    
    Args:
        opt_key_key: only print the metadata for one key, with no formatting:\
            the metadata key.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "only_metadata",
    }
    if opt_key_key is not None:
        params["opt_key_key"] = opt_key_key
    return params


def file_information_only_metadata_cargs(
    params: FileInformationOnlyMetadataParameters,
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
    cargs.append("-only-metadata")
    if params.get("opt_key_key") is not None:
        cargs.extend([
            "-key",
            params.get("opt_key_key")
        ])
    return cargs


class FileInformationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `file_information(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def file_information_params(
    data_file: str,
    opt_no_map_info: bool = False,
    opt_only_step_interval: bool = False,
    opt_only_number_of_maps: bool = False,
    opt_only_map_names: bool = False,
    only_metadata: FileInformationOnlyMetadataParameters | None = None,
    opt_only_cifti_xml: bool = False,
    opt_czi: bool = False,
    opt_czi_all_sub_blocks: bool = False,
    opt_czi_xml: bool = False,
) -> FileInformationParameters:
    """
    Build parameters.
    
    Args:
        data_file: data file.
        opt_no_map_info: do not show map information for files that support\
            maps.
        opt_only_step_interval: suppress normal output, print the interval\
            between maps.
        opt_only_number_of_maps: suppress normal output, print the number of\
            maps.
        opt_only_map_names: suppress normal output, print the names of all maps.
        only_metadata: suppress normal output, print file metadata.
        opt_only_cifti_xml: suppress normal output, print the cifti xml if the\
            file type has it.
        opt_czi: For a CZI file, show information from the libCZI Info Command\
            instead of the Workbench CZI File.
        opt_czi_all_sub_blocks: show all sub-blocks in CZI file (may produce\
            long output).
        opt_czi_xml: show XML from CZI file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "file-information",
        "data_file": data_file,
        "opt_no_map_info": opt_no_map_info,
        "opt_only_step_interval": opt_only_step_interval,
        "opt_only_number_of_maps": opt_only_number_of_maps,
        "opt_only_map_names": opt_only_map_names,
        "opt_only_cifti_xml": opt_only_cifti_xml,
        "opt_czi": opt_czi,
        "opt_czi_all_sub_blocks": opt_czi_all_sub_blocks,
        "opt_czi_xml": opt_czi_xml,
    }
    if only_metadata is not None:
        params["only_metadata"] = only_metadata
    return params


def file_information_cargs(
    params: FileInformationParameters,
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
    cargs.append("wb_command")
    cargs.append("-file-information")
    cargs.append(params.get("data_file"))
    if params.get("opt_no_map_info"):
        cargs.append("-no-map-info")
    if params.get("opt_only_step_interval"):
        cargs.append("-only-step-interval")
    if params.get("opt_only_number_of_maps"):
        cargs.append("-only-number-of-maps")
    if params.get("opt_only_map_names"):
        cargs.append("-only-map-names")
    if params.get("only_metadata") is not None:
        cargs.extend(dyn_cargs(params.get("only_metadata")["__STYXTYPE__"])(params.get("only_metadata"), execution))
    if params.get("opt_only_cifti_xml"):
        cargs.append("-only-cifti-xml")
    if params.get("opt_czi"):
        cargs.append("-czi")
    if params.get("opt_czi_all_sub_blocks"):
        cargs.append("-czi-all-sub-blocks")
    if params.get("opt_czi_xml"):
        cargs.append("-czi-xml")
    return cargs


def file_information_outputs(
    params: FileInformationParameters,
    execution: Execution,
) -> FileInformationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FileInformationOutputs(
        root=execution.output_file("."),
    )
    return ret


def file_information_execute(
    params: FileInformationParameters,
    execution: Execution,
) -> FileInformationOutputs:
    """
    List information about a file's content.
    
    List information about the content of a data file. Only one -only option may
    be specified. The information listed when no -only option is present is
    dependent upon the type of data file.
    
    Library paths:
    /usr/lib/x86_64-linux-gnu/qt5/plugins
    
    /mnt/c/Users/floru/Projects/cmi/nopype/extraction/workbench/source/build/CommandLine
    
    
    File and extensions for reading and writing:
    Annotation: wb_annot
    Annotation Text Substitution: wb_annsub.csv
    Border: border, wb_border
    CIFTI - Dense: dconn.nii
    CIFTI - Dense Label: dlabel.nii
    CIFTI - Dense Parcel: dpconn.nii
    CIFTI - Dense Scalar: dscalar.nii
    CIFTI - Dense Data Series: dtseries.nii
    CIFTI - Fiber Orientations TEMPORARY: fiberTEMP.nii
    CIFTI - Fiber Trajectory TEMPORARY: trajTEMP.wbsparse
    CIFTI - Parcel: pconn.nii
    CIFTI - Parcel Dense: pdconn.nii
    CIFTI - Parcel Label: plabel.nii
    CIFTI - Parcel Scalar: pscalar.nii
    CIFTI - Parcel Series: ptseries.nii
    CIFTI - Scalar Data Series: sdseries.nii
    CZI Image: czi
    Foci: foci, wb_foci
    Histology Slices: metaczi, meta-image
    Image Read: bmp, gif, jpeg, jpg, png, ppm
    Write: bmp, jpeg, jpg, png, ppm
    Label: label.gii
    Metric: func.gii, shape.gii
    Palette: palette, wb_palette
    RGBA: rgba.gii
    Samples: wb_samples
    Scene: scene, wb_scene
    Specification: spec, wb_spec
    Surface: surf.gii
    Volume: nii, nii.gz
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FileInformationOutputs`).
    """
    cargs = file_information_cargs(params, execution)
    ret = file_information_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def file_information(
    data_file: str,
    opt_no_map_info: bool = False,
    opt_only_step_interval: bool = False,
    opt_only_number_of_maps: bool = False,
    opt_only_map_names: bool = False,
    only_metadata: FileInformationOnlyMetadataParameters | None = None,
    opt_only_cifti_xml: bool = False,
    opt_czi: bool = False,
    opt_czi_all_sub_blocks: bool = False,
    opt_czi_xml: bool = False,
    runner: Runner | None = None,
) -> FileInformationOutputs:
    """
    List information about a file's content.
    
    List information about the content of a data file. Only one -only option may
    be specified. The information listed when no -only option is present is
    dependent upon the type of data file.
    
    Library paths:
    /usr/lib/x86_64-linux-gnu/qt5/plugins
    
    /mnt/c/Users/floru/Projects/cmi/nopype/extraction/workbench/source/build/CommandLine
    
    
    File and extensions for reading and writing:
    Annotation: wb_annot
    Annotation Text Substitution: wb_annsub.csv
    Border: border, wb_border
    CIFTI - Dense: dconn.nii
    CIFTI - Dense Label: dlabel.nii
    CIFTI - Dense Parcel: dpconn.nii
    CIFTI - Dense Scalar: dscalar.nii
    CIFTI - Dense Data Series: dtseries.nii
    CIFTI - Fiber Orientations TEMPORARY: fiberTEMP.nii
    CIFTI - Fiber Trajectory TEMPORARY: trajTEMP.wbsparse
    CIFTI - Parcel: pconn.nii
    CIFTI - Parcel Dense: pdconn.nii
    CIFTI - Parcel Label: plabel.nii
    CIFTI - Parcel Scalar: pscalar.nii
    CIFTI - Parcel Series: ptseries.nii
    CIFTI - Scalar Data Series: sdseries.nii
    CZI Image: czi
    Foci: foci, wb_foci
    Histology Slices: metaczi, meta-image
    Image Read: bmp, gif, jpeg, jpg, png, ppm
    Write: bmp, jpeg, jpg, png, ppm
    Label: label.gii
    Metric: func.gii, shape.gii
    Palette: palette, wb_palette
    RGBA: rgba.gii
    Samples: wb_samples
    Scene: scene, wb_scene
    Specification: spec, wb_spec
    Surface: surf.gii
    Volume: nii, nii.gz
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        data_file: data file.
        opt_no_map_info: do not show map information for files that support\
            maps.
        opt_only_step_interval: suppress normal output, print the interval\
            between maps.
        opt_only_number_of_maps: suppress normal output, print the number of\
            maps.
        opt_only_map_names: suppress normal output, print the names of all maps.
        only_metadata: suppress normal output, print file metadata.
        opt_only_cifti_xml: suppress normal output, print the cifti xml if the\
            file type has it.
        opt_czi: For a CZI file, show information from the libCZI Info Command\
            instead of the Workbench CZI File.
        opt_czi_all_sub_blocks: show all sub-blocks in CZI file (may produce\
            long output).
        opt_czi_xml: show XML from CZI file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FileInformationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILE_INFORMATION_METADATA)
    params = file_information_params(data_file=data_file, opt_no_map_info=opt_no_map_info, opt_only_step_interval=opt_only_step_interval, opt_only_number_of_maps=opt_only_number_of_maps, opt_only_map_names=opt_only_map_names, only_metadata=only_metadata, opt_only_cifti_xml=opt_only_cifti_xml, opt_czi=opt_czi, opt_czi_all_sub_blocks=opt_czi_all_sub_blocks, opt_czi_xml=opt_czi_xml)
    return file_information_execute(params, execution)


__all__ = [
    "FILE_INFORMATION_METADATA",
    "FileInformationOnlyMetadataParameters",
    "FileInformationOutputs",
    "FileInformationParameters",
    "file_information",
    "file_information_only_metadata_params",
    "file_information_params",
]

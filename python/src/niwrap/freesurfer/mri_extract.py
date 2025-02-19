# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EXTRACT_METADATA = Metadata(
    id="8ea8492114a69493e6fb6d2e1d9f2b2b63d51237.boutiques",
    name="mri_extract",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriExtractParameters = typing.TypedDict('MriExtractParameters', {
    "__STYX_TYPE__": typing.Literal["mri_extract"],
    "like_template": typing.NotRequired[InputPathType | None],
    "src_volume": InputPathType,
    "dst_volume": InputPathType,
    "coordinates": typing.NotRequired[list[float] | None],
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
        "mri_extract": mri_extract_cargs,
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
        "mri_extract": mri_extract_outputs,
    }.get(t)


class MriExtractOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_extract(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_extracted_volume: OutputPathType
    """Output file with extracted MRI data."""


def mri_extract_params(
    src_volume: InputPathType,
    dst_volume: InputPathType,
    like_template: InputPathType | None = None,
    coordinates: list[float] | None = None,
) -> MriExtractParameters:
    """
    Build parameters.
    
    Args:
        src_volume: Source MRI volume file from which data will be extracted.
        dst_volume: The destination file where the extracted data will be\
            saved.
        like_template: Extract region like the given template volume.
        coordinates: Coordinates and size of the extraction box: x0 y0 z0 dx dy\
            dz.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_extract",
        "src_volume": src_volume,
        "dst_volume": dst_volume,
    }
    if like_template is not None:
        params["like_template"] = like_template
    if coordinates is not None:
        params["coordinates"] = coordinates
    return params


def mri_extract_cargs(
    params: MriExtractParameters,
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
    cargs.append("mri_extract")
    if params.get("like_template") is not None:
        cargs.extend([
            "-like",
            execution.input_file(params.get("like_template"))
        ])
    cargs.append(execution.input_file(params.get("src_volume")))
    cargs.append(execution.input_file(params.get("dst_volume")))
    if params.get("coordinates") is not None:
        cargs.extend(map(str, params.get("coordinates")))
    return cargs


def mri_extract_outputs(
    params: MriExtractParameters,
    execution: Execution,
) -> MriExtractOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriExtractOutputs(
        root=execution.output_file("."),
        output_extracted_volume=execution.output_file(pathlib.Path(params.get("dst_volume")).name),
    )
    return ret


def mri_extract_execute(
    params: MriExtractParameters,
    execution: Execution,
) -> MriExtractOutputs:
    """
    MRI data extraction tool for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriExtractOutputs`).
    """
    params = execution.params(params)
    cargs = mri_extract_cargs(params, execution)
    ret = mri_extract_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_extract(
    src_volume: InputPathType,
    dst_volume: InputPathType,
    like_template: InputPathType | None = None,
    coordinates: list[float] | None = None,
    runner: Runner | None = None,
) -> MriExtractOutputs:
    """
    MRI data extraction tool for FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_volume: Source MRI volume file from which data will be extracted.
        dst_volume: The destination file where the extracted data will be\
            saved.
        like_template: Extract region like the given template volume.
        coordinates: Coordinates and size of the extraction box: x0 y0 z0 dx dy\
            dz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriExtractOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EXTRACT_METADATA)
    params = mri_extract_params(
        like_template=like_template,
        src_volume=src_volume,
        dst_volume=dst_volume,
        coordinates=coordinates,
    )
    return mri_extract_execute(params, execution)


__all__ = [
    "MRI_EXTRACT_METADATA",
    "MriExtractOutputs",
    "MriExtractParameters",
    "mri_extract",
    "mri_extract_params",
]

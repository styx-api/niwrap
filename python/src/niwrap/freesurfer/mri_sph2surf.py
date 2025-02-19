# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SPH2SURF_METADATA = Metadata(
    id="b6f756a7470f5c010ca807e14f237f111ed456b6.boutiques",
    name="mri-sph2surf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriSph2surfParameters = typing.TypedDict('MriSph2surfParameters', {
    "__STYX_TYPE__": typing.Literal["mri-sph2surf"],
    "instem": str,
    "outstem": str,
    "hemi": str,
    "subject": str,
    "offset": typing.NotRequired[float | None],
    "svitdir": typing.NotRequired[str | None],
    "umask": typing.NotRequired[str | None],
    "verbose": bool,
    "version": bool,
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
        "mri-sph2surf": mri_sph2surf_cargs,
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
        "mri-sph2surf": mri_sph2surf_outputs,
    }.get(t)


class MriSph2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_sph2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output surface data file in the form outstem-lh.w (or rh)."""


def mri_sph2surf_params(
    instem: str,
    outstem: str,
    hemi: str,
    subject: str,
    offset: float | None = 0,
    svitdir: str | None = "/usr/local/freesurfer/subjects/subject/svit",
    umask: str | None = None,
    verbose: bool = False,
    version: bool = False,
) -> MriSph2surfParameters:
    """
    Build parameters.
    
    Args:
        instem: Input stem of a bfloat file. The full input file name must take\
            the form instem-lh_000.bfloat (or rh).
        outstem: Output stem for the resulting file. The output file will have\
            the name outstem-lh.w (or rh).
        hemi: Specifies the hemisphere for processing. Acceptable values are\
            'lh' or 'rh'.
        subject: Specifies the subject identifier for the FreeSurfer processing\
            pipeline.
        offset: Zero-based plane/frame number. Default is 0.
        svitdir: Directory for svit. Default is\
            '/usr/local/freesurfer/subjects/subject/svit'.
        umask: Specifies a new user mask.
        verbose: Enable verbose output.
        version: Show version information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri-sph2surf",
        "instem": instem,
        "outstem": outstem,
        "hemi": hemi,
        "subject": subject,
        "verbose": verbose,
        "version": version,
    }
    if offset is not None:
        params["offset"] = offset
    if svitdir is not None:
        params["svitdir"] = svitdir
    if umask is not None:
        params["umask"] = umask
    return params


def mri_sph2surf_cargs(
    params: MriSph2surfParameters,
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
    cargs.append("mri-sph2surf")
    cargs.extend([
        "-i",
        params.get("instem")
    ])
    cargs.extend([
        "-o",
        params.get("outstem")
    ])
    cargs.extend([
        "-hemi",
        params.get("hemi")
    ])
    cargs.extend([
        "-s",
        params.get("subject")
    ])
    if params.get("offset") is not None:
        cargs.extend([
            "-offset",
            str(params.get("offset"))
        ])
    if params.get("svitdir") is not None:
        cargs.extend([
            "-svitdir",
            params.get("svitdir")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            params.get("umask")
        ])
    if params.get("verbose"):
        cargs.append("-verbose")
    if params.get("version"):
        cargs.append("-version")
    return cargs


def mri_sph2surf_outputs(
    params: MriSph2surfParameters,
    execution: Execution,
) -> MriSph2surfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSph2surfOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("outstem") + "-" + params.get("hemi") + ".w"),
    )
    return ret


def mri_sph2surf_execute(
    params: MriSph2surfParameters,
    execution: Execution,
) -> MriSph2surfOutputs:
    """
    Converts spherical functional data to surface data in the FreeSurfer processing
    pipeline.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSph2surfOutputs`).
    """
    params = execution.params(params)
    cargs = mri_sph2surf_cargs(params, execution)
    ret = mri_sph2surf_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_sph2surf(
    instem: str,
    outstem: str,
    hemi: str,
    subject: str,
    offset: float | None = 0,
    svitdir: str | None = "/usr/local/freesurfer/subjects/subject/svit",
    umask: str | None = None,
    verbose: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriSph2surfOutputs:
    """
    Converts spherical functional data to surface data in the FreeSurfer processing
    pipeline.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        instem: Input stem of a bfloat file. The full input file name must take\
            the form instem-lh_000.bfloat (or rh).
        outstem: Output stem for the resulting file. The output file will have\
            the name outstem-lh.w (or rh).
        hemi: Specifies the hemisphere for processing. Acceptable values are\
            'lh' or 'rh'.
        subject: Specifies the subject identifier for the FreeSurfer processing\
            pipeline.
        offset: Zero-based plane/frame number. Default is 0.
        svitdir: Directory for svit. Default is\
            '/usr/local/freesurfer/subjects/subject/svit'.
        umask: Specifies a new user mask.
        verbose: Enable verbose output.
        version: Show version information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSph2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SPH2SURF_METADATA)
    params = mri_sph2surf_params(
        instem=instem,
        outstem=outstem,
        hemi=hemi,
        subject=subject,
        offset=offset,
        svitdir=svitdir,
        umask=umask,
        verbose=verbose,
        version=version,
    )
    return mri_sph2surf_execute(params, execution)


__all__ = [
    "MRI_SPH2SURF_METADATA",
    "MriSph2surfOutputs",
    "MriSph2surfParameters",
    "mri_sph2surf",
    "mri_sph2surf_params",
]

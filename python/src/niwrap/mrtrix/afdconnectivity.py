# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AFDCONNECTIVITY_METADATA = Metadata(
    id="3290302704162d6eadb785f29be4535da532166f.boutiques",
    name="afdconnectivity",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


AfdconnectivityConfigParameters = typing.TypedDict('AfdconnectivityConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


AfdconnectivityParameters = typing.TypedDict('AfdconnectivityParameters', {
    "__STYX_TYPE__": typing.Literal["afdconnectivity"],
    "wbft": typing.NotRequired[InputPathType | None],
    "afd_map": typing.NotRequired[str | None],
    "all_fixels": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[AfdconnectivityConfigParameters] | None],
    "help": bool,
    "version": bool,
    "image": InputPathType,
    "tracks": InputPathType,
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
        "afdconnectivity": afdconnectivity_cargs,
        "config": afdconnectivity_config_cargs,
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
        "afdconnectivity": afdconnectivity_outputs,
    }.get(t)


def afdconnectivity_config_params(
    key: str,
    value: str,
) -> AfdconnectivityConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def afdconnectivity_config_cargs(
    params: AfdconnectivityConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class AfdconnectivityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afdconnectivity(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    afd_map: OutputPathType | None
    """output a 3D image containing the AFD estimated for each voxel. """


def afdconnectivity_params(
    image: InputPathType,
    tracks: InputPathType,
    wbft: InputPathType | None = None,
    afd_map: str | None = None,
    all_fixels: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[AfdconnectivityConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> AfdconnectivityParameters:
    """
    Build parameters.
    
    Args:
        image: the input FOD image.
        tracks: the input track file defining the bundle of interest.
        wbft: provide a whole-brain fibre-tracking data set (of which the input\
            track file should be a subset), to improve the estimate of fibre bundle\
            volume in the presence of partial volume.
        afd_map: output a 3D image containing the AFD estimated for each voxel.
        all_fixels: if whole-brain fibre-tracking is NOT provided, then if\
            multiple fixels within a voxel are traversed by the pathway of\
            interest, by default the fixel with the greatest streamlines density is\
            selected to contribute to the AFD in that voxel. If this option is\
            provided, then ALL fixels with non-zero streamlines density will\
            contribute to the result, even if multiple fixels per voxel are\
            selected.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "afdconnectivity",
        "all_fixels": all_fixels,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "image": image,
        "tracks": tracks,
    }
    if wbft is not None:
        params["wbft"] = wbft
    if afd_map is not None:
        params["afd_map"] = afd_map
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def afdconnectivity_cargs(
    params: AfdconnectivityParameters,
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
    cargs.append("afdconnectivity")
    if params.get("wbft") is not None:
        cargs.extend([
            "-wbft",
            execution.input_file(params.get("wbft"))
        ])
    if params.get("afd_map") is not None:
        cargs.extend([
            "-afd_map",
            params.get("afd_map")
        ])
    if params.get("all_fixels"):
        cargs.append("-all_fixels")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("image")))
    cargs.append(execution.input_file(params.get("tracks")))
    return cargs


def afdconnectivity_outputs(
    params: AfdconnectivityParameters,
    execution: Execution,
) -> AfdconnectivityOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AfdconnectivityOutputs(
        root=execution.output_file("."),
        afd_map=execution.output_file(params.get("afd_map")) if (params.get("afd_map") is not None) else None,
    )
    return ret


def afdconnectivity_execute(
    params: AfdconnectivityParameters,
    execution: Execution,
) -> AfdconnectivityOutputs:
    """
    Obtain an estimate of fibre connectivity between two regions using AFD and
    streamlines tractography.
    
    This estimate is obtained by determining a fibre volume (AFD) occupied by
    the pathway of interest, and dividing by the streamline length.
    
    If only the streamlines belonging to the pathway of interest are provided,
    then ALL of the fibre volume within each fixel selected will contribute to
    the result. If the -wbft option is used to provide whole-brain
    fibre-tracking (of which the pathway of interest should contain a subset),
    only the fraction of the fibre volume in each fixel estimated to belong to
    the pathway of interest will contribute to the result.
    
    Use -quiet to suppress progress messages and output fibre connectivity value
    only.
    
    For valid comparisons of AFD connectivity across scans, images MUST be
    intensity normalised and bias field corrected, and a common response
    function for all subjects must be used.
    
    Note that the sum of the AFD is normalised by streamline length to account
    for subject differences in fibre bundle length. This normalisation results
    in a measure that is more related to the cross-sectional volume of the tract
    (and therefore 'connectivity'). Note that SIFT-ed tract count is a superior
    measure because it is unaffected by tangential yet unrelated fibres.
    However, AFD connectivity may be used as a substitute when Anatomically
    Constrained Tractography is not possible due to uncorrectable EPI
    distortions, and SIFT may therefore not be as effective.
    
    Longer discussion regarding this command can additionally be found at:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/afd_connectivity.html (as
    well as in the relevant reference).
    
    References:
    
    Smith, R. E.; Raffelt, D.; Tournier, J.-D.; Connelly, A. Quantitative
    Streamlines Tractography: Methods and Inter-Subject Normalisation. Open
    Science Framework, https://doi.org/10.31219/osf.io/c67kn.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AfdconnectivityOutputs`).
    """
    params = execution.params(params)
    cargs = afdconnectivity_cargs(params, execution)
    ret = afdconnectivity_outputs(params, execution)
    execution.run(cargs)
    return ret


def afdconnectivity(
    image: InputPathType,
    tracks: InputPathType,
    wbft: InputPathType | None = None,
    afd_map: str | None = None,
    all_fixels: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[AfdconnectivityConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AfdconnectivityOutputs:
    """
    Obtain an estimate of fibre connectivity between two regions using AFD and
    streamlines tractography.
    
    This estimate is obtained by determining a fibre volume (AFD) occupied by
    the pathway of interest, and dividing by the streamline length.
    
    If only the streamlines belonging to the pathway of interest are provided,
    then ALL of the fibre volume within each fixel selected will contribute to
    the result. If the -wbft option is used to provide whole-brain
    fibre-tracking (of which the pathway of interest should contain a subset),
    only the fraction of the fibre volume in each fixel estimated to belong to
    the pathway of interest will contribute to the result.
    
    Use -quiet to suppress progress messages and output fibre connectivity value
    only.
    
    For valid comparisons of AFD connectivity across scans, images MUST be
    intensity normalised and bias field corrected, and a common response
    function for all subjects must be used.
    
    Note that the sum of the AFD is normalised by streamline length to account
    for subject differences in fibre bundle length. This normalisation results
    in a measure that is more related to the cross-sectional volume of the tract
    (and therefore 'connectivity'). Note that SIFT-ed tract count is a superior
    measure because it is unaffected by tangential yet unrelated fibres.
    However, AFD connectivity may be used as a substitute when Anatomically
    Constrained Tractography is not possible due to uncorrectable EPI
    distortions, and SIFT may therefore not be as effective.
    
    Longer discussion regarding this command can additionally be found at:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/afd_connectivity.html (as
    well as in the relevant reference).
    
    References:
    
    Smith, R. E.; Raffelt, D.; Tournier, J.-D.; Connelly, A. Quantitative
    Streamlines Tractography: Methods and Inter-Subject Normalisation. Open
    Science Framework, https://doi.org/10.31219/osf.io/c67kn.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        image: the input FOD image.
        tracks: the input track file defining the bundle of interest.
        wbft: provide a whole-brain fibre-tracking data set (of which the input\
            track file should be a subset), to improve the estimate of fibre bundle\
            volume in the presence of partial volume.
        afd_map: output a 3D image containing the AFD estimated for each voxel.
        all_fixels: if whole-brain fibre-tracking is NOT provided, then if\
            multiple fixels within a voxel are traversed by the pathway of\
            interest, by default the fixel with the greatest streamlines density is\
            selected to contribute to the AFD in that voxel. If this option is\
            provided, then ALL fixels with non-zero streamlines density will\
            contribute to the result, even if multiple fixels per voxel are\
            selected.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfdconnectivityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFDCONNECTIVITY_METADATA)
    params = afdconnectivity_params(
        wbft=wbft,
        afd_map=afd_map,
        all_fixels=all_fixels,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        image=image,
        tracks=tracks,
    )
    return afdconnectivity_execute(params, execution)


__all__ = [
    "AFDCONNECTIVITY_METADATA",
    "AfdconnectivityConfigParameters",
    "AfdconnectivityOutputs",
    "AfdconnectivityParameters",
    "afdconnectivity",
    "afdconnectivity_config_params",
    "afdconnectivity_params",
]

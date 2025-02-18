# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FOD2DEC_METADATA = Metadata(
    id="464092d0c46e0f6d44851c80e38f43548c357c00.boutiques",
    name="fod2dec",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Fod2decConfigParameters = typing.TypedDict('Fod2decConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Fod2decParameters = typing.TypedDict('Fod2decParameters', {
    "__STYX_TYPE__": typing.Literal["fod2dec"],
    "mask": typing.NotRequired[InputPathType | None],
    "contrast": typing.NotRequired[InputPathType | None],
    "lum": bool,
    "lum_coefs": typing.NotRequired[list[float] | None],
    "lum_gamma": typing.NotRequired[float | None],
    "threshold": typing.NotRequired[float | None],
    "no_weight": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Fod2decConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
    "output": str,
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
        "fod2dec": fod2dec_cargs,
        "config": fod2dec_config_cargs,
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
        "fod2dec": fod2dec_outputs,
    }.get(t)


def fod2dec_config_params(
    key: str,
    value: str,
) -> Fod2decConfigParameters:
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


def fod2dec_config_cargs(
    params: Fod2decConfigParameters,
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


class Fod2decOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fod2dec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """The output DEC image (weighted RGB triplets)."""


def fod2dec_params(
    input_: InputPathType,
    output: str,
    mask: InputPathType | None = None,
    contrast: InputPathType | None = None,
    lum: bool = False,
    lum_coefs: list[float] | None = None,
    lum_gamma: float | None = None,
    threshold: float | None = None,
    no_weight: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fod2decConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Fod2decParameters:
    """
    Build parameters.
    
    Args:
        input_: The input FOD image (spherical harmonic coefficients).
        output: The output DEC image (weighted RGB triplets).
        mask: Only perform DEC computation within the specified mask image.
        contrast: Weight the computed DEC map by the provided image contrast.\
            If the contrast has a different image grid, the DEC map is first\
            resliced and renormalised. To achieve panchromatic sharpening, provide\
            an image with a higher spatial resolution than the input FOD image;\
            e.g., a T1 anatomical volume. Only the DEC is subject to the mask, so\
            as to allow for partial colouring of the contrast image.\
            Default when this option is *not* provided: integral of input FOD,\
            subject to the same mask/threshold as used for DEC computation.
        lum: Correct for luminance/perception, using default values Cr,Cg,Cb =\
            0.3,0.5,0.2 and gamma = 2.2 (*not* correcting is the theoretical\
            equivalent of Cr,Cg,Cb = 1,1,1 and gamma = 2).
        lum_coefs: The coefficients Cr,Cg,Cb to correct for\
            luminance/perception.\
            Note: this implicitly switches on luminance/perception correction,\
            using a default gamma = 2.2 unless specified otherwise.
        lum_gamma: The gamma value to correct for luminance/perception.\
            Note: this implicitly switches on luminance/perception correction,\
            using a default Cr,Cg,Cb = 0.3,0.5,0.2 unless specified otherwise.
        threshold: FOD amplitudes below the threshold value are considered\
            zero.
        no_weight: Do not weight the DEC map; just output the unweighted\
            colours. Reslicing and renormalising of colours will still happen when\
            providing the -contrast option as a template.
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
        "__STYXTYPE__": "fod2dec",
        "lum": lum,
        "no_weight": no_weight,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if mask is not None:
        params["mask"] = mask
    if contrast is not None:
        params["contrast"] = contrast
    if lum_coefs is not None:
        params["lum_coefs"] = lum_coefs
    if lum_gamma is not None:
        params["lum_gamma"] = lum_gamma
    if threshold is not None:
        params["threshold"] = threshold
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fod2dec_cargs(
    params: Fod2decParameters,
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
    cargs.append("fod2dec")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("contrast") is not None:
        cargs.extend([
            "-contrast",
            execution.input_file(params.get("contrast"))
        ])
    if params.get("lum"):
        cargs.append("-lum")
    if params.get("lum_coefs") is not None:
        cargs.extend([
            "-lum_coefs",
            *map(str, params.get("lum_coefs"))
        ])
    if params.get("lum_gamma") is not None:
        cargs.extend([
            "-lum_gamma",
            str(params.get("lum_gamma"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-threshold",
            str(params.get("threshold"))
        ])
    if params.get("no_weight"):
        cargs.append("-no_weight")
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
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("output"))
    return cargs


def fod2dec_outputs(
    params: Fod2decParameters,
    execution: Execution,
) -> Fod2decOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fod2decOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def fod2dec_execute(
    params: Fod2decParameters,
    execution: Execution,
) -> Fod2decOutputs:
    """
    Generate FOD-based DEC maps, with optional panchromatic sharpening and/or
    luminance/perception correction.
    
    By default, the FOD-based DEC is weighted by the integral of the FOD. To
    weight by another scalar map, use the -contrast option. This option can also
    be used for panchromatic sharpening, e.g., by supplying a T1 (or other
    sensible) anatomical volume with a higher spatial resolution.
    
    References:
    
    Dhollander T, Smith RE, Tournier JD, Jeurissen B, Connelly A. Time to move
    on: an FOD-based DEC map to replace DTI's trademark DEC FA. Proc Intl Soc
    Mag Reson Med, 2015, 23, 1027
    
    Dhollander T, Raffelt D, Smith RE, Connelly A. Panchromatic sharpening of
    FOD-based DEC maps by structural T1 information. Proc Intl Soc Mag Reson
    Med, 2015, 23, 566.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fod2decOutputs`).
    """
    cargs = fod2dec_cargs(params, execution)
    ret = fod2dec_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def fod2dec(
    input_: InputPathType,
    output: str,
    mask: InputPathType | None = None,
    contrast: InputPathType | None = None,
    lum: bool = False,
    lum_coefs: list[float] | None = None,
    lum_gamma: float | None = None,
    threshold: float | None = None,
    no_weight: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fod2decConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Fod2decOutputs:
    """
    Generate FOD-based DEC maps, with optional panchromatic sharpening and/or
    luminance/perception correction.
    
    By default, the FOD-based DEC is weighted by the integral of the FOD. To
    weight by another scalar map, use the -contrast option. This option can also
    be used for panchromatic sharpening, e.g., by supplying a T1 (or other
    sensible) anatomical volume with a higher spatial resolution.
    
    References:
    
    Dhollander T, Smith RE, Tournier JD, Jeurissen B, Connelly A. Time to move
    on: an FOD-based DEC map to replace DTI's trademark DEC FA. Proc Intl Soc
    Mag Reson Med, 2015, 23, 1027
    
    Dhollander T, Raffelt D, Smith RE, Connelly A. Panchromatic sharpening of
    FOD-based DEC maps by structural T1 information. Proc Intl Soc Mag Reson
    Med, 2015, 23, 566.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: The input FOD image (spherical harmonic coefficients).
        output: The output DEC image (weighted RGB triplets).
        mask: Only perform DEC computation within the specified mask image.
        contrast: Weight the computed DEC map by the provided image contrast.\
            If the contrast has a different image grid, the DEC map is first\
            resliced and renormalised. To achieve panchromatic sharpening, provide\
            an image with a higher spatial resolution than the input FOD image;\
            e.g., a T1 anatomical volume. Only the DEC is subject to the mask, so\
            as to allow for partial colouring of the contrast image.\
            Default when this option is *not* provided: integral of input FOD,\
            subject to the same mask/threshold as used for DEC computation.
        lum: Correct for luminance/perception, using default values Cr,Cg,Cb =\
            0.3,0.5,0.2 and gamma = 2.2 (*not* correcting is the theoretical\
            equivalent of Cr,Cg,Cb = 1,1,1 and gamma = 2).
        lum_coefs: The coefficients Cr,Cg,Cb to correct for\
            luminance/perception.\
            Note: this implicitly switches on luminance/perception correction,\
            using a default gamma = 2.2 unless specified otherwise.
        lum_gamma: The gamma value to correct for luminance/perception.\
            Note: this implicitly switches on luminance/perception correction,\
            using a default Cr,Cg,Cb = 0.3,0.5,0.2 unless specified otherwise.
        threshold: FOD amplitudes below the threshold value are considered\
            zero.
        no_weight: Do not weight the DEC map; just output the unweighted\
            colours. Reslicing and renormalising of colours will still happen when\
            providing the -contrast option as a template.
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
        NamedTuple of outputs (described in `Fod2decOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOD2DEC_METADATA)
    params = fod2dec_params(mask=mask, contrast=contrast, lum=lum, lum_coefs=lum_coefs, lum_gamma=lum_gamma, threshold=threshold, no_weight=no_weight, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, output=output)
    return fod2dec_execute(params, execution)


__all__ = [
    "FOD2DEC_METADATA",
    "Fod2decConfigParameters",
    "Fod2decOutputs",
    "Fod2decParameters",
    "fod2dec",
    "fod2dec_config_params",
    "fod2dec_params",
]

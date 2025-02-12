# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DWI2TENSOR_METADATA = Metadata(
    id="da9a17f80c44190e972d6db8b17af753fd59d62f.boutiques",
    name="dwi2tensor",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Dwi2tensorFslgradParameters = typing.TypedDict('Dwi2tensorFslgradParameters', {
    "__STYX_TYPE__": typing.Literal["fslgrad"],
    "bvecs": InputPathType,
    "bvals": InputPathType,
})
Dwi2tensorConfigParameters = typing.TypedDict('Dwi2tensorConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Dwi2tensorParameters = typing.TypedDict('Dwi2tensorParameters', {
    "__STYX_TYPE__": typing.Literal["dwi2tensor"],
    "ols": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "b0": typing.NotRequired[str | None],
    "dkt": typing.NotRequired[str | None],
    "iter": typing.NotRequired[int | None],
    "predicted_signal": typing.NotRequired[str | None],
    "grad": typing.NotRequired[InputPathType | None],
    "fslgrad": typing.NotRequired[Dwi2tensorFslgradParameters | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Dwi2tensorConfigParameters] | None],
    "help": bool,
    "version": bool,
    "dwi": InputPathType,
    "dt": str,
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
        "dwi2tensor": dwi2tensor_cargs,
        "fslgrad": dwi2tensor_fslgrad_cargs,
        "config": dwi2tensor_config_cargs,
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
        "dwi2tensor": dwi2tensor_outputs,
    }.get(t)


def dwi2tensor_fslgrad_params(
    bvecs: InputPathType,
    bvals: InputPathType,
) -> Dwi2tensorFslgradParameters:
    """
    Build parameters.
    
    Args:
        bvecs: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        bvals: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslgrad",
        "bvecs": bvecs,
        "bvals": bvals,
    }
    return params


def dwi2tensor_fslgrad_cargs(
    params: Dwi2tensorFslgradParameters,
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
    cargs.append("-fslgrad")
    cargs.append(execution.input_file(params.get("bvecs")))
    cargs.append(execution.input_file(params.get("bvals")))
    return cargs


def dwi2tensor_config_params(
    key: str,
    value: str,
) -> Dwi2tensorConfigParameters:
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


def dwi2tensor_config_cargs(
    params: Dwi2tensorConfigParameters,
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


class Dwi2tensorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwi2tensor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dt: OutputPathType
    """the output dt image."""
    b0: OutputPathType | None
    """the output b0 image. """
    dkt: OutputPathType | None
    """the output dkt image. """
    predicted_signal: OutputPathType | None
    """the predicted dwi image. """


def dwi2tensor_params(
    dwi: InputPathType,
    dt: str,
    ols: bool = False,
    mask: InputPathType | None = None,
    b0: str | None = None,
    dkt: str | None = None,
    iter_: int | None = None,
    predicted_signal: str | None = None,
    grad: InputPathType | None = None,
    fslgrad: Dwi2tensorFslgradParameters | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2tensorConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Dwi2tensorParameters:
    """
    Build parameters.
    
    Args:
        dwi: the input dwi image.
        dt: the output dt image.
        ols: perform initial fit using an ordinary least-squares (OLS) fit (see\
            Description).
        mask: only perform computation within the specified binary brain mask\
            image.
        b0: the output b0 image.
        dkt: the output dkt image.
        iter_: number of iterative reweightings for IWLS algorithm (default: 2)\
            (see Description).
        predicted_signal: the predicted dwi image.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
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
        "__STYXTYPE__": "dwi2tensor",
        "ols": ols,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "dwi": dwi,
        "dt": dt,
    }
    if mask is not None:
        params["mask"] = mask
    if b0 is not None:
        params["b0"] = b0
    if dkt is not None:
        params["dkt"] = dkt
    if iter_ is not None:
        params["iter"] = iter_
    if predicted_signal is not None:
        params["predicted_signal"] = predicted_signal
    if grad is not None:
        params["grad"] = grad
    if fslgrad is not None:
        params["fslgrad"] = fslgrad
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dwi2tensor_cargs(
    params: Dwi2tensorParameters,
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
    cargs.append("dwi2tensor")
    if params.get("ols"):
        cargs.append("-ols")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("b0") is not None:
        cargs.extend([
            "-b0",
            params.get("b0")
        ])
    if params.get("dkt") is not None:
        cargs.extend([
            "-dkt",
            params.get("dkt")
        ])
    if params.get("iter") is not None:
        cargs.extend([
            "-iter",
            str(params.get("iter"))
        ])
    if params.get("predicted_signal") is not None:
        cargs.extend([
            "-predicted_signal",
            params.get("predicted_signal")
        ])
    if params.get("grad") is not None:
        cargs.extend([
            "-grad",
            execution.input_file(params.get("grad"))
        ])
    if params.get("fslgrad") is not None:
        cargs.extend(dyn_cargs(params.get("fslgrad")["__STYXTYPE__"])(params.get("fslgrad"), execution))
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
    cargs.append(execution.input_file(params.get("dwi")))
    cargs.append(params.get("dt"))
    return cargs


def dwi2tensor_outputs(
    params: Dwi2tensorParameters,
    execution: Execution,
) -> Dwi2tensorOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Dwi2tensorOutputs(
        root=execution.output_file("."),
        dt=execution.output_file(params.get("dt")),
        b0=execution.output_file(params.get("b0")) if (params.get("b0") is not None) else None,
        dkt=execution.output_file(params.get("dkt")) if (params.get("dkt") is not None) else None,
        predicted_signal=execution.output_file(params.get("predicted_signal")) if (params.get("predicted_signal") is not None) else None,
    )
    return ret


def dwi2tensor_execute(
    params: Dwi2tensorParameters,
    execution: Execution,
) -> Dwi2tensorOutputs:
    """
    Diffusion (kurtosis) tensor estimation.
    
    By default, the diffusion tensor (and optionally its kurtosis) is fitted to
    the log-signal in two steps: firstly, using weighted least-squares (WLS)
    with weights based on the empirical signal intensities; secondly, by further
    iterated weighted least-squares (IWLS) with weights determined by the signal
    predictions from the previous iteration (by default, 2 iterations will be
    performed). This behaviour can be altered in two ways:
    
    * The -ols option will cause the first fitting step to be performed using
    ordinary least-squares (OLS); that is, all measurements contribute equally
    to the fit, instead of the default behaviour of weighting based on the
    empirical signal intensities.
    
    * The -iter option controls the number of iterations of the IWLS prodedure.
    If this is set to zero, then the output model parameters will be those
    resulting from the first fitting step only: either WLS by default, or OLS if
    the -ols option is used in conjunction with -iter 0.
    
    The tensor coefficients are stored in the output image as follows:
    volumes 0-5: D11, D22, D33, D12, D13, D23
    
    If diffusion kurtosis is estimated using the -dkt option, these are stored
    as follows:
    volumes 0-2: W1111, W2222, W3333
    volumes 3-8: W1112, W1113, W1222, W1333, W2223, W2333
    volumes 9-11: W1122, W1133, W2233
    volumes 12-14: W1123, W1223, W1233
    
    References:
    
    References based on fitting algorithm used:
    
    * OLS, WLS:
    Basser, P.J.; Mattiello, J.; LeBihan, D. Estimation of the effective
    self-diffusion tensor from the NMR spin echo. J Magn Reson B., 1994, 103,
    247â€“254.
    
    * IWLS:
    Veraart, J.; Sijbers, J.; Sunaert, S.; Leemans, A. & Jeurissen, B. Weighted
    linear least squares estimation of diffusion MRI parameters: strengths,
    limitations, and pitfalls. NeuroImage, 2013, 81, 335-346.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Dwi2tensorOutputs`).
    """
    cargs = dwi2tensor_cargs(params, execution)
    ret = dwi2tensor_outputs(params, execution)
    execution.run(cargs)
    return ret


def dwi2tensor(
    dwi: InputPathType,
    dt: str,
    ols: bool = False,
    mask: InputPathType | None = None,
    b0: str | None = None,
    dkt: str | None = None,
    iter_: int | None = None,
    predicted_signal: str | None = None,
    grad: InputPathType | None = None,
    fslgrad: Dwi2tensorFslgradParameters | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2tensorConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Dwi2tensorOutputs:
    """
    Diffusion (kurtosis) tensor estimation.
    
    By default, the diffusion tensor (and optionally its kurtosis) is fitted to
    the log-signal in two steps: firstly, using weighted least-squares (WLS)
    with weights based on the empirical signal intensities; secondly, by further
    iterated weighted least-squares (IWLS) with weights determined by the signal
    predictions from the previous iteration (by default, 2 iterations will be
    performed). This behaviour can be altered in two ways:
    
    * The -ols option will cause the first fitting step to be performed using
    ordinary least-squares (OLS); that is, all measurements contribute equally
    to the fit, instead of the default behaviour of weighting based on the
    empirical signal intensities.
    
    * The -iter option controls the number of iterations of the IWLS prodedure.
    If this is set to zero, then the output model parameters will be those
    resulting from the first fitting step only: either WLS by default, or OLS if
    the -ols option is used in conjunction with -iter 0.
    
    The tensor coefficients are stored in the output image as follows:
    volumes 0-5: D11, D22, D33, D12, D13, D23
    
    If diffusion kurtosis is estimated using the -dkt option, these are stored
    as follows:
    volumes 0-2: W1111, W2222, W3333
    volumes 3-8: W1112, W1113, W1222, W1333, W2223, W2333
    volumes 9-11: W1122, W1133, W2233
    volumes 12-14: W1123, W1223, W1233
    
    References:
    
    References based on fitting algorithm used:
    
    * OLS, WLS:
    Basser, P.J.; Mattiello, J.; LeBihan, D. Estimation of the effective
    self-diffusion tensor from the NMR spin echo. J Magn Reson B., 1994, 103,
    247â€“254.
    
    * IWLS:
    Veraart, J.; Sijbers, J.; Sunaert, S.; Leemans, A. & Jeurissen, B. Weighted
    linear least squares estimation of diffusion MRI parameters: strengths,
    limitations, and pitfalls. NeuroImage, 2013, 81, 335-346.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        dwi: the input dwi image.
        dt: the output dt image.
        ols: perform initial fit using an ordinary least-squares (OLS) fit (see\
            Description).
        mask: only perform computation within the specified binary brain mask\
            image.
        b0: the output b0 image.
        dkt: the output dkt image.
        iter_: number of iterative reweightings for IWLS algorithm (default: 2)\
            (see Description).
        predicted_signal: the predicted dwi image.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
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
        NamedTuple of outputs (described in `Dwi2tensorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWI2TENSOR_METADATA)
    params = dwi2tensor_params(ols=ols, mask=mask, b0=b0, dkt=dkt, iter_=iter_, predicted_signal=predicted_signal, grad=grad, fslgrad=fslgrad, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, dwi=dwi, dt=dt)
    return dwi2tensor_execute(params, execution)


__all__ = [
    "DWI2TENSOR_METADATA",
    "Dwi2tensorConfigParameters",
    "Dwi2tensorFslgradParameters",
    "Dwi2tensorOutputs",
    "Dwi2tensorParameters",
    "dwi2tensor",
    "dwi2tensor_config_params",
    "dwi2tensor_fslgrad_params",
    "dwi2tensor_params",
]

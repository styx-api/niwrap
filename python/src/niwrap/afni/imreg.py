# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMREG_METADATA = Metadata(
    id="4ed217ec6db0c1ed0ca85263b118a5554ebb437a.boutiques",
    name="imreg",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ImregParameters = typing.TypedDict('ImregParameters', {
    "__STYX_TYPE__": typing.Literal["imreg"],
    "base_image": str,
    "image_sequence": list[InputPathType],
    "nowrite": bool,
    "prefix": typing.NotRequired[str | None],
    "suffix": typing.NotRequired[str | None],
    "start": typing.NotRequired[float | None],
    "step": typing.NotRequired[float | None],
    "flim": bool,
    "keepsize": bool,
    "quiet": bool,
    "debug": bool,
    "dprefix": typing.NotRequired[str | None],
    "bilinear": bool,
    "modes": typing.NotRequired[str | None],
    "mlcf": bool,
    "wtim": typing.NotRequired[InputPathType | None],
    "dfspace": bool,
    "cmass": bool,
    "fine": typing.NotRequired[list[float] | None],
    "nofine": bool,
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
        "imreg": imreg_cargs,
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
        "imreg": imreg_outputs,
    }.get(t)


class ImregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_images: OutputPathType | None
    """Registered images"""
    dx_file: OutputPathType | None
    """Time series dx file"""
    dy_file: OutputPathType | None
    """Time series dy file"""
    phi_file: OutputPathType | None
    """Time series phi file"""


def imreg_params(
    base_image: str,
    image_sequence: list[InputPathType],
    nowrite: bool = False,
    prefix: str | None = None,
    suffix: str | None = None,
    start: float | None = None,
    step: float | None = None,
    flim: bool = False,
    keepsize: bool = False,
    quiet: bool = False,
    debug: bool = False,
    dprefix: str | None = None,
    bilinear: bool = False,
    modes: str | None = None,
    mlcf: bool = False,
    wtim: InputPathType | None = None,
    dfspace: bool = False,
    cmass: bool = False,
    fine: list[float] | None = None,
    nofine: bool = False,
) -> ImregParameters:
    """
    Build parameters.
    
    Args:
        base_image: Base image or method to determine base image ('+AVER' or\
            '+count').
        image_sequence: Sequence of images to be registered.
        nowrite: Don't write outputs, just print progress reports.
        prefix: Prefix for output file names.
        suffix: Suffix for output file names.
        start: Start index for output file names.
        step: Step size for output file indices.
        flim: Write output in mrilib floating point format.
        keepsize: Preserve the original image size on output.
        quiet: Don't write progress report messages.
        debug: Write lots of debugging output.
        dprefix: Prefix for dx, dy, and phi files.
        bilinear: Use bilinear interpolation.
        modes: Interpolation modes during coarse, fine, and registration phases.
        mlcf: Equivalent to '-modes bilinear bicubic Fourier'.
        wtim: Weighting image file.
        dfspace: Use difiterated differential spatial method.
        cmass: Align centers of mass of the images.
        fine: Fine fit parameters: blur, dxy, dphi.
        nofine: Turn off the 'fine' fit algorithm.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imreg",
        "base_image": base_image,
        "image_sequence": image_sequence,
        "nowrite": nowrite,
        "flim": flim,
        "keepsize": keepsize,
        "quiet": quiet,
        "debug": debug,
        "bilinear": bilinear,
        "mlcf": mlcf,
        "dfspace": dfspace,
        "cmass": cmass,
        "nofine": nofine,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if suffix is not None:
        params["suffix"] = suffix
    if start is not None:
        params["start"] = start
    if step is not None:
        params["step"] = step
    if dprefix is not None:
        params["dprefix"] = dprefix
    if modes is not None:
        params["modes"] = modes
    if wtim is not None:
        params["wtim"] = wtim
    if fine is not None:
        params["fine"] = fine
    return params


def imreg_cargs(
    params: ImregParameters,
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
    cargs.append("imreg")
    cargs.append(params.get("base_image"))
    cargs.extend([execution.input_file(f) for f in params.get("image_sequence")])
    if params.get("nowrite"):
        cargs.append("-nowrite")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("suffix")
        ])
    if params.get("start") is not None:
        cargs.extend([
            "-start",
            str(params.get("start"))
        ])
    if params.get("step") is not None:
        cargs.extend([
            "-step",
            str(params.get("step"))
        ])
    if params.get("flim"):
        cargs.append("-flim")
    if params.get("keepsize"):
        cargs.append("-keepsize")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("dprefix") is not None:
        cargs.extend([
            "-dprefix",
            params.get("dprefix")
        ])
    if params.get("bilinear"):
        cargs.append("-bilinear")
    if params.get("modes") is not None:
        cargs.extend([
            "-modes",
            params.get("modes")
        ])
    if params.get("mlcf"):
        cargs.append("-mlcF")
    if params.get("wtim") is not None:
        cargs.extend([
            "-wtim",
            execution.input_file(params.get("wtim"))
        ])
    if params.get("dfspace"):
        cargs.append("-dfspace")
    if params.get("cmass"):
        cargs.append("-cmass")
    if params.get("fine") is not None:
        cargs.extend([
            "-fine",
            *map(str, params.get("fine"))
        ])
    if params.get("nofine"):
        cargs.append("-nofine")
    return cargs


def imreg_outputs(
    params: ImregParameters,
    execution: Execution,
) -> ImregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImregOutputs(
        root=execution.output_file("."),
        registered_images=execution.output_file(params.get("prefix") + ".[INDEX]." + params.get("suffix")) if (params.get("prefix") is not None and params.get("suffix") is not None) else None,
        dx_file=execution.output_file(params.get("dprefix") + ".dx") if (params.get("dprefix") is not None) else None,
        dy_file=execution.output_file(params.get("dprefix") + ".dy") if (params.get("dprefix") is not None) else None,
        phi_file=execution.output_file(params.get("dprefix") + ".phi") if (params.get("dprefix") is not None) else None,
    )
    return ret


def imreg_execute(
    params: ImregParameters,
    execution: Execution,
) -> ImregOutputs:
    """
    Registers each 2D image in 'image_sequence' to 'base_image'.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImregOutputs`).
    """
    cargs = imreg_cargs(params, execution)
    ret = imreg_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def imreg(
    base_image: str,
    image_sequence: list[InputPathType],
    nowrite: bool = False,
    prefix: str | None = None,
    suffix: str | None = None,
    start: float | None = None,
    step: float | None = None,
    flim: bool = False,
    keepsize: bool = False,
    quiet: bool = False,
    debug: bool = False,
    dprefix: str | None = None,
    bilinear: bool = False,
    modes: str | None = None,
    mlcf: bool = False,
    wtim: InputPathType | None = None,
    dfspace: bool = False,
    cmass: bool = False,
    fine: list[float] | None = None,
    nofine: bool = False,
    runner: Runner | None = None,
) -> ImregOutputs:
    """
    Registers each 2D image in 'image_sequence' to 'base_image'.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        base_image: Base image or method to determine base image ('+AVER' or\
            '+count').
        image_sequence: Sequence of images to be registered.
        nowrite: Don't write outputs, just print progress reports.
        prefix: Prefix for output file names.
        suffix: Suffix for output file names.
        start: Start index for output file names.
        step: Step size for output file indices.
        flim: Write output in mrilib floating point format.
        keepsize: Preserve the original image size on output.
        quiet: Don't write progress report messages.
        debug: Write lots of debugging output.
        dprefix: Prefix for dx, dy, and phi files.
        bilinear: Use bilinear interpolation.
        modes: Interpolation modes during coarse, fine, and registration phases.
        mlcf: Equivalent to '-modes bilinear bicubic Fourier'.
        wtim: Weighting image file.
        dfspace: Use difiterated differential spatial method.
        cmass: Align centers of mass of the images.
        fine: Fine fit parameters: blur, dxy, dphi.
        nofine: Turn off the 'fine' fit algorithm.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMREG_METADATA)
    params = imreg_params(base_image=base_image, image_sequence=image_sequence, nowrite=nowrite, prefix=prefix, suffix=suffix, start=start, step=step, flim=flim, keepsize=keepsize, quiet=quiet, debug=debug, dprefix=dprefix, bilinear=bilinear, modes=modes, mlcf=mlcf, wtim=wtim, dfspace=dfspace, cmass=cmass, fine=fine, nofine=nofine)
    return imreg_execute(params, execution)


__all__ = [
    "IMREG_METADATA",
    "ImregOutputs",
    "ImregParameters",
    "imreg",
    "imreg_params",
]

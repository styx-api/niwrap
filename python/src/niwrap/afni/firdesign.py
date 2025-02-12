# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIRDESIGN_METADATA = Metadata(
    id="a74504adf0b49ec5a0615bc609bf67d8b73823f0.boutiques",
    name="FIRdesign",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FirdesignParameters = typing.TypedDict('FirdesignParameters', {
    "__STYX_TYPE__": typing.Literal["FIRdesign"],
    "fbot": float,
    "ftop": float,
    "ntap": float,
    "tr": typing.NotRequired[float | None],
    "alternative_band": typing.NotRequired[list[float] | None],
    "alternative_ntap": typing.NotRequired[float | None],
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
        "FIRdesign": firdesign_cargs,
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


class FirdesignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `firdesign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def firdesign_params(
    fbot: float,
    ftop: float,
    ntap: float,
    tr: float | None = None,
    alternative_band: list[float] | None = None,
    alternative_ntap: float | None = None,
) -> FirdesignParameters:
    """
    Build parameters.
    
    Args:
        fbot: Lowest frequency in the pass band.
        ftop: Highest frequency in the pass band, must be higher than fbot and\
            <= 0.5/TR.
        ntap: Number of filter weights (AKA 'taps') to use, must be in the\
            range 8..2000 (inclusive).
        tr: Set time grid spacing to 'dd' [default is 1.0].
        alternative_band: Alternative way to specify the passband.
        alternative_ntap: Alternative way to specify the number of taps.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "FIRdesign",
        "fbot": fbot,
        "ftop": ftop,
        "ntap": ntap,
    }
    if tr is not None:
        params["tr"] = tr
    if alternative_band is not None:
        params["alternative_band"] = alternative_band
    if alternative_ntap is not None:
        params["alternative_ntap"] = alternative_ntap
    return params


def firdesign_cargs(
    params: FirdesignParameters,
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
    cargs.append("FIRdesign")
    cargs.append(str(params.get("fbot")))
    cargs.append(str(params.get("ftop")))
    cargs.append(str(params.get("ntap")))
    if params.get("tr") is not None:
        cargs.extend([
            "-TR",
            str(params.get("tr"))
        ])
    if params.get("alternative_band") is not None:
        cargs.extend([
            "-band",
            *map(str, params.get("alternative_band"))
        ])
    if params.get("alternative_ntap") is not None:
        cargs.extend([
            "-ntap",
            str(params.get("alternative_ntap"))
        ])
    return cargs


def firdesign_outputs(
    params: FirdesignParameters,
    execution: Execution,
) -> FirdesignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FirdesignOutputs(
        root=execution.output_file("."),
    )
    return ret


def firdesign_execute(
    params: FirdesignParameters,
    execution: Execution,
) -> FirdesignOutputs:
    """
    Uses the Remez algorithm to calculate the FIR filter weights for a bandpass
    filter; results are written to stdout in an unadorned (no header) column of
    numbers.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FirdesignOutputs`).
    """
    cargs = firdesign_cargs(params, execution)
    ret = firdesign_outputs(params, execution)
    execution.run(cargs)
    return ret


def firdesign(
    fbot: float,
    ftop: float,
    ntap: float,
    tr: float | None = None,
    alternative_band: list[float] | None = None,
    alternative_ntap: float | None = None,
    runner: Runner | None = None,
) -> FirdesignOutputs:
    """
    Uses the Remez algorithm to calculate the FIR filter weights for a bandpass
    filter; results are written to stdout in an unadorned (no header) column of
    numbers.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fbot: Lowest frequency in the pass band.
        ftop: Highest frequency in the pass band, must be higher than fbot and\
            <= 0.5/TR.
        ntap: Number of filter weights (AKA 'taps') to use, must be in the\
            range 8..2000 (inclusive).
        tr: Set time grid spacing to 'dd' [default is 1.0].
        alternative_band: Alternative way to specify the passband.
        alternative_ntap: Alternative way to specify the number of taps.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirdesignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRDESIGN_METADATA)
    params = firdesign_params(fbot=fbot, ftop=ftop, ntap=ntap, tr=tr, alternative_band=alternative_band, alternative_ntap=alternative_ntap)
    return firdesign_execute(params, execution)


__all__ = [
    "FIRDESIGN_METADATA",
    "FirdesignOutputs",
    "FirdesignParameters",
    "firdesign",
    "firdesign_params",
]

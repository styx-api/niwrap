# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FIRDESIGN_METADATA = Metadata(
    id="ff265fa55469437206f529906cbd23e0a409b702",
    name="FIRdesign",
)


class FirdesignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `firdesign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def firdesign(
    fbot: float | int,
    ftop: float | int,
    ntap: float | int,
    tr: float | int | None = None,
    alternative_band: list[float | int] | None = None,
    alternative_ntap: float | int | None = None,
    runner: Runner | None = None,
) -> FirdesignOutputs:
    """
    FIRdesign by RWCox.
    
    Uses the Remez algorithm to calculate the FIR filter weights for a bandpass
    filter; results are written to stdout in an unadorned (no header) column of
    numbers.
    
    More information:
    http://en.wikipedia.org/wiki/Parks-McClellan_filter_design_algorithm
    
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
    if not (0 <= fbot): 
        raise ValueError(f"'fbot' must be greater than 0 <= x but was {fbot}")
    if not (0 <= ftop): 
        raise ValueError(f"'ftop' must be greater than 0 <= x but was {ftop}")
    if not (8 <= ntap <= 2000): 
        raise ValueError(f"'ntap' must be between 8 <= x <= 2000 but was {ntap}")
    if alternative_band is not None and not (len(alternative_band) <= 2): 
        raise ValueError(f"Length of 'alternative_band' must be less than 2 but was {len(alternative_band)}")
    if alternative_ntap is not None and not (8 <= alternative_ntap <= 2000): 
        raise ValueError(f"'alternative_ntap' must be between 8 <= x <= 2000 but was {alternative_ntap}")
    execution = runner.start_execution(FIRDESIGN_METADATA)
    cargs = []
    cargs.append("FIRdesign")
    cargs.append("[OPTIONS]")
    cargs.append(str(fbot))
    cargs.append(str(ftop))
    cargs.append(str(ntap))
    ret = FirdesignOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIRDESIGN_METADATA",
    "FirdesignOutputs",
    "firdesign",
]

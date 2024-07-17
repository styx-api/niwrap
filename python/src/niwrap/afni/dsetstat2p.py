# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

DSETSTAT2P_METADATA = Metadata(
    id="6983800b039a4e48b10f7148db735976a03942b5",
    name="dsetstat2p",
)


class Dsetstat2pOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dsetstat2p(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output p-value or stat value"""


def dsetstat2p(
    dataset: str,
    statval: float | int,
    bisided: bool = False,
    two_sided: bool = False,
    one_sided: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> Dsetstat2pOutputs:
    """
    dsetstat2p by PA Taylor.
    
    Converts a statistic to a p-value with reference to a particular dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/README.attributes.html
    
    Args:
        dataset: Specify a dataset DDD and, if it has multiple sub-bricks, the\
            [i]th subbrick with the statistic of interest MUST be selected\
            explicitly; note the use of quotation marks around the brick selector\
            (because of the square-brackets). Note that 'i' can be either a number\
            of a string label selector.
        statval: Input stat-value S, which MUST be in the interval [0,\
            infinity).
        bisided: Choose one-sided or bi-sided/two-sided testing.
        two_sided: Choose one-sided or bi-sided/two-sided testing.
        one_sided: Choose one-sided or bi-sided/two-sided testing.
        quiet: An optional flag so that output ONLY the final statistic value\
            output to standard output; this can be then be viewed, redirected to a\
            text file or saved as a shell variable. (Default: display supplementary\
            text.).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Dsetstat2pOutputs`).
    """
    runner = runner or get_global_runner()
    if not (0 <= statval): 
        raise ValueError(f"'statval' must be greater than 0 <= x but was {statval}")
    execution = runner.start_execution(DSETSTAT2P_METADATA)
    cargs = []
    cargs.append("dsetstat2p")
    cargs.append(dataset)
    cargs.append(str(statval))
    if one_sided:
        cargs.append("-1sided")
    if quiet:
        cargs.append("-quiet")
    ret = Dsetstat2pOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"output.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DSETSTAT2P_METADATA",
    "Dsetstat2pOutputs",
    "dsetstat2p",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MP_DIFFPOW_METADATA = Metadata(
    id="5d6f81008119f2f4a31e758201b79a4cc2a55918.boutiques",
    name="mp_diffpow",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MpDiffpowParameters = typing.TypedDict('MpDiffpowParameters', {
    "__STYX_TYPE__": typing.Literal["mp_diffpow"],
    "reg_file": InputPathType,
    "diff_reg_file": str,
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
        "mp_diffpow": mp_diffpow_cargs,
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
        "mp_diffpow": mp_diffpow_outputs,
    }.get(t)


class MpDiffpowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mp_diffpow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """File containing squared motion parameters, temporal difference of motion
    parameters, and squared differenced values."""


def mp_diffpow_params(
    reg_file: InputPathType,
    diff_reg_file: str,
) -> MpDiffpowParameters:
    """
    Build parameters.
    
    Args:
        reg_file: Input file containing registration parameters (e.g.,\
            regparam.dat).
        diff_reg_file: Output file with differenced registration parameters\
            (e.g., diffregparam.dat).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mp_diffpow",
        "reg_file": reg_file,
        "diff_reg_file": diff_reg_file,
    }
    return params


def mp_diffpow_cargs(
    params: MpDiffpowParameters,
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
    cargs.append("mp_diffpow.sh")
    cargs.append(execution.input_file(params.get("reg_file")))
    cargs.append(params.get("diff_reg_file"))
    return cargs


def mp_diffpow_outputs(
    params: MpDiffpowParameters,
    execution: Execution,
) -> MpDiffpowOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MpDiffpowOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("diff_reg_file")),
    )
    return ret


def mp_diffpow_execute(
    params: MpDiffpowParameters,
    execution: Execution,
) -> MpDiffpowOutputs:
    """
    Generates a file with specific motion parameter calculations useful for
    accounting for 'spin history' effects and other variations not accounted for by
    motion correction.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MpDiffpowOutputs`).
    """
    cargs = mp_diffpow_cargs(params, execution)
    ret = mp_diffpow_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def mp_diffpow(
    reg_file: InputPathType,
    diff_reg_file: str,
    runner: Runner | None = None,
) -> MpDiffpowOutputs:
    """
    Generates a file with specific motion parameter calculations useful for
    accounting for 'spin history' effects and other variations not accounted for by
    motion correction.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        reg_file: Input file containing registration parameters (e.g.,\
            regparam.dat).
        diff_reg_file: Output file with differenced registration parameters\
            (e.g., diffregparam.dat).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MpDiffpowOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MP_DIFFPOW_METADATA)
    params = mp_diffpow_params(reg_file=reg_file, diff_reg_file=diff_reg_file)
    return mp_diffpow_execute(params, execution)


__all__ = [
    "MP_DIFFPOW_METADATA",
    "MpDiffpowOutputs",
    "MpDiffpowParameters",
    "mp_diffpow",
    "mp_diffpow_params",
]

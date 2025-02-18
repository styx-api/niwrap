# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

POSSUM_INTERPMOT_METADATA = Metadata(
    id="8ab9d694fafa3b09d7acaca8ca43d500f9c7675b.boutiques",
    name="possum_interpmot",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PossumInterpmotParameters = typing.TypedDict('PossumInterpmotParameters', {
    "__STYX_TYPE__": typing.Literal["possum_interpmot"],
    "motion_type": int,
    "tr": float,
    "tr_slice": float,
    "nslices": int,
    "nvols": int,
    "custom_motion_file": InputPathType,
    "output_file": str,
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
        "possum_interpmot": possum_interpmot_cargs,
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
        "possum_interpmot": possum_interpmot_outputs,
    }.get(t)


class PossumInterpmotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum_interpmot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Interpolated motion output file"""


def possum_interpmot_params(
    motion_type: int,
    tr: float,
    tr_slice: float,
    nslices: int,
    nvols: int,
    custom_motion_file: InputPathType,
    output_file: str,
) -> PossumInterpmotParameters:
    """
    Build parameters.
    
    Args:
        motion_type: Type of motion: 0 for continuous, 1 for between slices, 2\
            for between volumes.
        tr: Repetition time in seconds.
        tr_slice: Slice repetition time in seconds.
        nslices: Number of slices.
        nvols: Number of volumes.
        custom_motion_file: Custom motion file.
        output_file: Output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "possum_interpmot",
        "motion_type": motion_type,
        "tr": tr,
        "tr_slice": tr_slice,
        "nslices": nslices,
        "nvols": nvols,
        "custom_motion_file": custom_motion_file,
        "output_file": output_file,
    }
    return params


def possum_interpmot_cargs(
    params: PossumInterpmotParameters,
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
    cargs.append("possum_interpmot.py")
    cargs.append(str(params.get("motion_type")))
    cargs.append(str(params.get("tr")))
    cargs.append(str(params.get("tr_slice")))
    cargs.append(str(params.get("nslices")))
    cargs.append(str(params.get("nvols")))
    cargs.append(execution.input_file(params.get("custom_motion_file")))
    cargs.append(params.get("output_file"))
    return cargs


def possum_interpmot_outputs(
    params: PossumInterpmotParameters,
    execution: Execution,
) -> PossumInterpmotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PossumInterpmotOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_file")),
    )
    return ret


def possum_interpmot_execute(
    params: PossumInterpmotParameters,
    execution: Execution,
) -> PossumInterpmotOutputs:
    """
    Position Interpolation for Movers and Shakers.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PossumInterpmotOutputs`).
    """
    cargs = possum_interpmot_cargs(params, execution)
    ret = possum_interpmot_outputs(params, execution)
    params = execution.params(params)
    execution.run(cargs)
    return ret


def possum_interpmot(
    motion_type: int,
    tr: float,
    tr_slice: float,
    nslices: int,
    nvols: int,
    custom_motion_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> PossumInterpmotOutputs:
    """
    Position Interpolation for Movers and Shakers.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        motion_type: Type of motion: 0 for continuous, 1 for between slices, 2\
            for between volumes.
        tr: Repetition time in seconds.
        tr_slice: Slice repetition time in seconds.
        nslices: Number of slices.
        nvols: Number of volumes.
        custom_motion_file: Custom motion file.
        output_file: Output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumInterpmotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_INTERPMOT_METADATA)
    params = possum_interpmot_params(motion_type=motion_type, tr=tr, tr_slice=tr_slice, nslices=nslices, nvols=nvols, custom_motion_file=custom_motion_file, output_file=output_file)
    return possum_interpmot_execute(params, execution)


__all__ = [
    "POSSUM_INTERPMOT_METADATA",
    "PossumInterpmotOutputs",
    "PossumInterpmotParameters",
    "possum_interpmot",
    "possum_interpmot_params",
]

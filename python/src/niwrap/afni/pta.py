# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PTA_METADATA = Metadata(
    id="35ec814148c0f395aac72042f68d0106977ad2da",
    name="PTA",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-pta:latest",
)


class PtaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pta(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stat_output: OutputPathType
    """Statistical evidence output of PTA"""
    prediction_output: OutputPathType
    """Predicted values and their standard errors"""


def pta(
    prefix: str,
    input_file: InputPathType,
    model_formula: str,
    vt_formulation: str | None = None,
    prediction_table: InputPathType | None = None,
    verbosity_level: float | int | None = None,
    response_var: str | None = None,
    dbg_args: bool = False,
    runner: Runner | None = None,
) -> PtaOutputs:
    """
    PTA by Gang Chen (gangchen@mail.nih.gov).
    
    Program for Profile Tracking Analysis - estimates nonlinear trajectories
    through smoothing splines.
    
    More information: https://afni.nimh.nih.gov/gangchen_homepage
    
    Args:
        prefix: Prefix for output files.
        input_file: Input data file in table format (data frame structure of\
            long format in R).
        model_formula: Model formulation through multilevel smoothing splines.
        vt_formulation: Specify varying smoothing terms. Two components are\
            required: the first one 'var' indicates the variable (e.g., subject)\
            around which the smoothing will vary while the second component\
            specifies the smoothing formulation (e.g., s(age,subject)).
        prediction_table: Data table to generate predicted values for graphical\
            illustration.
        verbosity_level: Verbosity level (0 for quiet, 1 or more for talkative).
        response_var: Column name designated as the response/outcome variable\
            (default is 'Y').
        dbg_args: Enable R to save parameters for debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PtaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PTA_METADATA)
    cargs = []
    cargs.append("PTA")
    cargs.extend(["-prefix", prefix])
    cargs.extend(["-input", execution.input_file(input_file)])
    cargs.extend(["-model", model_formula])
    if vt_formulation is not None:
        cargs.extend(["-vt", vt_formulation])
    if prediction_table is not None:
        cargs.extend(["-prediction", execution.input_file(prediction_table)])
    if verbosity_level is not None:
        cargs.extend(["-verb", str(verbosity_level)])
    if response_var is not None:
        cargs.extend(["-Y", response_var])
    if dbg_args:
        cargs.append("-dbgArgs")
    ret = PtaOutputs(
        root=execution.output_file("."),
        stat_output=execution.output_file(f"{prefix}-stat.txt"),
        prediction_output=execution.output_file(f"{prefix}-prediction.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PTA_METADATA",
    "PtaOutputs",
    "pta",
]

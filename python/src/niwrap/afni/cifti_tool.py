# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_TOOL_METADATA = Metadata(
    id="fc2e3e53992537d6ba3769a1e46c322268b0206f.boutiques",
    name="cifti_tool",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class CiftiToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output file for results"""


def cifti_tool(
    input_file: InputPathType,
    as_cext: bool = False,
    disp_cext: bool = False,
    eval_cext: bool = False,
    eval_type: typing.Literal["has_data", "has_bdata", "num_tokens", "show", "show_names", "show_summary", "show_text_data"] | None = None,
    output_file: str | None = None,
    verbose_level: float | None = None,
    verbose_read_level: float | None = None,
    both_verbose_levels: float | None = None,
    runner: Runner | None = None,
) -> CiftiToolOutputs:
    """
    Example tool for reading/writing CIFTI-2 datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Specify input dataset.
        as_cext: Process the input as just an extension.
        disp_cext: Display the CIFTI extension.
        eval_cext: Evaluate the CIFTI extension.
        eval_type: Method for evaluation of axml elements.
        output_file: Where to write output.
        verbose_level: Set the verbose level.
        verbose_read_level: Set verbose level when reading.
        both_verbose_levels: Apply both -verb options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_TOOL_METADATA)
    cargs = []
    cargs.append("cifti_tool")
    cargs.append("-input")
    cargs.extend([
        "-input",
        execution.input_file(input_file)
    ])
    if as_cext:
        cargs.append("-as_cext")
    if disp_cext:
        cargs.append("-disp_cext")
    if eval_cext:
        cargs.append("-eval_cext")
    if eval_type is not None:
        cargs.extend([
            "-eval_type",
            eval_type
        ])
    cargs.append("-output")
    if output_file is not None:
        cargs.extend([
            "-output",
            output_file
        ])
    if verbose_level is not None:
        cargs.extend([
            "-verb",
            str(verbose_level)
        ])
    if verbose_read_level is not None:
        cargs.extend([
            "-verb_read",
            str(verbose_read_level)
        ])
    if both_verbose_levels is not None:
        cargs.extend([
            "-vboth",
            str(both_verbose_levels)
        ])
    ret = CiftiToolOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_file) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_TOOL_METADATA",
    "CiftiToolOutputs",
    "cifti_tool",
]

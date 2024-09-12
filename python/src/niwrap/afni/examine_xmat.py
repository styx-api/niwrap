# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EXAMINE_XMAT_METADATA = Metadata(
    id="eb70a859747a89594f1ce12cba7e48ea86cfea01.boutiques",
    name="ExamineXmat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ExamineXmatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `examine_xmat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    plot_image: OutputPathType | None
    """Output plot image"""
    plot_image_png: OutputPathType | None
    """Output plot image"""
    plot_image_pdf: OutputPathType | None
    """Output plot image"""
    cor_image: OutputPathType | None
    """Output cor image"""
    plot_image_prefix: OutputPathType | None
    """Output plot image"""


def examine_xmat(
    input_file: InputPathType | None = None,
    interactive: bool = False,
    prefix: str | None = None,
    cprefix: str | None = None,
    pprefix: str | None = None,
    select_: str | None = None,
    msg_trace: bool = False,
    verbosity: float | None = None,
    runner: Runner | None = None,
) -> ExamineXmatOutputs:
    """
    A program for examining the design matrix generated by 3dDeconvolve.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/ExamineXmat.html
    
    Args:
        input_file: xmat file to plot.
        interactive: Run ExamineXmat in interactive mode. This is the default\
            if -prefix is not given. If -interactive is used with -prefix, the last\
            plot you see is the plot saved to file.
        prefix: Prefix of plot image and cor image.
        cprefix: Prefix of cor image only.
        pprefix: Prefix of plot image only.
        select_: What to plot. Selection strings to specify regressors.
        msg_trace: Output trace information along with errors and notices.
        verbosity: Verbosity level. 0 for quiet, 1 or more for talkative.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExamineXmatOutputs`).
    """
    if verbosity is not None and not (0 <= verbosity): 
        raise ValueError(f"'verbosity' must be greater than 0 <= x but was {verbosity}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXAMINE_XMAT_METADATA)
    cargs = []
    cargs.append("ExamineXmat")
    if input_file is not None:
        cargs.extend([
            "-input",
            execution.input_file(input_file)
        ])
    if interactive:
        cargs.append("-interactive")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if cprefix is not None:
        cargs.extend([
            "-cprefix",
            cprefix
        ])
    if pprefix is not None:
        cargs.extend([
            "-pprefix",
            pprefix
        ])
    if select_ is not None:
        cargs.extend([
            "-select",
            select_
        ])
    if msg_trace:
        cargs.append("-msg.trace")
    if verbosity is not None:
        cargs.extend([
            "-verb",
            str(verbosity)
        ])
    ret = ExamineXmatOutputs(
        root=execution.output_file("."),
        plot_image=execution.output_file(prefix + ".jpg") if (prefix is not None) else None,
        plot_image_png=execution.output_file(prefix + ".png") if (prefix is not None) else None,
        plot_image_pdf=execution.output_file(prefix + ".pdf") if (prefix is not None) else None,
        cor_image=execution.output_file(cprefix + ".jpg") if (cprefix is not None) else None,
        plot_image_prefix=execution.output_file(pprefix + ".jpg") if (pprefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EXAMINE_XMAT_METADATA",
    "ExamineXmatOutputs",
    "examine_xmat",
]

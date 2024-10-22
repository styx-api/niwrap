# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RCA_LONG_TP_INIT_METADATA = Metadata(
    id="58c8f81ab3bff88031a93bb937908f681bef1add.boutiques",
    name="rca-long-tp-init",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RcaLongTpInitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_long_tp_init(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_long_tp_init(
    timepoint: str,
    base: str,
    use_long_base_ctrl_vol: bool = False,
    hemisphere: typing.Literal["lh", "rh"] | None = None,
    expert_opts: InputPathType | None = None,
    subject: str | None = None,
    runner: Runner | None = None,
) -> RcaLongTpInitOutputs:
    """
    Initialize long timepoint subject for recon-all processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        timepoint: Timepoint identifier.
        base: Base identifier.
        use_long_base_ctrl_vol: Use long base control volume.
        hemisphere: Specify the hemisphere (left or right).
        expert_opts: Expert options file.
        subject: Subject identifier for testing; put after -long.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaLongTpInitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_LONG_TP_INIT_METADATA)
    cargs = []
    cargs.append("rca-long-tp-init")
    cargs.append("-long")
    cargs.append(timepoint)
    cargs.append(base)
    if use_long_base_ctrl_vol:
        cargs.append("-uselongbasectrlvol")
    if hemisphere is not None:
        cargs.extend([
            "-hemi",
            hemisphere
        ])
    if expert_opts is not None:
        cargs.extend([
            "-expert",
            execution.input_file(expert_opts)
        ])
    if subject is not None:
        cargs.extend([
            "-s",
            subject
        ])
    ret = RcaLongTpInitOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RCA_LONG_TP_INIT_METADATA",
    "RcaLongTpInitOutputs",
    "rca_long_tp_init",
]

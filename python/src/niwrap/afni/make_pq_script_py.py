# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_PQ_SCRIPT_PY_METADATA = Metadata(
    id="2e44222ffa661bbbd3fe92eb28fb4f0520058b65.boutiques",
    name="make_pq_script.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class MakePqScriptPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_pq_script_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    script: OutputPathType
    """Generated output script"""


def make_pq_script_py(
    dataset: InputPathType,
    brick_index: float,
    mask: InputPathType,
    out_script: str,
    runner: Runner | None = None,
) -> MakePqScriptPyOutputs:
    """
    Creates a script to compute p-value and q-value curves.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/make_pq_script.py.html
    
    Args:
        dataset: Input dataset (no sub-brick selectors).
        brick_index: Volume sub-brick for specific t-stat.
        mask: Mask volume dataset.
        out_script: Name for output script to write.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakePqScriptPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_PQ_SCRIPT_PY_METADATA)
    cargs = []
    cargs.append("make_pq_script.py")
    cargs.append(execution.input_file(dataset))
    cargs.append(str(brick_index))
    cargs.append(execution.input_file(mask))
    cargs.append(out_script)
    ret = MakePqScriptPyOutputs(
        root=execution.output_file("."),
        script=execution.output_file(out_script),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_PQ_SCRIPT_PY_METADATA",
    "MakePqScriptPyOutputs",
    "make_pq_script_py",
]

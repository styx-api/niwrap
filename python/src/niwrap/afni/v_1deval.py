# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1DEVAL_METADATA = Metadata(
    id="85746f16464c1cf7f5b18c6ee2681d2b46ccf2fb",
    name="1deval",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="brainlife/afni:latest",
)


class V1devalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1deval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_1_d: OutputPathType
    """Output of evaluated expression."""


def v_1deval(
    expression: str,
    del_: float | int | None = None,
    start: float | int | None = None,
    num: float | int | None = None,
    index: InputPathType | None = None,
    v_1_d: bool = False,
    symbols: list[InputPathType] | None = None,
    symbol_values: list[str] | None = None,
    runner: Runner | None = None,
) -> V1devalOutputs:
    """
    1deval by RW Cox.
    
    Evaluates an expression that may include columns of data from one or more
    text files and writes the result to stdout.
    
    More information: https://afni.nimh.nih.gov
    
    Args:
        expression: Expression to evaluate.
        del_: Use 'd' as the step for a single undetermined variable in the\
            expression.
        start: Start at value 's' for a single undetermined variable in the\
            expression.
        num: Evaluate the expression 'n' times.
        index: Read index column from file i.1D and write it out as 1st column\
            of output.
        v_1_d: Write output in the form of a single '1D:' string suitable for\
            input on the command line of another program.
        symbols: Read time series file and assign it to the symbol 'a'. Letters\
            'a' to 'z' may be used as symbols.
        symbol_values: Assign a fixed numerical value to the symbol 'a'.\
            Letters 'a' to 'z' may be used as symbols.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1devalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DEVAL_METADATA)
    cargs = []
    cargs.append("1deval")
    if del_ is not None:
        cargs.extend(["-del", str(del_)])
    if start is not None:
        cargs.extend(["-start", str(start)])
    if num is not None:
        cargs.extend(["-num", str(num)])
    if index is not None:
        cargs.extend(["-index", execution.input_file(index)])
    if v_1_d:
        cargs.append("-1D:")
    if symbols is not None:
        cargs.extend(["-a", *[execution.input_file(f) for f in symbols]])
    cargs.append("-expr")
    cargs.extend(["-expr", expression])
    ret = V1devalOutputs(
        root=execution.output_file("."),
        output_1_d=execution.output_file(f"output.1D", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1devalOutputs",
    "V_1DEVAL_METADATA",
    "v_1deval",
]

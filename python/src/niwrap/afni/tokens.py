# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TOKENS_METADATA = Metadata(
    id="b7eb83c68f44a8e1e5f94df55e43d6e53bb675ee.boutiques",
    name="tokens",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class TokensOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tokens(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tokens(
    infile: InputPathType | None = None,
    extra_char: list[str] | None = None,
    runner: Runner | None = None,
) -> TokensOutputs:
    """
    Token counting tool.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/tokens.html
    
    Args:
        infile: Specify input file (stdin if none).
        extra_char: Specify extra character to count as valid. Can be used more\
            than once.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TokensOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TOKENS_METADATA)
    cargs = []
    cargs.append("tokens")
    if infile is not None:
        cargs.extend([
            "-infile",
            execution.input_file(infile)
        ])
    if extra_char is not None:
        cargs.extend([
            "-extra",
            *extra_char
        ])
    ret = TokensOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TOKENS_METADATA",
    "TokensOutputs",
    "tokens",
]

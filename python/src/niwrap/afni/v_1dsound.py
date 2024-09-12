# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1DSOUND_METADATA = Metadata(
    id="f44e57b50ed08b06652bace730d6a8f1c13f54cd.boutiques",
    name="1dsound",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dsoundOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dsound(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output audio file."""


def v_1dsound(
    tsfile: InputPathType,
    prefix: str | None = None,
    encoding_8ulaw: bool = False,
    tper_option: float | None = None,
    notes_option: bool = False,
    despike_option: bool = False,
    play_option: bool = False,
    runner: Runner | None = None,
) -> V1dsoundOutputs:
    """
    Program to create a sound file from a 1D file (column of numbers).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dsound.html
    
    Args:
        tsfile: The input 1D time series file containing the data to transform\
            into sound.
        prefix: Prefix for the output filename, which will have '.au'\
            extension.
        encoding_8ulaw: Output in 8-bit mu-law encoding.
        tper_option: Time in seconds per time point in 'tsfile'. Allowed range\
            is 0.01 to 1.0 (inclusive). [default is 0.2s].
        notes_option: Output sound is a sequence of notes, low to high pitch\
            based on min to max in the input 1D file. Uses pentatonic scale.
        despike_option: Apply a simple despiking algorithm to avoid artifacts\
            from large/small values in the input.
        play_option: Plays the sound file after it is written.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dsoundOutputs`).
    """
    if tper_option is not None and not (0.01 <= tper_option <= 1.0): 
        raise ValueError(f"'tper_option' must be between 0.01 <= x <= 1.0 but was {tper_option}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DSOUND_METADATA)
    cargs = []
    cargs.append("1dsound")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if encoding_8ulaw:
        cargs.append("-8ulaw")
    if tper_option is not None:
        cargs.extend([
            "-tper",
            str(tper_option)
        ])
    if notes_option:
        cargs.append("-notes")
    if despike_option:
        cargs.append("-despike")
    if play_option:
        cargs.append("-play")
    cargs.append(execution.input_file(tsfile))
    ret = V1dsoundOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[PREFIX].au"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dsoundOutputs",
    "V_1DSOUND_METADATA",
    "v_1dsound",
]

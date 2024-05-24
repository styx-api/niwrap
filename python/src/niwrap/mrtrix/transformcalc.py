# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


TRANSFORMCALC_METADATA = Metadata(
    id="9e99fd568e51dd1a6a0c59040654e58e985e1de8",
    name="transformcalc",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TransformcalcConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class TransformcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `transformcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output transformation matrix."""


def transformcalc(
    inputs: list[str],
    operation: typing.Literal["operation"],
    output: InputPathType,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TransformcalcConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TransformcalcOutputs:
    """
    transformcalc by Max Pietsch (maximilian.pietsch@kcl.ac.uk).
    
    Perform calculations on linear transformation matrices.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/transformcalc.html
    
    Args:
        inputs: the input(s) for the specified operation
        operation: the operation to perform, one of: invert, half, rigid,
            header, average, interpolate, decompose, align_vertices_rigid,
            align_vertices_rigid_scale (see description section for details).
        output: the output transformation matrix.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `TransformcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRANSFORMCALC_METADATA)
    cargs = []
    cargs.append("transformcalc")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(["", *inputs])
    cargs.extend(["", operation])
    cargs.extend(["", execution.input_file(output)])
    ret = TransformcalcOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TRANSFORMCALC_METADATA",
    "TransformcalcConfig",
    "TransformcalcOutputs",
    "transformcalc",
]

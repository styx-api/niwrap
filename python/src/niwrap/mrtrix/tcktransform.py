# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


TCKTRANSFORM_METADATA = Metadata(
    id="5fb0bb168ed62fa78905a340d5410e4bf4dcd529",
    name="tcktransform",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TcktransformConfig:
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


class TcktransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tcktransform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track file"""


def tcktransform(
    tracks: InputPathType,
    transform: InputPathType,
    output: InputPathType,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TcktransformConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TcktransformOutputs:
    """
    tcktransform by J-Donald Tournier (jdtournier@gmail.com).
    
    Apply a spatial transformation to a tracks file.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tcktransform.html
    
    Args:
        tracks: the input track file.
        transform: the image containing the transform.
        output: the output track file
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
        NamedTuple of outputs (described in `TcktransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKTRANSFORM_METADATA)
    cargs = []
    cargs.append("tcktransform")
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
    cargs.extend(["", execution.input_file(tracks)])
    cargs.extend(["", execution.input_file(transform)])
    cargs.extend(["", execution.input_file(output)])
    ret = TcktransformOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKTRANSFORM_METADATA",
    "TcktransformConfig",
    "TcktransformOutputs",
    "tcktransform",
]

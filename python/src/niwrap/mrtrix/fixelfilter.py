# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


FIXELFILTER_METADATA = Metadata(
    id="a7529c0c66750af4b532674b5632cf33574b7319",
    name="fixelfilter",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class FixelfilterConfig:
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


class FixelfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fixelfilter(
    input_: str,
    filter_: typing.Literal["filter"],
    output: str,
    matrix: InputPathType,
    threshold_value: float | int | None = None,
    threshold_connectivity: float | int | None = None,
    fwhm: float | int | None = None,
    minweight: float | int | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelfilterConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> FixelfilterOutputs:
    """
    fixelfilter by Robert E. Smith (robert.smith@florey.edu.au).
    
    Perform filtering operations on fixel-based data.
    
    If the first input to the command is a specific fixel data file, then a
    filtered version of only that file will be generated by the command.
    Alternatively, if the input is the location of a fixel directory, then the
    command will create a duplicate of the fixel directory, and apply the
    specified filter operation to all fixel data files within the directory.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fixelfilter.html
    
    Args:
        input_: the input: either a fixel data file, or a fixel directory (see
            Description)
        filter_: the filtering operation to perform; options are: connect,
            smooth
        output: the output: either a fixel data file, or a fixel directory (see
            Description)
        matrix: provide a fixel-fixel connectivity matrix for filtering
            operations that require it
        threshold_value: specify a threshold for the input fixel data file
            values (default = 0.5)
        threshold_connectivity: specify a fixel-fixel connectivity threshold for
            connected-component analysis (default = 0.10000000000000001)
        fwhm: the full-width half-maximum (FWHM) of the spatial component of the
            smoothing filter (default = 10mm)
        minweight: apply a minimum threshold to smoothing weights (default =
            0.01)
        mask: only perform smoothing within a specified binary fixel mask
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
        NamedTuple of outputs (described in `FixelfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELFILTER_METADATA)
    cargs = []
    cargs.append("fixelfilter")
    cargs.extend(["-matrix", execution.input_file(matrix)])
    if threshold_value is not None:
        cargs.extend(["-threshold_value", str(threshold_value)])
    if threshold_connectivity is not None:
        cargs.extend(["-threshold_connectivity", str(threshold_connectivity)])
    if fwhm is not None:
        cargs.extend(["-fwhm", str(fwhm)])
    if minweight is not None:
        cargs.extend(["-minweight", str(minweight)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
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
    cargs.extend(["", input_])
    cargs.extend(["", filter_])
    cargs.extend(["", output])
    ret = FixelfilterOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXELFILTER_METADATA",
    "FixelfilterConfig",
    "FixelfilterOutputs",
    "fixelfilter",
]

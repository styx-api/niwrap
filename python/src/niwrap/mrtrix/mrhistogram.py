# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRHISTOGRAM_METADATA = Metadata(
    id="c7dfb67e2e501bcbba267491785f23b16d1adc85",
    name="mrhistogram",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrhistogramConfig:
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


class MrhistogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrhistogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    hist: OutputPathType
    """the output histogram file"""


def mrhistogram(
    image: InputPathType,
    hist: InputPathType,
    bins: int | None = None,
    template: InputPathType | None = None,
    mask: InputPathType | None = None,
    ignorezero: bool = False,
    allvolumes: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrhistogramConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrhistogramOutputs:
    """
    mrhistogram by Robert E. Smith (robert.smith@florey.edu.au).
    
    Generate a histogram of image intensities.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrhistogram.html
    
    Args:
        image: the input image from which the histogram will be computed
        hist: the output histogram file
        bins: Manually set the number of bins to use to generate the histogram.
        template: Use an existing histogram file as the template for histogram
            formation
        mask: Calculate the histogram only within a mask image.
        ignorezero: ignore zero-valued data during histogram construction.
        allvolumes: generate one histogram across all image volumes, rather than
            one per image volume
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
        NamedTuple of outputs (described in `MrhistogramOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRHISTOGRAM_METADATA)
    cargs = []
    cargs.append("mrhistogram")
    if bins is not None:
        cargs.extend(["-bins", str(bins)])
    if template is not None:
        cargs.extend(["-template", execution.input_file(template)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if ignorezero:
        cargs.append("-ignorezero")
    if allvolumes:
        cargs.append("-allvolumes")
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
    cargs.extend(["", execution.input_file(image)])
    cargs.extend(["", execution.input_file(hist)])
    ret = MrhistogramOutputs(
        root=execution.output_file("."),
        hist=execution.output_file(f"{pathlib.Path(hist).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRHISTOGRAM_METADATA",
    "MrhistogramConfig",
    "MrhistogramOutputs",
    "mrhistogram",
]

# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


V_5TT2VIS_METADATA = Metadata(
    id="bb692a9a3678ecee279e216cd2e258cce8ac783c",
    name="5tt2vis",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class V5tt2visConfig:
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


class V5tt2visOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_5tt2vis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output 3D image for visualisation"""


def v_5tt2vis(
    input_: InputPathType,
    output: InputPathType,
    bg: float | int | None = None,
    cgm: float | int | None = None,
    sgm: float | int | None = None,
    wm: float | int | None = None,
    csf: float | int | None = None,
    path: float | int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[V5tt2visConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> V5tt2visOutputs:
    """
    5tt2vis by Robert E. Smith (robert.smith@florey.edu.au).
    
    Generate an image for visualisation purposes from an ACT 5TT segmented
    anatomical image.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/5tt2vis.html
    
    Args:
        input_: the input 4D tissue-segmented image
        output: the output 3D image for visualisation
        bg: image intensity of background (default: 0)
        cgm: image intensity of cortical grey matter (default: 0.5)
        sgm: image intensity of sub-cortical grey matter (default: 0.75)
        wm: image intensity of white matter (default: 1)
        csf: image intensity of CSF (default: 0.15)
        path: image intensity of pathological tissue (default: 2)
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
        NamedTuple of outputs (described in `V5tt2visOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_5TT2VIS_METADATA)
    cargs = []
    cargs.append("5tt2vis")
    if bg is not None:
        cargs.extend(["-bg", str(bg)])
    if cgm is not None:
        cargs.extend(["-cgm", str(cgm)])
    if sgm is not None:
        cargs.extend(["-sgm", str(sgm)])
    if wm is not None:
        cargs.extend(["-wm", str(wm)])
    if csf is not None:
        cargs.extend(["-csf", str(csf)])
    if path is not None:
        cargs.extend(["-path", str(path)])
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
    cargs.extend(["", execution.input_file(input_)])
    cargs.extend(["", execution.input_file(output)])
    ret = V5tt2visOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V5tt2visConfig",
    "V5tt2visOutputs",
    "V_5TT2VIS_METADATA",
    "v_5tt2vis",
]

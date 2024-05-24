# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


TCKRESAMPLE_METADATA = Metadata(
    id="86fa3eefbc88d8c1bd99e382d350629c63c7cd4b",
    name="tckresample",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TckresampleLine:
    """
    resample tracks at 'num' equidistant locations along a line between 'start' and 'end' (specified as comma-separated 3-vectors in scanner coordinates)
    """
    num: int
    """resample tracks at 'num' equidistant locations along a line between
    'start' and 'end' (specified as comma-separated 3-vectors in scanner
    coordinates)"""
    start: list[float | int]
    """resample tracks at 'num' equidistant locations along a line between
    'start' and 'end' (specified as comma-separated 3-vectors in scanner
    coordinates)"""
    end: list[float | int]
    """resample tracks at 'num' equidistant locations along a line between
    'start' and 'end' (specified as comma-separated 3-vectors in scanner
    coordinates)"""
    
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
        cargs.append("-line")
        cargs.extend(["", str(self.num)])
        cargs.extend(["", *map(str, self.start)])
        cargs.extend(["", *map(str, self.end)])
        return cargs


@dataclasses.dataclass
class TckresampleArc:
    """
    resample tracks at 'num' equidistant locations along a circular arc specified by points 'start', 'mid' and 'end' (specified as comma-separated 3-vectors in scanner coordinates)
    """
    num: int
    """resample tracks at 'num' equidistant locations along a circular arc
    specified by points 'start', 'mid' and 'end' (specified as comma-separated
    3-vectors in scanner coordinates)"""
    start: list[float | int]
    """resample tracks at 'num' equidistant locations along a circular arc
    specified by points 'start', 'mid' and 'end' (specified as comma-separated
    3-vectors in scanner coordinates)"""
    mid: list[float | int]
    """resample tracks at 'num' equidistant locations along a circular arc
    specified by points 'start', 'mid' and 'end' (specified as comma-separated
    3-vectors in scanner coordinates)"""
    end: list[float | int]
    """resample tracks at 'num' equidistant locations along a circular arc
    specified by points 'start', 'mid' and 'end' (specified as comma-separated
    3-vectors in scanner coordinates)"""
    
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
        cargs.append("-arc")
        cargs.extend(["", str(self.num)])
        cargs.extend(["", *map(str, self.start)])
        cargs.extend(["", *map(str, self.mid)])
        cargs.extend(["", *map(str, self.end)])
        return cargs


@dataclasses.dataclass
class TckresampleConfig:
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


class TckresampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckresample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_tracks: OutputPathType
    """the output resampled tracks"""


def tckresample(
    in_tracks: InputPathType,
    out_tracks: InputPathType,
    upsample: int | None = None,
    downsample: int | None = None,
    step_size: float | int | None = None,
    num_points: int | None = None,
    endpoints: bool = False,
    line: TckresampleLine | None = None,
    arc: TckresampleArc | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckresampleConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TckresampleOutputs:
    """
    tckresample by Robert E. Smith (robert.smith@florey.edu.au) and J-Donald
    Tournier (jdtournier@gmail.com).
    
    Resample each streamline in a track file to a new set of vertices.
    
    It is necessary to specify precisely ONE of the command-line options for
    controlling how this resampling takes place; this may be either increasing
    or decreasing the number of samples along each streamline, or may involve
    changing the positions of the samples according to some specified
    trajectory.
    
    Note that because the length of a streamline is calculated based on the sums
    of distances between adjacent vertices, resampling a streamline to a new set
    of vertices will typically change the quantified length of that streamline;
    the magnitude of the difference will typically depend on the discrepancy in
    the number of vertices, with less vertices leading to a shorter length (due
    to taking chordal lengths of curved trajectories).
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tckresample.html
    
    Args:
        in_tracks: the input track file
        out_tracks: the output resampled tracks
        upsample: increase the density of points along the length of each
            streamline by some factor (may improve mapping streamlines to ROIs,
            and/or visualisation)
        downsample: increase the density of points along the length of each
            streamline by some factor (decreases required storage space)
        step_size: re-sample the streamlines to a desired step size (in mm)
        num_points: re-sample each streamline to a fixed number of points
        endpoints: only output the two endpoints of each streamline
        line: resample tracks at 'num' equidistant locations along a line
            between 'start' and 'end' (specified as comma-separated 3-vectors in
            scanner coordinates)
        arc: resample tracks at 'num' equidistant locations along a circular arc
            specified by points 'start', 'mid' and 'end' (specified as
            comma-separated 3-vectors in scanner coordinates)
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
        NamedTuple of outputs (described in `TckresampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKRESAMPLE_METADATA)
    cargs = []
    cargs.append("tckresample")
    if upsample is not None:
        cargs.extend(["-upsample", str(upsample)])
    if downsample is not None:
        cargs.extend(["-downsample", str(downsample)])
    if step_size is not None:
        cargs.extend(["-step_size", str(step_size)])
    if num_points is not None:
        cargs.extend(["-num_points", str(num_points)])
    if endpoints:
        cargs.append("-endpoints")
    if line is not None:
        cargs.extend(line.run(execution))
    if arc is not None:
        cargs.extend(arc.run(execution))
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
    cargs.extend(["", execution.input_file(in_tracks)])
    cargs.extend(["", execution.input_file(out_tracks)])
    ret = TckresampleOutputs(
        root=execution.output_file("."),
        out_tracks=execution.output_file(f"{pathlib.Path(out_tracks).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKRESAMPLE_METADATA",
    "TckresampleArc",
    "TckresampleConfig",
    "TckresampleLine",
    "TckresampleOutputs",
    "tckresample",
]

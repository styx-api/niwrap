# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_FIX_TOPOLOGY_METADATA = Metadata(
    id="4f9d60e228057441b5837a38b5a5b31e620a5eb4.boutiques",
    name="mris_fix_topology",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisFixTopologyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_fix_topology(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_fix_topology(
    subject_name: str,
    hemisphere: str,
    orig_name: str | None = "orig.nofix",
    sphere_name: str | None = "qsphere.nofix",
    inflated_name: str | None = "inflated.nofix",
    output_name: str | None = "orig",
    defect_base_name: str | None = "defect",
    write_fixed_inflated: bool = False,
    verbose: bool = False,
    verbose_low: bool = False,
    warnings_: bool = False,
    errors: bool = False,
    movies: bool = False,
    intersect: bool = False,
    mappings: bool = False,
    correct_defect: float | None = None,
    niters: float | None = None,
    genetic: bool = False,
    optimize: bool = False,
    random_: float | None = None,
    seed: float | None = None,
    diag: bool = False,
    mgz: bool = False,
    smooth: float | None = None,
    diagnostic_level: float | None = None,
    threads: float | None = None,
    runner: Runner | None = None,
) -> MrisFixTopologyOutputs:
    """
    Computes a mapping from the unit sphere onto the cortical surface, ensuring a
    topologically correct surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name.
        hemisphere: Hemisphere.
        orig_name: Input orig name (default is orig.nofix).
        sphere_name: Sphere name (default is qsphere.nofix).
        inflated_name: Inflated name (default is inflated.nofix).
        output_name: Output name (default is orig).
        defect_base_name: Defect basename (default is defect).
        write_fixed_inflated: Write fixed inflated.
        verbose: Increase verbosity.
        verbose_low: Low verbosity.
        warnings_: Show warnings.
        errors: Show errors.
        movies: Generate movies.
        intersect: Check if the final surface self-intersects.
        mappings: Generate several different mappings.
        correct_defect: Correct specific defect number.
        niters: Number of iterations for genetic algorithm.
        genetic: Use genetic search.
        optimize: Optimize genetic search.
        random_: Use random search with specified iterations.
        seed: Set random number generator seed.
        diag: Sets DIAG_SAVE_DIAGS.
        mgz: Assume volumes are in mgz format.
        smooth: Smooth corrected surface by N iterations.
        diagnostic_level: Set diagnostic level.
        threads: Set number of OpenMP threads.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisFixTopologyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_FIX_TOPOLOGY_METADATA)
    cargs = []
    cargs.append("mris_fix_topology")
    cargs.append(subject_name)
    cargs.append(hemisphere)
    if orig_name is not None:
        cargs.extend([
            "-orig",
            orig_name
        ])
    if sphere_name is not None:
        cargs.extend([
            "-sphere",
            sphere_name
        ])
    if inflated_name is not None:
        cargs.extend([
            "-inflated",
            inflated_name
        ])
    if output_name is not None:
        cargs.extend([
            "-out",
            output_name
        ])
    if defect_base_name is not None:
        cargs.extend([
            "-defect",
            defect_base_name
        ])
    if write_fixed_inflated:
        cargs.append("-wi")
    if verbose:
        cargs.append("-verbose")
    if verbose_low:
        cargs.append("-verbose_low")
    if warnings_:
        cargs.append("-warnings")
    if errors:
        cargs.append("-errors")
    if movies:
        cargs.append("-movies")
    if intersect:
        cargs.append("-intersect")
    if mappings:
        cargs.append("-mappings")
    if correct_defect is not None:
        cargs.extend([
            "-correct_defect",
            str(correct_defect)
        ])
    if niters is not None:
        cargs.extend([
            "-niters",
            str(niters)
        ])
    if genetic:
        cargs.append("-genetic")
    if optimize:
        cargs.append("-optimize")
    if random_ is not None:
        cargs.extend([
            "-random",
            str(random_)
        ])
    if seed is not None:
        cargs.extend([
            "-seed",
            str(seed)
        ])
    if diag:
        cargs.append("-diag")
    if mgz:
        cargs.append("-mgz")
    if smooth is not None:
        cargs.extend([
            "-s",
            str(smooth)
        ])
    if diagnostic_level is not None:
        cargs.extend([
            "-v",
            str(diagnostic_level)
        ])
    if threads is not None:
        cargs.extend([
            "-threads",
            str(threads)
        ])
    ret = MrisFixTopologyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_FIX_TOPOLOGY_METADATA",
    "MrisFixTopologyOutputs",
    "mris_fix_topology",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_FIX_FSSPHERE_METADATA = Metadata(
    id="562366f0e1751b624c37f952f68eaf166d6837d7",
    name="@fix_FSsphere",
)


class FixFssphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_fix_fssphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_surface: OutputPathType
    """Corrected surface"""


def _fix_fssphere(
    spec_file: InputPathType,
    sphere_file: InputPathType,
    num_iterations: int | None = None,
    extent_lim: float | int | None = None,
    project_first: bool = False,
    keep_temp: bool = False,
    runner: Runner | None = None,
) -> FixFssphereOutputs:
    """
    @fix_FSsphere by Unknown.
    
    Tool for fixing errors in FreeSurfer spherical surfaces.
    
    Args:
        spec_file: Spec file.
        sphere_file: SPHERE.asc is the sphere to be used.
        num_iterations: Number of local smoothing operations. Default is 3000.
        extent_lim: Extent, in mm, by which troubled sections are fattened.\
            Default is 6.
        project_first: Project to a sphere, before smoothing. Default is 0.
        keep_temp: Keep temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FixFssphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_FIX_FSSPHERE_METADATA)
    cargs = []
    cargs.append("@fix_FSsphere")
    cargs.append("<-spec")
    cargs.append("SPEC>")
    cargs.append("<-sphere")
    cargs.append("SPHERE.asc>")
    cargs.append("[-niter")
    cargs.append("NITER]")
    cargs.append("[-lim")
    cargs.append("LIM]")
    cargs.append("[-keep_temp]")
    cargs.append("[-project_first]")
    ret = FixFssphereOutputs(
        root=execution.output_file("."),
        corrected_surface=execution.output_file(f"[SPHERE]_fxd.asc"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FixFssphereOutputs",
    "_FIX_FSSPHERE_METADATA",
    "_fix_fssphere",
]

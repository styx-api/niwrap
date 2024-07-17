# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SUMA_METADATA = Metadata(
    id="c106091bed062058a8781e3c2d3f907a6c28a7d9",
    name="suma",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class SumaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `suma(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def suma(
    spec_file: InputPathType | None = None,
    surf_vol: InputPathType | None = None,
    afni_host: str | None = None,
    niml: bool = False,
    noniml: bool = False,
    surface_file: InputPathType | None = None,
    surface_type: str | None = None,
    cifti_dataset: InputPathType | None = None,
    graph_dataset: InputPathType | None = None,
    tractography_dataset: InputPathType | None = None,
    volume: InputPathType | None = None,
    onestate: bool = False,
    anatomical: bool = False,
    linear_depth: float | int | None = None,
    recursive_depth: float | int | None = None,
    novolreg: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    port_offset: float | int | None = None,
    port_offset_bloc: float | int | None = None,
    drive_command: str | None = None,
    clipping_plane_verbose: float | int | None = None,
    runner: Runner | None = None,
) -> SumaOutputs:
    """
    suma by Ziad S. Saad, Peter D. Lauren SSCC/NIMH/NIH.
    
    SUMA: Surface Mapper for visualization and analysis of brain data.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/suma.html
    
    Args:
        spec_file: Surface specification file.
        surf_vol: Anatomical volume used in creating the surface and registered\
            to the current experiment's anatomical volume.
        afni_host: Name or IP address of the computer running AFNI.
        niml: Start listening for communications with NIML-formatted elements.
        noniml: Do not start listening for communications with NIML-formatted\
            elements.
        surface_file: Path to the surface file.
        surface_type: Specify a surface type (e.g. fs, sf, vec, ply, stl, mni,\
            byu, bv, dx, gii, obj).
        cifti_dataset: CIFTI dataset to display.
        graph_dataset: Graph dataset to display.
        tractography_dataset: Tractography dataset to display.
        volume: Volume to display.
        onestate: Make all -i_* surfaces have the same state.
        anatomical: Label all -i surfaces as anatomically correct.
        linear_depth: Specify a standard-mesh sphere through linear depth.
        recursive_depth: Specify a standard-mesh sphere through recursive\
            depth.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations.
        setenv: Set environment variable.
        trace_: Use debugging options for SUMA.
        extreme_trace: Use extreme debugging options for SUMA.
        nomall: Ignore memory tracing options for SUMA.
        yesmall: Use memory tracing options for SUMA.
        port_offset: Specify the port offset for SUMA.
        port_offset_bloc: Provide port offset bloc for SUMA.
        drive_command: Drive SUMA with a specific command.
        clipping_plane_verbose: Provide verbose output in clipping plane mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SumaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUMA_METADATA)
    cargs = []
    cargs.append("suma")
    cargs.append("[MODE]")
    cargs.append("[OPTIONS]")
    ret = SumaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SUMA_METADATA",
    "SumaOutputs",
    "suma",
]

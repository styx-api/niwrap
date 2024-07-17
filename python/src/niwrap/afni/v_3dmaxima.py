# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DMAXIMA_METADATA = Metadata(
    id="135dc5292ce09d0c1f645355d93f6ce24f5e6f5a",
    name="3dmaxima",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="your-container-image",
)


class V3dmaximaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaxima(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask: OutputPathType | None
    """Output mask dataset with extrema locations"""


def v_3dmaxima(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    threshold: float | int | None = None,
    min_dist: float | int | None = None,
    out_rad: float | int | None = None,
    input_flag: bool = False,
    spheres_1_flag: bool = False,
    spheres_1to_n_flag: bool = False,
    spheres_nto1_flag: bool = False,
    neg_ext_flag: bool = False,
    true_max_flag: bool = False,
    dset_coords_flag: bool = False,
    no_text_flag: bool = False,
    coords_only_flag: bool = False,
    n_style_sort_flag: bool = False,
    n_style_weight_ave_flag: bool = False,
    debug_level: float | int | None = None,
    help_flag: bool = False,
    hist_flag: bool = False,
    ver_flag: bool = False,
    runner: Runner | None = None,
) -> V3dmaximaOutputs:
    """
    3dmaxima by R Reynolds.
    
    Locate extrema in a functional dataset.
    
    Args:
        input_dataset: Specify input dataset (e.g. func+orig'[7]').
        output_prefix: Prefix for an output mask dataset (e.g. -prefix\
            maskNto1).
        threshold: Provides a cutoff value for extrema (e.g. -thresh 17.4).
        min_dist: Minimum acceptable distance between extrema in voxels (e.g.\
            -min_dist 4).
        out_rad: Set the output radius around extrema voxels in voxel units\
            (e.g. -out_rad 9).
        input_flag: Specify input dataset (e.g. -input func+orig'[7]').
        spheres_1_flag: Set all output values to 1.
        spheres_1to_n_flag: Output values will range from 1 to N.
        spheres_nto1_flag: Output values will range from N to 1.
        neg_ext_flag: Search for negative extrema (minima).
        true_max_flag: Extrema may not have equal neighbors.
        dset_coords_flag: Display output in the dataset orientation.
        no_text_flag: Do not display the extrema points as text.
        coords_only_flag: Only output coordinates (no text or values).
        n_style_sort_flag: Use 'Sort-n-Remove' style (default).
        n_style_weight_ave_flag: Use 'Weighted-Average' style.
        debug_level: Output extra information to the terminal (e.g. -debug 2).
        help_flag: Display help information.
        hist_flag: Display module history.
        ver_flag: Display version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaximaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMAXIMA_METADATA)
    cargs = []
    cargs.append("3dmaxima")
    cargs.append(execution.input_file(input_dataset))
    if output_prefix is not None:
        cargs.extend(["-prefix", output_prefix])
    if threshold is not None:
        cargs.extend(["-thresh", str(threshold)])
    if min_dist is not None:
        cargs.extend(["-min_dist", str(min_dist)])
    if out_rad is not None:
        cargs.extend(["-out_rad", str(out_rad)])
    if input_flag:
        cargs.append("-input")
    if spheres_1_flag:
        cargs.append("-spheres_1")
    if spheres_1to_n_flag:
        cargs.append("-spheres_1toN")
    if spheres_nto1_flag:
        cargs.append("-spheres_Nto1")
    if neg_ext_flag:
        cargs.append("-neg_ext")
    if true_max_flag:
        cargs.append("-true_max")
    if dset_coords_flag:
        cargs.append("-dset_coords")
    if no_text_flag:
        cargs.append("-no_text")
    if coords_only_flag:
        cargs.append("-coords_only")
    if n_style_sort_flag:
        cargs.append("-n_style_sort")
    if n_style_weight_ave_flag:
        cargs.append("-n_style_weight_ave")
    if debug_level is not None:
        cargs.extend(["-debug", str(debug_level)])
    if help_flag:
        cargs.append("-help")
    if hist_flag:
        cargs.append("-hist")
    if ver_flag:
        cargs.append("-ver")
    ret = V3dmaximaOutputs(
        root=execution.output_file("."),
        output_mask=execution.output_file(f"{output_prefix}_mask+orig.[HEAD | BRIK]", optional=True) if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmaximaOutputs",
    "V_3DMAXIMA_METADATA",
    "v_3dmaxima",
]

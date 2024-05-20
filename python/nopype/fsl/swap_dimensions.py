# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SWAP_DIMENSIONS_METADATA = Metadata(
    id="33d08885dfdcaa07b997128f89ff9b23447bb9dd",
    name="SwapDimensions",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SwapDimensionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swap_dimensions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file_outfile: OutputPathType | None
    """Output name of image, if not provided, writes to standard output."""


def swap_dimensions(
    runner: Runner,
    in_file: InputPathType,
    x_dims_cart: typing.Literal["x", "-x", "y", "-y", "z", "-z"] | None = None,
    y_dims_cart: typing.Literal["x", "-x", "y", "-y", "z", "-z"] | None = None,
    z_dims_cart: typing.Literal["x", "-x", "y", "-y", "z", "-z"] | None = None,
    x_dims_ras: typing.Literal["LR", "RL", "AP", "PA", "SI", "IS"] | None = None,
    y_dims_ras: typing.Literal["LR", "RL", "AP", "PA", "SI", "IS"] | None = None,
    z_dims_ras: typing.Literal["LR", "RL", "AP", "PA", "SI", "IS"] | None = None,
    out_file: str | None = None,
) -> SwapDimensionsOutputs:
    """
    this is an advanced tool that re-orders the data storage to permit changes
    between axial, sagittal and coronal slicing. When used in this mode the same
    left-right convention (also called coordinate handedness or
    radiological/neurological convention) will be maintained as long as no warning
    is printed.
    
    Args:
        runner: Command runner
        in_file: Input image to swap dimensions of
        x_dims_cart: Representation of new x axes in terms of old cartesian
            axes.
        y_dims_cart: Representation of new y axes in terms of old cartesian
            axes.
        z_dims_cart: Representation of new z axes in terms of old cartesian
            axes.
        x_dims_ras: Representation of new x axes in terms of old anatomical
            axes.
        y_dims_ras: Representation of new y axes in terms of old anatomical
            axes.
        z_dims_ras: Representation of new z axes in terms of old anatomical
            axes.
        out_file: Output name of image, if not provided, writes to standard
            output.
    Returns:
        NamedTuple of outputs (described in `SwapDimensionsOutputs`).
    """
    if (
        (x_dims_cart is not None) +
        (x_dims_ras is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "x_dims_cart,\n"
            "x_dims_ras"
        )
    if not (
        (x_dims_cart is not None) or
        (x_dims_ras is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- x_dims_cart\n"
            "- x_dims_ras"
        )
    if (
        (y_dims_cart is not None) +
        (y_dims_ras is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "y_dims_cart,\n"
            "y_dims_ras"
        )
    if not (
        (y_dims_cart is not None) or
        (y_dims_ras is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- y_dims_cart\n"
            "- y_dims_ras"
        )
    if (
        (z_dims_cart is not None) +
        (z_dims_ras is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "z_dims_cart,\n"
            "z_dims_ras"
        )
    if not (
        (z_dims_cart is not None) or
        (z_dims_ras is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- z_dims_cart\n"
            "- z_dims_ras"
        )
    execution = runner.start_execution(SWAP_DIMENSIONS_METADATA)
    cargs = []
    cargs.append("fslswapdim")
    cargs.append(execution.input_file(in_file))
    if x_dims_cart is not None:
        cargs.append(x_dims_cart)
    if x_dims_ras is not None:
        cargs.append(x_dims_ras)
    if y_dims_ras is not None:
        cargs.append(y_dims_ras)
    cargs.append("[B_RAS]")
    if z_dims_cart is not None:
        cargs.append(z_dims_cart)
    if z_dims_ras is not None:
        cargs.append(z_dims_ras)
    if out_file is not None:
        cargs.append(out_file)
    ret = SwapDimensionsOutputs(
        root=execution.output_file("."),
        out_file_outfile=execution.output_file(f"{out_file}", optional=True) if out_file is not None else None,
    )
    execution.run(cargs)
    return ret

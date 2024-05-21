# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


APPLY_TRANSFORMS_METADATA = Metadata(
    id="268cd966e05b235ee4033293179ef628c694c196",
    name="ApplyTransforms",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ApplyTransformsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apply_transforms(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_outfile: OutputPathType | None
    """Warped image."""


def apply_transforms(
    runner: Runner,
    input_image: InputPathType,
    reference_image: InputPathType,
    transforms: list[InputPathType],
    default_value: float | int | None = 0.0,
    dimension: typing.Literal[2, 3, 4] | None = None,
    float_: bool = False,
    input_image_type: typing.Literal[0, 1, 2, 3] | None = None,
    interpolation: typing.Literal["Linear", "NearestNeighbor", "CosineWindowedSinc", "WelchWindowedSinc", "HammingWindowedSinc", "LanczosWindowedSinc", "MultiLabel", "Gaussian", "BSpline"] | None = "Linear",
    interpolation_parameters: list[str] = None,
    interpolation_parameters_2: list[str] = None,
    invert_transform_flags: list[InputPathType] = None,
    num_threads: int | None = 1,
    out_postfix: str | None = "_trans",
    output_image: str | None = None,
    print_out_composite_warp_file: bool = False,
) -> ApplyTransformsOutputs:
    """
    ApplyTransforms by Nipype (interface).
    
    ApplyTransforms, applied to an input image, transforms it according to a
    reference image and a transform (or a set of transforms).
    
    Args:
        runner: Command runner
        input_image: Image to apply transformation to (generally a coregistered
            functional).
        reference_image: Reference image space that you wish to warp into.
        transforms: A list of items which are file or string or 'identity'.
            Transform files: will be applied in reverse order. for example, the last
            specified transform will be applied first.
        default_value: No description provided.
        dimension: 2 or 3 or 4. This option forces the image to be treated as a
            specified-dimensional image. if not specified, antswarp tries to infer
            the dimensionality from the input image.
        float_: Use float instead of double for computations.
        input_image_type: 0 or 1 or 2 or 3. Option specifying the input image
            type of scalar (default), vector, tensor, or time series.
        interpolation: 'linear' or 'nearestneighbor' or 'cosinewindowedsinc' or
            'welchwindowedsinc' or 'hammingwindowedsinc' or 'lanczoswindowedsinc' or
            'multilabel' or 'gaussian' or 'bspline'. No description provided.
        interpolation_parameters: (an integer) or a tuple of the form: (a float,
            a float). No description provided.
        interpolation_parameters_2: (an integer) or a tuple of the form: (a
            float, a float). No description provided.
        invert_transform_flags: A list of items which are a boolean. No
            description provided.
        num_threads: Number of itk threads to use.
        out_postfix: Postfix that is appended to all output files (default =
            _trans).
        output_image: Output file name.
        print_out_composite_warp_file: Output a composite warp file instead of a
            transformed image.
    Returns:
        NamedTuple of outputs (described in `ApplyTransformsOutputs`).
    """
    if (
        (interpolation_parameters is not None) +
        (interpolation_parameters_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "interpolation_parameters,\n"
            "interpolation_parameters_2"
        )
    execution = runner.start_execution(APPLY_TRANSFORMS_METADATA)
    cargs = []
    cargs.append("ApplyTransforms")
    if default_value is not None:
        cargs.extend(["--default-value", str(default_value)])
    if dimension is not None:
        cargs.extend(["--dimensionality", str(dimension)])
    if float_:
        cargs.append("--float")
    cargs.extend(["--input", execution.input_file(input_image)])
    if input_image_type is not None:
        cargs.extend(["--input-image-type", str(input_image_type)])
    if interpolation is not None:
        cargs.append(interpolation)
    if interpolation_parameters_2 is not None:
        cargs.extend(interpolation_parameters_2)
    if invert_transform_flags is not None:
        cargs.extend([execution.input_file(f) for f in invert_transform_flags])
    if num_threads is not None:
        cargs.append(str(num_threads))
    if out_postfix is not None:
        cargs.append(out_postfix)
    if output_image is not None:
        cargs.extend(["--output", output_image])
    if print_out_composite_warp_file:
        cargs.append("--print_out_composite_warp_file")
    cargs.extend(["--reference-image", execution.input_file(reference_image)])
    cargs.extend([execution.input_file(f) for f in transforms])
    ret = ApplyTransformsOutputs(
        root=execution.output_file("."),
        output_image_outfile=execution.output_file(f"{output_image}", optional=True) if output_image is not None else None,
    )
    execution.run(cargs)
    return ret

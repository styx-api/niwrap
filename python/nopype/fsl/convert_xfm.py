# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.895009

import typing

from ..styxdefs import *


CONVERT_XFM_METADATA = Metadata(
    id="222f751c82f9bc46bed0e86abade5828223e11ff",
    name="convert_xfm",
    container_image_type="docker",
    container_image_tag="fcp-indi/c-pac:nightly",
)


class ConvertXfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_xfm(...)`.
    """
    output_trasnformation: OutputPathType
    """Output transformation matrix."""


def convert_xfm(
    runner: Runner,
    in_file: InputPathType,
    concat_xfm: InputPathType | None = None,
    fix_scale_skew: InputPathType | None = None,
    invert_xfm: bool = False,
    out_file: InputPathType | None = None,
) -> ConvertXfmOutputs:
    """
    convert_xfm, as implemented in Nipype (module: nipype.interfaces.fsl.utils,
    interface: ConvertXFM). Use the FSL utility convert_xfm to modify FLIRT
    transformation matrices.
    
    Args:
        runner: Command runner
        in_file: Input transformation matrix.
        concat_xfm: A File. Write joint transformation of two input matrices.
        fix_scale_skew: A File. Use secondary matrix to fix scale and skew.
        invert_xfm: Invert input transformation.
        out_file: Final transformation matrix.
    Returns:
        NamedTuple of outputs (described in `ConvertXfmOutputs`).
    """
    if (
        invert_xfm +
        (fix_scale_skew is not None) +
        (concat_xfm is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "invert_xfm,\n"
            "fix_scale_skew,\n"
            "concat_xfm"
        )
    execution = runner.start_execution(CONVERT_XFM_METADATA)
    cargs = []
    cargs.append("convert_xfm")
    cargs.append(execution.input_file(in_file))
    if invert_xfm:
        cargs.append("-inverse")
    if concat_xfm is not None:
        cargs.extend(["-concat", execution.input_file(concat_xfm)])
    if fix_scale_skew is not None:
        cargs.extend(["-fixscaleskew", execution.input_file(fix_scale_skew)])
    if out_file is not None:
        cargs.extend(["-omat", execution.input_file(out_file)])
    ret = ConvertXfmOutputs(
        output_trasnformation=execution.output_file(f"{out_file}"),
    )
    execution.run(cargs)
    return ret

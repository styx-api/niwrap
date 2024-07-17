# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_TOY_PROG_METADATA = Metadata(
    id="92c21394694110b7a20bb2f4200e6486e823543c",
    name="3dToyProg",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni:latest",
)


class V3dToyProgOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_toy_prog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_toy_prog(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    mask_dataset: InputPathType | None = None,
    output_datum: typing.Literal["float", "short"] | None = None,
    mini_help: bool = False,
    help_: bool = False,
    extreme_help: bool = False,
    help_view: bool = False,
    help_web: bool = False,
    help_find: str | None = None,
    help_raw: bool = False,
    help_spx: bool = False,
    help_aspx: bool = False,
    help_all_opts: bool = False,
    runner: Runner | None = None,
) -> V3dToyProgOutputs:
    """
    3dToyProg by AFNI (Analysis of Functional NeuroImages) Development Team.
    
    A program to illustrate dataset creation and manipulation in C using AFNI's
    API.
    
    Args:
        input_dataset: Reference dataset.
        output_prefix: Prefix of the output datasets.
        mask_dataset: Restrict analysis to non-zero voxels in the mask dataset.
        output_datum: Output datum type for one of the datasets. Choose from\
            'float' or 'short'. Default is 'float'.
        mini_help: Mini help, at time, same as -help in many cases.
        help_: The entire help output.
        extreme_help: Extreme help, same as -help in majority of cases.
        help_view: Open help in text editor. AFNI will try to find a GUI editor\
            on your machine. You can control which it should use by setting\
            environment variable AFNI_GUI_EDITOR.
        help_web: Open help in web browser. AFNI will try to find a browser on\
            your machine. You can control which it should use by setting\
            environment variable AFNI_GUI_EDITOR.
        help_find: Look for lines in this program's -help output that match\
            (approximately) WORD.
        help_raw: Help string unedited.
        help_spx: Help string in sphinx loveliness, but do not try to\
            autoformat.
        help_aspx: Help string in sphinx with autoformatting of options, etc.
        help_all_opts: Try to identify all options for the program from the\
            output of its -help option. Some options might be missed and others\
            misidentified. Use this output for hints only.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dToyProgOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TOY_PROG_METADATA)
    cargs = []
    cargs.append("3dToyProg")
    cargs.extend(["-input", execution.input_file(input_dataset)])
    if output_prefix is not None:
        cargs.extend(["-prefix", output_prefix])
    if mask_dataset is not None:
        cargs.extend(["-mask", execution.input_file(mask_dataset)])
    if output_datum is not None:
        cargs.extend(["-datum", output_datum])
    ret = V3dToyProgOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dToyProgOutputs",
    "V_3D_TOY_PROG_METADATA",
    "v_3d_toy_prog",
]

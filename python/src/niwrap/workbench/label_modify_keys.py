# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

LABEL_MODIFY_KEYS_METADATA = Metadata(
    id="c18c1365a6156f60ad4a4e0699070a74f756e0e2",
    name="label-modify-keys",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class LabelModifyKeysOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_modify_keys(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """output label file"""


def label_modify_keys(
    label_in: InputPathType,
    remap_file: str,
    label_out: str,
    opt_column_column: str | None = None,
    runner: Runner = None,
) -> LabelModifyKeysOutputs:
    """
    label-modify-keys by Washington University School of Medicin.
    
    Change key values in a label file.
    
    <remap-file> should have lines of the form 'oldkey newkey', like so:
    
    3 5
    5 8
    8 2
    
    This would change the current label with key '3' to use the key '5' instead,
    5 would use 8, and 8 would use 2. Any collision in key values results in the
    label that was not specified in the remap file getting remapped to an
    otherwise unused key. Remapping more than one key to the same new key, or
    the same key to more than one new key, results in an error. This will not
    change the appearance of the file when displayed, as it will change the key
    values in the data at the same time.
    
    Args:
        label_in: the input label file.
        remap_file: text file with old and new key values.
        label_out: output label file.
        opt_column_column: select a single column to use: the column number or\
            name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelModifyKeysOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MODIFY_KEYS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-modify-keys")
    cargs.append(execution.input_file(label_in))
    cargs.append(remap_file)
    cargs.append(label_out)
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = LabelModifyKeysOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{label_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_MODIFY_KEYS_METADATA",
    "LabelModifyKeysOutputs",
    "label_modify_keys",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CIFTI_LABEL_MODIFY_KEYS_METADATA = Metadata(
    id="27924c8949337f2c008cf83af99fa3aaa7226a2a",
    name="cifti-label-modify-keys",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiLabelModifyKeysOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_modify_keys(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output dlabel file"""


def cifti_label_modify_keys(
    cifti_in: InputPathType,
    remap_file: str,
    cifti_out: str,
    opt_column_column: str | None = None,
    runner: Runner = None,
) -> CiftiLabelModifyKeysOutputs:
    """
    cifti-label-modify-keys by Washington University School of Medicin.
    
    Change key values in a dlabel file.
    
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
        cifti_in: the input dlabel file.
        remap_file: text file with old and new key values.
        cifti_out: the output dlabel file.
        opt_column_column: select a single column to use: the column number or\
            name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelModifyKeysOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_MODIFY_KEYS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-modify-keys")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(remap_file)
    cargs.append(cifti_out)
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = CiftiLabelModifyKeysOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_LABEL_MODIFY_KEYS_METADATA",
    "CiftiLabelModifyKeysOutputs",
    "cifti_label_modify_keys",
]

# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T19:06:12.746629

import typing

from ..styxdefs import *


CIFTI_LABEL_MODIFY_KEYS_METADATA = Metadata(
    id="475718459757e2dfe8c14dd90cde83d4beb086b0",
    name="cifti-label-modify-keys",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiLabelModifyKeysOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_modify_keys(...)`.
    """
    cifti_out: OutputPathType
    """the output dlabel file"""


def cifti_label_modify_keys(
    runner: Runner,
    cifti_in: InputPathType,
    remap_file: str,
    cifti_out: InputPathType,
    opt_column_column: str | None = None,
) -> CiftiLabelModifyKeysOutputs:
    """
    CHANGE KEY VALUES IN A DLABEL FILE.
    
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
        runner: Command runner
        cifti_in: the input dlabel file
        remap_file: text file with old and new key values
        cifti_out: the output dlabel file
        opt_column_column: select a single column to use: the column number or
            name
    Returns:
        NamedTuple of outputs (described in `CiftiLabelModifyKeysOutputs`).
    """
    execution = runner.start_execution(CIFTI_LABEL_MODIFY_KEYS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-modify-keys")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(remap_file)
    cargs.append(execution.input_file(cifti_out))
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = CiftiLabelModifyKeysOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret
